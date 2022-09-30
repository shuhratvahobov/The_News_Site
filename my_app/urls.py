from django.urls import path
from .views import IndexPageView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('',IndexPageView.as_view(),name='index'), 

	]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
	