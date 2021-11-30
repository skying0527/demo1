import xadmin
from .models import Student, Card, CardDetail, Teacher, ArticleDetail, FileImage, UploadImage, TeacherMan
from xadmin.layout import Main, TabHolder, Tab, Fieldset, Row, Col, AppendedText, Side, Field
from xadmin import views

from .adminx_actions import ClearAction
from django.utils.safestring import mark_safe
from . import models

# class ControlTeacher(object):
#     list_display = ["teacher_name", "tel", "mail"]


class ControlStudent(object):
    # 显示的字段
    list_display = ('student_id', 'name', 'gender', 'age', 'score', '老师', 'create_time')
    # 搜索条件
    search_fields = ('name',)

    # 每页显示10条
    list_per_page = 10

    actions = [ClearAction]

    def 老师(self, obj):
        return [x.teacher_name for x in obj.teachers.all()]


xadmin.site.register(Student, ControlStudent)

class TeacherAdmin(object):
    # 显示的字段
    list_display = ["teacher_name", "sex", "tel", "mail"]


# 注册新的表
class TeacherManAdmin(TeacherAdmin):
    # 显示的字段
    list_display = ["teacher_name", "sex", "tel", "mail"]

    def queryset(self):
        qs = super(TeacherAdmin, self).queryset()
        qs = qs.filter(sex="M")      # 筛选 sex="男"
        return qs


xadmin.site.register(Teacher, TeacherAdmin)

xadmin.site.register(TeacherMan, TeacherManAdmin)




class MoreInfo(object):
    model = CardDetail


class ControlCard(object):
    list_display = ["card_id", "card_user", "add_time"]

    # 在Card页面显示更多信息CardDetail
    inlines = [MoreInfo]


class ControlActicl(object):
    list_display = ['title', 'body', 'auth']


class MoreActicl(object):
    list_display = ['title', 'body', 'auth']
    readonly_fields = ['detail']  # 只读字段
    # exclude = ['auth']  # 不显示某个字段
    form_layout = (
        Fieldset(u'',
            Row('title', 'auth'),
            Row('classify'),
            css_class='unsort'   # 不让区块拖动
            ),
        Fieldset(('正文内容'),
            'body',
                 css_class='unsort'
            ),
        Fieldset(('备注'),
            Row('detail'),
                 css_class='unsort no_title'
            ),
        TabHolder(
            Tab('字段一',
                Field('title', css_class='extra'),
                Field('body'),
                css_class='unsort'),
            Tab('字段二',
                Field('body'),
                css_class='unsort')
        ),
    )


# xadmin.site.register(ArticleDetail, ControlActicl)
xadmin.site.register(ArticleDetail, MoreActicl)

# 注册Student表
# xadmin.site.register(Teacher, ControlTeacher)
# xadmin.site.register(Student, ControlStudent)

# 注册card表，关联CardDetail
xadmin.site.register(Card, ControlCard)


class GlobalSettings(object):
    site_title = "开发平台"
    site_footer = "skying"

    def get_site_menu(self):
        return [
            {
                'title': '自定义菜单',
                'icon': 'fa fa-bars',
                'menus': (
                    {
                        'title': 'Card表',
                        'icon': 'fa fa-bug',
                        'url': self.get_model_url(Card, 'changelist')
                    },
                    {
                        'title': '学生',
                        'icon': 'fa fa-envelope-o',
                        'url': self.get_model_url(Student, 'changelist')
                    }
                )
            },
            {
                'title': 'Bug统计',
                'icon': 'fa fa-bug',
                'menus': (
                    {
                        'title': 'Bug表',
                        'icon': 'fa fa-bug',
                        'url': "https://www.cnblogs.com/yoyoketang/"
                    },
                )
            }
        ]


xadmin.site.register(views.CommAdminView, GlobalSettings)


class ThemeSetting(object):
    '''主题设置'''
    enable_themes = True    # 使用主题
    use_bootswatch = True   # bootswatch是一款基于bootstrap的汇集了多种风格的前端UI解决方案


xadmin.site.register(views.BaseAdminView, ThemeSetting)

class ControlFiles(object):
    list_display = ['title', 'add_time']


xadmin.site.register(FileImage, ControlFiles)

class ControlImage(object):
    # 显示不要用image，而应该用image_img
    list_display = ['name', 'image_img', 'url', 'add_time', 'image_tag', '操作']

    def image_tag(self, obj):
        if obj.image:
            href = obj.image.url  # 点击后显示的放大图片
            src = obj.image.thumbnail.url  # 页面显示的缩略图
            # 插入html代码<a href="/media/path/to/yoyoaaa.jpg" target="_blank" title="传图片" data-gallery="gallery" </a>
            image_html = '<a href="%s" target="_blank" title="传图片"><img alt="" src="%s" class="field_img"></a>' % (
            href, src)
            return mark_safe(image_html)
        else:
            return '上传图片'
    image_tag.short_description = 'Photo'  # 显示在页面的内容
    # get_image_tag.allow_tags = True # redundant
    image_tag.admin_order_field = 'name'  # 排序

    def 操作(self, obj):
        # button = '<button id="", type="submit" class="default btn btn-primary hide-xs" name="_delete" data-loading-text="删除"><i class="fa fa-save"></i>删除</button>'
        button = '<p id="%s" class="default btn btn-primary hide-xs" onclick="click_action_info(\'%s\')">执行</p>'%(str(obj.name),str(obj.name))
        r = mark_safe(button)
        return r

    def get_media(self):
        # media is the parent's return value (modified by any plugins)
        media = super(ControlImage, self).get_media() + self.vendor('xadmin.page.list.js', 'xadmin.page.form.js')
        # if self.list_display_links_details:
        #     media += self.vendor('xadmin.plugin.details.js', 'xadmin.form.css')

        # xadmin.list.xxx.js是自己写的js脚本
        media += self.vendor('xadmin.list.xxx.js', 'xadmin.form.css')
        return media

        # media = super(ControlImage,self).get_media()
        # media.add_js(('js/content.js',))    # 这种方法行不通，会报找不到.add_js方法
        # return media


xadmin.site.register(UploadImage, ControlImage)

class BlogAdmin(object):
    list_display = ['title',]

xadmin.site.register(models.Blog, BlogAdmin)