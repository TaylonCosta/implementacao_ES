from django.urls import path

from . import views

urlpatterns = [
    path ('', views.index, name='index'),
    #path ('monitorias', views.monitorias, name='monitoria'),
    #path ('monitorias/new', views.monitorias, name='monitorias-new'),
    #path ('monitorias/update/<int:pk>', views.monitorias, name='monitorias-update'),
    #path ('monitorias/delete/<int:pk>', views.monitorias, name='monitorias-delete'),
    path ('register', views.register, name='register')


]