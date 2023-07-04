from django.contrib import admin
from django.urls import path
from django.urls import include
# from courses.views import first_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('courses/', include('courses.urls')),
    # path('courses/',first_view,name="first_view"),
]
