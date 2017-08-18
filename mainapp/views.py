

from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError

from django.shortcuts import render, render_to_response




from django.http import HttpResponse, HttpResponseRedirect




from django.shortcuts import redirect

from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template

from mainapp.models import ContactInfo,ContactLinks,Design_photo,Design_projects,Arch_photo,Arch_projects,Architects_supervision,Paragraphs_AS,Architecture,Paragraphs_Arch_SD,Paragraphs_Arch_DD,Paragraphs_Arch_CD,Interior_design,Paragraphs_ID,Product_design,Paragraphs_PD
from mainapp.forms import ContactForm



def index(request):
    return render(request, 'home.html')

def architecture(request):
    xcontent = {
        'Arch_projects' : Arch_projects.objects.all().order_by('number'),
    }
    return render(request, 'architecture.html', xcontent)

def design(request):
    xcontent = {
        'Design_projects' : Design_projects.objects.all().order_by('number'),
    }
    return render(request, 'design.html', xcontent)

def archproject(request, pk):
    photos = {

        'Arch_projects' : Arch_projects.objects.all().filter(id=pk),
        'Arch_photo' : Arch_photo.objects.all().filter(project_id=pk),
    }
    return render(request, 'archproject.html', photos)

def designproject(request, pk):
    photos = {

        'Design_projects' : Design_projects.objects.all().filter(id=pk),
        'Design_photo' : Design_photo.objects.all().filter(project_id=pk),
    }
    return render(request, 'designproject.html', photos)

def services(request):
    content = {
        'Architects_supervision' : Architects_supervision.objects.all(),
        'Paragraphs_AS' : Paragraphs_AS.objects.all(),
        'Architecture' : Architecture.objects.all(),
        'Paragraphs_Arch_SD' : Paragraphs_Arch_SD.objects.all(),
        'Paragraphs_Arch_DD' : Paragraphs_Arch_DD.objects.all(),
        'Paragraphs_Arch_CD' : Paragraphs_Arch_CD.objects.all(),
        'Interior_design' : Interior_design.objects.all(),
        'Paragraphs_ID' : Paragraphs_ID.objects.all(),
        'Product_design' : Product_design.objects.all(),
        'Paragraphs_PD' : Paragraphs_PD.objects.all(),
    }
    return render(request, 'services.html', content)


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print('yes')
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        subject = form.cleaned_data.get('subject')
        message = form.cleaned_data.get('message')
        from_email = settings.EMAIL_HOST_USER
        contact_message= "NAME: \n%s \n\nMESSAGE: \n%s \n\n from %s"%(
                name,
                message,
                email)
        send_mail(subject,contact_message,from_email,['office@agarch.com.ua'],fail_silently=False)

    xcontent = {
        'form': form,
        'ContactInfo' : ContactInfo.objects.all().order_by('number'),
        'ContactLinks' : ContactLinks.objects.all().order_by('number'),
    }
    return render(request, "contact.html", xcontent)




def thanks(request):
    return HttpResponse('Thank you for your message.')
#### RU ####

def ruindex(request):
    return render(request, 'ruhome.html')

def ruarchitecture(request):
    xcontent = {
        'Arch_projects' : Arch_projects.objects.all().order_by('number'),
    }
    return render(request, 'ruarchitecture.html', xcontent)

def rudesign(request):
    xcontent = {
        'Design_projects' : Design_projects.objects.all().order_by('number'),
    }
    return render(request, 'rudesign.html', xcontent)

def ruarchproject(request, pk):
    photos = {

        'Arch_projects' : Arch_projects.objects.all().filter(id=pk),
        'Arch_photo' : Arch_photo.objects.all().filter(project_id=pk),
    }
    return render(request, 'ruarchproject.html', photos)

def rudesignproject(request, pk):
    photos = {

        'Design_projects' : Design_projects.objects.all().filter(id=pk),
        'Design_photo' : Design_photo.objects.all().filter(project_id=pk),
    }
    return render(request, 'rudesignproject.html', photos)

def ruservices(request):
    content = {
        'Architects_supervision' : Architects_supervision.objects.all(),
        'Paragraphs_AS' : Paragraphs_AS.objects.all(),
        'Architecture' : Architecture.objects.all(),
        'Paragraphs_Arch_SD' : Paragraphs_Arch_SD.objects.all(),
        'Paragraphs_Arch_DD' : Paragraphs_Arch_DD.objects.all(),
        'Paragraphs_Arch_CD' : Paragraphs_Arch_CD.objects.all(),
        'Interior_design' : Interior_design.objects.all(),
        'Paragraphs_ID' : Paragraphs_ID.objects.all(),
        'Product_design' : Product_design.objects.all(),
        'Paragraphs_PD' : Paragraphs_PD.objects.all(),
    }
    return render(request, 'ruservices.html', content)

def rucontact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print('yes')
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        subject = form.cleaned_data.get('subject')
        message = form.cleaned_data.get('message')
        from_email = settings.EMAIL_HOST_USER
        contact_message= "NAME: \n%s \n\nMESSAGE: \n%s \n\n from %s"%(
                name,
                message,
                email)
        send_mail(subject,contact_message,from_email,['office@agarch.com.ua'],fail_silently=False)

    xcontent = {
        'form': form,
        'ContactInfo' : ContactInfo.objects.all().order_by('number'),
        'ContactLinks' : ContactLinks.objects.all().order_by('number'),
    }
    return render(request, "rucontact.html", xcontent)

#### UA ####

def uaindex(request):
    return render(request, 'uahome.html')

def uadesign(request):
    xcontent = {
        'Design_projects' : Design_projects.objects.all().order_by('number'),
    }
    return render(request, 'uadesign.html', xcontent)

def uaarchitecture(request):
    xcontent = {
        'Arch_projects' : Arch_projects.objects.all().order_by('number'),
    }
    return render(request, 'uaarchitecture.html', xcontent)


def uaarchproject(request, pk):
    photos = {

        'Arch_projects' : Arch_projects.objects.all().filter(id=pk),
        'Arch_photo' : Arch_photo.objects.all().filter(project_id=pk),
    }
    return render(request, 'uaarchproject.html', photos)

def uadesignproject(request, pk):
    photos = {

        'Design_projects' : Design_projects.objects.all().filter(id=pk),
        'Design_photo' : Design_photo.objects.all().filter(project_id=pk),
    }
    return render(request, 'uadesignproject.html', photos)

def uaservices(request):
    content = {
        'Architects_supervision' : Architects_supervision.objects.all(),
        'Paragraphs_AS' : Paragraphs_AS.objects.all(),
        'Architecture' : Architecture.objects.all(),
        'Paragraphs_Arch_SD' : Paragraphs_Arch_SD.objects.all(),
        'Paragraphs_Arch_DD' : Paragraphs_Arch_DD.objects.all(),
        'Paragraphs_Arch_CD' : Paragraphs_Arch_CD.objects.all(),
        'Interior_design' : Interior_design.objects.all(),
        'Paragraphs_ID' : Paragraphs_ID.objects.all(),
        'Product_design' : Product_design.objects.all(),
        'Paragraphs_PD' : Paragraphs_PD.objects.all(),
    }
    return render(request, 'uaservices.html', content)

def uacontact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print('yes')
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        subject = form.cleaned_data.get('subject')
        message = form.cleaned_data.get('message')
        from_email = settings.EMAIL_HOST_USER
        contact_message= "NAME: \n%s \n\nMESSAGE: \n%s \n\n from %s"%(
                name,
                message,
                email)
        send_mail(subject,contact_message,from_email,['office@agarch.com.ua'],fail_silently=False)

    xcontent = {
        'form': form,
        'ContactInfo' : ContactInfo.objects.all().order_by('number'),
        'ContactLinks' : ContactLinks.objects.all().order_by('number'),
    }
    return render(request, "uacontact.html", xcontent)
