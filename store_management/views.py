from django.shortcuts import render

# 页面渲染
#登陆页面
def login(request):
  return render(request, 'login.html')

#管理员页面: 仓库管理
def admin_store(request):
  return render(request, 'admin_store.html')

#管理员页面: 入库记录
def admin_in_store(request):
  return render(request, 'admin_in_store.html')

#管理员页面: 出库记录
def admin_out_store(request):
  return render(request, 'admin_out_store.html')

#管理员页面: 用户管理
def admin_user(request):
  return render(request, 'admin_user.html')


#货主页面: 个人中心
def user_owner_user(request):
  return render(request, 'user_owner_user.html')

#货主页面: 货物
def user_owner_cargo(request):
  return render(request, 'user_owner_cargo.html')

#货主页面: 入库记录
def user_owner_in_store(request):
  return render(request, 'user_owner_in_store.html')

#货主页面: 出库记录
def user_owner_out_store(request):
  return render(request, 'user_owner_out_store.html')

#采购页面: 货物大厅
def user_buyer_cargo(request):
  return render(request, 'user_buyer_cargo.html')

#采购页面: 我的订单
def user_buyer_order(request):
  return render(request, 'user_buyer_order.html')

#采购页面: 个人中心
def user_buyer_user(request):
  return render(request, 'user_buyer_user.html')
