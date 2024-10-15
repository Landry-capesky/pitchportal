from django.urls import path
from .views import *

urlpatterns = [
    # differents vues du projet
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('users/', user_list_view, name="user_list"),
    path('users/<int:pk>/edit/', user_update_view, name='user_update'),
    path('users/<int:pk>/delete/', user_delete_view, name='user_delete'),

    # differents vues du projet
    path('projects/', project_list, name='project_list'),
    path('projects/<int:pk>/', project_detail, name='project_detail'),
    path('projects/new/', project_create, name='project_create'),
    path('projects/<int:pk>/edit/', project_update, name='project_update'),
    path('projects/<int:pk>/delete/', project_delete, name='project_delete'),

    # differents vues du porteur de projet
    path('projectowners/', projectowner_list, name='projectowner_list'),
    path('projectowners/<int:pk>/', projectowner_detail, name='projectowner_detail'),
    path('projectowners/new/', projectowner_create, name='projectowner_create'),
    path('projectowners/<int:pk>/edit/', projectowner_update, name='projectowner_update'),
    path('projectowners/<int:pk>/delete/', projectowner_delete, name='projectowner_delete'),

    # differents vues de l'investisseur
    path('investors/', investor_list, name='investor_list'),
    path('investors/<int:pk>/', investor_detail, name='investor_detail'),
    path('investors/new/', investor_create, name='investor_create'),
    path('investors/<int:pk>/edit/', investor_update, name='investor_update'),
    path('investors/<int:pk>/delete/', investor_delete, name='investor_delete'),

    # differents vues de l'analyste
    path('analysts/', analyst_list, name='analyst_list'),
    path('analysts/<int:pk>/', analyst_detail, name='analyst_detail'),
    path('analysts/new/', analyst_create, name='analyst_create'),
    path('analysts/<int:pk>/edit/', analyst_update, name='analyst_update'),
    path('analysts/<int:pk>/delete/', analyst_delete, name='analyst_delete'),

    # differents vues pour les nouvelles fonctionnalités sur le projet
    path('projects/<int:project_id>/activate/', activate_project, name='activate_project'),
    path('projects/<int:project_id>/propose_funding/', propose_funding, name='propose_funding'),
    path('projects/<int:project_id>/progress/create/', create_project_progress, name='create_project_progress'),
    path('project_progress/', project_progress_list, name='project_progress_list'),
    path('project_progress/<int:progress_id>/update/', update_project_progress, name='update_project_progress'),
    path('project_progress/<int:progress_id>/delete/', delete_project_progress, name='delete_project_progress'),

    # differents vues pour les nouvelles fonctionnalités sur les utilisateurs
   # path('admin/users/<int:user_id>/toggle/', toggle_user_status, name='toggle_user_status'),
    #path('admin/dashboard/', admin_dashboard, name='admin_dashboard'),
]
