from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail
from django.conf import settings

# Create your models here.
class User(AbstractUser):

    pass

    followings = models.ManyToManyField(
        "self", symmetrical=False, related_name="followers"
    )
    image = ProcessedImageField(
        upload_to="images/",
        blank=True,
        processors=[Thumbnail(60, 60)],
        format="JPEG",
        options={"quality": 90},
    )

    @property
    def full_name(self):
        return f"{self.last_name}{self.first_name}"


class Profile(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_pk"
    )
    image = ProcessedImageField(
        blank=True,
        processors=[Thumbnail(200, 300)],
        format="JPEG",
        options={"quality": 50},
    )


