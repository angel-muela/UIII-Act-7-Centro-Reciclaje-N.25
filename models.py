from django.db import models

class MaterialReciclable(models.Model):
    nombre_material = models.CharField(max_length=100)
    descripcion = models.TextField()
    tipo_material = models.CharField(max_length=50)
    precio_por_kg = models.DecimalField(max_digits=5, decimal_places=2)
    unidad_medida = models.CharField(max_length=20)
    es_toxico = models.BooleanField()
    punto_acopio_recomendado = models.CharField(max_length=100)
    codigo_identificacion = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_material


class CentroAcopio(models.Model):
    nombre_centro = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    horario_atencion = models.TextField()
    capacidad_toneladas = models.DecimalField(max_digits=10, decimal_places=2)
    latitud = models.DecimalField(max_digits=10, decimal_places=6)
    longitud = models.DecimalField(max_digits=10, decimal_places=6)

    def __str__(self):
        return self.nombre_centro


class Donante(models.Model):
    nombre_donante = models.CharField(max_length=255)
    tipo_donante = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    direccion_donante = models.CharField(max_length=255)
    ruc_dni = models.CharField(max_length=20)
    fecha_registro = models.DateField()
    es_anonimo = models.BooleanField()

    def __str__(self):
        return self.nombre_donante


class EmpleadoReciclaje(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=20)
    fecha_contratacion = models.DateField()
    cargo = models.CharField(max_length=50)
    turno = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    certificaciones = models.TextField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class RecepcionMaterial(models.Model):
    material = models.ForeignKey(MaterialReciclable, on_delete=models.CASCADE)
    centro = models.ForeignKey(CentroAcopio, on_delete=models.CASCADE)
    donante = models.ForeignKey(Donante, on_delete=models.SET_NULL, null=True)
    fecha_recepcion = models.DateTimeField()
    cantidad_kg = models.DecimalField(max_digits=10, decimal_places=2)
    estado_material = models.CharField(max_length=50)
    observaciones = models.TextField()
    empleado_recepciono = models.ForeignKey(EmpleadoReciclaje, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Recepción {self.id}"


class ProcesamientoMaterial(models.Model):
    recepcion = models.ForeignKey(RecepcionMaterial, on_delete=models.CASCADE)
    fecha_inicio_procesamiento = models.DateTimeField()
    fecha_fin_procesamiento = models.DateTimeField()
    tipo_proceso = models.CharField(max_length=100)
    cantidad_resultante_kg = models.DecimalField(max_digits=10, decimal_places=2)
    subproductos = models.TextField()
    empleado_procesa = models.ForeignKey(EmpleadoReciclaje, on_delete=models.SET_NULL, null=True)
    costo_procesamiento = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Procesamiento {self.id}"


class VentaMaterial(models.Model):
    material = models.ForeignKey(MaterialReciclable, on_delete=models.CASCADE)
    id_cliente_comprador = models.IntegerField()  # Puedes cambiarlo si luego haces tabla Cliente
    fecha_venta = models.DateTimeField()
    cantidad_kg_vendido = models.DecimalField(max_digits=10, decimal_places=2)
    precio_por_kg_venta = models.DecimalField(max_digits=5, decimal_places=2)
    total_venta = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(max_length=50)
    empleado_venta = models.ForeignKey(EmpleadoReciclaje, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Venta {self.id}"
