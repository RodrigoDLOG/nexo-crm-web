from django.db import models

class Agente(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True, verbose_name='ID')  # Field name made lowercase.
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    apellidopaterno = models.CharField(db_column='apellidoPaterno', max_length=50, verbose_name='Apellido paterno')  # Field name made lowercase.
    apellidomaterno = models.CharField(db_column='apellidoMaterno', max_length=50, verbose_name='Apellido materno')  # Field name made lowercase.
    creado = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creado')
    modificado = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificado')

    class Meta:
        managed = False
        db_table = 'agente'
        verbose_name = 'Agente'
        verbose_name_plural = 'Agentes'
        ordering = ['-creado']

    def __str__(self):
        return f'{self.nombre} {self.apellidopaterno} {self.apellidomaterno}'