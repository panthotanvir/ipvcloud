"""cloudadmin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$','admin_panel.views.login_page', name="admin_panel"),
    url(r'^login_admin/$', 'admin_panel.views.admin_login', name="admin_login"),
    url(r'^login_panel/$', 'admin_panel.views.admin_panel', name="admin_panel"),
    url(r'^admin_form/([0-9])/$', 'admin_panel.views.admin_form', name="admin_form"),

]
