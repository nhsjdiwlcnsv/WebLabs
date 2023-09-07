import os.path
import random
import json

import requests
# from django.contrib.auth import login
# from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseNotFound
from django.shortcuts import redirect, render
# from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
)

from .constants import HOME_PAGE_TEXT
from .models import Service, ServiceType
from .utils import DataMixin


# Create your views here.
class HomeView(DataMixin, TemplateView):
    template_name = 'workshop/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            **self.get_context(title="Home"),
            'text': HOME_PAGE_TEXT
        }


class ServicesView(DataMixin, ListView):
    model = Service
    template_name = 'workshop/services.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            **self.get_context(title="Services")
        }


class ServiceView(DataMixin, DetailView):
    model = Service
    template_name = 'workshop/service.html'
    slug_url_kwarg = 'service_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            **self.get_context(title="Service")
        }


class ServiceTypeView(DataMixin, ListView):
    model = Service
    template_name = 'workshop/service_type.html'
    slug_url_kwarg = 'service_type_slug'

    def get_queryset(self):
        return Service.objects.filter(service_type__slug=self.kwargs['service_type_slug'])

    def get_context_data(self, *args, object_list=None, **kwargs):
        title = "Service"
        service_type = self.kwargs["service_type_slug"]
        image = ServiceType.objects.get(slug=service_type).image

        return {
            **super().get_context_data(**kwargs),
            **self.get_context(title=title),
            'service_type': service_type,
            'image': image
        }


def apis(request):
    fucks: list = [
        'awesome', 'because', 'bye', 'cup',
        'give', 'immensity', 'maybe', 'no',
        'shit', 'too', 'what'
    ]

    context = {
        'title': 'APIs',
        'fuck_engine': random.choice(fucks),
        'img_url': json.loads(requests.get('https://api.waifu.pics/sfw/cringe').content)['url']
    }

    return render(request, "workshop/apis.html", context=context)


def page_not_found(request, exception):
    return HttpResponseNotFound(
        "<div style='display: flex; justify-content: center; align-items:center'><h1>404, "
        "friendo...🫠</h1></div>"
    )
