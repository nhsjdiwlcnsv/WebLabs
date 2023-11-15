import json

import requests
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseNotFound
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    DetailView,
)

from .constants import HOME_PAGE_TEXT, ABOUT_PAGE_TEXT
from .forms import CreateServiceForm, CreateOrderForm, RegisterUserForm, LoginUserForm
from .models import (
    Question,
    Service,
    NewsPost,
    ServiceType,
    Order,
    Person,
    Banner,
    BannerRotationInterval,
)
from .utils import DataMixin


# Create your views here.
class HomeView(DataMixin, TemplateView):
    template_name = "workshop/index.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            **self.get_context(title="Home"),
            "text": HOME_PAGE_TEXT,
            "post": NewsPost.objects.latest("created_at"),
            "banners": Banner.objects.all(),
            "banner_interval": BannerRotationInterval.objects.first().interval_seconds,
        }


class AboutView(DataMixin, TemplateView):
    template_name = "workshop/about.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            **self.get_context(title="About us"),
            "text": ABOUT_PAGE_TEXT,
        }


class ContactView(DataMixin, TemplateView):
    model = Person
    template_name = "workshop/contact.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            **self.get_context(title="Contact us"),
        }


class GlossaryView(DataMixin, ListView):
    model = Question
    template_name = "workshop/glossary.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            **self.get_context(title="Glossary"),
        }


class ServicesView(DataMixin, ListView):
    model = Service
    template_name = "workshop/services.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            **self.get_context(title="Services"),
        }


class ServiceView(DataMixin, DetailView):
    model = Service
    template_name = "workshop/service.html"
    slug_url_kwarg = "service_slug"

    def get_context_data(self, *, object_list=None, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            **self.get_context(title="Service"),
        }


class NewsView(DataMixin, ListView):
    model = NewsPost
    template_name = "workshop/news.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        return {**super().get_context_data(**kwargs), **self.get_context(title="News")}


class NewsPostView(DataMixin, DetailView):
    model = NewsPost
    template_name = "workshop/newspost.html"
    slug_url_kwarg = "newspost_slug"

    def get_context_data(self, *, object_list=None, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            **self.get_context(title="News post"),
        }


class PrivacyPolicyView(DataMixin, TemplateView):
    template_name = "workshop/privacy_policy.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            **self.get_context(title="Privacy policy"),
        }


class ExperimentsView(DataMixin, TemplateView):
    template_name = "workshop/experiments.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            **self.get_context(title="Experiments"),
        }


class ServiceTypeView(DataMixin, ListView):
    model = Service
    template_name = "workshop/service_type.html"
    slug_url_kwarg = "service_type_slug"

    def get_queryset(self):
        return Service.objects.filter(
            service_type__slug=self.kwargs["service_type_slug"]
        )

    def get_context_data(self, *args, object_list=None, **kwargs):
        title = "Service"
        service_type = self.kwargs["service_type_slug"]
        image = ServiceType.objects.get(slug=service_type).image

        return {
            **super().get_context_data(**kwargs),
            **self.get_context(title=title),
            "service_type": service_type,
            "image": image,
        }


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = "workshop/register.html"
    success_url = reverse_lazy("home")

    def get_context_data(self, *, object_list=None, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            **self.get_context(title="Sign up"),
        }

    def form_valid(self, form):
        login(self.request, form.save())

        return redirect("home")


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = "workshop/login.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            **self.get_context(title="Log in"),
        }

    def get_success_url(self):
        return reverse_lazy("home")


class LogoutUser(DataMixin, LogoutView):
    def get_success_url(self):
        return reverse_lazy("home")


class CreateServiceView(DataMixin, CreateView):
    form_class = CreateServiceForm
    template_name = "workshop/createservice.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            **self.get_context(title="Create service"),
        }

    def get_success_url(self):
        return reverse_lazy("services")


class CreateOrderView(DataMixin, CreateView):
    form_class = CreateOrderForm
    template_name = "workshop/order.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            **self.get_context(title="Order"),
        }

    #
    # def post(self, request, *args, **kwargs):
    #     print("--------------")
    #     print(self.form_class())
    #     print("--------------")

    def get_success_url(self):
        return reverse_lazy("my-orders")


class OrdersView(DataMixin, ListView):
    model = Order
    template_name = "workshop/myorders.html"

    def get_queryset(self):
        return Order.objects.filter(created_by=self.request.user.id)

    def get_context_data(self, *, object_list=None, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            **self.get_context(title="My orders"),
        }


class OrderView(DataMixin, DetailView):
    model = Order
    template_name = "workshop/myorder.html"
    pk_url_kwarg = "order_id"

    def get_context_data(self, *, object_list=None, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            **self.get_context(title="Order"),
        }


def apis(request):
    context = {
        "title": "APIs",
        "img_url": json.loads(
            requests.get("https://api.waifu.pics/sfw/cringe").content
        )["url"],
    }

    return render(request, "workshop/apis.html", context=context)


def page_not_found(request, exception):
    return HttpResponseNotFound(
        "<div style='display: flex; justify-content: center; align-items:center'><h1>404, "
        "friendo...🫠</h1></div>"
    )
