from django.shortcuts import render
from app.models import *
# Create your views here.
def school_info(request):
    
    if request.method=='POST':
        scn=request.POST['scn']
        pn=request.POST['pn']
        fe=request.POST['fe']
        s=school.objects.get_or_create(schlname=scn,pname=pn,fee=fe)
        s.save()
        sinfo=school.objects.all()
        d={'sinfo':sinfo}
        return render(request,'display_school.html',d)


    return render(request,'insert_school.html')
