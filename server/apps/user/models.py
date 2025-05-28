import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
	userId = models.UUIDField(default=uuid.uuid4)
	image = models.ImageField(upload_to="user")


class OnlineUser(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.user.username
