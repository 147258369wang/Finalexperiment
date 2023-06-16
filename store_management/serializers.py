from rest_framework import serializers
from store_management.models import *

# 用户
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = user
        fields = ['id', 'name', 'account', 'password', 'tel', 'type']

# 仓库
class StoreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = store
        fields = ['id', 'name', 'type', 'capacity', 'unit', 'exist_amount']

# 货物
class CargoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = cargo
        fields = ['id', 'type', 'name', 'num', 'owner_id', 'store_id', 'status', 'time']

# 入库记录
class InStoreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = in_store
        fields = ['id', 'cargo_id', 'owner_id', 'store_id', 'num', 'status', 'time']

# 出库记录
class OutStoreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = out_store
        fields = ['id', 'cargo_id', 'user_id', 'store_id', 'num', 'status', 'time']

# 采购订单
class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = order
        fields = ['id', 'user_id', 'cargo_id', 'num', 'status', 'time']
