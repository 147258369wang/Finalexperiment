from rest_framework.decorators import api_view
from store_management.Action import Action
from store_management.serializers import *


@api_view(['GET',"POST"])
# 列表
def in_storeList(request):
  owner_id = request.POST.get('owner_id')
  list = in_store.objects.all()
  if owner_id:
    list = list.filter(owner_id=owner_id)
  arr = []
  for item in list:
    temp_cargo = {}
    temp_cargo['id'] = item.id
    temp_cargo['cargo_id'] = item.cargo_id
    temp_cargo['cargo_name'] = cargo.objects.filter(id=item.cargo_id).first().name
    temp_cargo['owner_id'] = item.owner_id
    temp_cargo['owner_name'] = user.objects.filter(id=item.owner_id).first().name
    temp_cargo['store_id'] = item.store_id
    temp_cargo['store_name'] = store.objects.filter(id=item.store_id).first().name
    temp_cargo['num'] = item.num
    temp_cargo['time'] = item.time
    temp_cargo['status'] = item.status
    arr.append(temp_cargo)
  return Action.success(arr)
  # return Action.success(InStoreSerializer(list, many = True).data)