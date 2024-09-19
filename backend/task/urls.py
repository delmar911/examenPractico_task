from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from task import views

router_tarea = routers.DefaultRouter()
router_tarea.register(r'tarea', views.TareaView)

urlpatterns = [
    # Incluir las URLs de los enrutadores correspondientes en los patrones de URL
    path("api/v1/", include(router_tarea.urls)),
    path("docs/", include_docs_urls(title="Tarea Api")),
  
    
]