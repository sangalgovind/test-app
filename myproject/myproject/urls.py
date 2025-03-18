from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('htop/', include('monitor.urls')),  # Keep this as is
    path('', lambda request: HttpResponseRedirect('/htop/')),  # Redirect root URL to /htop/
]
