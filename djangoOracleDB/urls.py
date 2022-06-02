"""djangoOracleDB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import logging
import re
from importlib import import_module
from pathlib import Path

import yaml
from django.urls import path, include
from rest_framework import routers

logger = logging.getLogger(__name__)

router = routers.DefaultRouter()
for x in Path('djangoOracleDB/routes/').glob('*.yaml'):
    try:
        route_dict = yaml.full_load(x.read_text())
        viewset = route_dict['viewset']
        group_dict = re.match(r'^(?P<module>.+)\.(?P<class>[^.]+)$', viewset).groupdict()
        route_dict['viewset'] = getattr(import_module(group_dict['module']), group_dict['class'])
        router.register(**route_dict)
    except Exception as e:
        logger.warning(e)

urlpatterns = [
    path('', include(router.urls))
]
