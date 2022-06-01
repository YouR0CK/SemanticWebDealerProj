from django.urls import path

from . import views

app_name = 'CDealer'

urlpatterns = [
    #Dealer URLs
    path('create-dealer/', views.DealerCreationView.as_view(), name='dealer-creation'),
    path('update-dealer/<int:id>/', views.DealerUpdateView.as_view(), name='dealer-update'),
    path('get-dealer/<int:id>/', views.DealerRetrieveView.as_view(), name='dealer-retrieve'),
    path('list-dealer/', views.DealerListView.as_view(), name='dealer-list'),
    path('delete-dealer/<int:id>/', views.DealerDeleteView.as_view(), name='dealer-delete'),

    #Employee URLs
    path('create-employee/', views.EmployeeCreationView.as_view(), name='employee-creation'),
    path('update-employee/<int:id>/', views.EmployeeUpdateView.as_view(), name='employee-update'),
    path('get-employee/<int:id>/', views.EmployeeRetrieveView.as_view(), name='employee-retrieve'),
    path('list-employee/', views.EmployeeListView.as_view(), name='employee-list'),
    path('delete-employee/<int:id>/', views.EmployeeDeleteView.as_view(), name='employee-delete'),

    #Engine URLs
    path('create-engine/', views.EngineCreationView.as_view(), name='engine-creation'),
    path('update-engine/<int:id>/', views.EngineUpdateView.as_view(), name='engine-update'),
    path('get-engine/<int:id>/', views.EngineRetrieveView.as_view(), name='engine-retrieve'),
    path('list-engine/', views.EngineListView.as_view(), name='engine-list'),
    path('delete-engine/<int:id>/', views.EngineDeleteView.as_view(), name='engine-delete'),

    #Car URLs
    path('create-car/', views.CarCreationView.as_view(), name='car-creation'),
    path('update-car/<int:id>/', views.CarUpdateView.as_view(), name='car-update'),
    path('get-car/<int:id>/', views.CarRetrieveView.as_view(), name='car-retrieve'),
    path('list-car/', views.CarListView.as_view(), name='car-list'),
    path('delete-car/<int:id>/', views.CarDeleteView.as_view(), name='car-delete'),
]