from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Api
from .serializers import *

@api_view(['GET', 'POST'])
def api_list(request):
    if request.method == 'GET':
        data = Api.objects.all()
        serializer = ApiSerializer(data, context={'request':request}, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ApiSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT', 'DELETE'])
def api_detail(request, pk):
    try:
        api = Api.objects.get(pk=pk)
    except Api.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        serializer = ApiSerializer(api, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        api.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)