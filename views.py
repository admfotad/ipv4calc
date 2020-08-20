from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.template import Template, Context
from django.contrib.auth.decorators import login_required
#from .models import cobraz
from .forms import Calc
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.http import HttpResponse
import os
import os.path
from django.utils.encoding import smart_text
from .ipcalc import spr 
from .forms import Calc



# Create your views here.


def sprt(adres):
    wynik=True
    w=[]
    try:
        try:
            w=adres.split('.')
        except:
            wynik=False
        if len(w)!=4:
            wynik=False
#    try:
#        temp=int(n)
#    except:
#        return None
        if w[0]==0 and w[1]==0 and w[2]==0 and w[3]==0:
            wynik=False
        if w[0]==255 and w[1]==255 and w[2]==255 and w[3]==255:
            wynik=False
        for n in w:
            if int(n)<0 or int(n)>255:
                wynik=False
    except:
        wynik=False

    return wynik
        
def klasa_sieci(adres):
    b2=range(16,32)
    a1=range(0,128)
    b1=range(128,192)
    c1=range(192,224)
    d1=range(224,240)
    e1=range(240,256)
    p=adres.split('.')
    if int(p[0]) in a1:
        if int(p[0])==10:
            return 'A (private)'
        else:
            return 'A'
    if int(p[0]) in b1:
        if int(p[1]) in b2:
            return 'B (private)'
        else:
            return 'B (public)'
    if int(p[0]) in c1:
        if int(p[1])==168:
            return 'C (private)'
        else:
            return 'C (public)'
    if int(p[0]) in d1:
        return 'D (multicast)'
    if int(p[0]) in e1:
        return 'E (reserved)'    


#@login_required(login_url='/login/')
def ipv4(request):

    if request.POST:
        kalk=Calc
        form=kalk(data=request.POST)
        if form.is_valid():
            ip_maska=''
            ip_adres=''
            Subnet_mask=''
            dane=[]
            ipadres=request.POST.get('IPv4_address')
            Subnet_mask = form.cleaned_data['Subnet_mask']
            Subnet_mask = dict(form.fields['Subnet_mask'].choices)[Subnet_mask]
            ip_maska=Subnet_mask.split('/')
#            ipmaska=request.POST.get('Subnet_mask')
                # tutaj sprawdzenie czy prawidlowe dane
            sprawdzenie=sprt(ipadres)
            
            if sprawdzenie is not False:
                dane=spr(ipadres,ip_maska[0])
                klasa=klasa_sieci(ipadres)  
                test=''
#            return HttpResponse(len(dane))
                if len(dane)>6 and len(dane)<10:
                    test=8
                    ip_a=dane[0]
                    net=dane[1]
                    adr_sieci=dane[3]
                    broad=dane[6]	#broadcast
                    host_max=dane[4]  # max ilosc hostow
                    net_max=dane[5]	# max ilosc sieci
                    first_host=dane[7]	# pierwszy adres hosta
                    last_host=dane[8]	# adres ostatniego hosta
                    context={
                    "klasa":klasa,
                    "test":test,
                    "ip_a":ip_a,
                    "net":net,
                    "form":form,
                    "adr_sieci":adr_sieci,
                    "broad":broad,
                    "host_max":host_max,
                    "net_max":net_max,
                    "first_host":first_host,
                    "last_host":last_host,
                
                    }
                elif len(dane)==6:
                    test=6
                    first_host=dane[3]
                    last_host=dane[4]
                    adr_sieci=dane[5]
                    ip_a=dane[0]
                    net=dane[1]
                    context={
                    "ip_a":ip_a,
                    "net":net,
                    "test":test,
                    "first_host":first_host,
                    "last_host":last_host,
                    "adr_sieci":adr_sieci,
                    "form":form,
                
                    }
            else:
                test=-1
                context={
                "blad":ipadres,
                "test":test,
                "form":form,
                }
                return render(request,"calc.html", context)
        # tu gdy forma jest zla
            
#        ip_adres='ip'
#        ip_maska='maska'
#        form=Calc(request.POST or None)
#        return HttpResponse(dane)
#        context={
#        "form":form,      
#        }
        return render(request,"calc.html", context)    
    else:
        form=Calc()
        context={
        "form":form,
        }
        return render(request,"calc.html", context)