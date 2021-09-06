from django.contrib import admin
from .models import Comments, Threads


admin.site.register(Threads)
admin.site.register(Comments)