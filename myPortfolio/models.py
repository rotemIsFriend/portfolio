from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    technologies = models.CharField(max_length=200)
    image = models.ImageField(upload_to='projects/images/', default='projects/images/default.jpg')
    link = models.URLField(blank=True)
    github_link = models.URLField(blank=True)

    def __str__(self):
        return self.title
    
    def get_technologies_list(self):
        return self.technologies.split(',')

class Skill(models.Model):
    name = models.CharField(max_length=50)
    icon_url = models.URLField(blank=True)

    def __str__(self):
        return self.name
