from django.db import models

class Tema(models.Model):
    id_api = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


class Decreto(models.Model):
    id_api = models.IntegerField(unique=True)
    numero = models.IntegerField()

    def __str__(self):
        return f"Decreto {self.numero}"


class Ley(models.Model):
    id_api = models.IntegerField(unique=True)
    titulo = models.CharField(max_length=500)
    abrogada = models.BooleanField(default=False)
    comentario = models.TextField(blank=True, null=True)
    temas = models.ManyToManyField(Tema, related_name='leyes')

    def __str__(self):
        return self.titulo


class Historial(models.Model):
    id_api = models.IntegerField(unique=True)
    ley = models.ForeignKey(Ley, on_delete=models.CASCADE, related_name='historial')
    fecha_ppo = models.DateField()
    ruta_archivo = models.URLField()
    comentario = models.TextField(blank=True, null=True)
    estatus = models.BooleanField(default=False)
    activo = models.BooleanField(default=True)
    decretos = models.ManyToManyField(Decreto, blank=True)

    def __str__(self):
        return f"Historial de {self.ley.titulo} ({self.fecha_ppo})"