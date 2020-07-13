from django.urls import path
from web import views

    urlpatterns = [
        path('consolidacion/', views.upload, name='upload'),
    ]
