from django.db import models

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, unique=True)
    rut = models.CharField(max_length=12)
    correo_electronico = models.EmailField()
    telefono = models.IntegerField()
    monto_costo = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nombre} {self.rut}"

    def formato_clp(self):
        return f"${self.monto_costo:,.0f}".replace(",", ".")

class Atencion(models.Model):
    id_atencion = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    descripcion = models.TextField(blank=True)
    monto_costo = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Atención {self.id_atencion} - Cliente: {self.cliente.nombre}"

    def formato_clp(self):
        return f"${self.monto_costo:,.0f}".replace(",", ".")