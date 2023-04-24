from django.contrib import admin
from .models import Flag
from .models import Hint
from .models import Classified
from .models import Encryption

# Register your models here.
admin.site.register(Flag)
admin.site.register(Hint)
admin.site.register(Classified)
admin.site.register(Encryption)