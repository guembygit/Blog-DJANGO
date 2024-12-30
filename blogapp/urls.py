from django.urls import path
from blogapp import views as on

urlpatterns = [
    path('/home', on.index, name="index"),
    path("register/", on.register, name="register"),
    path("", on.login, name="login"),
    path("create/", on.createpost, name="create"),
    path('post/<str:pk>', on.post_id),
    path('edit/<int:id>', on.edit),
    path('update/<int:id>', on.update),
    path('delete/<int:id>', on.destroy),
    path('/propos', on.propos, name='propos'),
    path('search/', on.search_results, name='search_results'),
    path('deconnect/',on.deconnect,name='deconect'),
    path('category/<int:id>', on.category, name='category'),
    path('editcomment/<int:id>', on.editcomment),
    path('updatecomment/<int:id>', on.updatecomment),
    path('deletecomment/<int:id>', on.destroycomment),
    path('updateuser/<int:id>', on.updateuser ),
    path('edituser/<int:id>', on.edituser, ),


]
