from decimal import Decimal
from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models
# Create your models here.
from django.urls import reverse


class Step(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    steps: float = models.DecimalField(default=0, max_digits=7, decimal_places=2)
    Day_1: float = models.DecimalField(blank=True, null=True, default=0, max_digits=5, decimal_places=2,
                                       validators=[MinValueValidator(Decimal('0'))])
    Day_2: float = models.DecimalField(blank=True, null=True, default=0, max_digits=5, decimal_places=2,
                                       validators=[MinValueValidator(Decimal('0'))])
    Day_3: float = models.DecimalField(blank=True, null=True, default=0, max_digits=5, decimal_places=2,
                                       validators=[MinValueValidator(Decimal('0'))])
    Day_4: float = models.DecimalField(blank=True, null=True, default=0, max_digits=5, decimal_places=2,
                                       validators=[MinValueValidator(Decimal('0'))])
    Day_5: float = models.DecimalField(blank=True, null=True, default=0, max_digits=5, decimal_places=2,
                                       validators=[MinValueValidator(Decimal('0'))])
    Day_6: float = models.DecimalField(blank=True, null=True, default=0, max_digits=5, decimal_places=2,
                                       validators=[MinValueValidator(Decimal('0'))])
    Day_7: float = models.DecimalField(blank=True, null=True, default=0, max_digits=5, decimal_places=2,
                                       validators=[MinValueValidator(Decimal('0'))])

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('view-steps', args=[str(self.id)])

    def save(self, *args, **kwargs):
        self.steps = self.Day_1 + self.Day_2 + self.Day_3 + self.Day_4 + self.Day_5 + self.Day_6 + self.Day_7
        super().save(*args, **kwargs)
