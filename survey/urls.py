from django.contrib import admin
from django.urls import path,include
from mainsurvey import views as mainsurvey_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('survey/',include("mainsurvey.urls")),
    path('thankyou/',mainsurvey_views.thankyou,name="thankyou"),    
]
