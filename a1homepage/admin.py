from django.contrib import admin
from .models import Banner,AdminBanner, Economy, BannerBackground


class BannerAdmin(admin.ModelAdmin):
  list_display = ('H1_Heading', 'Paragraph')

class Admin_BannerAdmin(admin.ModelAdmin):
  list_display = ('H1_Heading', 'Paragraph')

class EconomyAdmin(admin.ModelAdmin):
  list_display = ('H1_Heading', 'MCI', 'AMG')

class BannerBackgroundAdmin(admin.ModelAdmin):
  list_display = ('div_class', 'style','div_class_info_banner', 'style_info_banner')

admin.site.register(Banner,BannerAdmin)
admin.site.register(Economy,EconomyAdmin)
admin.site.register(BannerBackground,BannerBackgroundAdmin)


admin.site.register(AdminBanner,Admin_BannerAdmin)



# Register your models here.
