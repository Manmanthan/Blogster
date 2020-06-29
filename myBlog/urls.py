from django.contrib import admin
from django.contrib.auth import views
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('accounts/login/', views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts//logout/', views.LogoutView.as_view(), name='logout', kwargs={'next_page': '/'}),
]
