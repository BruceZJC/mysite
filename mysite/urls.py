from django.contrib import admin
from django.urls import include, path
from FirePredict import views

urlpatterns = [
    #path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('FirePredict/firedata_detail/<int:fire_id>',views.firedata_detail,name ="firedata_detail")
]