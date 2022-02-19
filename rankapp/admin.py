from django.contrib import admin
from rankapp.models import Data,jejusi_food,haeundae_food,seomyun_food,gyodong_food,chodangdong_food
from rankapp.models import seoguipo_rest,jejusi_rest,haeundae_rest,seomyun_rest,gyodong_rest,chodangdong_rest
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin
from import_export.admin import ImportExportActionModelAdmin
'''
from import_export import resources, fields
from import_export.admin import ImportExportActionModelAdmin
from import_export.widgets import ForeignKeyWidget
#import csv

# Register your models here.

class DataAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = Data
    list_display = ['title','score','addr']
    #pass

#admin.site.register(Boards, BoardAdmin)
'''
class DataAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

admin.site.register(Data,DataAdmin)
admin.site.register(jejusi_food)
admin.site.register(haeundae_food)
admin.site.register(seomyun_food)
admin.site.register(gyodong_food)
admin.site.register(chodangdong_food)
admin.site.register(seoguipo_rest)
admin.site.register(jejusi_rest)
admin.site.register(haeundae_rest)
admin.site.register(seomyun_rest)
admin.site.register(gyodong_rest)
admin.site.register(chodangdong_rest)
