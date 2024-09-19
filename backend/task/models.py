from django.db import models

# Create your models here.
class tarea(models.Model):
    
    class EstadoTarea(models.TextChoices):
        FINALIZADA = 'finalizada', 'Finalizada'#se registra con FIN
        PENDIENTE = 'pendiente', 'Pendiente'#PEN
        VENCIDA = 'vencida', 'Vencida'#VEN
        TERMINADA_VENCIDA = 'terminada_vencida', 'Terminada Vencida'#TER_VEN

    status  = models.CharField(
        max_length=30,
        choices=EstadoTarea.choices,
        default=EstadoTarea.PENDIENTE,
    )

    title = models.CharField(max_length=30)
    due_date = models.DateField()
    assigned_to = models.CharField(max_length=255)
    

    def __str__(self):
       return self.title