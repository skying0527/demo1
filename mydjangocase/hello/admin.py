from django.contrib import admin
from hello import models

from hello.models import User, Person ,Article

# Register your models here.
# admin.py
admin.site.site_header = '项目管理系统'
admin.site.site_title = '登录系统后台'
admin.site.index_title = '后台管理'

# class ControlUser(admin.ModelAdmin):
#     """自定义列表中栏目 添加list_display 属性"""
#     # 显示的字段
#     list_display = ('user_name', 'pwd', 'mail')
#     # 搜索条件user_name
#     search_fields = ('user_name', 'pwd')
#
#
# admin.site.register(models.User, ControlUser)
# admin.site.register(models.Person)

# 装饰器
@admin.register(User)
class ControlUser(admin.ModelAdmin):
    """自定义列表中栏目 添加list_display 属性"""
    # 显示的字段
    list_display = ('user_name', 'pwd', 'mail')
    # 搜索条件user_name
    search_fields = ('user_name', 'pwd')
@admin.register(Article)
class ControlArticle(admin.ModelAdmin):
    # 显示字段
    list_display = ('title', 'body', 'auth', 'create_time', 'update_time')
    # 搜索条件user_name
    search_fields = ('title', )
    # 按字段排序 -表示降序
    ordering = ('create_time',)
    # 每页显示10条
    list_per_page = 3
    # 可编辑字段
    list_editable = ('auth',)
    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('title', 'body')
    # 过滤器
    list_filter = ('auth', 'title')
    # 时间分层
    date_hierarchy = 'create_time'

admin.site.register(Person)

class ControlBank(admin.ModelAdmin):
    # 显示的字段
    list_display = ["bank_name", "city", "point"]

class ControlCardInfo(admin.ModelAdmin):
    # 显示的字段
    list_display = ["card_id", "card_name", "info"]


admin.site.register(models.Bank, ControlBank)
admin.site.register(models.CardInfo, ControlCardInfo)