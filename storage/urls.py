from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('download/<int:file_id>/', views.download_file, name='download'),
    path('favorite/<int:file_id>/', views.toggle_favorite, name='toggle_favorite'),
    path('delete/<int:file_id>/', views.delete_file, name='delete_file'),
    path('restore/<int:file_id>/', views.restore_file, name='restore_file'),
    path('delete_permanent/<int:file_id>/', views.delete_permanent, name='delete_permanent'),  # добавить эту строку
]