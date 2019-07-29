from django import forms
from ongc.models import Survey_add
from ongc.models import Block_add
from ongc.models import Acquisition_add
from ongc.models import Media_add


class SurveyForm(forms.ModelForm):
    class Meta:
            model=Survey_add
            fields ="__all__"

class BlockForm(forms.ModelForm):
    class Meta:
        model=Block_add
        fields="__all__"

class AcquisitionForm(forms.ModelForm):
    class Meta:
        model=Acquisition_add
        fields="__all__"

class MediaForm(forms.ModelForm):
    class Meta:
        model=Media_add
        fields="__all__"