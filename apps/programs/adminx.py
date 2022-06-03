# from django.contrib import admin
import xadmin
from .models import ProgramInfo # add this

class ProgramsAdminSetting():
    list_display = ['name', 'desc', 'location', 'is_completed']
    search_fields = ['name','desc','location']
    list_filter = ['id', 'add_time']

    # trade app example
    # class OrderGoodsInline(object):
    #     model = OrderGoods
    #     exclude = ['add_time', ]
    #     extra = 1
    #     style = 'tab'

    # inlines = [OrderGoodsInline, ]

    # a lot more fields
    # https://github.com/sshwsfc/xadmin-demo/blob/6f321f2688fc4f7737a39cda07a807bdb2f1561a/host/adminx.py

# does not include program app now
# xadmin.site.register(ProgramInfo, ProgramsAdminSetting)