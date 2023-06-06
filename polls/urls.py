from django.urls import path
from . import views

urlpatterns = [
    # ex: 127.0.0.1:8000/polls/
    path("", views.index, name="index"),

 # ex: 127.0.0.1:8000/polls/5/
    path("<int:question_id>/", views.detail, name="detail"),

  # ex: 127.0.0.1:8000/polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),  
]