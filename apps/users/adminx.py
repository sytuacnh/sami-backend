# from django.contrib import admin
import xadmin
from .models import UserProfile # add this
from programs.models import ProgramInfo
class UsersAdminSetting():
    list_display = ['first_name', 'last_name', 'email', 'mobile', "gender"]
    search_fields = ['first_name','last_name']
    list_filter = ['id', 'add_time', 'last_name']

# xadmin.site.register(UserProfile, UsersAdminSetting)


# temporary solution for importing global settings
from xadmin import views
class BaseSetting():
    """xadmin basic """
    enable_themes = True 
    use_bootswatch = True

class GlobalSetting():
    """xadmin global settings"""
    site_title = "SaMi Admin"
    site_footer = "San Antonio Math Include"
    menu_style = "accordion"
    # globe_search_models = [ProgramInfo, UserProfile]

xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)