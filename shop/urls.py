from django.conf.urls import url, include
from . import views
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'marks', views.Mark)
router.register(r'auto_model', views.AutoModel)

urlpatterns = [
    url(r'^order_call$', views.OrderCall.as_view()),
    url(r'^partners_call$', views.PartnersCall.as_view()),
    url(r'^order_buy$', views.OrderBuy.as_view()),
]
urlpatterns += router.urls