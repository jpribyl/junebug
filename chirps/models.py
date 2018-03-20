from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.

from .validators import validate_content




# classes should begin with a capital and be singular
class Chirp(models.Model):

    """
    The equivalent of a tweet
    """

    user        = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete='CASCADE')
    content     = models.CharField(max_length=140, validators=[validate_content])
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content)

    # success_url will override this
    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk":self.pk})


    # a second way to order by the reverse of the timestamp
    class Meta:
        ordering = ['-timestamp', 'content']
    # you could also do it with something called a model manager



    # a second way to do validations inside the model
    # def clean(self, *args, **kwargs):
        # content = self.content

        # if content == 'abc':
            # raise ValidationError("content cannot be abc")

        # return super(chirp, self).clean(*args, **kwargs)
