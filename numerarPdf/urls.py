from django.contrib import admin
from django.urls import path
from numerador.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", NumerarPdfView.as_view(), name='numerar-pdf'),
]
