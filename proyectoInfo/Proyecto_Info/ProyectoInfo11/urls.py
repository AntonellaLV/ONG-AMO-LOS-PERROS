from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blog.urls')),
    path('login/', include('django.contrib.auth.urls')),
    path('login/',include('login.urls')),

]
