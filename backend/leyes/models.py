from django.db import models

class Tema(models.Model):
    tema = models.CharField(max_length=255)
    external_id = models.IntegerField(null=True, blank=True, unique=True)  # ID de la API

    def __str__(self):
        return self.tema


class Decreto(models.Model):
    numero = models.IntegerField()
    external_id = models.IntegerField(null=True, blank=True, unique=True)  # ID de la API

    def __str__(self):
        return f"Decreto {self.numero}"


class Ley(models.Model):
    id = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=500)
    abrogada = models.BooleanField(default=False)
    comentario = models.TextField(blank=True, null=True)
    tema = models.ManyToManyField(Tema, related_name='leyes')

    def __str__(self):
        return self.titulo


class Historial(models.Model):
    id = models.IntegerField(primary_key=True)
    ley = models.ForeignKey(Ley, on_delete=models.CASCADE, related_name='historial')
    fecha_ppo = models.DateField()
    rutaArchivo = models.URLField()
    comentario = models.TextField(blank=True, null=True)
    estatus = models.BooleanField(default=False)
    activo = models.BooleanField(default=True)
    decretos = models.ManyToManyField(Decreto, blank=True)

    def __str__(self):
        return f"Historial de {self.ley.titulo} ({self.fecha_ppo})"