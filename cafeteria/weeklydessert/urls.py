from django.urls import path, include

from . import views

urlpatterns = [
	path("", views.index, name="index"),
  # Add a path to your auth links below:
  path("account/",include("django.contrib.auth.urls")),
	# Add a path to your signup request below:

	# Add a path to your logout request below:

	path("polls/<int:pk>/", views.DetailsView.as_view(), name="detail"),
	path("polls/<int:pk>/results/", views.ResultsView.as_view(), name="results"),
	path("polls/<int:week_id>/vote/", views.vote, name="vote"),
  path("signup/",views.SignUp.as_view(),name="signup"),
  path("logout/",views.logout_request,name="logout"),
]