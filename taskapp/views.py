from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render



# Create your views here.
from taskapp.models import *


def main(request):
    if request.method=="POST":
        u = request.POST['u']
        p = request.POST['p']
        ob = login.objects.get(uname=u,pswd=p)
        if ob is not None:
            if ob.utype=='admin':
                ob1 = auth.authenticate(username='admin', password='admin')
                auth.login(request,ob1)
                return render(request, 'adminhome.html')
            else:
                request.session['lid']=ob.id
                ob1 = auth.authenticate(username='admin',password='admin')
                auth.login(request, ob1)
                return render(request, 'studenthome.html')

    return render(request,'login.html')




def admin_reg(request):
    if request.method=="POST":
        name = request.POST['n']
        dob = request.POST['d']
        phone = request.POST['p']
        password = request.POST['pass']
        img = request.FILES['file']

        fname = FileSystemStorage()
        path = fname.save(img.name,img)

        ob = login()
        ob.uname = name
        ob.pswd = password
        ob.utype = 'admin'
        ob.save()

        ob1 = admin()
        ob1.name = name
        ob1.dob = dob
        ob1.phone = phone
        ob1.image = path
        ob1.login_id = ob
        ob1.save()

        return HttpResponse('''<script>alert("Registered...");window.location='/' </script>''')
    else:
        return render(request,'admin_reg.html')


def user_reg(request):
    if request.method=="POST":
        name = request.POST['n']
        dob = request.POST['d']
        phone = request.POST['p']
        password = request.POST['pass']
        img = request.FILES['file']

        fname = FileSystemStorage()
        path = fname.save(img.name,img)

        ob = login()
        ob.uname = name
        ob.pswd = password
        ob.utype = 'student'
        ob.save()

        ob1 = student()
        ob1.name = name
        ob1.dob = dob
        ob1.phone = phone
        ob1.image = path
        ob1.login_id = ob
        ob1.save()

        return HttpResponse('''<script>alert("Registered...");window.location='/' </script>''')
    else:
        return render(request,'user_reg.html')

@login_required(login_url='/')
def view_student(request):
    ob = student.objects.all()
    return render(request,'view_users.html',{'data':ob})

@login_required(login_url='/')
def admin_add_mark(request,id):
    if request.method=="POST":
        sub = request.POST['s']
        mark1 = request.POST['m']
        print(sub,mark1,"eeeeeeeeeeeeee")
        ob = mark()
        ob.subject= sub
        ob.mark= mark1
        ob.stud_id = student.objects.get(id = id)
        ob.save()
        return HttpResponse('''<script>alert("Added...");window.location='/view_student' </script>''')
    return render(request,'add_mark.html')

@login_required(login_url='/')
def admin_view_mark(request,id):
    ob = mark.objects.filter(stud_id__id = id)
    return render(request,'view_marks.html',{'data':ob,'uid':id})

@login_required(login_url='/')
def admin_delete_mark(request,id):
    ob = mark.objects.get(id = id)
    ob.delete()
    return HttpResponse('''<script>alert("Deleted...");window.location='/view_student' </script>''')

@login_required(login_url='/')
def student_view_profile(request):
    if request.method=="POST":
        print(request.POST)
        n = request.POST['n']
        # d = request.POST['d']
        p = request.POST['p']

        f = request.FILES['f']
        fname = FileSystemStorage()
        path = fname.save(f.name, f)

        ob1 = student.objects.get(login_id__id=request.session['lid'])
        ob1.name=n
        # ob1.dob=d
        ob1.phone=p
        ob1.image=path
        ob1.save()
        return HttpResponse('''<script>alert("Updated...");window.location='/student_view_profile' </script>''')
    else:
        ob = student.objects.get(login_id__id = request.session['lid'])
        return render(request,'viewprofile.html',{'data':ob,'uid':id})




def logout(request):
    auth.logout(request)
    return HttpResponse('''<script>alert("Logged out...");window.location='/' </script>''')

