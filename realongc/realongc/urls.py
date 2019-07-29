"""realongc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ongc import views
urlpatterns = [
     path('admin/', admin.site.urls),
     path('index/',views.index),
     path('survey_add',views.survey_add),
     path('block_add',views.block_add),
     path('acquisition_add',views.acquisition_add),
     path('media_add',views.media_add),
     path('surveyv',views.surveyv),
     path('survey_view',views.survey_view),
     path('blockv',views.blockv),
     path('block_view',views.block_view),
     path('acquisitionv/',views.acquisitionv),
     path('acq_view',views.acq_view),
     path('mediav/',views.mediav),
     path('media_view',views.media_view),
     path('surveye/',views.surveye),
     path('edit_survey',views.edit_survey),
     path('survey_edit',views.survey_edit),
     path('blocke/',views.blocke),
     path('edit_block',views.edit_block),
     path('block_edit',views.block_edit),
     path('acquisitione/',views.acquisitione),
     path('edit_acq',views.edit_acq),
     path('acq_edit',views.acq_edit),
     path('mediae/',views.mediae),
     path('edit_media',views.edit_media),
     path('media_edit',views.media_edit),
     path('mainadmin/',views.mainadmin),
]
