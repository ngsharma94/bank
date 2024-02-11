from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from rest_framework.routers import SimpleRouter

routeruser = SimpleRouter()
routeruser.register('user', views.SignUp)

routerprofile = SimpleRouter()
routerprofile.register('profile', views.ProfileView)

urlpatterns = [
    path('', include(routeruser.urls)),
    path('', include(routerprofile.urls)),
    path('api/create/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/verify/', TokenVerifyView.as_view(), name='token_verify'),
]



    # eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwODMzMTE5NywiaWF0IjoxNzA3NDY3MTk3LCJqdGkiOiI0MGNiMjY1ZGYxZWE0Njg5OTM3ZTJhYjljNzU3YmFmNSIsInVzZXJfaWQiOjV9.3hY-mLK3WV3HzKHcTaI2N6Fp5LmgMr70nSfCQpnyV38
    # eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA3ODk5MTk3LCJpYXQiOjE3MDc0NjcxOTcsImp0aSI6IjZhNDViZmI0Y2FjYjQ1M2JhMTY4ZGQ5ODAxODBiODNlIiwidXNlcl9pZCI6NX0.45IstT_0DMSKW4RU6gxlgqi-AQbT2YoE0X9o_ljMZ2M
