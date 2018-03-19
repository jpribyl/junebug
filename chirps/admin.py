from django.contrib import admin

# Register your models here.
from .forms import ChirpModelForm
from .models import Chirp

# admin.site.register(Chirp)

class ChirpModelAdmin(admin.ModelAdmin):
    # form = ChirpModelForm

    class Meta:
        model = Chirp

admin.site.register(Chirp, ChirpModelAdmin)
