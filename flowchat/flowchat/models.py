from django.db import models

class Message(models.Model):
    """ A model representing a text message in FlowRoute.
    See https://developer.flowroute.com/api/messages/v2.1/receive-an-sms/
    """

    flowId = models.CharField(max_length=64, db_index=True)
    type = models.CharField(max_length=32)
    amount_display = models.DecimalField(max_digits=8, decimal_places=6)
    amount_nanodollars = models.PositiveIntegerField()
    body = models.TextField()
    direction = models.CharField(max_length=32)
    sender = models.ForeignKey('Number', models.SET_NULL, related_name='senders', null=True, blank=True)
    is_mms = models.BooleanField()
    message_callback_url = models.CharField(max_length=256)
    message_encoding = models.IntegerField()
    message_type = models.CharField(max_length=32)
    status = models.CharField(max_length=32)
    timestamp = models.DateTimeField()
    recipient = models.ForeignKey('Number', models.SET_NULL, related_name='recipients', null=True, blank=True)

class Media(models.Model):
    """ A model representing Media within a message"""
    message = models.ForeignKey('Message',
                             on_delete=models.SET_NULL, null=True, blank=True)
    type = models.CharField(max_length=32)
    file_name = models.CharField(max_length=256)
    mime_type = models.CharField(max_length=64)
    url = models.TextField()

class Contact(models.Model):
    name = models.CharField(max_length=64)
    user = models.BooleanField()

class Number(models.Model):
    number = models.CharField(max_length=16)
    contact = models.ForeignKey('Contact', models.SET_NULL, null=True, blank=True)
