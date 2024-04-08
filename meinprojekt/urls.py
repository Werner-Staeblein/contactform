from django.contrib import admin
from django.urls import path
from django.urls import include  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('send_email/', include('send_email.urls')),  
    path('', include('send_email.urls')),  
]
