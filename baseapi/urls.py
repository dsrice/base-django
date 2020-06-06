from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework_jwt.views import obtain_jwt_token

from v1.urls import router as v1_router

urlpatterns = [
    path('admin/', admin.site.urls),
    url('v1/', include(v1_router.urls)),
    url(r'^auth/', obtain_jwt_token),
]
