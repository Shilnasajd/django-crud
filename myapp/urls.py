from django.urls import path
from.import views


urlpatterns = [
    path('',views.add,name='add'),
    path("stdnt/remove/<int:id>",views.DeleteView.as_view(),name="dlt"),
    path('update/<int:id>/', views.UpdateView.as_view(), name='update'),

]
