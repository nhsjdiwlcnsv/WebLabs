from django.urls import path

from workshop.views import (
    ServicesView,
    ServiceView,
    ServiceTypeView,
    HomeView,
    apis
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('services/', ServicesView.as_view(), name='services'),
    path('service/<slug:service_slug>/', ServiceView.as_view(), name='service'),
    path('service-type/<slug:service_type_slug>/', ServiceTypeView.as_view(), name='service-type'),
    # path('add-service/', CreateServiceView.as_view(), name='add-service'),
    # path('register/', RegisterUser.as_view(), name='register'),
    # path('login/', LoginUser.as_view(), name='login'),
    # path('logout/', LogoutUser.as_view(), name='logout'),
    # path('order/', CreateOrderView.as_view(), name='order'),
    # path('my-order/<int:order_id>', OrderView.as_view(), name='my-order'),
    # path('my-orders/', OrdersView.as_view(), name='my-orders'),
    path('apis/', apis, name='apis'),
]
