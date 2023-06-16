from django.db import models
from datetime import datetime

# 用户类
class user(models.Model):
    id = models.AutoField(primary_key=True) # id 会自动创建,可以手动写入
    name = models.CharField(max_length=45) # 姓名
    account = models.CharField(max_length=45) # 登陆账户
    password = models.CharField(max_length=45) # 密码
    tel = models.CharField(max_length=45) # 电话
    type = models.SmallIntegerField(default=3) # 类型

    class Meta:
        managed = False
        db_table = 'user'

# 仓库
class store(models.Model):
    id = models.AutoField(primary_key=True) # id 会自动创建,可以手动写入
    name = models.CharField(max_length=45) # 仓库名称
    type = models.SmallIntegerField() # 仓库类型
    capacity = models.DecimalField(max_digits=10, decimal_places=2) # 容积大小
    unit = models.CharField(max_length=45) # 容积单位
    exist_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0) # 已使用

    class Meta:
        managed = False
        db_table = 'store'

# 货物
class cargo(models.Model):
    id = models.AutoField(primary_key=True) # id 会自动创建,可以手动写入
    type = models.SmallIntegerField() # 货物类型
    name = models.CharField(max_length=45) # 名称
    num = models.DecimalField(max_digits=10, decimal_places=2) # 数量
    owner_id = models.IntegerField() # 用户id
    store_id = models.IntegerField() # 仓库id
    status = models.SmallIntegerField() # 状态
    time = models.DateTimeField(auto_now_add=True) # 创建时间

    class Meta:
        managed = False
        db_table = 'cargo'

# 入库记录
class in_store(models.Model):
    id = models.AutoField(primary_key=True) # id 会自动创建,可以手动写入
    cargo_id = models.IntegerField() # 货物id
    owner_id = models.IntegerField() # 货主id
    store_id = models.IntegerField() # 仓库id
    num = models.DecimalField(max_digits=10, decimal_places=2) # 数量
    time = models.DateTimeField(auto_now_add=True) # 创建时间
    status = models.SmallIntegerField(default=1) # 状态

    class Meta:
        managed = False
        db_table = 'in_store'

# 出库记录
class out_store(models.Model):
    id = models.AutoField(primary_key=True) # id 会自动创建,可以手动写入
    cargo_id = models.IntegerField() # 货物id
    user_id = models.IntegerField() # 采购id
    store_id = models.IntegerField() # 仓库id
    num = models.DecimalField(max_digits=10, decimal_places=2) # 大小/数量
    time = models.DateTimeField(auto_now_add=True) # 创建时间
    status = models.SmallIntegerField(default=1) # 状态

    class Meta:
        managed = False
        db_table = 'out_store'

# 采购订单
class order(models.Model):
    id = models.AutoField(primary_key=True) # id 会自动创建,可以手动写入
    user_id = models.IntegerField() # 采购用户id
    cargo_id = models.IntegerField() # 货物id
    num = models.DecimalField(max_digits=10, decimal_places=2) # 数量
    time = models.DateTimeField(auto_now_add=True) # 创建时间
    status = models.SmallIntegerField(default=1) # 状态

    class Meta:
        managed = False
        db_table = 'order'

