from rest_framework.decorators import api_view
from store_management.Action import Action
from store_management.serializers import *


@api_view(['GET',"POST"])
# 列表
def orderList(request):
  user_id = request.POST.get('user_id')
  cargo_id = request.POST.get('cargo_id')
  list = order.objects.all()
  if user_id:
    list = list.filter(user_id=user_id)
  if cargo_id:
    list = list.filter(cargo_id=cargo_id)
  arr = []
  for item in list:
    temp_cargo = {}
    temp_cargo['id'] = item.id
    temp_cargo['user_id'] = item.user_id
    temp_cargo['user_name'] = user.objects.filter(id=item.user_id).first().name
    temp_cargo['cargo_id'] = item.cargo_id
    temp_cargo['cargo_name'] = cargo.objects.filter(id=item.cargo_id).first().name
    temp_cargo['num'] = item.num
    temp_cargo['status'] = item.status
    temp_cargo['time'] = item.time
    arr.append(temp_cargo)
  return Action.success(arr)

@api_view(['GET',"POST"])
# 添加
def orderAdd(request):
  # 获取参数
  buyer_id = request.POST.get('buyer_id')
  cargo_id = request.POST.get('cargo_id')
  num = int(request.POST.get('num'))
  # 查询
  checkCargo = cargo.objects.filter(id=cargo_id)
  if checkCargo.exists() == False :
    return Action.fail("无此物品")
  checkCargo = checkCargo.first()
  if int(checkCargo.num) < num:
    return Action.fail("库存不足")
  checkStore = store.objects.filter(id=checkCargo.store_id).first()
  #下单 
  newOrder = order(user_id=buyer_id,cargo_id=cargo_id,num=num,status=2)
  newOrder.save()
  #出库记录
  neOutStore = out_store(cargo_id=newOrder.id, user_id=buyer_id, store_id=checkCargo.store_id, num=num)
  neOutStore.save()
  # 物品库存减少
  checkCargo.num = checkCargo.num - num
  checkCargo.save()
  # 仓库库存减少
  checkStore.exist_amount = checkStore.exist_amount - num
  checkStore.save()
  # 添加成功
  return Action.success()