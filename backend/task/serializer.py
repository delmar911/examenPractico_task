from rest_framework import serializers
#se importa el modulo serializer
from .models import tarea
class TareaSerializer(serializers.ModelSerializer):
    #agregar los campos necesarios para mostrar
    #si de desea agregar todos los campos se puede utilizar la 
    #funcion __all__
    
    class Meta:
        model = tarea
        fields = 'id','title','status', 'assigned_to', 'due_date'