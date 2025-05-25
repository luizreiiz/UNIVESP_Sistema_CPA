
from django.urls import path

#from django1.urls import urlpatterns
from .views import index , colaboradores, genitores, populacao, pasto

urlpatterns = [
    path('', index),
    path('colaboradores' , colaboradores),
    path('genitores' , genitores),
    path('populacao' ,populacao ),
    path('pasto' , pasto)

]
