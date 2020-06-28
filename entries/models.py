from django.core.validators import MinLengthValidator
from django.db import models


class Plans(models.Model):
    STATUS = {(0, 'completed'), (1, 'Pending')}
    name_plan = models.CharField(max_length=50, blank=False, validators=[MinLengthValidator(4)])
    status_plan = models.IntegerField(choices=STATUS)
    description_plan = models.TextField(max_length=300, blank=True)

    def __str__(self):
        return self.name_plan


