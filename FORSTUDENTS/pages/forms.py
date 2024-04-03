from django import forms
from .models import SignUp
from .models import PrivateClasses,PrivateCivilClasses,PrivateChemicalClasses,PrivateMechanicalClasses
from django .forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import PrivateElectricClasses
from .models import scholarship
from .models import Apartments



class SignUpForm(ModelForm):
    class Meta:
          model=SignUp
          fields=['Username','Email','Password','Re_Password']

   # class Meta:
    #    model=SignUp
     #   fields=['Username','Email','Password','Re_Password']
      #  labels={

       #     'Username':'Username',
        #    'Email':'Email',
         #   'Password':'Password',
          #  'Re_Password':'Re_Password'

        #}
        #widgets={
         #   'Username' : forms.TextInput(attrs={'class':'form-control', 'readonly':'readonly'}),
          #  'Email': forms.EmailInput(attrs={'class':'form-control'}),
           # 'Passsword':forms.TextInput(attrs={'class':'form-control','type':'password'}),
            #'Re_Password':forms.TextInput(attrs={'class':'form-control','type':"password"}),
       # }
    ##########
     #Username=forms.CharField(max_length=100)
     #Email=forms.CharField(max_length=100)
     #Password=forms.CharField(max_length=100)
     #Re_Password=forms.CharField(max_length=100)
        

    #def __str__(self):
       # return self.Username


class addclassesform(ModelForm):  
    class Meta:
        model = PrivateClasses
        fields =['coursename','teachername','teacherphonenumber','content']


class addelectricclassesform(ModelForm):  
    class Meta:
        model = PrivateElectricClasses
        fields =['coursename','teachername','teacherphonenumber','content']

class addcivilclassesform(ModelForm):  
    class Meta:
        model = PrivateCivilClasses
        fields =['coursename','teachername','teacherphonenumber','content']


class addchemicalclassesform(ModelForm):  
    class Meta:
        model = PrivateChemicalClasses
        fields =['coursename','teachername','teacherphonenumber','content']

class addmechanicalclassesform(ModelForm):  
    class Meta:
        model = PrivateMechanicalClasses
        fields =['coursename','teachername','teacherphonenumber','content']

class addscholarshipform(ModelForm):  
    class Meta:
        model = scholarship
        fields =['category','contant','phonenumber']





class addApartmentform(ModelForm):  
    class Meta:
        model = Apartments
        fields =['price','rooms','area','content','phonenumber']


class updateApartmentform(ModelForm):  
    class Meta:
        model = Apartments
        fields =['id','price','rooms','area','content','phonenumber']


class updatesoftwarform(ModelForm):  
    class Meta:
        model = PrivateClasses
        fields =['coursename','teachername','teacherphonenumber','content']

class updatecivilform(ModelForm):  
    class Meta:
        model = PrivateCivilClasses
        fields =['coursename','teachername','teacherphonenumber','content']

class updatemechanicalform(ModelForm):  
    class Meta:
        model = PrivateMechanicalClasses
        fields =['coursename','teachername','teacherphonenumber','content']

class updateelectricform(ModelForm):  
    class Meta:
        model = PrivateElectricClasses
        fields =['coursename','teachername','teacherphonenumber','content']
        
class updatechemicalform(ModelForm):  
    class Meta:
        model = PrivateChemicalClasses
        fields =['coursename','teachername','teacherphonenumber','content']


class updatescholarshipform(ModelForm):  
    class Meta:
        model = scholarship
        fields =['id','category','contant','phonenumber']







class CreatUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password1','password2']
        
   