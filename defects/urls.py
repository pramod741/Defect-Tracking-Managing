from django.urls import path
from . import views
from . import api_views

urlpatterns = [
    path('', views.all_defects, name='defects'),
    # path('description/', views.description_list, name='description'),
    path('<int:id>', views.description_list, name='description'),
    path('edit/<int:id>', views.edit_defects, name='edit'),
    path('add/', views.add_defect, name='add'),
    path('filter', views.filter_data, name='filter'),


    # urls for apis
    path('developers/', api_views.developers_list, name='developers_api'),
    path('testers/', api_views.testers_list, name='testers_api'),
    path('defects/', api_views.defects_list, name='defects_api'),
    path('defects/<int:id>/', api_views.defect_detail, name='defect_detail_api'),
    path('screenshots/', api_views.screenshots_list, name='screenshots_api'),

]
