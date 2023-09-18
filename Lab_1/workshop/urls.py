from django.urls import path

from workshop.views import (
    ServicesView,
    ServiceView,
    ServiceTypeView,
    NewsView,
    NewsPostView,
    HomeView,
    AboutView,
    ContactView,
    GlossaryView,
    RegisterUser,
    LoginUser,
    LogoutUser,
    CreateServiceView,
    CreateOrderView,
    OrdersView,
    OrderView,
    apis
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('glossary/', GlossaryView.as_view(), name='glossary'),
    path('news/', NewsView.as_view(), name='news'),
    path('news/<slug:newspost_slug>', NewsPostView.as_view(), name='news-post'),
    path('services/', ServicesView.as_view(), name='services'),
    path('service/<slug:service_slug>/', ServiceView.as_view(), name='service'),
    path('service-type/<slug:service_type_slug>/', ServiceTypeView.as_view(), name='service-type'),
    path('add-service/', CreateServiceView.as_view(), name='add-service'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutUser.as_view(), name='logout'),
    path('order/', CreateOrderView.as_view(), name='order'),
    path('my-order/<int:order_id>', OrderView.as_view(), name='my-order'),
    path('my-orders/', OrdersView.as_view(), name='my-orders'),
    path('apis/', apis, name='apis'),
]
