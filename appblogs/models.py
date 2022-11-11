from django.db import models

# Create your models here.
class article(models.Model):
    title = models.CharField(max_length = 100)
    created_at = models.DateField(auto_now_add = True)
    cover_image = models.ImageField(upload_to = 'uploads/')
    content = models.CharField(max_length = 100000000)

    def __str__(self):
        return f'{self.title}'
    
    
    
