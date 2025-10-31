from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import Ley
from .serializers import LeySerializer

class LeyViewSet(viewsets.ModelViewSet):
    queryset = Ley.objects.all()
    serializer_class = LeySerializer

    @action(detail=False, methods=['post'])
    def bulk(self, request):
        serializer = LeySerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)