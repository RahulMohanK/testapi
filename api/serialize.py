from rest_framework import serializers
from .models import Report_db

class Report_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Report_db
        fields = '__all__'
