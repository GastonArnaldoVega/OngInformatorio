from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeNotice.as_view(), name="home"),
    path('detail/<int:pk>', views.DetailNotice.as_view(), name='detail_notice'),
    path('addNoticia/', views.CreateNotice.as_view(), name='add_notice'),
    path('updateNotice/<int:pk>', views.UpdateNotice.as_view(), name='Update_Notice'),
    path('deleteNotice/<int:pk>', views.DeleteNotice.as_view(), name='Delete_Notice'),
    path('addCategoria/', views.CreateCategoria.as_view(), name='add_categoria'),
]
