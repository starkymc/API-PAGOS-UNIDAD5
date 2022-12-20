from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import User
# Create your models here.

class Pagos(models.Model):
    class Servicios(models.TextChoices):
        NETFLIX = 'NF', _('Netflix')
        AMAZON = 'AP', _('Amazon Video')
        START = 'ST', _('Start+')
        PARAMOUNT = 'PM', _('Paramount+')

    servicio = models.CharField(
        max_length=2,
        choices=Servicios.choices,
        default=Servicios.NETFLIX,
    )
    fecha_pago = models.DateField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete =models.CASCADE, related_name='users')
    monto = models.FloatField(default=0.0)


class Servicios(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    logo = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Payment_user(models.Model):
    id_payments = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(User, on_delete =models.CASCADE, related_name='usersp')
    servicio = models.ForeignKey(Servicios, on_delete=models.CASCADE,related_name='servicio')
    monto = models.FloatField(default=0.0)
    PaymentDate = models.DateField(auto_now_add=True)
    ExpirationDate = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.id_payments

class Expired_payments(models.Model):
    payment = models.ForeignKey(Payment_user,on_delete =models.CASCADE, related_name='payment_user')
    Penalty_fee_amount = models.FloatField(default=0.0)

    def __str__(self):
        return str(self.payment)