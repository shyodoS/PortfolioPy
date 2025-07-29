from django.contrib import admin
from .models import Profile, Skill, Experience, Project, Education

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['nome', 'titulo', 'email']
    
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['nome', 'categoria', 'nivel']
    list_filter = ['categoria']
    
@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['cargo', 'empresa', 'inicio', 'fim']
    list_filter = ['empresa']
    
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['nome', 'destaque', 'data_criacao']
    list_filter = ['destaque', 'data_criacao']
    
@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['curso', 'instituicao', 'inicio', 'fim']