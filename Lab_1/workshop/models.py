# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Person(AbstractUser):
    STATUS = (("customer", "customer"), ("staff", "staff"))

    email = models.EmailField(unique=True)
    status = models.CharField(max_length=100, choices=STATUS, default="customer")

    def __str__(self):
        return self.username


class Question(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField(null=True, blank=True, max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question


class ServiceType(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(
        max_length=255,
        unique=True,
        verbose_name="URL",
    )
    image = models.ImageField(upload_to="images/", null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("service-type", kwargs={"service_type_slug": self.slug})


class Service(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(
        max_length=255,
        unique=True,
        verbose_name="URL",
    )
    service_type = models.ForeignKey(ServiceType, on_delete=models.PROTECT, default=0)
    price = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(1000.0)], default=0.0
    )
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("service", kwargs={"service_slug": self.slug})


class NewsPost(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(
        max_length=255,
        unique=True,
        verbose_name="URL",
    )
    description = models.TextField(null=True)
    content = models.TextField()
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("news-post", kwargs={"newspost_slug": self.slug})


class Order(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    content = models.TextField(max_length=2000)
    created_by = models.ForeignKey(
        Person, null=True, blank=True, on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("my-order", kwargs={"order_id": self.pk})


class Banner(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/banner/")
    link = models.URLField()

    def __str__(self):
        return self.title


class BannerRotationInterval(models.Model):
    interval_seconds = models.PositiveIntegerField(default=3000)

    def __str__(self):
        return f"{self.interval_seconds} s"


class Voucher(models.Model):
    title = models.TextField()
    code = models.CharField(max_length=20, unique=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2)

    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    max_usages = models.PositiveIntegerField()
    usage_count = models.PositiveIntegerField(default=0)

    def is_valid(self) -> bool:
        return (
            self.start_date <= timezone.now() <= self.end_date
            and self.usage_count < self.max_usages
        )

    def apply(self):
        if self.is_valid():
            self.usage_count += 1
            self.save()

    def __str__(self):
        return self.code
