from django.contrib import admin

# Register your models here.
from .models import CustomUser, Project, ProjectOwner, Investor, Analyst
from django.contrib.auth.admin import UserAdmin

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_project_owner', 'is_investor', 'is_analyst')
    fieldsets = UserAdmin.fieldsets + ((None,{'fields':('is_project_owner', 'is_investor', 'is_analyst')}),)

@admin.register(Project)
class ProjectOwnerAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user_username', 'user_email')
    
@admin.register(Investor)
class InvestorAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user_username', 'user_email')
    
@admin.register(Analyst)
class AnalystAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user_username', 'user_email')

