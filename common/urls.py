from django.urls import path

from app_comment.views import CommentView
from app_product.views import ProductViewForUser, ProductViewForAdmin
from app_user.views import RegisterView, LoginView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('product/', ProductViewForUser.as_view()),
    path('product-for-admin/', ProductViewForAdmin.as_view()),
    path('comment/', CommentView.as_view())
]
