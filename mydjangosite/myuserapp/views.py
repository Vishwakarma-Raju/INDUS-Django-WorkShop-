from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def homepage(request):
    return render(request,"home.html")

def aboutpage(request):
    return render(request,"about.html")   
 
def contactpage(request):
    return render(request,"contact.html")  

def ToyShoppage(request):
    return render(request,"ToyShop.html")

def contactprocess(request):
    a = int(request.POST['txt1'])
    b = int(request.POST['txt2'])
    c = a + b 
    msg = "A Value is",a," ","B Value is",b," ","Sum is",c
    # return HttpResponse(msg)
    d = ""
    if c == 30:
        d = "If Condition Called"
    elif c<30:
        d = "Esleif Called"
    else:
        d = "Esle Called"

    return render(request,'ans.html',{'mya':a,'myb':b,'myc':c,'myd':d})

def homeprocess(request):
    a = int(request.POST['input1'])
    b = int(request.POST['input2'])
    c = int(request.POST['input3'])
    d = int(request.POST['input4'])
    e = ((a+b+c+d)/400)*100
    g = ""
    if e >= 80 and e <= 100:
        g = "Grade A" 
    elif e >= 60 and e < 80:
        g = "Grade B"
    elif e >= 40 and e < 60:
        g = "Grade C"
    else:
        g = "Grade D"
    # msg = a," ",b
    return render(request,'ans.html',{'mya':a,'myb':b,'myc':c,'myd':d,'mye':e,'myg':g})


def saveSessionData(request):
    request.session['username'] = 'Raju Vishwakrama'
    return HttpResponse("Session Created")


def getSessionData(request):
    if  request.session.has_key('username'):
        msg = request.session['username']
        return HttpResponse(msg)

    else:
        return HttpResponse("Session Variable Not Found")
    
def deleteSessionData(request):
    del request.session['username']
    return HttpResponse("Session Removed")

def getSessionData2(request):
    msg = request.session['username']
    return HttpResponse(msg)

def loginPage(request):
    return render(request,'login.html')

def loginProcess(request):
    txt1 = request.POST['email']
    request.session['myemail'] = txt1
    return redirect(dashboard)

def dashboard(request):
    if request.session.has_key('myemail'):
        return render(request,"dashboard.html")
    else:
        return redirect(loginPage)

def logout(request):
    del request.session['myemail']
    return redirect(loginPage)


# EmailsendDemo

def mailsenddemo(request):
    subject = 'Django Mail Demo'
    message = ' Hello How are you ?'
    email_form = settings.Email_HOST_USER
    recipient_list = ['faltoomaal69@gamil.com']
    send_mail(subject,message,email_form,recipient_list)
    return HttpResponse("Mail Sent")
    

