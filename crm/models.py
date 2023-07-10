from django.db import models
from django.core import validators


class Employ(models.Model):
    name = models.CharField(max_length=32)
    email = models.EmailField(max_length=254)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = "employ"

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = "product"

    def __str__(self):
        return self.name


class PaymentMethods(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        db_table = "payment_method"

    def __str__(self):
        return self.name


class Operations(models.Model):
    fk_name_of_product = models.ForeignKey(Products, on_delete=models.PROTECT, null=True)
    deb_cred = models.BooleanField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    amount = models.IntegerField(validators=[validators.MinValueValidator(0)])

    class Meta:
        db_table = "operation"

    def __str__(self):
        return f"{self.fk_name_of_product} - {self.price}"


class Check(models.Model):
    sell_id = models.IntegerField(validators=[validators.MinValueValidator(0)])
    date = models.DateTimeField(auto_now_add=True)
    fk_stuff = models.ForeignKey(Employ, on_delete=models.PROTECT, null=True)
    total = models.DecimalField(max_digits=15, decimal_places=2, validators=[validators.MinValueValidator(0)])
    fk_payment = models.ForeignKey(PaymentMethods, on_delete=models.PROTECT, null=True)
    notice = models.TextField(null=True)

    class Meta:
        db_table = "check"

    def __str__(self):
        return f"Check ID: {self.sell_id}"
