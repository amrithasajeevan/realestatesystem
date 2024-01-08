from django.db import models
import re
from django.core.exceptions import ValidationError

# Create your models here.

def contact_validate(value):
    rule = r"^[9876][0-9]{9}$"
    match = re.fullmatch(rule, value)
    if not match:
        raise ValidationError("Please enter a valid contact number")

def email_validate(value):
    rule = r"^[a-z]+[0-9]*[*_]?[a-z0-9]*@gmail.com"
    match = re.fullmatch(rule, value)
    if not match:
        raise ValidationError("Please enter a valid email")

class adminuser(models.Model):
    username=models.CharField(max_length=30,unique=True)
    email=models.EmailField(unique=True,validators=[email_validate])
    contact=models.CharField(max_length=10,validators=[contact_validate])
    password=models.CharField(max_length=15)

    def __str__(self):
        return self.username
    

class propertydetail(models.Model):
    property_name=models.CharField(max_length=60)
    address=models.TextField()
    location=models.CharField(max_length=100)
    features=models.TextField()
    PROPERTY_TYPES = [
        ('1BHK', '1BHK'),
        ('2BHK', '2BHK'),
        ('3BHK', '3BHK'),
        ('4BHK', '4BHK')
    ]
    property_type=models.CharField(max_length=6,choices=PROPERTY_TYPES)
    rent_cost = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=False)


class tenentreg(models.Model):
    name=models.CharField(max_length=50)
    address=models.TextField()
    id_proof = models.FileField(upload_to='idproof/')
    contact=models.CharField(max_length=10,validators=[contact_validate])
    password=models.CharField(max_length=15)
    

class TenantRequest(models.Model):
    tenant = models.ForeignKey(tenentreg, on_delete=models.CASCADE)
    property_interest = models.ForeignKey(propertydetail, on_delete=models.CASCADE)
    message = models.TextField()
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)