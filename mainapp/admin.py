from django.contrib import admin

# Register your models here.

from mainapp.models import Design_photo,Design_projects,Arch_photo,Arch_projects,Architects_supervision,Paragraphs_AS,Architecture,Paragraphs_Arch_SD,Paragraphs_Arch_DD,Paragraphs_Arch_CD,Interior_design,Paragraphs_ID,Product_design,Paragraphs_PD

admin.site.register(Architects_supervision)
admin.site.register(Paragraphs_AS)
admin.site.register(Architecture)
admin.site.register(Paragraphs_Arch_SD)
admin.site.register(Paragraphs_Arch_DD)
admin.site.register(Paragraphs_Arch_CD)
admin.site.register(Interior_design)
admin.site.register(Paragraphs_ID)
admin.site.register(Product_design)
admin.site.register(Paragraphs_PD)
admin.site.register(Arch_projects)
admin.site.register(Arch_photo)
admin.site.register(Design_projects)
admin.site.register(Design_photo)
