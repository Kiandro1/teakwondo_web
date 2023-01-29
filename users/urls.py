from django.urls import path
from users.views import practicing_list, practicing_create, practicing_update, \
    PracticingDeleteView

urlpatterns = [
    path('practicing-list/', practicing_list, name='practicing-list'),
    path('practicing-create/', practicing_create, name='practicing-create'),
    path('practicing-update/<int:pk>/', practicing_update, name='practicing_update'),
    path('practicing-delete/<int:pk>/', PracticingDeleteView.as_view(), name='practicing_delete'),

]
