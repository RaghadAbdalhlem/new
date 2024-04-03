from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.







class SignUp(models.Model):


    Username=models.CharField(max_length=100,null=True,blank=True)
    Email=models.CharField(max_length=100,null=True,blank=True)
    Password=models.CharField(max_length=100,null=True,blank=True)
    Re_Password=models.CharField(max_length=100,null=True,blank=True)


    def __str__(self):
         return self.Username
   
    
class Area(models.Model):
    area=models.CharField(max_length=100)
    def __str__(self):
        return self.area

# Create your models here.
class Apartments(models.Model):
    id = models.AutoField(primary_key=True)
    price=models.IntegerField(
        default=1000,
        validators=[MaxValueValidator(5000), MinValueValidator(1000)])
    rooms=models.IntegerField(
        default=1,
        validators=[MaxValueValidator(5), MinValueValidator(1)])
    area=models.CharField(max_length=100)
    content=models.TextField(null=False)
   # img=models.ImageField(upload_to=('static/image/'))
    phonenumber=models.CharField(max_length=10,null=True)
    # def __str__(self):
    #     return self.area
    class Meta:
        verbose_name='Apartment'





class CatigoryClasses(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name





class PrivateClasses(models.Model):
    #  CATEGORY = (
    #     ('Softwar-Engineering', 'Softwar-Engineering'),
    #     ('Civil-Engineering', 'Civil-Engineering'), ('Chemical-Engineering', 'Chemical-Engineering'),
    #     ('Electric-Engineering', 'Electric-Engineering'),
    #     ('Mechanical-Engineering', 'Mechanical-Engineering')

    #    )
                        
    #  departmentcours=models.CharField(max_length=200, null=True, choices=CATEGORY)
     coursename=models.CharField(max_length=50,null=True,blank=True)
     teachername=models.CharField(max_length=50,null=True,blank=True)
     teacherphonenumber=models.CharField(max_length=50,null=True,blank=True)
     content=models.CharField(max_length=100,null=True,blank=True)
        #img=models.ImageField(default="static/image/personalclass.png")
     def __str__(self):
        return self.coursename   
    



    
class PrivateCivilClasses(models.Model):

    #departmentcours= models.CharField(max_length=100)
    coursename=models.CharField(max_length=50,null=True,blank=True)
    teachername=models.CharField(max_length=50,null=True,blank=True)
    teacherphonenumber=models.CharField(max_length=50,null=True,blank=True)
    content=models.CharField(max_length=100,null=True,blank=True)
    #img=models.ImageField(default="static/image/personalclass.png")
    # def __str__(self):
    #     return self.departmentcours
    def __str__(self):
        return self.coursename   



class PrivateElectricClasses(models.Model):

    #departmentcours= models.CharField(max_length=100)
    coursename=models.CharField(max_length=50,null=True,blank=True)
    teachername=models.CharField(max_length=50,null=True,blank=True)
    teacherphonenumber=models.CharField(max_length=50,null=True,blank=True)
    content=models.CharField(max_length=100,null=True,blank=True)
    #img=models.ImageField(default="static/image/personalclass.png")
    # def __str__(self):
    #     return self.departmentcours




class PrivateMechanicalClasses(models.Model):

    #departmentcours= models.CharField(max_length=100)
    coursename=models.CharField(max_length=50,null=True,blank=True)
    teachername=models.CharField(max_length=50,null=True,blank=True)
    teacherphonenumber=models.CharField(max_length=50,null=True,blank=True)
    content=models.CharField(max_length=100,null=True,blank=True)
    #img=models.ImageField(default="static/image/personalclass.png")
    # def __str__(self):
    #     return self.departmentcours







class PrivateChemicalClasses(models.Model):

   # departmentcours= models.CharField(max_length=100)
    coursename=models.CharField(max_length=50,null=True,blank=True)
    teachername=models.CharField(max_length=50,null=True,blank=True)
    teacherphonenumber=models.CharField(max_length=50,null=True,blank=True)
    content=models.CharField(max_length=100,null=True,blank=True)
    #img=models.ImageField(default="static/image/personalclass.png")
    # def __str__(self):
    #      return self.departmentcours




class Catigory(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    


class scholarship(models.Model):
    id = models.AutoField(primary_key=True)
    category=models.ForeignKey(Catigory,on_delete=models.CASCADE,default=True,null=False)
    contant=models.CharField(max_length=1000)
    phonenumber=models.CharField(max_length=10,null=True)