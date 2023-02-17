from django.urls import path
from .views import ViewForms,ViewSubmited,viewDetailJobs
urlpatterns = [
    path('form/',ViewForms,name = 'forms'),
    path('form/<str:pk>',ViewForms,name = 'save'),
    path('submision',ViewSubmited.as_view(),name='submited'),
    path('detail/<str:pk>',viewDetailJobs.as_view(),name='detail')
    
]