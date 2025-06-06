import uuid
from django.db import models
from apps.user.models import User


class ChatRoom(models.Model):
	roomId = models.UUIDField(default=uuid.uuid4)
	type = models.CharField(max_length=10, default='DM')
	member = models.ManyToManyField(User)
	name = models.CharField(max_length=20, null=True, blank=True)

	def __str__(self):
		return self.roomId + ' -> ' + str(self.name)


class ChatMessage(models.Model):
	chat = models.ForeignKey(ChatRoom, on_delete=models.SET_NULL, null=True)
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	message = models.CharField(max_length=255)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.message
