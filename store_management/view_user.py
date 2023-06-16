from rest_framework.decorators import api_view
from store_management.Action import Action
from store_management.serializers import *
from django.db.models import Q


@api_view(['GET',"POST"])
# 用户注册
def userRegister(request):
  # 获取参数
  name = request.POST.get('name')
  account = request.POST.get('account')
  password = request.POST.get('password')
  address = request.POST.get('address')
  tel = request.POST.get('tel')
  type = request.POST.get('type')
  # 查询是否已被注册
  checkUser = user.objects.filter(Q(name=name) | Q(account=account))
  if checkUser.exists() == True :
    # 如果已经被注册,则直接返回错误消息
    return Action.fail("已注册")
  # 若没注册，添加入数据库
  newUser = user(name=name, account=account, password=password, tel=tel, type=type)
  newUser.save()
  return Action.success()

@api_view(['GET',"POST"])
# 用户编辑
def userEdit(request):
  # 获取参数
  id = request.POST.get('id')
  password = request.POST.get('password')
  tel = request.POST.get('tel')
  # 查询是否存在
  checkUser = user.objects.filter(id=id)
  if checkUser.exists() == True :
    # 如果存在则开始更改
    newuser = checkUser.first()
    newuser.password = password
    newuser.tel = tel
    newuser.save()
    return Action.success(UserSerializer(newuser, many = False).data)
  else:
    # 若没注册
    return Action.fail("信息有误")

@api_view(['GET',"POST"])
# 用户登录
def userLogin(request):
  # 获取参数
  account = request.POST.get('account')
  password = request.POST.get('password')
  checkUser = user.objects.filter(account=account).first()
  if not checkUser:
    return Action.fail("用户不存在")
  if checkUser.password != password:
    # 用户存在,密码不一致,则直接返回错误消息
    return Action.fail("密码错误")
  # 登陆成功
  return Action.success(UserSerializer(checkUser, many = False).data)

@api_view(['GET',"POST"])
# 用户列表
def userList(request):
  # 获取参数
  return Action.success(UserSerializer(user.objects.all(), many = True).data)


'''
#重置密码
@api_view(['GET',"POST"])
def userResetPassword(request):
  id = request.POST.get('id')
  checkUser= user.objects.filter(id=id)
  if checkUser.exists() == False :
    return Action.fail("用户不存在")
  checkUser = checkUser.first()
  checkUser.password = '123@456'
  checkUser.save()
  return Action.success()
'''