from django.urls import path
from .views import project_list, project_detail, ProjectAPIView, ProjectDetails, GenericAPIView

app_name = 'projects'

urlpatterns = [
    # path('project/', project_list),
    path('project/', ProjectAPIView.as_view()),
    path('generic/project/<int:id>/', GenericAPIView.as_view()),
    # path('project_detail/<int:pk>/', project_detail)
    path('project_detail/<int:id>/', ProjectDetails.as_view())
]
