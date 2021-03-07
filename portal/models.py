from django.db import models
from django.dispatch import receiver
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = CustomUser(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        assert extra_fields["is_staff"]
        assert extra_fields["is_superuser"]
        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    USER_TYPE = ((1, "Admin"), (2, "Company"), (3, "Student"))
    GENDER = [("M", "Male"), ("F", "Female")]
    first_name = None
    last_name = None
    username = None  # Removed username, using email instead
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=11, unique=True)
    user_type = models.CharField(default=1, choices=USER_TYPE, max_length=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Admin(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)


class Company(models.Model):
    name = models.CharField(max_length=70)
    address = models.CharField(max_length=150)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " - " + self.address


class Student(models.Model):
    fullname = models.CharField(max_length=70)
    regno = models.CharField(max_length=10, unique=True)
    picture = models.ImageField(upload_to="students/")
    start_date = models.DateField(null=True)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.fullname


class FinalRemark(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    remark = models.TextField()


class Logbook(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    week = models.IntegerField()
    report = RichTextUploadingField()
    remark = models.CharField(max_length=500, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# @receiver(post_save, sender=CustomUser)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         if instance.user_type == 1:
#             Admin.objects.create(admin=instance)
#         if instance.user_type == 2:
#             Company.objects.create(admin=instance)
#         if instance.user_type == 3:
#             Student.objects.create(admin=instance)


# @receiver(post_save, sender=CustomUser)
# def save_user_profile(sender, instance, **kwargs):
#     if instance.user_type == 1:
#         print("Hmm")
#         instance.admin.save()
#     if instance.user_type == 2:
#         instance.staff.save()
#     if instance.user_type == 3:
#         instance.student.save()
