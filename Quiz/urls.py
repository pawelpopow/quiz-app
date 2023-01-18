from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from Quiz import views

urlpatterns = [
    path('', views.home, name='home'),
    path('addQuestion/', views.addQuestion, name='addQuestion'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('register/', views.registerPage, name='register'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)