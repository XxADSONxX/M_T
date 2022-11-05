
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework.status import (
HTTP_200_OK, 
HTTP_201_CREATED, 
HTTP_400_BAD_REQUEST)
from teacher.models import professor, Aula
from teacher.serializers import (
    ProfessorSerializer, 
    CadastrarAulaSerializer, 
    AulaSerializer
)

class professorAPIView(APIView):
    def get(self, request, format=None):
        professores = professor.objects.all()
        serializer = ProfessorSerializer(professores, many=True)
        return Response(serializer.data, status=HTTP_200_OK)



class CadastrarAulaAPIView(APIView):
    def post(self, request, id, format=None):
        Professor = get_object_or_404(professor, id=id)
        serializer = CadastrarAulaSerializer(data=request.data)
        if serializer.is_valid():
            aula = Aula(
                nome=serializer.validated_data.get('nome'),
                email=serializer.validated_data.get('email'),
                Professor=Professor
            )
            Aula.save()
            """ revisar essa parte """
            aula_serializer = AulaSerializer(aula, many=False)
            return Response(aula_serializer.data, status=HTTP_201_CREATED)
        return Response({"message": "Houveram erros de validação", "errors": serializer.errors}, 
            status=HTTP_400_BAD_REQUEST)
          