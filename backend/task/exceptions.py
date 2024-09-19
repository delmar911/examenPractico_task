from rest_framework.views import exception_handler
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

def custom_exception_handler(exc, context):
    # Llama al manejador de excepciones de DRF
    response = exception_handler(exc, context)

    # Personaliza la respuesta para NotFound
    if response is None and isinstance(exc, NotFound):
        return Response({"error": "Tarea no encontrada"}, status=404)

    return response
