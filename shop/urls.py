from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.teacher_list, name='teacher_list'),
    path('<slug:category_slug>/', views.teacher_list, 
         name='teacher_list_by_category'),
    path('<int:id>/<slug:slug>/', views.teacher_detail,
         name='teacher_detail'),
]
