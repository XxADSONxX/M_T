from django.forms import ValidationError
from rest_framework import serializers
from teacher.models import professor, Aula

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = professor
        fields = '__all__'



class CadastrarAulaSerializer(serializers.Serializer):
    nome = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=255)

    def validate_nome(self, value):
        if len(value) < 3:
            raise ValidationError("deve conter pelo menos três caracteres")
        return value

class AulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aula
        fields = '__all__'