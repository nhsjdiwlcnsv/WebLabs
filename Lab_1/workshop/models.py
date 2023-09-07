from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse


class Person(AbstractUser):
    STATUS = (
       ('customer', 'customer'),
       ('staff', 'staff')
    )

    email = models.EmailField(unique=True)
    status = models.CharField(max_length=100, choices=STATUS, default='customer')

    def __str__(self):
        return self.username


class ServiceType(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(
        max_length=255,
        unique=True,
        verbose_name='URL',
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('service-type', kwargs={'service_type_slug': self.slug})


class Service(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(
        max_length=255,
        unique=True,
        verbose_name='URL',
    )
    service_type = models.ForeignKey(
        ServiceType,
        on_delete=models.PROTECT,
        default=0
    )
    price = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(1000.0)],
        default=0.0
    )
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('service', kwargs={'service_slug': self.slug})


class Order(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    content = models.TextField(max_length=2000)
    created_by = models.ForeignKey(Person, auto_created=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('my-order', kwargs={'order_id': self.pk})
