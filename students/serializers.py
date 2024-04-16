from rest_framework import serializers

from students.models import Students

class StudentsSerializer(serializers.Serializer):

        pk = serializers.IntegerField(read_only=True)

        student_name = serializers.CharField(max_length=200)

        student_college = serializers.CharField(max_length=200)

        student_avg = serializers.IntegerField()

        admission_date = serializers.DateTimeField()

        def create(self, validated_data):

            return Students.objects.create(**validated_data)

        def update(self, instance, validated_data):

            instance.student_name = validated_data.get('student_name',instance.student_name)

            instnace.student_college = validated_data.get('student_college',instance.student_college)

            instance.student_avg = validated_data.get('student_avg',instance.student_avg)

            instance.admission_date = validated_data.get('admission_date',instance.admission_date)