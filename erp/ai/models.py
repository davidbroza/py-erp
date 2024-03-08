from django.db import models

class DocumentprocessingTaskStatus:
    PENDING = 'PENDING'
    PROCESSING = 'PROCESSING'
    DONE = 'DONE'
    ERROR = 'ERROR'
    CHOICES = [
        (PENDING, 'Pending'),
        (PROCESSING, 'Processing'),
        (DONE, 'Done'),
        (ERROR, 'Error'),
    ]
    @classmethod
    def get_default(cls):
        return cls.PENDING

class DocumentProcessingTask(models.Model)# Create your models here.
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    file = models.FileField(upload_to='documents')
    note = models.TextField(blank=True)
                            

