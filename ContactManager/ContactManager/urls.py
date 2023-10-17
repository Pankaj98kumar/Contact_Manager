
from django.contrib import admin
from django.urls import path
from apiapp.views import ContactView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',ContactView.as_view(),name='contacts'),
    
]
