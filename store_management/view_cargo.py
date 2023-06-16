from rest_framework.decorators import api_view
from store_management.Action import Action
from store_management.serializers import *


@api_view(['GET',"POST"])
# 列表
def cargoList(request):
  owner_id = request.POST.get('owner_id')
  name = request.POST.get('name')
  store_id = request.POST.get('store_id')
  list = cargo.objects.all()
  if owner_id:
    list = list.filter(owner_id=owner_id)
  if  name:
    list = list.filter(name__icontains=name)
  if  store_id:
    list = list.filter(store_id=store_id)
  arr = []
  for item in list:
    temp_cargo = {}
    temp_cargo['id'] = item.id
    temp_cargo['type'] = item.type
    temp_cargo['name'] = item.name
    temp_cargo['num'] = item.num
    temp_cargo['owner_id'] = item.owner_id
    temp_cargo['owner_name'] = user.objects.filter(id=item.owner_id).first().name
    temp_cargo['store_id'] = item.store_id
    temp_cargo['store_name'] = store.objects.filter(id=item.store_id).first().name
    temp_cargo['status'] = item.status
    temp_cargo['time'] = item.time
    arr.append(temp_cargo)
  return Action.success(arr)

@api_view(['GET',"POST"])
# 添加
def cargoAdd(request):
  # 获取参数
  type = int(request.POST.get('type'))
  name = request.POST.get('name')
  num = int(request.POST.get('num'))
  owner_id = request.POST.get('owner_id')
  store_id = request.POST.get('store_id')
  # 查询
  has = cargo.objects.filter(name=name, owner_id=owner_id)
  if has.exists() == True :
    return Action.fail("仓库中已登记此货物，请直接添加数量")
  checkStore = store.objects.filter(id=store_id)
  if checkStore.exists() == False :
    return Action.fail("查无此仓库")
  checkStore = checkStore.first()
  if int(checkStore.capacity - checkStore.exist_amount) < num:
    return Action.fail("该仓库已满")
  if not checkStore.type == type:
    return Action.fail("仓库类型不一致")
  # 若没,添加入数据库
  new = cargo(type=type,name=name,num=num,owner_id=owner_id,store_id=store_id)
  new.save()
  #入库记录
  newInStore = in_store(cargo_id=new.id, owner_id=owner_id, store_id=store_id, num=num)
  newInStore.save()
  # 仓库库存增加
  checkStore.exist_amount = checkStore.exist_amount + num
  checkStore.save()
  # 添加成功
  return Action.success()

@api_view(['GET',"POST"])
# 添加
def cargoNumAdd(request):
  # 获取参数
  id = request.POST.get('id')
  num = int(request.POST.get('num'))
  # 查询
  checkCargo = cargo.objects.filter(id=id)
  if checkCargo.exists() == False :
    return Action.fail("查无此货")
  checkCargo = checkCargo.first()
  checkStore = store.objects.filter(id=checkCargo.store_id)
  if checkStore.exists() == False :
    return Action.fail("查无此仓库")
  checkStore = checkStore.first()
  if int(checkStore.capacity - checkStore.exist_amount) < num:
    return Action.fail("该仓库已满")
  # 若没,添加入数据库
  checkCargo.num = checkCargo.num + num
  checkCargo.save()
  #入库记录
  newInStore = in_store(cargo_id=checkCargo.id, owner_id=checkCargo.owner_id, store_id=checkCargo.store_id, num=num)
  newInStore.save()
  # 仓库库存增加
  checkStore.exist_amount = checkStore.exist_amount + num
  checkStore.save()
  # 添加成功
  return Action.success()