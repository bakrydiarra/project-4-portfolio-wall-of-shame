from django.db import models


class ContactForm(models.Model):

    REASON_CHOICES = (
        ("1", "Registration issue"),
        ("2", "Login issue"),
        ("3", "Delete Persona"),
        ("4", "General Enquiry"),
        ("5", "Report a comment"),
        ("6", "Report a Persona"),
    )

    reason = models.CharField(
        max_length=2, choices=REASON_CHOICES, default="4"
        )

    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    message = models.TextField(max_length=2000)
    written_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Massage'
        verbose_name_plural = 'Messages'

    def __str__(self):
        return f'Message from {self.name} on {self.written_on}'
