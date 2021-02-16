from decimal import Decimal
from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models
# Create your models here.
from django.urls import reverse


class Step(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    steps: int = models.IntegerField(default=0)
    Day_1: int = models.IntegerField(blank=True, null=True, default=0,
                                     validators=[MinValueValidator(Decimal('0'))])
    Day_2: int = models.IntegerField(blank=True, null=True, default=0,
                                     validators=[MinValueValidator(Decimal('0'))])
    Day_3: int = models.IntegerField(blank=True, null=True, default=0,
                                     validators=[MinValueValidator(Decimal('0'))])
    Day_4: int = models.IntegerField(blank=True, null=True, default=0,
                                     validators=[MinValueValidator(Decimal('0'))])
    Day_5: int = models.IntegerField(blank=True, null=True, default=0,
                                     validators=[MinValueValidator(Decimal('0'))])
    Day_6: int = models.IntegerField(blank=True, null=True, default=0,
                                     validators=[MinValueValidator(Decimal('0'))])
    Day_7: int = models.IntegerField(blank=True, null=True, default=0,
                                     validators=[MinValueValidator(Decimal('0'))])

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('view-steps', args=[str(self.id)])

    def save(self, *args, **kwargs):
        self.steps = self.Day_1 + self.Day_2 + self.Day_3 + self.Day_4 + self.Day_5 + self.Day_6 + self.Day_7
        super().save(*args, **kwargs)
