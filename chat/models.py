from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

# Create your models here.
class Message(models.Model):
  author = models.ForeignKey(User, related_name='author_messages', on_delete=models.CASCADE)
  content = models.TextField()
  room = models.TextField()
  timestamp = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.author.username

  @staticmethod
  def last_10_messages(room_name):
    return Message.objects.filter(room=room_name).order_by('timestamp').all()[:10]


# class Rooms(models.Model):
#   name = models.TextField()
#   author
