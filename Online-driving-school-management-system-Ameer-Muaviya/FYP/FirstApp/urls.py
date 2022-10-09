from django import views
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [ 
    path('', views.index),
    path('signup/', views.signup,name='signup'),
    path('markAttendence/<str:name>', views.markAttendence,name='markAttendence'),
    path('adminDashboard/notificationHistory/delete/<int:id>', views.deleteNotification ,name='deleteNotification'),
    path('adminDashboard/managePrograms/', views.managePrograms ,name='managePrograms'),
    path('studentAdminPanel/myPrograms', views.showPrograms ,name='myPrograms'),
    path('adminDashboard/manageNotifications', views.manageNotifications ,name='manageNotifications'), 
    path('logout/', views.logoutUser,name='logout'),
    path('adminDashboard/attendence/', views.manageAttendence,name='manageAttendence'),
    path('studentAdminPanel/setting',views.settings,name='settings'),
    path('studentAdminPanel/update',views.updateUser,name='update'),
    path('studentAdminPanel/changePassword',views.changePassword,name='changePassword'),
    path('login/', views.loginForm,name='login'),
    path('deleteStudent/<str:username>',views.deleteStudent,name='deleteStudent'),
    path('recoveryEmail/', views.recoveryEmail),
    path('recoveryEmail/confirmCode', views.confirmCode),
    path('recoveryEmail/newPassword/', views.newPassword),
    path('studentAdminPanel/', views.studentAdminPanel),
    path('studentAdminPanel/calenderstd/', views.calenderstd),
    path('adminLogin/', views.adminLogin),
    path('adminDashboard/', views.adminDashboard,name='adminDashboard'),
    # path('adminDashboard/manageLinks/', views.manageLinks,name='manageLinks'),
    path('changePrograms/<str:action>/<int:id>', views.changeProgram,name='changeProgram'),

    path('manageLinks/', views.manageLinks,name='manageLinks'),
    path('manageLinks/delete/<int:id>', views.deleteLink,name='deleteLink'),
    path('manageAssignments/', views.manageAssignments,name='manageAssignments'),
    path('deleteAssignment/delete/<str:name>/<str:student>/', views.deleteAssignments,name='deleteAssignment'),
    path('submitAssignment/', views.submitAssignment,name='submitAssignment'),
    path('pendingAssignments/', views.pendingAssignments,name='pendingAssignments'),
    path('pendingAssignments/delete/<int:id>', views.deletePendingAssignment,name='deletePendingAssignment'),
    path('approveAssignment/<str:name>/<str:date>/<str:state>', views.approveAssignment,name='approveAssignment'),
    path('clearAttendence/', views.clearAttendence,name='clearAttendence'),

 
    path('manageStudent/', views.manageStudent,name='manageStudents'),

    path('manageVehicels/', views.manageVehicels,name='manageVehicels'),
    path('manageVehicels/<str:action>/<int:id>', views.changeVehicle,name='changeVehicle'),
    
    path('manageInstructor/', views.manageInstructor,name='manageInstructors'),
    path('manageInstructor/<str:action>/<int:id>', views.changeInstructor,name='alterInstructor'),
    path('manageCourses/', views.manageCourses,name='manageCourses'),
 
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)