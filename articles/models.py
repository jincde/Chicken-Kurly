from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail, ResizeToFill

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = ProcessedImageField(
        upload_to="images/",
        blank=True,
        processors=[ResizeToFill(400, 300)],  
        format="JPEG", 
        options={"quality": 80},  #
    )