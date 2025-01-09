from django.urls import path
from .views import (
    DepartmentCreateAPIView,
    DepartmentGetAPIView,
    DepartmentUpdateAPIView,
    DepartmentDeactivateAPIView,
    WorkCategoryCreateAPIView,
    WorkCategoryGetAPIView,
    WorkCategoryUpdateAPIView,
    WorkCategoryDeactivateAPIView,
    WorkCategoryFilesRequiredCreateAPIView,
    WorkCategoryFilesRequiredGetAPIView,
    WorkCategoryFilesRequiredUpdateAPIView,
    WorkCategoryFilesRequiredDeactivateAPIView,
    WorkCategoryActivityListCreateAPIView,
    WorkCategoryActivityListGetAPIView,
    WorkCategoryActivityListUpdateAPIView,
    WorkCategoryActivityListDeactivateAPIView,
    WorkCategoryUploadDocumentRequiredCreateAPIView,
    WorkCategoryUploadDocumentRequiredGetAPIView,
    WorkCategoryUploadDocumentRequiredUpdateAPIView,
    WorkCategoryUploadDocumentRequiredDeactivateAPIView,
)

urlpatterns = [
    path('department/create/', DepartmentCreateAPIView.as_view(), name='department_create'),
    path('department/get/', DepartmentGetAPIView.as_view(), name='department_get'),
    path('department/update/<int:id>/', DepartmentUpdateAPIView.as_view(), name='department_update'),
    path('department/deactivate/<int:id>/', DepartmentDeactivateAPIView.as_view(), name='department_deactivate'),
    path('work-category/create/', WorkCategoryCreateAPIView.as_view(), name='work_category_create'),
    path('work-category/get/', WorkCategoryGetAPIView.as_view(), name='work_category_get'),
    path('work-category/update/<int:id>/', WorkCategoryUpdateAPIView.as_view(), name='work_category_update'),
    path('work-category/deactivate/', WorkCategoryDeactivateAPIView.as_view(), name='work_category_deactivate'),
    path('work-category-files-required/create/', WorkCategoryFilesRequiredCreateAPIView.as_view(), name='work_category_files_required_create'),
    path('work-category-files-required/get/', WorkCategoryFilesRequiredGetAPIView.as_view(), name='work_category_files_required_get'),
    path('work-category-files-required/update/', WorkCategoryFilesRequiredUpdateAPIView.as_view(), name='work_category_files_required_update'),
    path('work-category-files-required/deactivate/', WorkCategoryFilesRequiredDeactivateAPIView.as_view(), name='work_category_files_required_deactivate'),
    path('work-category-activity-list/create/', WorkCategoryActivityListCreateAPIView.as_view(), name='work_category_activity_list_create'),
    path('work-category-activity-list/get/', WorkCategoryActivityListGetAPIView.as_view(), name='work_category_activity_list_get'),
    path('work-category-activity-list/update/', WorkCategoryActivityListUpdateAPIView.as_view(), name='work_category_activity_list_update'),
    path('work-category-activity-list/deactivate/', WorkCategoryActivityListDeactivateAPIView.as_view(), name='work_category_activity_list_deactivate'),
    path('work-category-upload-document-required/create/', WorkCategoryUploadDocumentRequiredCreateAPIView.as_view(), name='work_category_upload_document_required_create'),
    path('work-category-upload-document-required/get/', WorkCategoryUploadDocumentRequiredGetAPIView.as_view(),
            name='work_category_upload_document_required_get'),
    path('work-category-upload-document-required/update/', WorkCategoryUploadDocumentRequiredUpdateAPIView.as_view(),
            name='work_category_upload_document_required_update'),
    path('work-category-upload-document-required/deactivate/', WorkCategoryUploadDocumentRequiredDeactivateAPIView.as_view(),
         name='work_category_upload_document_required_deactivate'),
]