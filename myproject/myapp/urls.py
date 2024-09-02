from django.urls import path
from . import views
from .all_apis import test_apis

urlpatterns = [
    path('json/', views.my_json_view),  # make sure this maps to your view
    path('signup/', views.signup_page, name='signup_page'),
    path('api/signup/', views.signup, name='signup'),
    path('login/', views.login_page, name='login_page'),
    path('api/login/', views.login, name='login_api'),
    path('testing/', test_apis.testing_api),
]
