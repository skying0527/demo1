from django.db import models
from django.contrib.auth.models import User, AbstractUser, AbstractBaseUser
# Create your models here.
from django.utils import timezone
from datetime import datetime
from stdimage.models import StdImageField
from mdeditor.fields import MDTextField   # 必须导入


class Test(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    author = models.CharField(max_length=100, null=False)


# 我们新建了一个Person类，继承自models.Model,
class Person(models.Model):
    """用户信息"""
    name = models.CharField(max_length=30)
    age = models.IntegerField()

    def __str__(self):
        return self.__doc__+"name->"+self.name


# 新增一张用户表，表名为user 字段user_name, psw ,mail 都是字符串类型
class User(models.Model):
    """注册表"""
    user_name = models.CharField(max_length=30, primary_key=True)
    pwd = models.CharField(max_length=30)
    mail = models.CharField(max_length=30)

    def __str__(self):
        return self.__doc__+"user_name->"+self.user_name


class Article(models.Model):
    """文章"""
    title = models.CharField(max_length=30, verbose_name="标题")   # 标题
    body = models.TextField(verbose_name="正文")  # 正文
    auth = models.CharField(max_length=20, verbose_name="作者")  # 作者
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    # 最后更新时间
    update_time = models.DateTimeField(auto_now=True, verbose_name="最后更新时间")

    def __str__(self):
        return self.__doc__+"title->"+self.title
    class Meta:
       verbose_name_plural = '文章列表'
class ArticleClassifty(models.Model):
    """文章分类"""
    n = models.CharField(max_length=30, verbose_name='分类', default='')
    def __str__(self):
        return self.__doc__+"->"+self.n
    class Meta:
        verbose_name = "文章分类"
        verbose_name_plural = verbose_name
class ArticleDetail(models.Model):
    """文章"""
    title = models.CharField(max_length=30, verbose_name="标题", default="输入你的标题")
    classify = models.ForeignKey(ArticleClassifty,
                                 on_delete=models.CASCADE,
                                 related_name="classify_name",
                                 verbose_name="文章分类",)
    body = models.TextField(verbose_name="正文", default="输入正文")
    auth = models.CharField(max_length=10, verbose_name="作者", default="admin", blank=True, null=True)
    detail = models.TextField(verbose_name="备注", default="添加备注")
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    # 最后更新时间
    update_time = models.DateTimeField(auto_now=True, verbose_name="最后更新时间")

    def __str__(self):
        return self.__doc__+"title->"+self.title

    class Meta:
        verbose_name = "文章列表"
        verbose_name_plural = "文章列表"


class Card(models.Model):
    """银行卡基本信息"""
    card_id = models.CharField(max_length=30, verbose_name="卡号", default="")
    card_user = models.CharField(max_length=10, verbose_name="姓名", default="")
    add_time = models.DateField(auto_now=True, verbose_name="添加时间")

    class Meta:
        verbose_name_plural = '银行卡账户'
        verbose_name = "银行卡账户_基本信息"

    def __str__(self):
        return self.card_id


class CardDetail(models.Model):
    """银行卡详情信息"""
    card = models.OneToOneField(Card,
                                on_delete=models.CASCADE,
                                verbose_name="卡号")
    tel = models.CharField(max_length=30, verbose_name="电话", default="")
    mail = models.CharField(max_length=30, verbose_name="邮箱", default="")
    city = models.CharField(max_length=10, verbose_name="城市", default="")
    address = models.CharField(max_length=30, verbose_name="详细地址", default="")

    class Meta:
        verbose_name_plural = "个人资料"
        verbose_name = "账户_个人资料"

    def __str__(self):
        return self.card.card_user





class Bank(models.Model):
    '''银行信息'''
    bank_name = models.CharField(max_length=50, verbose_name="银行名称")
    city = models.CharField(max_length=30, verbose_name="城市")
    point = models.CharField(max_length=60, verbose_name="网点")

    class Meta:
       verbose_name_plural = '银行卡'

    def __str__(self):
        return self.bank_name

class CardInfo(models.Model):
    '''卡信息'''
    card_id = models.CharField(max_length=30, verbose_name="卡号")
    card_name = models.CharField(max_length=10, verbose_name="姓名")
    info = models.ForeignKey(Bank, on_delete=models.CASCADE, verbose_name="选择银行")
    class Meta:
       verbose_name_plural = '卡号信息'

    def __str__(self):
        return self.card_id

class Teacher(models.Model):
    """老师表"""
    teacher_name = models.CharField(max_length=30, verbose_name="老师", default="")
    tel = models.CharField(max_length=30, verbose_name="电话", default="")
    mail = models.CharField(max_length=30, verbose_name="邮箱", default="")
    gender_choices = (
        (u'M', u'男'),
        (u'F', u'女'),
    )
    sex = models.CharField(max_length=10,
                           choices=gender_choices,
                           verbose_name="性别",
                           default="",
                           null=True,
                           blank=False)

    class Meta:
        verbose_name = "老师"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.teacher_name

class TeacherMan(Teacher):
    """男老师"""
    class Meta:
        verbose_name = "男老师"
        verbose_name_plural = verbose_name
        proxy = True  #不会生成新的表
    def __str__(self):
        return  self.teacher_name



class Student(models.Model):
    '''学生成绩'''
    student_id = models.CharField(max_length=30, verbose_name="学号", default="")
    name = models.CharField(max_length=30, verbose_name="姓名")
    age = models.IntegerField(verbose_name="年龄", default="")
    score = models.IntegerField(verbose_name="分数")
    gender_choices = (
        (u'M', u'男'),
        (u'F', u'女')
    )
    gender = models.CharField(max_length=10,
                             choices=gender_choices,
                             verbose_name="性别",
                             default="")
    create_time = models.DateTimeField(auto_now=True, verbose_name="创建时间")

    """多对多"""
    teachers = models.ManyToManyField(Teacher, verbose_name="老师")

    class Meta:
        verbose_name = "学生"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class FileImage(models.Model):
    """上传图片"""
    title = models.CharField(max_length=30, verbose_name="名称", default="")
    image = models.ImageField(verbose_name="上传图片", upload_to="up_image", blank=True)
    fiels = models.FileField(verbose_name="上传文件", upload_to="up_file", blank=True)
    add_time = models.DateField(auto_now=True, verbose_name="添加时间")

    def __str__(self):
        return self.__doc__ + 'title->' + self.title

    class Meta:
        verbose_name = "上传图片"
        verbose_name_plural = verbose_name

class UploadImage(models.Model):
    """上传图片"""
    name = models.CharField(max_length=30, verbose_name="名称",default="")
    image = StdImageField(max_length=100,
                          upload_to='path/to',
                          verbose_name=u'传图片',
                          variations={'thumbnail': {'width': 100, 'height': 75}})
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    def url(self):
        if self.image:
            return self.image.url
        else:
            return "url为空"

    def image_img(self):
        if self.image:
            href = self.image.url  # 点击后显示的放大图片
            src = self.image.thumbnail.url  # 页面显示的缩略图
            # 插入html代码
            image_html = '<a href="%s" target="_blank" title="传图片"><img alt="" src="%s"/>' % (href, src)
            return image_html
        else:
            return '上传图片'
    image_img.short_description = '图片'
    image_img.allow_tags = True     # 列表页显示图片

    class Meta:
        verbose_name = "传图片"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Blog(models.Model):
    '''博客管理'''
    title = models.CharField(max_length=30)
    content = MDTextField()    # 注意为MDTextField()

    def __str__(self):
        return self.__doc__ + "title->" + self.title

    class Meta:
        verbose_name = "博客发布"
        verbose_name_plural = verbose_name


class UserPersonalInfo(models.Model):
    '''用户个人信息'''
    name = models.CharField(max_length=10, verbose_name="昵称")  # 昵称
    sex_choices = (
        (u'M', u'男'),
        (u'F', u'女'),
    )
    sex = models.CharField(max_length=11,
                           choices=sex_choices,
                           verbose_name="性别",
                            )
    age = models.IntegerField(verbose_name="年龄",  default="", blank=True)
    mail = models.EmailField(max_length=30, default="", blank=True)
    create_time = models.DateField(auto_now=True, verbose_name="添加时间")