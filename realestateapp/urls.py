from django.urls import path
from .views import *

urlpatterns = [
    path('adminregister/',Adminregister.as_view(),name="register"),
    path('adminlogin/',AdminLogin.as_view(),name='admin_login'),
    path('addproperty/',PropertyAddView.as_view(),name="addproperty"),
    path('propertydisp/',PropertyListView.as_view(),name='propertydisp'),
    path('tenentreg/',TenentReg.as_view()),
    path('tenentlogin/',TenentLogin.as_view(),name='tenent_login'),
    path('propertyview/',Tenent_PropertyView.as_view()),
    path('send-request/<int:tenant_id>/<int:property_interest_id>/', SendRequestToLandlordView.as_view(), name='send_request'),
]