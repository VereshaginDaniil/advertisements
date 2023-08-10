from django.urls import path
from .views import lsn_4, start


urlpatterns = [
    path('lesson_4/', lsn_4),
    path('', start),
]