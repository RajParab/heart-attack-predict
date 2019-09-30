from django.urls import path
from . import views
"""from rest_framework import routers

router = routers.DefaultRouter()
router.register('Form', views.form_view)
"""
app_name='form'
urlpatterns=[
			path('', views.form_view, name='test'),
			#path('api/', include(router.urls)),

]