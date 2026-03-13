from django.db import models

class Aseguradora(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True, verbose_name='ID')  # Field name made lowercase.
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    imagen = models.ImageField(upload_to='aseguradoras', verbose_name='Imagen')
    creado = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creado')
    modificado = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificado')

    class Meta:
        managed = False
        db_table = 'aseguradora'
        verbose_name = 'Aseguradora'
        verbose_name_plural = 'Aseguradoras'
        ordering = ['-creado']

    def __str__(self):
            return self.nombre