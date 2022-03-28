from asyncio.windows_events import NULL
from django.http import HttpResponse
from django.shortcuts import render,redirect
from flask import request
from pyparsing import col
from .models import Content,Category,Note,Resume
from home.models import Course
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm,NoteForm
from django.contrib import messages

from django.contrib.auth import authenticate, login

from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):

    list = []
    for menu in Category.objects.all().order_by('id'):
        menus = {}
        menus["menu"] =menu.name
        menus["id"] =menu.id
        # return HttpResponse(Content.objects.get(category=menu.id))
        sub=Content.objects.filter(category_id=menu.id).values('title','category_id','id','slug')
        menus["submenus"] =sub
        list.append(menus)
        # return HttpResponse( menus["submenus"])

    return render(request,'home.html',{'menus':list})
    # return HttpResponse(Content.objects.get(category_id=menu.id))

def course_list(request,foo):
    list = []
    course = Course.objects.get(course_name= foo)
    for menu in Category.objects.select_related('course').filter(course_id=course.id):
        menus = {}
        menus["menu"] =menu.name
        menus["id"] =menu.id
        # return HttpResponse(Content.objects.get(category=menu.id))
        sub=Content.objects.filter(category_id=menu.id).values('title','category_id','id','slug')
        menus["submenus"] =sub
        list.append(menus)
        # return HttpResponse( menus["submenus"])

    return render(request,'home.html',{'menus':list,'course':foo})


class BlogDetailView(DetailView):
    model = Content

    context_object_name = 'content'
    template_name = 'content_details.html'

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        list = []
        course = Course.objects.get(course_name= self.kwargs['foo'])
        context['course']=course
        for menu in Category.objects.select_related('course').filter(course_id=course.id):
            menus = {}
            menus["menu"] =menu.name
            menus["id"] =menu.id
            # return HttpResponse(Content.objects.get(category=menu.id))
            sub=Content.objects.filter(category_id=menu.id).values('title','category_id','id','slug')
            menus["submenus"] =sub
            menus["submenus"] =sub
            list.append(menus)
        context['menus'] = list
        return context 

def search(request,foo):
    results = []
    list = []
    course = Course.objects.get(course_name= foo)
    for menu in Category.objects.select_related('course').filter(course_id=course.id):
        menus = {}
        menus["menu"] =menu.name
        menus["id"] =menu.id
        # return HttpResponse(Content.objects.get(category=menu.id))
        sub=Content.objects.filter(category_id=menu.id)
        menus["submenus"] =sub
        list.append(menus)
    if request.method == "GET":
        query = request.GET.get('search')
        if query == '':
            query = 'None'
        results = Content.objects.filter(Q(title__icontains=query) | Q(slug__icontains=query) | Q(body__icontains=query) )

    return render(request, 'search.html', {'query': query, 'results': results,'menus':list,'course':foo})


# def login(request):
#     return render(request,'login.html')


# ########### register here #####################################
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            ######################### mail system ####################################
            # htmly = get_template('user/Email.html')
            # d = { 'username': username }
            # subject, from_email, to = 'welcome', 'your_email@gmail.com', email
            # html_content = htmly.render(d)
            # msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            # msg.attach_alternative(html_content, "text/html")
            # msg.send()
            ##################################################################
            messages.success(request, f'Your account has been created ! You are now able to log in')
            return redirect('/cms/login')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form, 'title':'reqister here'})
  
# ################ login forms###################################################
# def Login(request):
#     if request.method == 'POST':
  
#         # AuthenticationForm_can_also_be_used__
  
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username = username, password = password)
#         if user is not None:
#             # form = login(request, user)
#             messages.success(request, f' wecome {username} !!')
#             return redirect('/cms/')
#         else:
#             messages.info(request, f'account done not exit plz sign in')
#     form = AuthenticationForm()
#     return render(request, 'login.html', {'form':form, 'title':'log in'})

@login_required(login_url='/accounts/login/')
def dashboard(request):
    note=Note.objects.filter(user_id=request.user.id).order_by('-id')
    return render(request,'dashboard.html',{'note':note})

@login_required(login_url='/accounts/login/')
def note_details(request,id):
    note =Note.objects.get(id=id)
    return render(request,'note_details.html',{'note':note})

@login_required(login_url='/accounts/login/')
def add_note(request):
    # form = NoteForm()
    # return render(request, 'add_note.html', {'form': form})
    form =NoteForm()
    if request.method =='POST':
        form=NoteForm(request.POST)
        
        # return HttpResponse(form)
        if form.is_valid():
            # form.save()
            obj = Note() #gets new object
            obj.title = form.cleaned_data['title']
            obj.message = form.cleaned_data['message']
            obj.user_id = request.user.id
            obj.save()
            return redirect('/cms/dashboard/')
        else:
            return HttpResponse(form.errors)
    else:
        # return HttpResponse('okay')
        return render(request, 'add_note.html', {'form': form})

@login_required(login_url='/accounts/login/')
def delete(request,id):
    student =Note.objects.get(id=id)
    student.delete()
    # return redirect('/students/list')
    return redirect('/cms/dashboard/')

@login_required(login_url='/accounts/login/')
def update_note(request):
    if request.method =='GET':
        
            # if request.GET['color'] == 3:
            #     color ='bg_btn_chose_2'
            # elif request.GET['color'] == 1:
            #     color ='bg_btn_chose_1'
            # else:
            #     color ='bg_btn_chose_3'

            note =Note.objects.get(id=request.GET['note_id'])
            note.color = 'bg_btn_chose_'+request.GET['color']
            note.save()
            # return HttpResponse(color)
            return redirect('/cms/dashboard/')
      
    else:
        return redirect('/cms/dashboard/')

@login_required(login_url='/accounts/login/')
def search_notes(request):
    note = []
 
    if request.method == "GET":
        query = request.GET.get('search')
        if query == '':
            query = 'None'
        note = Note.objects.filter(Q(title__icontains=query) | Q(message__icontains=query)).filter(user_id=request.user.id)

        return render(request,'dashboard.html',{'note':note,'query':query})

@login_required(login_url='/accounts/login/')
def create_resume(request):

    if request.method=="POST":
            obj=Resume.objects.get(user_id=request.user.id)
            if obj == NULL:
            
                obj=Resume()

            obj.user_id=request.user.id
            obj.full_name=request.POST.get("name")
            obj.address=request.POST.get("address")
            obj.phone=request.POST.get("phone")
            obj.email=request.POST.get("email")
            obj.about_you=request.POST.get("about")
            obj.education=request.POST.get("education")
            obj.career=request.POST.get("career")
            obj.job_1_start=request.POST.get("job-1__start")
            obj.job_1_end=request.POST.get("job-1__end")
            obj.job_1_details=request.POST.get("job-1__details")
            obj.job_2_start=request.POST.get("job-2__start")
            obj.job_2_end=request.POST.get("job-2__end")
            obj.job_2_details=request.POST.get("job-2__details")
            obj.job_3_start=request.POST.get("job-3__start")
            obj.job_3_end=request.POST.get("job-3__end")
            obj.job_3_details=request.POST.get("job-3__details")
            obj.references=request.POST.get("references")
            obj.save()
            messages.add_message(request, messages.INFO, 'Resume Info Saved Successfully. Download Resume Now')
            return redirect("cms:resume")
    else:
            try:
                resume_info = Resume.objects.get(user_id= request.user.id)
                
            except Resume.DoesNotExist: 
                resume_info=[] 
            context={"resume_info":resume_info}
            return render(request,"create-resume.html",context)

@login_required(login_url='/accounts/login/')
def resume(request):
        try:
            resume_info = Resume.objects.get(user_id= request.user.id)   
            context={"resume_info":resume_info}
            return render(request,"resume.html",context)
        except Resume.DoesNotExist: 
            resume_info=[]
            messages.add_message(request, messages.INFO, 'Create resume then try Resume')
            return redirect('/cms/create-resume/')
        # resume_info = Resume.objects.get(user_id= request.user.id)
        # context={"resume_info":resume_info}
        # return render(request,"resume.html",context)

@login_required(login_url='/accounts/login/')
def manual_resume(request):
        try:
            resume_info = Resume.objects.get(user_id= request.user.id)   
            context={"resume_info":resume_info}
            return render(request,"manual_resume.html",context)
        except Resume.DoesNotExist: 
            resume_info=[]
            messages.add_message(request, messages.INFO, 'Create resume then try Manual Resume')
            return redirect('/cms/create-resume/')
        
        

@login_required(login_url='/accounts/login/')
def profile(request):
        
        try:
            resume_info = Resume.objects.get(user_id= request.user.id)
            result =resume_info
        except Resume.DoesNotExist: 
            result =[]

        context={"resume_info":result}
        return render(request,"profile.html",context)