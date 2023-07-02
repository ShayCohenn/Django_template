from django.contrib import admin
from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('contact', views.contact),
    path('prods', views.ProductViewSet.as_view()),
    path('prods/<pk>', views.ProductViewSet.as_view()),
    path('checkout', views.CartView.as_view()),
    path('login', TokenObtainPairView.as_view()),
    path('register', views.register),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)