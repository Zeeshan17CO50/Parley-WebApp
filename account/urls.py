from django.urls import path
from . import views
from django.views.static import serve
from django.conf.urls import url
from django.conf import settings

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='reg'),
    path('logout/', views.logoutUser, name='logout'),
    url(r'^media/(?P<path>.*)$', serve,
        {'document_root':       settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,
        {'document_root': settings.STATIC_ROOT})
]
