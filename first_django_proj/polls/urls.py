from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # path("", views.index, name="index"),
    # path("", views.IndexView.as_view(number_of_tasks=2), name="index"),
    path("", views.QuestionListView.as_view(), name="index"),
    path("about/", views.about, {'language': 'en'}),
    # path("<slug:q_slug>/", views.detail, name="detail"),
    path("<int:pk>/", views.QuestionDetailView.as_view(), name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("new/", views.NewQuestionView.as_view(), name="new"),
    path("success/", views.SuccessView.as_view(), name="success"),
    path("update/<int:pk>/", views.QuestionUpdateView.as_view(), name="update"),
    path("delete/<int:pk>/", views.QuestionDeleteView.as_view(), name="delete"),
    path("contact/", views.ContactUsView.as_view(), name="contact"),
    path("password_change/", auth_views.PasswordChangeView.as_view(template_name='pass.html'), name="passchange"),
]