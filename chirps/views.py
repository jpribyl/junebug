from django import forms
from django.shortcuts import render, get_object_or_404
from django.forms.utils import ErrorList
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib.auth.models import User

from django.views.generic import (
    DetailView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView)


from .models import Chirp
from .forms import ChirpModelForm
from .mixins import FormUserNeededMixin, UserOwnerMixin

# Create your views here.
# CRUD --> Create Retrieve Update Delete


#########################
# CLASS BASED VIEWS
#########################

#########################
# create
#########################

# LoginRequiredMixin is Django's default one, FormUserNeededMixin is mine
#mixins are one of the strongest arguments for class based views
class ChirpCreateView(LoginRequiredMixin, FormUserNeededMixin, CreateView):
    form_class = ChirpModelForm
    template_name = 'chirps/create_view.html'
    # success_url = "/chirp/create/"
    login_url = '/admin'


#########################
# Retrieve
#########################

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


class ChirpListView(LoginRequiredMixin, ListView):
    # you could also use the default at chirps/chirp_list.html
    template_name = "chirps/list_view.html"

    def get_queryset(self, *args, **kwargs):
        qs = Chirp.objects.all()

        # q is the input to the search box from search_form.html
        query = self.request.GET.get("q", None)
        if query is not None:
            # filter based on it
            qs = qs.filter(
                Q(content__icontains=query) |
                Q(user__username__icontains=query))

        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(ChirpListView, self).get_context_data(*args, **kwargs)
        print(context)
        context['create_form'] = ChirpModelForm()
        context['create_url'] = reverse_lazy('create')
        context['user_list'] = User.objects.all()

        return(context)


#########################
# update
#########################


class ChirpUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    queryset = Chirp.objects.all()

    form_class = ChirpModelForm
    template_name = 'chirps/update_view.html'

    # uncomment this to show list of chirps instead of updated chirp
    # success_url = "/chirp/"


#########################
# delete
#########################

class ChirpDeleteView(LoginRequiredMixin, DeleteView):
    model = Chirp
    template_name = 'chirps/delete_confirm.html'
    success_url = reverse_lazy("list")








#########################
# FUNCTION BASED VIEWS
#########################

# without using class based models
# def chirp_list_view(request):
    # queryset = Chirp.objects.all() #QUERY all objects (list)
    # print(queryset)

    # for obj in queryset:
        # print(obj.content)

    # context = {
        # "object_list": queryset
    # }

    # # combines request, template, context passed into it
    # return render(request, "chirps/list_view.html", context)


# def chirp_detail_view(request, id=1):
    # obj = Chirp.objects.get(id=1) #GET from the DB (one item)

    # print(obj)

    # context = {
        # "object": obj,
    # }

    # return render(request, "chirps/detail_view.html", context)



# def chirp_create_view(request):
    # form = ChirpModelForm(request.POST or None)
    # if form.is_valid():
        # instance = form.save(commit=False)
        # instance.user = request.user
        # instance.save()
    # context = {
        # "form":form
    # }
    # return render(request, 'chirps/create_view.html', context)
