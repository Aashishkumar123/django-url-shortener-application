from django.urls import path
from .views import url_shortner

urlpatterns = [

	#path('',views.url_shortner,name="url-shortner"),
	path('',url_shortner.as_view(),name="url-shortner"),

]
