from django.urls import path,include
from . import views
from django.conf.urls import url
from rest_framework import routers
from .views import SpamList,UserAuthentication

router = routers.DefaultRouter()
router.register('spam_filter',views.SpamView)

urlpatterns = [
    path('<int:listing_id>',views.detect_spam,name='detect_spam'),
    # path('api/',include(router.urls)),
    url('api/test_spam/$',SpamList.as_view(),name='test_spam'),
    url('api/auth/$',UserAuthentication.as_view()),
path('api/predict/', views.api_sentiment_pred, name='api_sentiment_pred'),]