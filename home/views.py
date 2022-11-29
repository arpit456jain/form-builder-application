from django.shortcuts import render
from rest_framework.response import Response
from home.models import FormBuilder
from home.serializers import FormBuilderSerializer
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.
def home(request):
    return render(request, 'index.html')

class FormBuilderView(APIView):
    def post(self, request, format=None):
        serializer = FormBuilderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data Uploaded Successfully', 'status':'success', 'candidate':serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

    def get(self, request, format=None):
        data = FormBuilder.objects.all()
        serializer = FormBuilderSerializer(data, many=True)
        return Response({'status':'success', 'data':serializer.data}, status=status.HTTP_200_OK)