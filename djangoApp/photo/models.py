from django.db import models

class Photo(models.Model):
    image_file=models.ImageField(upload_to='C:\\SDPDEV\\workspace\\uploaded')
    filtered_image_file=models.ImageField(upload_to='C:\\SDPDEV\\workspace\\uploaded')
    description=models.TextField(max_length=500)
    created_at=models.DateTimeField(auto_now_add=True)
