from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from .models import Chirp

# Create your views here.
# CRUD --> Create Retrieve Update Delete

# Retrieve
def chirp_list_view(request):
    queryset = Chirp.objects.all() #QUERY all objects (list)
    print(queryset)

    for obj in queryset:
        print(obj.content)

    context = {
        "object_list": queryset
    }

    # combines request, template, context passed into it
    return render(request, "chirps/list_view.html", context)


def chirp_detail_view(request, id=1):
    obj = Chirp.objects.get(id=1) #GET from the DB (one item)

    print(obj)

    context = {
        "object": obj,
    }

    return render(request, "chirps/detail_view.html", context)


class ChirpDetailView(DetailView):
    template_name = "chirps/detail_view.html"
    queryset = Chirp.objects.all()

    def get_object(self):
        print(self.kwargs)
        # pk is a dictionary because we make it one in chirps/urls.py
        pk = self.kwargs.get("pk")
        obj = get_object_or_404(Chirp, pk=pk)

        # return Chirp.objects.get(id=pk)
        return obj


class ChirpListView(ListView):
    # you could also use the default at chirps/chirp_list.html
    template_name = "chirps/list_view.html"
    queryset = Chirp.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(ChirpListView, self).get_context_data(*args, **kwargs)
        print(context)
        return(context)
