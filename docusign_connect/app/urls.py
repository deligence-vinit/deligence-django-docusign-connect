from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.sign),
    path('form/getpdf/', views.get_pdf),
    path('form/getfile/', views.download_pdf),
    # path('',views.homepage),
    path('manage/',views.manage),
    path('detailedView/',views.detailedView),
    path('logout/',views.logout_request),
    path('change_password/',views.change_password),
    path('files/',views.get_file),
    path('getfile/',views.download_pdf)
]
