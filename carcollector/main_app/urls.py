from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    
    # Car Routes
    path('cars/', views.cars_index, name='cars_index'),
    path('cars/<int:car_id>/', views.cars_detail, name='detail'),
    path('cars/create/', views.CarCreate.as_view(), name='cars_create'),
    path('cars/<int:pk>/update/', views.CarUpdate.as_view(), name='cars_update'),
    path('cars/<int:pk>/delete/', views.CarDelete.as_view(), name='cars_delete'),
    path('cars/<int:car_id>/add_service/', views.add_service, name='add_service'),

    # Accessory Routes
    path('accessories/', views.AccessoryList.as_view(), name='accessories_index'),
    path('accessories/<int:pk>/', views.AccessoryDetail.as_view(), name='accessories_detail'),
    path('accessories/create/', views.AccessoryCreate.as_view(), name='accessories_create'),
    path('accessories/<int:pk>/update/', views.AccessoryUpdate.as_view(), name='accessories_update'),
    path('accessories/<int:pk>/delete/', views.AccessoryDelete.as_view(), name='accessories_delete'),

    # Associate and Unassociate Accessories with Cars (Many-to-Many)
    path('cars/<int:car_id>/assoc_accessory/<int:accessory_id>/', views.assoc_accessory, name='assoc_accessory'),
    path('cars/<int:car_id>/unassoc_accessory/<int:accessory_id>/', views.unassoc_accessory, name='unassoc_accessory'),

    # Signup route
    path('accounts/signup/', views.signup, name='signup'),
]
