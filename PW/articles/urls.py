from django.urls import path
from .import views

app_name = 'articles'

urlpatterns = [
    path('', views.articles_list, name= "list"),
    path('create',  views.article_create, name="create"),
    path('<str:slug>/', views.article_details, name="details"),
]

