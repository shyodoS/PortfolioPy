from django.db import models

class Profile(models.Model):
    nome = models.CharField(max_length=100)
    titulo = models.CharField(max_length=200)
    email = models.EmailField()
    telefone = models.CharField(max_length=20, blank=True)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    bio = models.TextField()
    foto = models.ImageField(upload_to='profile/', blank=True, null=True)
    cv_pdf = models.FileField(upload_to='cv/', blank=True, null=True)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'

class Skill(models.Model):
    CATEGORIA_CHOICES = [
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('database', 'Database'),
        ('tools', 'Tools & Others'),
        ('soft', 'Soft Skills'),
    ]
    
    nome = models.CharField(max_length=50)
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES)
    nivel = models.IntegerField(default=50, help_text="0-100")
    icone = models.CharField(max_length=50, blank=True, help_text="Nome do ícone (ex: python, django)")
    
    def __str__(self):
        return f"{self.nome} ({self.get_categoria_display()})"
    
    class Meta:
        verbose_name = 'Habilidade'
        verbose_name_plural = 'Habilidades'

class Experience(models.Model):
    empresa = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    inicio = models.DateField()
    fim = models.DateField(null=True, blank=True, help_text="Deixe em branco se ainda trabalha aqui")
    descricao = models.TextField()
    tecnologias = models.CharField(max_length=200, help_text="Separadas por vírgula")
    
    def __str__(self):
        return f"{self.cargo} - {self.empresa}"
    
    class Meta:
        verbose_name = 'Experiência'
        verbose_name_plural = 'Experiências'
        ordering = ['-inicio']

class Project(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    tecnologias = models.CharField(max_length=200)
    github_url = models.URLField(blank=True)
    demo_url = models.URLField(blank=True)
    imagem = models.ImageField(upload_to='projects/', blank=True, null=True)
    destaque = models.BooleanField(default=False)
    data_criacao = models.DateField()
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'
        ordering = ['-data_criacao']

class Education(models.Model):
    instituicao = models.CharField(max_length=100)
    curso = models.CharField(max_length=100)
    inicio = models.DateField()
    fim = models.DateField(null=True, blank=True)
    descricao = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.curso} - {self.instituicao}"
    
    class Meta:
        verbose_name = 'Educação'
        verbose_name_plural = 'Educação'
        ordering = ['-inicio']
