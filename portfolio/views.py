from django.shortcuts import render
from .models import Profile, Skill, Experience, Project, Education

def index(request):
    context = {}
    
    # Tenta buscar dados do banco, senão usa dados estáticos
    try:
        profile = Profile.objects.first()
        skills = Skill.objects.all()
        experiences = Experience.objects.all()
        projects = Project.objects.all()
        education = Education.objects.all()
        
        context = {
            'profile': profile,
            'skills': skills,
            'experiences': experiences,
            'projects': projects,
            'education': education,
        }
    except:
        # Dados estáticos de exemplo (fallback)
        context = {
            'profile': {
                'nome': 'Seu Nome',
                'titulo': 'Desenvolvedor Full Stack',
                'email': 'seu@email.com',
                'bio': 'Desenvolvedor apaixonado por tecnologia...',
            },
            'skills': [
                {'nome': 'Python', 'categoria': 'backend', 'nivel': 90},
                {'nome': 'Django', 'categoria': 'backend', 'nivel': 85},
                {'nome': 'JavaScript', 'categoria': 'frontend', 'nivel': 80},
            ],
            'experiences': [],
            'projects': [],
            'education': [],
        }
    
    return render(request, 'portfolio/index.html', context)