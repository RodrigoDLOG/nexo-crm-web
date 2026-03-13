from django.db import models

class Tipopoliza(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True, verbose_name='ID')  # Field name made lowercase.
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    descripcion = models.TextField(verbose_name='Descripción')
    imagen = models.ImageField(upload_to='tipoPolizas', verbose_name='Imagen')
    creado = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creado')
    modificado = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificado')

    class Meta:
        managed = False
        db_table = 'tipoPoliza'
        verbose_name = 'Tipo de póliza'
        verbose_name_plural = 'Tipos de póliza'
        ordering = ['-creado']

    def __str__(self):
            return self.nombre

class Formapago(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True, verbose_name='ID')  # Field name made lowercase.
    forma = models.CharField(max_length=50, verbose_name='Forma de pago')
    creado = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creado')
    modificado = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificado')

    class Meta:
        managed = False
        db_table = 'formaPago'
        verbose_name = 'Forma de pago'
        verbose_name_plural = 'Formas de pago'
        ordering = ['-creado']

    def __str__(self):
            return self.forma

class Metodopago(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True, verbose_name='ID')  # Field name made lowercase.
    metodo = models.CharField(max_length=50, verbose_name='Método de pago')
    creado = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creado')
    modificado = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificado')

    class Meta:
        managed = False
        db_table = 'metodoPago'
        verbose_name = 'Método de pago'
        verbose_name_plural = 'Métodos de pago'
        ordering = ['-creado']

    def __str__(self):
            return self.metodo

class Poliza(models.Model):
    id = models.CharField(primary_key=True, max_length=15, verbose_name='ID')
    aseguradoraid = models.ForeignKey('aseguradoras.Aseguradora', on_delete=models.PROTECT, db_column='aseguradoraID', verbose_name='Aseguradora')  # Field name made lowercase.
    agenteid = models.ForeignKey('agentes.Agente', on_delete=models.PROTECT, db_column='agenteID', verbose_name='Agente')  # Field name made lowercase.
    clienteid = models.ForeignKey('clientes.Cliente', on_delete=models.PROTECT, db_column='clienteID', verbose_name='Cliente')  # Field name made lowercase.
    tipopolizaid = models.ForeignKey(Tipopoliza, on_delete=models.PROTECT, db_column='tipoPolizaID', verbose_name='Tipo de póliza')  # Field name made lowercasea.
    formapagoid = models.ForeignKey(Formapago, on_delete=models.PROTECT, db_column='formaPagoID', verbose_name='Forma de pago')  # Field name made lowercase.
    metodopagoid = models.ForeignKey(Metodopago, on_delete=models.PROTECT, db_column='metodoPagoID', verbose_name='Método de pago')  # Field name made lowercase.
    prima = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Prima')
    fechainicio = models.DateTimeField(db_column='fechaInicio', auto_now_add=True, verbose_name='Fehca de inicio')  # Field name made lowercase.
    fechafin = models.DateField(db_column='fechaFin', verbose_name='Fecha de fin')  # Field name made lowercase.
    modificado = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificado')

    class Meta:
        managed = False
        db_table = 'poliza'
        verbose_name = 'Póliza'
        verbose_name_plural = 'Pólizas'
        ordering = ['-fechainicio']

    def __str__(self):
            return self.id