from django.urls import path
from . import views

urlpatterns = [
    path('',views.analysis_results,name='analysis_results'),
]
