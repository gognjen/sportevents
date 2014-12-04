from django.db import models


class Invitation(models.Model):
    pass    

class Message(models.Model):
    text = models.TextField(default='')
    invitation = models.ForeignKey(Invitation, default=None)
