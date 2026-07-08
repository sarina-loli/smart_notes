from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('profile/', views.profile_view, name='profile'),

    path('notes/', views.note_list_view, name='note_list'),
    path('notes/create/', views.note_create_view, name='note_create'),
    path('notes/<int:pk>/', views.note_detail_view, name='note_detail'),
    path('notes/<int:pk>/edit/', views.note_edit_view, name='note_edit'),
    path('notes/<int:pk>/delete/', views.note_delete_view, name='note_delete'),
]
