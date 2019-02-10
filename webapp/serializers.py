from rest_framework import serializers
from . models import Patient
from . models import Record

class RecordSerializer(serializers.ModelSerializer):
    #patient = serializers.RelatedField(many=True, read_only=True)
    class Meta:
        model = Record
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    #records = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    records = RecordSerializer(many=True, read_only=True)

    class Meta:
        model = Patient
        fields = ('fname', 'sname', 'records')
        #fields = '__all__'


class RecordCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'

class RecordUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'
