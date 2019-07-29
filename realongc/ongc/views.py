from django.shortcuts import render,redirect
from ongc.forms import SurveyForm
from ongc.models import Survey_add
from ongc.forms import BlockForm
from ongc.models import Block_add
from ongc.forms import AcquisitionForm
from ongc.models import Acquisition_add
from ongc.models import Media_add
from ongc.forms import MediaForm

# Create your views here.
def index(request):
	return render(request,"dashadmin.html")
def mainadmin(request):
	return render(request,"dashadmin.html")
def blockv(request):
	return render(request,"blockview.html")
def acquisitionv(request):
	return render(request,"acqview.html")
def surveyv(request):
	return render(request,"surveyview.html")
def mediav(request):
	return render(request,"mediaview.html")
def mediae(request):
	return render(request,"mediaedit.html")
def surveye(request):
	return render(request,"surveyedit.html")
def blocke(request):
	return render(request,"blockedit.html")
def acquisitione(request):
	return render(request,"acqedit.html")
def survey_add(request):
        if request.method=="POST":
            form=SurveyForm(request.POST)
            if form.is_valid():
                try:
                    form.save()
                    return redirect("/survey_add")
                except:
                    pass
        else:
            form=SurveyForm()
        return render(request,"surveyadd.html",{'form':form})

def block_add(request):
		if request.method=="POST":
			form=BlockForm(request.POST)
			if form.is_valid():
				try:
					form.save()
					return redirect("/block_add")
				except:
						pass
		else:
			form=BlockForm()
		return render(request,"blockadd.html",{'form':form})

def acquisition_add(request):
		if request.method=="POST":
			form=AcquisitionForm(request.POST)
			if form.is_valid():
				try:
					form.save()
					return redirect("/acquisition_add")
				except:
					pass
		else:
			form=AcquisitionForm()
		return render(request,"acqadd.html",{'form':form})

def media_add(request):
		if request.method=="POST":
			form=MediaForm(request.POST)
			if form.is_valid():
				try:
					form.save()
					return redirect("/media_add")
				except:
					pass
		else:
			form=MediaForm()
		return render(request,"mediaadd.html",{'form':form})

def survey_view(request):
	if request.method=="POST":
		surveynumber = request.POST["surveynumber"]
		all_survey= Survey_add.objects.all()
		context = {'all_survey': all_survey,'surveynumber':surveynumber}
		return render(request,"surveypost.html",context)

def block_view(request):
	if request.method=="POST":
		blocknumber=request.POST["blocknumber"]
		all_block=Block_add.objects.all()
		context={'all_block':all_block,'blocknumber':blocknumber}
		return render(request,"blockpost.html",context)

def acq_view(request):
	if request.method=="POST":
		acquisitionnumber=request.POST["acquisitionnumber"]
		all_acquisition = Acquisition_add.objects.all()
		context = {'all_acquisition':all_acquisition,'acquisitionnumber':acquisitionnumber}
		return render(request,"acqpost.html",context)

def media_view(request):
	if request.method=="POST":
		medianumber=request.POST["medianumber"]
		all_media = Media_add.objects.all()
		context = {'all_media':all_media,'medianumber':medianumber}
		return render(request,"mediapost.html",context)

def edit_survey(request):
	if request.method=="POST":
		surveynumber=request.POST["surveynumber"]
		all_survey=Survey_add.objects.all()
		getvalue=Survey_add.objects.get(surveynumber=surveynumber)
		form=SurveyForm(request.POST,instance=getvalue)
		context={'all_survey':all_survey,'surveynumber':surveynumber,'form':form}
		return render(request,"postsurvey.html",context)

def survey_edit(request):
	if request.method=="POST":
		surveynumber=request.POST["surveynumber"]
		getvalue=Survey_add.objects.get(surveynumber=surveynumber)
		form=SurveyForm(request.POST,instance=getvalue)
		if form.is_valid():
			form.save()
			return render(request,"dashadmin.html")
		return render(request,"postsurvey.html",{'form':form})

def edit_block(request):
	if request.method=="POST":
		blocknumber = request.POST["blocknumber"]
		all_block=Block_add.objects.all()
		getvalue=Block_add.objects.get(blocknumber=blocknumber)
		form=BlockForm(request.POST,instance=getvalue)
		context={'all_block':all_block,'blocknumber':blocknumber,'form':form}
		return render(request,"postblock.html",context)

def block_edit(request):
	if request.method=="POST":
		blocknumber=request.POST["blocknumber"]
		getvalue=Block_add.objects.get(blocknumber=blocknumber)
		form=BlockForm(request.POST,instance=getvalue)
		if form.is_valid():
			form.save()
			return render(request,"dashadmin.html")
		return render(request,"postblock.html",{'form':form})

def edit_acq(request):
	if request.method=="POST":
		acquisitionnumber = request.POST["acquisitionnumber"]
		all_acq=Acquisition_add.objects.all()
		getvalue=Acquisition_add.objects.get(acquisitionnumber=acquisitionnumber)
		form=AcquisitionForm(request.POST,instance=getvalue)
		context={'all_acq':all_acq,'acquisitionnumber':acquisitionnumber,'form':form}
		return render(request,"postacq.html",context)

def acq_edit(request):
	if request.method=="POST":
		acquisitionnumber=request.POST["acquisitionnumber"]
		getvalue=Acquisition_add.objects.get(acquisitionnumber=acquisitionnumber)
		form=AcquisitionForm(request.POST,instance=getvalue)
		if form.is_valid():
			form.save()
			return render(request,"dashadmin.html")
		return render(request,"postacq.html",{'form':form})

def edit_media(request):
	if request.method=="POST":
		medianumber = request.POST["medianumber"]
		all_media=Media_add.objects.all()
		getvalue=Media_add.objects.get(medianumber=medianumber)
		form=MediaForm(request.POST,instance=getvalue)
		context={'all_media':all_media,'medianumber':medianumber,'form':form}
		return render(request,"postmedia.html",context)

def media_edit(request):
	if request.method=="POST":
		medianumber=request.POST["medianumber"]
		getvalue=Media_add.objects.get(medianumber=medianumber)
		form=MediaForm(request.POST,instance=getvalue)
		if form.is_valid():
			form.save()
			return render(request,"dashadmin.html")
		return render(request,"postmedia.html",{'form':form})


		

