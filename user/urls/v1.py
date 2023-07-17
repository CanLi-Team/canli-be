from django.urls import path, include
from rest_framework import routers
from user import views

router = routers.DefaultRouter()
router.register(r'profiles', views.UserViewSet)

profile_create = views.UserViewSet.as_view({
    'post': 'create'
})

urlpatterns = [
	path('', include(router.urls)),
	path('generate_otp', views.GenerateOTP.as_view(), name='generate-otp'),
    path('re_generate_otp', views.GenerateOTP.as_view(), name='re-generate-otp'),
    path('verify_otp', views.VerifyOTP.as_view(), name='verify-otp'),
    path('add/feedback', views.UserFeedbackAPIView.as_view(), name='user-feedback'),
    path('add/test_date', views.AddTestDate.as_view(), name='add-testdate'),
]