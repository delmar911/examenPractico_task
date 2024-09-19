from apscheduler.schedulers.background import BackgroundScheduler
from .models import tarea
from django.utils import timezone

def actualizar_tareas_vencidas():
    tareas = tarea.objects.filter(due_date__lt=timezone.now().date(), status__in=[tarea.EstadoTarea.PENDIENTE, tarea.EstadoTarea.TERMINADA_VENCIDA])
    for t in tareas:
        t.status = tarea.EstadoTarea.VENCIDA
        t.save()

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(actualizar_tareas_vencidas, 'interval', minutes=1)  # Cambia la frecuencia según necesites
    scheduler.start()
