from django.contrib import admin
from .models import Articles, Coureses, Aja_look
from .models import Job
# Register your models here.
admin.site.register(Articles)
admin.site.register(Job)
admin.site.register(Coureses)
admin.site.register(Aja_look)