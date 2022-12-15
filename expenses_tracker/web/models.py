from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from expenses_tracker.web.validators import validate_only_letters, MaxFileSizeInMbValidator


class Profile(models.Model):
    MIN_FIRST_NAME = 2
    MAX_FIRST_NAME = 15
    MIN_LAST_NAME = 2
    MAX_LAST_NAME = 15
    DEFAULT_BUDGET_VALUE = 0
    MIN_BUDGET_VALUE = 0
    MAX_SIZE_IMAGE_MB = 5
    IMAGE_UPLOAD_TO_DIR = 'profiles/'

    first_name = models.CharField(
        max_length=MAX_FIRST_NAME,
        validators=(
            MinLengthValidator(MIN_FIRST_NAME),
            validate_only_letters,
        ),
    )
    last_name = models.CharField(
        max_length=MAX_LAST_NAME,
        validators=(
            MinLengthValidator(MIN_LAST_NAME),
            validate_only_letters,
        ),
    )
    budget = models.FloatField(
        default=DEFAULT_BUDGET_VALUE,
        validators=(
          MinValueValidator(MIN_BUDGET_VALUE),
        ),
    )
    profile_image = models.ImageField(
        upload_to=IMAGE_UPLOAD_TO_DIR,
        null=True,
        blank=True,
        validators=(
            MaxFileSizeInMbValidator(MAX_SIZE_IMAGE_MB),
        ),
    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Expense(models.Model):
    MAX_TITLE_LEN = 30
    title = models.CharField(
        max_length=MAX_TITLE_LEN,
    )
    expense_image = models.URLField()
    description = models.TextField(
        null=True,
        blank=True,
    )
    price = models.FloatField()


