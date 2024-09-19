from .serializer import TareaSerializer
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework import status

from .models import tarea

class TareaView(viewsets.ModelViewSet):
    serializer_class = TareaSerializer
    queryset = tarea.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['$title', '$due_date', '$assigned_to', '$status']
    
    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except NotFound:
            return Response({'detail': 'Tarea no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.get_serializer(instance)
        return Response({'message': 'Tarea encontrada', 'data': serializer.data})

    def get_object(self):
        queryset = self.get_queryset()
        filter_kwargs = {self.lookup_field: self.kwargs.get(self.lookup_field)}
        obj = queryset.filter(**filter_kwargs).first()
        if obj is None:
            raise NotFound('Tarea no encontrada')
        return obj

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'message': 'Tarea eliminada con éxito'}, status=status.HTTP_204_NO_CONTENT)
