from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_all_users, name='all_users'),
    path('<int:id>/', views.show_user_by_id, name='user_by_id'),
    path('form_user/', views.form_user, name='form_user'),
    path('form_user/<int:id>/', views.form_user, name='form_user_update'),
    path('delete_user/<int:id>/', views.delete_user, name='delete_user'),
]