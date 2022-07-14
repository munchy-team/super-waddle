from django.contrib import admin
from .models import Banner,AdminBanner


class BannerAdmin(admin.ModelAdmin):
  list_display = ('H1_Heading', 'Paragraph')

class Admin_BannerAdmin(admin.ModelAdmin):
  list_display = ('H1_Heading', 'Paragraph')


admin.site.register(Banner,BannerAdmin)


admin.site.register(AdminBanner,Admin_BannerAdmin)



# Register your models here.
