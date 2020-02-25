from django.shortcuts import render,redirect
from . models import Course
def index(request):
	if request.method=='POST' and request.POST['btnsubmit']:
		p = request.POST["txtp"]
		r = request.POST["txtr"]
		if request.POST['btnsubmit']=='+':
			c=int(p)+int(r)
		elif request.POST['btnsubmit']=='-':
			c=int(p)-int(r)
		elif request.POST['btnsubmit']=='*':
			c=int(p)*int(r)
		return render(request,"siapp/index.html",{'res':c})
	return render(request,"siapp/index.html")
def reg(request):
	return render(request,"siapp/reg.html")
def reglogic(request):
	s = request.GET["course"]
	cmb=request.GET["country"]
	msg = request.GET["txtpost"]
	s1=''
	data = request.GET.getlist('c[]')
	for d in data:
		s1=s1+d+" "
	st = request.GET.getlist('state[]')
	stdata=''
	for d in st:
		stdata=stdata+d+" "
	c = Course(adcourse=s,basiccourse=s1,countryname=cmb,statename=stdata,message=msg)
	c.save()
	return render(request,"siapp/reglogic.html",{'res':s+' '+s1+' '+cmb+' '+stdata+' '+msg})
def viewall(request):
	r = Course.objects.all()
	return render(request,"siapp/viewreg.html",{'res':r})
def findcourse(request):
	data = Course.objects.get(pk=request.GET["q"])
	return render(request,"siapp/editcourse.html",{'res':data})
def courseupdate(request):
	data = Course.objects.get(pk=request.POST["txtcourseid"])
	data.adcourse= request.POST["txtadcourse"]
	data.basiccourse= request.POST["txtbasiccourse"]
	data.countryname= request.POST["txtcountry"]
	data.statename= request.POST["txtstate"]
	data.message= request.POST["txtmessage"]
	data.save()
	return redirect('viewall')
def deletecourse(request):
	data = Course.objects.get(pk=request.GET["q"])
	data.delete()
	return redirect('viewall')

	
	

