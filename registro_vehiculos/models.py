from django.db import models

# Modelo para los propietarios del condominio
class Propietario(models.Model):
    nombre = models.CharField(max_length=100)
    numero_apartamento = models.CharField(max_length=10)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} (Apto: {self.numero_apartamento})"

# Modelo para los vehículos
class Vehiculo(models.Model):
    matricula = models.CharField(max_length=10)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE, related_name='vehiculos')

    def __str__(self):
        return f"{self.matricula} - {self.marca} {self.modelo}"

# Modelo para los registros de entrada y salida
class Registro(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    fecha_hora_entrada = models.DateTimeField(auto_now_add=True)
    fecha_hora_salida = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Entrada: {self.fecha_hora_entrada} - Vehículo: {self.vehiculo.matricula}"
