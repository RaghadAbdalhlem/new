from django.contrib import admin
from .models import SignUp
from .models import Apartments
from .models import PrivateChemicalClasses
from .models import PrivateCivilClasses
from .models import PrivateElectricClasses
from .models import PrivateMechanicalClasses
from .models import PrivateClasses
from .models import scholarship
from .models import Catigory
from .models import CatigoryClasses
from .models import Area


# Register your models here.

admin.site.register(SignUp)
admin.site.register(Apartments)
admin.site.register(PrivateClasses)
admin.site.register(PrivateChemicalClasses)
admin.site.register(PrivateCivilClasses)
admin.site.register(PrivateElectricClasses)
admin.site.register(PrivateMechanicalClasses)
admin.site.register(scholarship)
admin.site.register(Catigory)
admin.site.register(CatigoryClasses)
admin.site.register(Area)
