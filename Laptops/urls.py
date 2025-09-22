from django.urls import path
from . import views

urlpatterns = [
    path('show/', views.home_view),             # Home Page URL
    path('add/',views.add_view),                # Add Laptops Page URL
    path('register/',views.register_view),      # New User Registration Page URL
    path('update/<i>/',views.update_view),      # Update Laptops Info Page URL
    path('delete/<i>/',views.delete_view),      # Delete Laptops Detail  URL
    path('login/',views.login_view),            # Login Page URL
    path('logout/',views.logout_view),          # Logout  URL


]