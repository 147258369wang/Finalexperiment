from rest_framework.decorators import api_view
from store_management.Action import Action
from store_management.serializers import *

@api_view(['GET',"POST"])
# 列表
def out_storeList(request):
  owner_id = request.POST.get('owner_id')
  user_id = request.POST.get('user_id')
  store_id = request.POST.get('store_id')
  list = out_store.objects.all()
  if owner_id:
    list = list.filter(owner_id=owner_id)
  if user_id:
    list = list.filter(user_id=user_id)
  if store_id:
    list = list.filter(store_id=store_id)
  arr = []
  for item in list:
    if owner_id:
      if owner_id != temp_cargo_check.owner_id:
        continue
    temp_cargo = {}
    temp_cargo['id'] = item.id
    temp_cargo['cargo_id'] = item.cargo_id
    temp_cargo_check = cargo.objects.filter(id=item.cargo_id).first()
    temp_cargo['owner_id'] = temp_cargo_check.owner_id
    temp_cargo['owner_name'] = user.objects.filter(id=temp_cargo_check.owner_id).first().name
    temp_cargo['cargo_name'] = cargo.objects.filter(id=item.cargo_id).first().name
    temp_cargo['user_id'] = item.user_id
    temp_cargo['user_name'] = user.objects.filter(id=item.user_id).first().name
    temp_cargo['store_id'] = item.store_id
    temp_cargo['store_name'] = store.objects.filter(id=item.store_id).first().name
    temp_cargo['num'] = item.num
    temp_cargo['time'] = item.time
    temp_cargo['status'] = item.status
    arr.append(temp_cargo)
  return Action.success(arr)