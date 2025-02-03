from django.db import models

# Create your models here.

class UploadedFile(models.Model):
    FILE_TYPE_CHOICES = (
        ('normal', 'Normal'),
        ('anomalous', 'Anomalous'),
    )

    file = models.FileField(upload_to='uploads/%Y/%m/%d/')
    file_type = models.CharField(max_length=20, choices=FILE_TYPE_CHOICES)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name

