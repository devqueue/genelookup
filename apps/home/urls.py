# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path, include
from apps.home import views

urlpatterns = [

    # The home page
    # path('', views.index, name='home'),
    # upload app
    path('',  include('apps.upload.urls')),
    # search app
    path('',  include('apps.search.urls')),
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),
] 
