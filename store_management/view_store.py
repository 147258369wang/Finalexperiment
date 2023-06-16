from rest_framework.decorators import api_view
from store_management.Action import Action
from store_management.serializers import *


@api_view(['GET',"POST"])
# 列表
def storeList(request):
  list = store.objects.all()
  return Action.success(StoreSerializer(list, many = True).data)

@api_view(['GET',"POST"])
# 添加
def storeAdd(request):
  # 获取参数
  name = request.POST.get('name')
  type = request.POST.get('type')
  capacity = request.POST.get('capacity')
  unit = request.POST.get('unit')
  # 查询
  checkStore = store.objects.filter(name=name)
  if checkStore.exists() == True :
    return Action.fail("该仓库已存在")
  # 若没,添加入数据库
  newStore = store(type=type,name=name,capacity=capacity,unit=unit)
  newStore.save()
  # 添加成功
  return Action.success()