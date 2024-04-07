from django.urls import path
from myApp import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('center', views.center.as_view(),name='center'),
    path('centerLeft', views.centerLeft.as_view(),name='centerLeft'),
    path('bottomLeft', views.bottomLeft.as_view(),name='柱状图数据'),
    path('centerRight', views.centerRight.as_view()),
    path('centerRightChange/<int:energyType>', views.centerRightChange.as_view()),
    path('bottomRight/', views.bottomRight.as_view()),
]