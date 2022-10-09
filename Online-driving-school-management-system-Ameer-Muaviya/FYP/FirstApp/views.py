from django.shortcuts import redirect, render
from django.http import HttpResponse
from FirstApp.models import Assignments, Instructor, Links, Notifications, Programs, Students, Attendence, SubmitAssignment,ManageVehicles 

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User 
from datetime import date, timedelta, datetime
from django.contrib.auth.decorators import login_required
import os,re


# Create your views here.
def index(request):
    return render(request, 'index.html')

# method for udpating user password (uer login required)
def changePassword(request):
    if request.method == 'POST':
        old_password = request.POST.get('oldpassword')
        newpassword = request.POST.get('newpassword')
        u = User.objects.get(username__exact=request.user)
        user = authenticate(username=request.user, password=old_password)
        if user is not None:
            u.set_password(newpassword)
            u.save()
            logout(request)
            return redirect('/login')
        else:
            content = {
                'type': 'danger',
                'message': 'Old password isn\'t correct'
            }
            return render(request, 'changePassword.html', {'content': content})
    return render(request, 'changePassword.html')


# signup form for local user

def signup(request):
    vehicles=ManageVehicles.objects.all()
    context = {'message': None,'vehicles': vehicles}
    if request.method == 'POST':
        try:
            pic = request.FILES['profile_pic']
            if(not (pic.name.endswith('.img') or pic.name.endswith('.png') or pic.name.endswith('.jpg') or pic.name.endswith('.jpeg'))):
                context['message']='invalidImageError'
                return render(request, 'signup.html', {'context': context})
        except Exception:
            pic=None
        name = request.POST.get('Name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        vehicle = request.POST.get('course_name')
        time = request.POST.get('time')
        if(password != confirm_password):
            context['message']='confirmPasswordError'
            return render(request, 'signup.html', {'context': context})
        try:
            user = User.objects.create_user(username=name, email=email, password=password)
            newStd = Students(username=name, email=email, phone=phone, address=address,
                              age=age, gender=gender, vehicle=vehicle, time=time,profile_pic=pic)
            user.save()
            newStd.save()
            login(request, user)
        except Exception as e:
            context['message']='invalidUsernameError'
            return render(request, 'signup.html', {'context': context})
        return redirect('/studentAdminPanel')
    return render(request, 'signup.html',{'context':context})

# method for logging out any user e.g localUser,adminUser
def logoutUser(request):
    logout(request)
    return redirect('/')

# method for updating user after user updates his credentials (user login required)

@login_required(login_url='login')
def updateUser(request):
    if request.method == 'POST':
        name = request.POST.get('Name')
        if(str(request.user) != name):
            getName = User.objects.all().filter(username=name)
            if(len(getName) != 0):
                return HttpResponse('this username already exists select another one')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        course = request.POST.get('vehicle_name')
        time = request.POST.get('time')
        ins = Students.objects.get(username=request.user)
        #change name in notifications
        ntfs=Notifications.objects.all().filter(username=request.user)
        stds=Assignments.objects.all().filter(username=request.user)
        submitAssignment=SubmitAssignment.objects.all().filter(username=request.user)
        att=Attendence.objects.all().filter(username=request.user)
        arr=[stds,submitAssignment,ntfs,att]
        for i in arr:
            for j in i:
                j.username=name
                j.save()
        userins = User.objects.get(username=request.user)
        ins.username = name
        ins.phone = phone
        ins.address = address
        ins.email = email
        ins.age = age
        ins.gender = gender
        ins.vehicle = course
        ins.time = time
        userins.username = name
        try:
            pic = request.FILES['profile_pic']
            if(not (pic.name.endswith('.img') or pic.name.endswith('.png') or pic.name.endswith('.jpg'))):
                return HttpResponse('please select a valid image !')
            if(ins.profile_pic):
                os.remove(ins.profile_pic.path)
            ins.profile_pic=pic
        except Exception as e:
            pass
        ins.save()
        userins.save()
        logout(request)
        return redirect('/login')

# user personal details manager! (localuser login required)
@login_required(login_url='login')
def settings(request):
    vehicles=ManageVehicles.objects.all()
    # print(request.user)
    ins = Students.objects.get(username=request.user)
    return render(request, 'settings.html', {'data': ins,'vhs':vehicles})

# user login form
def loginForm(request):
    if request.user.is_authenticated and not(request.user.is_superuser):
        return redirect('/studentAdminPanel')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/studentAdminPanel')
    return render(request, 'login.html')


# Marking user attendence (user Login required)
@login_required(login_url='login')
def markAttendence(request, name):
    if (str(request.user) == name):
        markAll(date.today())
        date_now = date.today()
        # print(name)
        check = Attendence.objects.all().filter(
            username=name, date=date_now, status='Present')
        # print(check)
        if(len(check) != 0):
            return redirect('/studentAdminPanel')
        newstudent = Attendence.objects.get(
            date=date_now, username=name, status='Absent')
        newstudent.status = 'Present'
        newstudent.save()
        # print('attendence saved !')
        return redirect('/studentAdminPanel')
    return HttpResponse(status=404)



def clearAttendence(request):
    if isAdmin(request.user):
        att=Attendence.objects.all()
        for i in att:
            i.delete()
        return redirect('manageAttendence')


# absent laga do agar abhi tak attendence mark nahi ki to !
def markAll(_date):
    allStds = Students.objects.all()
    date_today = _date
    for i in allStds:
        try:
            Attendence.objects.get(
                username=i.username, date=date_today, status='Present')
        except Exception as e:
            # check if already marked absent
            check_absent = Attendence.objects.all().filter(
                username=i.username, date=date_today, status='Absent')
            if(len(check_absent) == 0):
                newatt = Attendence(
                    username=i.username, date=date_today, status='Absent')
                newatt.save()

# manage students attendence (admin login required)
def manageAttendence(request):
    if isAdmin(request.user):
        markAll(date.today())
        attendence = []
        lday = date.today()
        context = {}
        try:
            fday = Attendence.objects.first().date  # Getting First date
        except Exception as e:
            return render(request, 'attendence.html', {'data':None})
        while(lday != fday-timedelta(days=1)):
            day = lday
            todayAttendence = Attendence.objects.all().filter(date=day)
            if(len(todayAttendence) <= 0):
                markAll(day) # if attendence of a specific day isn't found mark absend of all stds
            attendence.append(
                    {'todayAttendence': todayAttendence, 'date': day})
            lday = day-timedelta(days=1)
            context = {'attendence': attendence}
        return render(request, 'attendence.html', context)
    else:
        return HttpResponse(status=404)


# TODO

def recoveryEmail(request):
    return render(request, 'recoveryEmail.html')

# TODO


def confirmCode(request):
    return render(request, 'confirmCode.html')

# TODO


def newPassword(request):
    return render(request, 'newPassword.html')

def split(strng,chr):
    return strng.split(chr)

# user home page (user login required)

@login_required(login_url='login')
def studentAdminPanel(request):
    if request.user.is_superuser:
        return redirect('/login')
    name = request.user
    check = Attendence.objects.all().filter(username=name, date=date.today(), status='Present')
    message = ''
    pic=Students.objects.get(username=request.user).profile_pic
    if(len(check) != 0):
        message = 'You have marked your attendence'
    allNotifications = Notifications.objects.all().filter(username=request.user)
    docs = Assignments.objects.all().filter(username=str(request.user))
    try:
        result=SubmitAssignment.objects.get(username=str(request.user)).state
    except Exception as e:
        result='No Assignments uploaded Yet'
    return render(request, 'studentAdminPanel.html', {'notifications': allNotifications, 'message': message, 'docs': docs,'result':result,'profile_pic':pic,'links':Links.objects.all().filter(username=request.user),'split':split})

# TODO

def calenderstd(request):
    return render(request, 'calenderstd.html')

# admin login page
def adminLogin(request):
    if request.user.is_active and request.user.is_superuser:
        return redirect('/adminDashboard')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('/adminDashboard')
    return render(request, 'adminLogin.html')

# display admin Dashboard (admin login required)
def adminDashboard(request):
    if not(isAdmin(request.user)):
        return redirect('/login')
    return render(request, 'adminDashboard.html')

# TODO

def manageLinks(request):
    if not isAdmin(request.user):
        return HttpResponse(status=404)
    links = Links.objects.all()
    stds=Students.objects.all()
    if(not len(links)):
        links = None
    if request.method == 'POST':
        students = request.POST.get('students')
        message = request.POST.get('message').split('/')[3]
        extractedNames = students.split(',')
        print('extracted names :',extractedNames)
        for i in extractedNames:
            link = Links(username=i, link=message)
            link.save()
        return redirect('manageLinks')
    return render(request, 'manageLinks.html', {'links': links,'students':stds})

def deleteLink(request,id):
    if not isAdmin(request.user):
        return HttpResponse(status=404)
    Links.objects.get(id=id).delete()
    return redirect('manageLinks')

# method to set program for users and manage all settings for user (admin login required)sssssass
def manageStudent(request):
    if isAdmin(request.user):
        students = Students.objects.all()
        if(len(students) == 0):
            students = None
        context = {'students': students}
        return render(request, 'manageStudent.html', context)
    else:
        return HttpResponse(status=404)

# manage students (remove user) (admin login required)

def deleteStudent(request, username):
    if request.user.is_anonymous or not isAdmin(request.user):
        return redirect('/login')

    u=Students.objects.get(username=username)
    if (u.profile_pic and os.path.exists(u.profile_pic.path)):
             os.remove(u.profile_pic.path)
    u.delete()
    deleteAllAssignments(username) #delete it's all the data and assignments from media dir
    clearData(Attendence,username) #clear all the attendence data
    clearData(User,username) # clear all user data
    clearData(Notifications,username) # clear all notification associated with his name !
    clearData(Links,username) # remove all links associated with his name !
    return redirect('/manageStudent')

def deleteAllAssignments(student):
    #delete submitted assignments !
        submitAssignment=SubmitAssignment.objects.all().filter(username=student)
        for i in submitAssignment:
                if(os.path.exists(i.file.path)):
                    os.remove(i.file.path)
                i.delete()
    #delete assigned assignmets !        
        assignment = Assignments.objects.all().filter( username=student)
        for i in assignment:
                if(os.path.exists(i.file.path)):
                    os.remove(i.file.path)
                i.delete()
        return 1
        

def clearData(model,name):
    a=model.objects.all().filter(username=name)
    for i in a:
        i.delete()

# method to list all programs used by various users (admin login required)

def showPrograms(request):
    try:
        vehicle = Students.objects.get(username=request.user).vehicle
        print(vehicle,'   vehicls is tis')
        vh_details=ManageVehicles.objects.get(name=vehicle)
        programs = Programs.objects.get(vehicle=vehicle)
    except Exception as e:
        print('here',e)
        programs=None
        vehicle=None
        vh_details=None
    return render(request, 'Myprograms.html', {'data': programs,'vh':vh_details})

# Getting content from admin and storing into database (admin login required)
def sendNotification(request):
    if not(isAdmin(request.user)):
        return redirect('/login')
    if request.method == 'POST':
        students = request.POST.get('students')
        message = request.POST.get('message')
        extractedNames = students.split(',')
        for i in extractedNames:
            notification = Notifications(username=i, message=message,date=datetime.now())
            notification.save()
    return render(request,'sendNotification.html')

# manage vehicles
def manageVehicels(request):
    if isAdmin(request.user):
        allVehicles=ManageVehicles.objects.all()
        notification={'msgtype':None}
        if request.method=='POST':
            name = request.POST.get('name')
            fee = request.POST.get('fee')
            number = request.POST.get('number')
            try:
                data=ManageVehicles(name=name,fee=fee,number=number)
                data.save()
                notification['msgtype']='success'
            except Exception as e:
                notification['msgtype']='danger'
    return render(request, 'manageVehicels.html',{'notification':notification,'allVehicles':allVehicles})

# Edit or remove a Vehicle
def changeVehicle(request,id,action):
    if not isAdmin(request.user):
        return HttpResponse('not found')
    vehicle_data=ManageVehicles.objects.get(id=id)
    if action=='delete':
        pgs=Programs.objects.all().filter(vehicle=vehicle_data.name)
        if(pgs):
            return redirect('manageVehicels')
        vehicle_data.delete()
    elif action=='update':
        if request.method=='POST':
            name=request.POST.get('name')
            try:
                student=Students.objects.get(vehicle=vehicle_data.name)
                program=Programs.objects.get(vehicle=vehicle_data.name)
                student.vehicle=name
                program.vehicle=name
                student.save()
                program.save()
            except Exception as e:
                print('user or program not found ',e)
            vehicle_data.name=name
            vehicle_data.number=request.POST.get('number')
            vehicle_data.fee=request.POST.get('fee')
            vehicle_data.save()
            return redirect('manageVehicels')   
        return render(request,'edit_vehicle.html',{'vehicleData':vehicle_data})
    return redirect('manageVehicels')

# add/display Instructors (admin Login requred)
def manageInstructor(request):
    if not isAdmin(request.user):
        return redirect ('/')
    ins=Instructor.objects.all()
    context={'instructors':(None if not len(ins) else ins),'message':None}
    if request.method=='POST':
        name=request.POST.get('name')
        experience=request.POST.get('experience')
        sallary=request.POST.get('sallary')
        phone=request.POST.get('phone')
        try:
            a=Instructor(name=name,experience=experience,sallary=sallary,number=phone)
            a.save()
            return redirect('manageInstructors')
        except Exception:
            context['message']='existingCredentials'
    return render(request, 'manageInstructor.html',{'context':context})

# update/delete Instructors
def changeInstructor(request,action,id):
    if not isAdmin(request.user):
        return redirect('/')
    validate_phone_number_pattern = "^\\+?[1-9][0-9]{7,14}$"
    ins=Instructor.objects.get(id=id) 
    context={'instructor':ins,'msg':None}
    if action=='delete':
        pgs=Programs.objects.all().filter(instructor=ins.name)
        if(pgs):
            return redirect('manageInstructors')
        ins.delete()
        return redirect('manageInstructors')
    elif action=='update':
        if request.method=='POST':
            name=request.POST.get('name')
            try:
                program=Programs.objects.get(instructor=ins.name)
                program.instructor=name
                program.save()
            except Exception as e:
                print('user or program not found ',e)
            ins.number=request.POST.get('phone')
            matched=re.match(validate_phone_number_pattern, ins.number) 
            if not matched:
                context['msg']='invalidPhone'
            ins.name=name
            ins.experience=request.POST.get('experience')
            ins.sallary=request.POST.get('sallary') 
            try:
                ins.save()
            except Exception as e:
                context['msg']='exists'
            if (context['msg']):
                print('message is :',context['msg']) 
                return render(request,'updateInstructors.html',context)
            else:
                return redirect('manageInstructors')
        return render(request,'updateInstructors.html',context)
    return redirect('manageInstructors')
# TODO


def manageCourses(request):
    return render(request, 'manageCourses.html')

# method to manage user programs from admin side (admin login required)


def managePrograms(request):
    if not(isAdmin(request.user)):
        return redirect('/login')
    allPrograms=Programs.objects.all()
    context={'message':None,'vehicles':ManageVehicles.objects.all(),'programs':(None if not len(allPrograms) else allPrograms),'instructors':Instructor.objects.all()}
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            summary = request.POST.get('summary')
            vehicle = request.POST.get('vehicle')
            instructor = request.POST.get('instructor')
            newprogram = Programs(program_name=name, summary=summary, vehicle=vehicle,instructor=instructor)
            newprogram.save()
            return redirect('managePrograms')
        except Exception as e: 
            if(str(e).split('.')[1]=='category'):
                context['message']='existingVehicleError'
                return render(request, 'managePrograms.html',{'context':context} )
            elif(str(e).split('.')[1]=='instructor'):
                context['message']='insNotAvailable'
    return render(request, 'managePrograms.html',{'context':context} )


# method to remove user programs (admin login required)
def changeProgram(request,action, id):
    if not(isAdmin(request.user)):
        return redirect('/login')
    program = Programs.objects.get(id=id)
    context={'program':program,'vehicles':ManageVehicles.objects.all(),'instructors':Instructor.objects.all(),'message':None}
    if action=='delete':
        program.delete()
    elif action=='update':
        if request.method=='POST':
            program.program_name = request.POST.get('name')
            program.summary = request.POST.get('summary')
            program.vehicle = request.POST.get('vehicle')
            program.instructor = request.POST.get('instructor')
            try:
                program.save()
                return redirect('managePrograms')
            except Exception as e: 
                if(str(e).split('.')[1]=='category'):
                    context['message']='existingVehicleError'
                    return render(request, 'updateProgram.html',{'data':context} )
                elif(str(e).split('.')[1]=='instructor'):
                    context['message']='insNotAvailable'
        return render(request ,'updateProgram.html',{'data':context})
    return redirect('managePrograms')


# method to get all notifications on admin panel (admin login required)

def manageNotifications(request):
    if not(isAdmin(request.user)):
        return redirect('/login')
    notifications = Notifications.objects.all()
    stds=Students.objects.all()
    if(len(notifications) == 0):
        notifications = None
    if request.method == 'POST':
        students = request.POST.get('students')
        message = request.POST.get('message')
        extractedNames = students.split(',')
        for i in extractedNames:
            notification = Notifications(username=i, message=message,date=datetime.now())
            notification.save()
            return redirect('manageNotifications')
    return render(request, 'manageNotifications.html', {'notifications': notifications,'students':stds})

# method to check if user is super user (admin or not)
def isAdmin(user):
    return user.is_superuser

# method for deleting notification (admin login required)

def deleteNotification(request,id):
    if not(isAdmin(request.user)):
        return redirect('/login')
    notification = Notifications.objects.get(id=id)
    notification.delete()
    return redirect('manageNotifications')


# add and display assignments (admin login required)
def manageAssignments(request):
    if not(isAdmin(request.user)):
        return redirect('/login')
    allAssignments = Assignments.objects.all()
    context = {
        'students': (Students.objects.all() if len(Students.objects.all()) else None), 'assignments': allAssignments if len(allAssignments) else None
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        checkAssignment = allAssignments.filter(name=name)
        alert = {
            'type': 'danger', 
            'message': 'An assignment with this name already exists. Please choose a Unique name for Assignments', 
            'visibility': 'visible'
                }
        if (len(checkAssignment)):
            return render(request, 'manageAssignments.html', {'context': context, 'alert': alert})
        std_names = request.POST.get('students').split(',')
        if (std_names[0] == ''):
            alert['message'] = 'Please select at least one student !'
            return render(request, 'manageAssignments.html', {'context': context, 'alert': alert})
        file = request.FILES['doc_file']
        for i in std_names: #send same assignment to selected students individually !
            newassignment = Assignments(name=name, username=i, file=file)
            newassignment.save()
    allAssignments = Assignments.objects.all()
    if(len(allAssignments)):
        context['assignments'] = Assignments.objects.all()
    return render(request, 'manageAssignments.html', {'context': context})


# delete the assignment (admin login required)
def deleteAssignments(request, name, student):
    if(isAdmin(request.user)):
        assignment = Assignments.objects.get(name=name, username=student)
        if(os.path.exists(assignment.file.path)):
            os.remove(assignment.file.path)# remove the file associated with that user or assignment
        assignment.delete()
        return redirect('/manageAssignments')
    return HttpResponse(status=400) 

# user assignment submission (user login required !)
@login_required(login_url='login/')
def submitAssignment(request): 
    if request.method=='POST':
        file=request.FILES['file']
        try:
            # try to get previous submitted assignmets of user 
            prev_assignments=SubmitAssignment.objects.get(username=str(request.user))
            os.remove(prev_assignments.file.path)
            prev_assignments.file=file
            prev_assignments.date=datetime.now()
            prev_assignments.state='Pending'
            prev_assignments.save()
            # create a new assignment of doesn't exist !
        except Exception as e:
            newassignment=SubmitAssignment(date=datetime.now(),username=str(request.user),state='Pending',file=file)
            newassignment.save()
    return redirect('/studentAdminPanel')

def pendingAssignments(request):
    pendings=SubmitAssignment.objects.all().filter(state='Pending')
    if(not len(pendings)):
        pendings=None
    return render(request,'pendingAssignments.html',{'assignments':pendings})

def approveAssignment(request,name,date,state):
    assignment=SubmitAssignment.objects.get(username=name,date=date)
    assignment.state=state
    assignment.save()
    return redirect('/pendingAssignments')

#method of removing pending assignments form the database (admin Login required!)
def deletePendingAssignment(request,id):
    if isAdmin(request.user):
        assignment=SubmitAssignment.objects.get(id=id)
        assignment.state='Fail'
        assignment.save()
        return redirect('/pendingAssignments')
