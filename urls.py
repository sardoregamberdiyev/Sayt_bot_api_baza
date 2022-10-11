from django.urls import path
from api.v1.category.views import CategoryView

urlpatterns = [
    path('ctg/', CategoryView.as_view(), name="ctg_api_list"),
    path('ctg/<int:pk>/', CategoryView.as_view(), name="ctg_api_one"),
]
