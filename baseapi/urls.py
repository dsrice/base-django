from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from v1.urls import router as v1_router

urlpatterns = [
    path('admin/', admin.site.urls),
    url('v1/', include(v1_router.urls)),
]
