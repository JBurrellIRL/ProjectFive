from django.db import models


class Contact(models.Model):

    class Meta:
        verbose_name_plural = 'Contact Form Messages'

    name = models.CharField(max_length=60)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()
    replied_to = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class ContactNotes(models.Model):
    """
    Model to store internal notes for customer messages
    """
    REPLIED = [(False, 'No'), (True, 'Yes')]

    class Meta:
        verbose_name_plural = 'Contact Form Notes'

    related_message = models.ForeignKey(
        Contact,
        on_delete=models.CASCADE,
        related_name='related_message')
    date = models.DateTimeField(auto_now_add=True)
    replied_to = models.BooleanField(
        "Replied?", default=False, choices=REPLIED)
    reply_sent = models.TextField()

    def __str__(self):
        return f'Contact form notes for message ID: {self.related_message.id}'
