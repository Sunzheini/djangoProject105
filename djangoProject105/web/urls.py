from django.urls import path
from djangoProject105.web.views import index

urlpatterns = (
    path('', index, name='index'),
)
