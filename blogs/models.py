from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    modelo_da_moto = models.TextField()
    information = models.TextField()
    motor = models.IntegerField(help_text="Em centímetros cúbicos")
    imagem = models.ImageField(upload_to='imagens/', blank=True, null=True)

    def __str__(self):
        return self.title