# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Detalleagas(models.Model):
    agenteid = models.ForeignKey('agentes.Agente', on_delete=models.PROTECT, db_column='agenteID', verbose_name='Agente')
    aseguradoraid = models.ForeignKey('aseguradoras.Aseguradora', on_delete=models.PROTECT, db_column='aseguradoraID', verbose_name='Aseguradora')

    class Meta:
        managed = False
        db_table = 'detalleAgAs'
        unique_together = (('agenteid', 'aseguradoraid'),)
        verbose_name = 'Detalle de agente y aseguradora'
        verbose_name_plural = 'Detalles de agente y aseguradora'

    def __str__(self):
        return f'{self.agenteid} - {self.aseguradoraid}'

class Detalleastp(models.Model):
    aseguradoraid = models.ForeignKey('aseguradoras.Aseguradora', on_delete=models.PROTECT, db_column='aseguradoraID', verbose_name='Aseguradora')
    tipopolizaid = models.ForeignKey('polizas.Tipopoliza', on_delete=models.PROTECT, db_column='tipoPolizaID', verbose_name='Tipo de póliza')
    comision = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'detalleAsTP'
        unique_together = (('aseguradoraid', 'tipopolizaid'),)
        verbose_name = 'Detalle de aseguradora y tipo de póliza'
        verbose_name_plural = 'Detalles de aseguradora y tipo de póliza'

    def __str__(self):
        return f'{self.aseguradoraid} - {self.tipopolizaid}'