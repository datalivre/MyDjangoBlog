from django.db import models
from django.utils import timezone

# DEFININDO O OBJETO
# O argumento models.Model diz que Post é um modelo de Django
# isso significa que ele terá de ser salvo no BD.
class Post(models.Model):
    # PROPRIEDADES DO OBJETO
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # definindo um campo de texto limitado a 200 caracteres 
    title = models.CharField(max_length = 200)
    # definindo um campo de texto ilimitado
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    # método publish
    def publish(self):
        self.publish_date = timezone.now()
        self.save()
    # método str
    def __str__(self):
        return self.title
    