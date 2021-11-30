from django.http import HttpResponse, JsonResponse
from hello.models import *
from django.core import serializers
import json
# 数据库操作
def testdb(request):
    test1 = Test(name='skying', author='尚柯')
    test1.save()
    return HttpResponse("数据库hello_test添加name成功！看去看看吧")

# 增加数据
def add_user(request):
    test1 = User(user_name='yoyo2', pwd='1234562', mail='2234516@qq.com')
    test1.save()
    return HttpResponse("yoyo用户创建成功！看看创建成功了！")

# 更新数据
def update_user(request):
    test2 = User.objects.get(user_name='yoyo')
    test2.pwd = '999999'
    test2.mail = '41255585@qq.com'
    test2.save()
    # 另外一种方式
    # Test.objects.filter(id=1).update(name='Google')
    # 修改所有的列
    # Test.objects.all().update(name='Google')
    return HttpResponse("<p>密码修改成功</p>")
# 删除数据
def delete_user(request):
    test3 = User.objects.get(user_name='yoyo')
    test3.delete()
    # 另外一种方式
    # Test.objects.filter(id=1).delete()
    # 删除所有数据
    # Test.objects.all().delete()
    return HttpResponse('<p>删除成功</p>')
# 查询数据
def select_user(request):
    # 方法1 可以查询单个结果直接获取mail值
    # test4 = User.objects.get(user_name='yoyo').mail

    # 方法2 filter相当于SQL中的WHERE，可设置条件过滤结果
    test4 = User.objects.filter(user_name='yoyo')
    # 查询结果是list，取下标后，获取mail字段的值
    # m = test4[0].mail

    return HttpResponse("<p>查询结果：%s</p>" % m)

def select_all(request):
    """取出User表里面user_name 、psw 、mail全部数据"""
    users = ''
    psws = ''
    mails=''
    res = User.objects.all()

    for i in res:
        users += '-' + i.user_name
        psws += '-' + i.pwd
        mails += '-' + i.mail

    return HttpResponse("<p>查询users结果：%s</p>"
                        "<p>查询psws结果：%s</p>"
                        "<p>查询mails结果：%s</p>" % (users, psws, mails))

def select_valus(request):
    r = ''
    tets5 = User.objects.all().values('user_name', 'pwd', 'mail')
    for i in tets5:
        r +=str(i)
    return HttpResponse("<p>查询mails结果：%s</p>" % r)

def sele_first_last(request):
    fi = User.objects.all().order_by('mail').first()
    f = fi.mail

    last = User.objects.all().order_by('mail').last()
    L = last.mail

    return HttpResponse("<p>查询mails第一个结果：%s</p>" "<p>查询mails最后一个结果：%s</p>" % (f, L))
# 转json
def get_json(request):
    """返回json数据"""
    data = {}
    a = User.objects.all()
    data['result'] = json.loads(serializers.serialize('json',a))
    return JsonResponse(data)