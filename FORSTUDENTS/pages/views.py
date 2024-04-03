from django.shortcuts import render ,redirect
from django . contrib.auth.forms import UserCreationForm
from django.shortcuts import render

#from .forms import ProfileForm
from django.contrib import messages
#from .models import UploadFile
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from .models import SignUp
from .models import Apartments
from .forms import SignUpForm,addchemicalclassesform,addcivilclassesform,addclassesform,addelectricclassesform,addmechanicalclassesform,updatemechanicalform
from .forms import addclassesform,addelectricclassesform
from .models import PrivateMechanicalClasses
from .models import PrivateCivilClasses
from .models import PrivateChemicalClasses
from .models import PrivateElectricClasses
from .models import PrivateClasses
#from .forms import addsoftwarclassesform
from django .contrib.auth.models import User
from .models import scholarship
from django .contrib.auth.forms import UserCreationForm
from .filters import PrivateClassesFilter
from django.contrib.auth import authenticate, login,logout
from .forms import CreatUserForm
from django.contrib.auth.models import Group
from django.core.exceptions import ObjectDoesNotExist
from .forms import addApartmentform,addscholarshipform,updateApartmentform,updatescholarshipform,updatesoftwarform,updatecivilform,updateelectricform,updatechemicalform

def masterpage(request):
    return render(request,'masterpage.html')



def SignUpUser(request):
    form = CreatUserForm()
    if request.method == 'POST':
        form = CreatUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            try:
              group =  Group.objects.get(name='Users')
            except ObjectDoesNotExist:
                group=None
            user.groups.add(group)
            messages.success(request, 'Account was created for ' + username)
            return redirect('Loginuser')
    context = {'form': form}
    return render(request, 'pages/SignUpUser.html', context)


def Loginuser(request):
    if request.method == 'POST':
        Username = request.POST.get('username')
        Password = request.POST.get('password')
        user = authenticate(request, username=Username, password=Password)
        if user is not None:
            users_in_group = Group.objects.get(name='Users').user_set.all()
            if user in users_in_group:
                login(request, user)
                return redirect('forusers')
            else:
                messages.info(request, 'username OR password incorrert')
        else:
            messages.info(request, 'username OR password incorrert')
    context = {}
    return render(request, 'pages/Loginuser.html', context)












# def SignUpAdmin(request):
#      form=SignUpForm()
#      # username=request.POST.get('Username')
#      # email=request.POST.get('Email')
#      # password=request.POST.get('Password')
#      # re_Password=request.POST.get('Re_Password')
#      if request.method=='POST':
#           form=SignUpForm(request.POST)

#           if form.is_valid():
#                form.save()
#                return redirect('SignUpStudent')
#     # data=SignUp(Username=username,Email=email,Password=password,Re_Password=re_Password)
#      #data.save()
#      conaxt={'form':form}
#      return render(request,'pages/SignUpAdmin.html',conaxt)


def logoutAdmin(request):
     logout(request)
     
           


def SignUpStudent(request):
    form = CreatUserForm()
    if request.method == 'POST':
        form = CreatUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            try:
              group =  Group.objects.get(name='Students')
            except ObjectDoesNotExist:
                group=None
            user.groups.add(group)
            messages.success(request, 'Account was created for ' + username)
            return redirect('Loginstudent')
    context = {'form': form}
    return render(request, 'pages/SignUpStudent.html', context)



def logoutstudent(request):
 logout(request)

def Loginstudent(request):
    if request.method == 'POST':
        Username = request.POST.get('username')
        Password = request.POST.get('password')
        user = authenticate(request, username=Username, password=Password)
        if user is not None:
            users_in_group = Group.objects.get(name='Students').user_set.all()
            if user in users_in_group:
                login(request, user)
                return redirect('forstudentsusers')
            else:
                messages.info(request, 'username OR password incorrert')
        else:
            messages.info(request, 'username OR password incorrert')
    context = {}
    return render(request, 'pages/Loginstudent.html', context)






def Logiadmin(request):
    if request.method == 'POST':
        Username = request.POST.get('username')
        Password = request.POST.get('password')
        user = authenticate(request, username=Username, password=Password)
        if user is not None:
            users_in_group = Group.objects.get(name='Admin').user_set.all()
            if user in users_in_group:
                login(request, user)
                return redirect('foradmin')
            else:
                messages.info(request, 'username OR password incorrert')
        else:
            messages.info(request, 'username OR password incorrert')
    context = {}
    return render(request, 'pages/Loginadmin.html', context)

               



# def SignUpUser(request):
#      form=SignUpForm()
  
#      if request.method=='POST':
#           form=SignUpForm(request.POST)

#           if form.is_valid():
#                form.save()
#                return redirect('SignUpStudent')
   
#      conaxt={'form':form}
#      return render(request,'pages/SignUpUser.html',conaxt)

def logoutuser(request):
     logout(request)

def addsoftwarclasses(request):
    
        
     form=addclassesform()
     if request.method=='POST':
          form=addclassesform(request.POST)
          if form.is_valid():
               form.save()
               return redirect('forusers')
   
     conaxt={'form':form}
     return render(request,'pages/addsoftwarclasses.html',conaxt)


def More(request):
    return render(request,'pages/More.html')      




def addelectricclasses(request):
    
        
     form=addclassesform()
     if request.method=='POST':
          form=addelectricclassesform(request.POST)
          if form.is_valid():
               form.save()
               return redirect('addclasses')
   
     conaxt={'form':form}
     return render(request,'pages/addelectricclasses.html',conaxt)



def addcivilclasses(request):
    
        
     form=addcivilclassesform()
     if request.method=='POST':
          form=addcivilclassesform(request.POST)
          if form.is_valid():
               form.save()
               return redirect('addclasses')
   
     conaxt={'form':form}
     return render(request,'pages/addcivilclasses.html',conaxt)




def addchemicalclasses(request):
    
        
     form=addchemicalclassesform()
     if request.method=='POST':
          form=addchemicalclassesform(request.POST)
          if form.is_valid():
               form.save()
               return redirect('addclasses')
   
     conaxt={'form':form}
     return render(request,'pages/addchemicalclasses.html',conaxt)



def addscholarship(request):
    
        
     form=addscholarshipform()
     if request.method=='POST':
          form=addscholarshipform(request.POST)
          if form.is_valid():
               form.save()
               return redirect('addclasses')
   
     conaxt={'form':form}
     return render(request,'pages/addscholarship.html',conaxt)






def addmechanicalclasses(request):
    
        
     form=addmechanicalclassesform()
     if request.method=='POST':
          form=addmechanicalclassesform(request.POST)
          if form.is_valid():
               form.save()
               return redirect('addclasses')
   
     conaxt={'form':form}
     return render(request,'pages/addmechanicalclasses.html',conaxt)







def addapartment(request):
     form=addApartmentform()
     if request.method=='POST':
          form=addApartmentform(request.POST)
          if form.is_valid():
               form.save()
               return redirect('addclasses')
   
     conaxt={'form':form}
     return render(request,'pages/addapartment.html',conaxt)








       
#         if request.method == 'POST':
#           coursename=request.POST['coursename']
#           teachername=request.POST['teachername']
#           techerphonenumber=request.POST['teacherphonenumber']
#           content=request.POST['content']
              	
        

#           new= addsoftwarclasses(coursename=coursename,teachername=teachername,techerphonenumber=techerphonenumber,content=content)   
#           new.save()   
# ################################################
#      submitted = False
#      if request.method == "POST":
#               form=addsoftwarclasses(request.POST)
#               if form.is_valid():
#                    form.save()
#                    return HttpResponseRedirect('pages/addsoftwarclasses?submitted=True')
#      else:
#              form =addsoftwarclasses 
#              if 'submitted' in request.GET:
#                    submitted=True
#      return render(request, 'pages/addsoftwarclasses.html',{'form':form,'submitted':submitted})
#      #####################################

 














def ToSignUp(request):
    return render(request,'pages\ToSignUp.html')


def choose(request):
     return render(request,'pages\choose.html')


def apartmentsroom (request):

      if request.method=="POST":
       searched=request.POST['searched']
       apart=Apartments.objects.filter(rooms=searched)

       #apart=Apartments.objects.all()
       return render(request,'pages/apartmentsroom.html',{'searched':searched,'apart':apart})
      else:
        return render(request, 'pages/apartmentsroom.html')
      
def apartmentsprice (request):

      if request.method=="POST":
       searched=request.POST['searched']
       apart=Apartments.objects.filter(price=searched)

       #apart=Apartments.objects.all()
       return render(request,'pages/apartmentsprice.html',{'searched':searched,'apart':apart})
      else:
        return render(request, 'pages/apartmentsprice.html')


def oneapartment(request):
     return render(request,'pages\oneapartment.html')

def privateclass(request):
     return render(request,'pages/privateclass.html')
def searchingapartments(request):
     return render(request,'pages/searchingapartments.html')



def aboutus(request):
    return render(request,'pages/aboutus.html')



def departmentcourses(request):
    return render(request,'pages/departmentcourses.html')












def showSoftwarclasses(request):
     soft=PrivateClasses.objects.all()
     return render(request,'pages/showSoftwarclasses.html',{'soft':soft})

def showchemicalclasses(request):
     soft=PrivateChemicalClasses.objects.all()
     return render(request,'pages/showchemicalclasses.html',{'soft':soft})


def showmechanicalclasses(request):
     soft=PrivateMechanicalClasses.objects.all()
     return render(request,'pages/showmechanicalclasses.html',{'soft':soft})


def showelectricclasses(request):
     soft=PrivateElectricClasses.objects.all()
     return render(request,'pages/showelectricclasses.html',{'soft':soft})



def showcivilclasses(request):
     soft=PrivateCivilClasses.objects.all()
     return render(request,'pages/showcivilclasses.html',{'soft':soft})

def addclasses(request):
     return render(request,'pages/addclasses.html')

def forstudentsusers(request):
     return render(request,'pages/forstudentsusers.html')

def forusers(request):
     return render(request,'pages/forusers.html')
def ADDING(request):
     return render(request,'pages/ADDING.html')

def showscholarships(request):
     # soft=scholarship.objects.all()
     #,{'soft':soft}
     return render(request,'pages/showscholarships.html')


def scholarshipswith(request):
      soft=scholarship.objects.all()
     
      return render(request,'pages/scholarshipswith.html',{'soft':soft})

def scholarshipswithout(request):
     soft=scholarship.objects.all()
     return render(request,'pages/scholarshipswithout.html',{'soft':soft})




def apartmentarea(request):



  if request.method=="POST":
       searched=request.POST['searched']
       apart=Apartments.objects.filter(area=searched)

       #apart=Apartments.objects.all()
       return render(request,'pages/apartmentarea.html',{'searched':searched,'apart':apart})
  else:
        return render(request, 'pages/apartmentarea.html')



def adminapartments(request):
     soft=Apartments.objects.all()
     return render(request,'pages/adminapartments.html',{'soft':soft})


def adminusers(request):
     soft=User.objects.all()
     return render(request,'pages/adminusers.html',{'soft':soft})

def adminsoftwar(request):
     soft=PrivateClasses.objects.all()
     return render(request,'pages/adminsoftwar.html',{'soft':soft})
  
def admincivil(request):
     soft=PrivateCivilClasses.objects.all()
     return render(request,'pages/admincivil.html',{'soft':soft})

def adminchemical(request):
     soft=PrivateChemicalClasses.objects.all()
     return render(request,'pages/adminchemical.html',{'soft':soft})


def adminelectrical(request):
     soft=PrivateElectricClasses.objects.all()
     return render(request,'pages/adminelectrical.html',{'soft':soft})

def adminmechanical(request):
     soft=PrivateMechanicalClasses.objects.all()
     return render(request,'pages/adminmechanical.html',{'soft':soft})

def adminscholarship(request):
     soft=scholarship.objects.all()
     return render(request,'pages/adminscholarship.html',{'soft':soft})

def privateclassestables(request):
    return render(request,'pages/privateclassestables.html')
def wichtable(request):
    return render(request,'pages/wichtable.html')
def foradmin(request):
    return render(request,'pages/foradmin.html')


def updateapartment(request,pk):
     apartment=Apartments.objects.get(id=pk)
     form= updateApartmentform(request.POST or None , instance=apartment )
     if form.is_valid():
         form.save()
         return redirect('adminapartments')
     return render (request,'pages/updateapartment.html',{'form':form})


def updatescholarship(request,pk):
     scho=scholarship.objects.get(id=pk)
     form= updatescholarshipform(request.POST  , instance=scho )

     if form.is_valid():
         form.save()
         return redirect('adminscholarship')
     return render (request,'pages/updatescholarship.html',{'form':form})


def updatesoftwar(request,pk):
     scho=PrivateClasses.objects.get(id=pk)
     form= updatesoftwarform(request.POST or None  , instance=scho )

     if form.is_valid():
         form.save()
         return redirect('adminsoftwar')
     return render (request,'pages/updatesoftwar.html',{'form':form})



def updatecivil(request,pk):
     scho=PrivateCivilClasses.objects.get(id=pk)
     form= updatecivilform(request.POST or None  , instance=scho )

     if form.is_valid():
         form.save()
         return redirect('admincivil')
     return render (request,'pages/updatecivil.html',{'form':form})

def updateelectric(request,pk):
     scho=PrivateElectricClasses.objects.get(id=pk)
     form= updateelectricform(request.POST or None  , instance=scho )

     if form.is_valid():
         form.save()
         return redirect('adminelectrical')
     return render (request,'pages/updateelectric.html',{'form':form})



def updatechemical(request,pk):
     scho=PrivateChemicalClasses.objects.get(id=pk)
     form= updatechemicalform(request.POST or None  , instance=scho )

     if form.is_valid():
         form.save()
         return redirect('adminchemical')
     return render (request,'pages/updatechemical.html',{'form':form})


def updatemechanical(request,pk):
     scho=PrivateMechanicalClasses.objects.get(id=pk)
     form= updatemechanicalform(request.POST or None  , instance=scho )

     if form.is_valid():
         form.save()
         return redirect('adminmechanical')
     return render (request,'pages/updatemechanical.html',{'form':form})

def wichuser(request):
    return render(request,'pages/wichuser.html')

def wichlogin(request):
    return render(request,'pages/wichlogin.html')

def signorlog(request):
    return render(request,'pages/signorlog.html')

def home(request):
    return render(request,'pages/home.html')