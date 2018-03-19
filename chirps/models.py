from django.db import models
from django.conf import settings

# Create your models here.

# classes should begin with a capital and be singular
class Chirp(models.Model):

    """
    The equivalent of a tweet
    """

    user        = models.ForeignKey(settings.AUTH_USER_MODEL,
                                    on_delete='CASCADE')
    content     = models.CharField(max_length=140)
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content)
