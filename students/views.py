from django.shortcuts import render

from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt

from rest_framework.renderers import JSONRenderer

from rest_framework.parsers import JSONParser

from rest_framework import status

from students.models import Students

from students.serializers import StudentsSerializer

class JSONResponse(HttpResponse):

    def __init__(self, data, **kwargs):

        content = JSONRenderer().render(data)

        kwargs['content_type'] = 'application/json'

        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt

def students_list(request):

    if request.method == 'GET':

        students = Students.objects.all()

        students_serializer = StudentsSerializer(students, many=True)

        return JSONResponse(students_serializer.data)

    elif request.method == 'POST':

        students_data = JSONParser().parse(request)

        students_serializer = StudentsSerializer(data=students_data)

        if students_serializer.is_valid():

            students_serializer.save()

            return JSONResponse(students_serializer.data,status=status.HTTP_201_CREATED)

        return JSONResponse(students_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt

def student_detail(request, pk):

    try:

        student = Students.objects.get(pk=pk)

    except Game.DoesNotExist:

        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':

        student_serializer = StudentsSerializer(student)

        return JSONResponse(student_serializer.data)

    elif request.method == 'PUT':

        student_data = JSONParser().parse(request)

        student_serializer = StudentsSerializer(student, data=student_data)

        if student_serializer.is_valid():

            student_serializer.save()

            return JSONResponse(student_serializer.data)

        return JSONResponse(student_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':

        student.delete()

        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
