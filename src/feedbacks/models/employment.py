from django.db import models
from common.models.base import BaseModel


class EmploymentApplication(BaseModel):
    """
    Employment application
    """

    name = models.CharField(max_length=100, verbose_name='First name')
    surname = models.CharField(max_length=100, verbose_name='Last name')
    phone_number = models.CharField(
        max_length=20,
        verbose_name='Phone number',
        help_text='Example: +996707123456',
        blank=True,
        null=True
    )
    email = models.EmailField(verbose_name='Email', blank=True, null=True)
    cv = models.FileField(
        upload_to='employees/cvs/',
        verbose_name='Resume (CV)'
    )
    message = models.TextField(
        verbose_name='Message or cover letter',
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.name} {self.surname}"

    class Meta:
        verbose_name = 'Employment application'
        verbose_name_plural = 'Employment applications'
