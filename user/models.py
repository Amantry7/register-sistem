from django.db import models
from django.contrib.auth.models import AbstractUser,Group,Permission
# Create your models here.

class User(AbstractUser):
    phone = models.CharField(
        max_length=255,
        verbose_name="Телефонный номер"
    )
    
    # Добавим related_name для избежания конфликтов
    groups = models.ManyToManyField(Group, related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions')
    
    def __str__(self):
        return self.username 
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
