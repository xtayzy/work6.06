from django.urls import path

from post import views

urlpatterns = [
    path('', views.index, name='index_page'),
    path('add', views.add_store),
    path('store/<int:id>', views.store, name='store_page'),
    path('categories/store/<int:store_id>', views.categories, name='categories_page'),
    path('product/store/<int:store_id>/category/<int:cat_id>', views.products, name='products_page'),
    path('dell/<int:id>', views.dell_cat, name='dell_cat'),
    path('add_cat', views.add_cat),
    path('edit_cat/<int:id>', views.edit_page, name='edit_page'),
    path('edit', views.edit_cat, name='edit_page'),
    path('dell_pr/<int:id>', views.dell_pr, name='dell_pr'),
    path('edit_pr/<int:id>', views.edit_pr, name='edit_pr'),
    path('pr_edit', views.pr_edit, name='pr_edit'),
    path('pr_infa/<int:id>', views.pr_infa, name='pr_infa')
]
