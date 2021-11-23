from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from django.urls import reverse


class User(AbstractUser):
    is_admin = models.BooleanField(default=True)
    is_technician = models.BooleanField(default=False)


class Profile(models.Model):
    """
    User Profile model
    """

    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    ROLE_CHOICES = (
        ("admin", "Admin"),
        ("technician", "Technician"),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="technician")
    dob = models.DateField("date of birth", blank=True, null=True)
    GENDER_LIST = (
        ("M", "M"),
        ("F", "F"),
    )
    gender = models.CharField(max_length=1, choices=GENDER_LIST, default="M")
    contact = models.CharField(max_length=15)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        super(Profile, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("users:profile-detail", kwargs={"slug": self.slug})

    def get_email(self):
        return self.user.email

    def __str__(self):
        if self.first_name and self.last_name:
            return self.first_name + " " + self.last_name
        return self.user.username


class Zone(models.Model):
    """
    Zone model
    """

    zone = models.CharField(max_length=100, unique=True)
    tech = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="techs", null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    agency = models.ManyToManyField("Agency")

    class Meta:
        ordering = ["zone"]

    def get_absolute_url(self):
        return reverse("zone-detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.zone)
        super(Zone, self).save(*args, **kwargs)

    def __str__(self):
        return self.zone


class Agency(models.Model):
    """
    Agency model
    """

    agency = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)

    class Meta:
        verbose_name_plural = "agencies"
        ordering = ["agency"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.agency)
        super(Agency, self).save(*args, **kwargs)

    def __str__(self):
        return self.agency
