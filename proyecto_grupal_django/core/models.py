from django.db import models

# Create your models here.



class Persona(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email=models.EmailField(max_length=150,verbose_name="Email")
    dni=models.IntegerField(verbose_name="DNI")
    telefono = models.CharField(max_length=15)
    ubicacion = models.CharField(max_length=100)
    
    class Meta:
        abstract= True

    def nombre_completo(self):
        return f"{self.nombre}{self.apellido}"
    def __str__(self):
        return self.nombre_completo()
    



class Vendedor(Persona):
    FINANCIAMIENTO_CHOICES = (
        ('Financiamiento a Plazos', 'Financiamiento a Plazos'),
        ('Leasing', 'Leasing'),
        ('Pago al Contado', 'Pago al Contado'),
    )
    
    financiamiento_ofrecido = models.CharField(
        max_length=30,
        choices=FINANCIAMIENTO_CHOICES,
        
    )
    licencia_vendedor = models.CharField(max_length=50)
    tipo_vendedor = models.CharField(max_length=50, choices=[("Persona", "Persona"), ("Empresa", "Empresa")])
   
   
class Vehiculo(models.Model):
    listadoMarcas = [
        ('Abarth', 'Abarth'),
        ('Alfa Romeo', 'Alfa Romeo'),
        ('Aston Martin', 'Aston Martin'),
        ('Audi', 'Audi'),
        ('Bentley', 'Bentley'),
        ('BMW', 'BMW'),
        ('Cadillac', 'Cadillac'),
        ('Caterham', 'Caterham'),
        ('Chevrolet', 'Chevrolet'),
        ('Citroen', 'Citroen'),
        ('Dacia', 'Dacia'),
        ('Ferrari','Ferrari'), 
        ('Fiat', 'Fiat'),
        ('Ford', 'Ford'),
        ('Honda', 'Honda'),
        ('Infiniti','Infiniti'),
        ('Isuzu', 'Isuzu'),
        ('Iveco', 'Iveco'),
        ('Jaguar', 'Jaguar'),
        ('Jeep', 'Jeep'),
        ('Kia', 'Kia'),
        ('KTM', 'KTM'),
        ('Lada', 'Lada'),
        ('Lamborghini', 'Lamborghini'),
        ('Lancia', 'Lancia'),
        ('Land Rover', 'Land Rover'),
        ('Lexus', 'Lexus'),
        ('Lotus', 'Lotus'),
        ('Maserati', 'Maserati'),
        ('Mazda', 'Mazda'),
        ('Mercedes-Benz', 'Mercedes-Benz'),
        ('Mini', 'Mini'),
        ('Mitsubishi', 'Mitsubishi'),
        ('Morgan', 'Morgan'),
        ('Nissan', 'Nissan'),
        ('Opel', 'Opel'),
        ('Peugeot', 'Peugeot'),
        ('Piaggio', 'Piaggio'),
        ('Porsche', 'Porsche'),
        ('Renault', 'Renault'),
        ('Rolls-Royce', 'Rolls-Royce'),
        ('Seat', 'Seat'),
        ('Skoda', 'Skoda'),
        ('Smart', 'Smart'),
        ('SsangYong', 'SsangYong'),
        ('Subaru', 'Subaru'),
        ('Suzuki', 'Suzuki'),
        ('Tata', 'Tata'),
        ('Tesla', 'Tesla'),
        ('Toyota', 'Toyota'),
        ('Volkswagen', 'Volkswagen'),
        ('Volvo', 'Volvo'), 	

    ]
    tipo_auto = [
        ('Usado','Usado'),
        ('0KM', '0KM')
    ]
    marca = models.CharField(max_length=50,choices=listadoMarcas,)
    modelo = models.CharField(max_length=50)
    anio = models.PositiveIntegerField()
    tipo = models.CharField(max_length=20,choices=tipo_auto)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    def __str__(self):
        return f" {self.marca} - {self.modelo} - {self.anio}"

class Comprador(Persona):
    
    PREFERENCIAS_FINANCIAMIENTO_CHOICES = (
        ('Financiamiento a Plazos', 'Financiamiento a Plazos'),
        ('Leasing', 'Leasing'),
        ('Pago al Contado', 'Pago al Contado'),
    )
   
    tipo_comprador = models.CharField(max_length=50, choices=[("Persona", "Persona"), ("Empresa", "Empresa")])
    
    #----------------------relacion muchos a muchos-------------------------------------
    vehiculos_favoritos = models.ManyToManyField(Vehiculo, related_name='compradores_favoritos', blank=True)
    
    preferencias_financiamiento = models.CharField(
        max_length=30,
        choices=PREFERENCIAS_FINANCIAMIENTO_CHOICES,
        
    )
    def __str__(self):
        return f" {self.nombre} - {self.apellido} - {self.tipo_comprador}"
    

class Transaccion(models.Model):
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    comprador = models.ForeignKey(Comprador, on_delete=models.CASCADE)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    fecha_transaccion = models.DateTimeField(auto_now_add=True)
    precio_transaccion = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(max_length=50)
    estado_transaccion = models.CharField(max_length=20)  # Puede ser "En proceso", "Completada", etc.
    observaciones = models.TextField( null=True)

class Reporte(models.Model):
   
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)