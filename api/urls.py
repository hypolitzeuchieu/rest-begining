from .views import ProductMixinsViews
from django.conf.urls.static import static
from django.urls import path
from crud import settings

urlpatterns = [
    path('create', ProductMixinsViews.as_view()),
    path('list', ProductMixinsViews.as_view()),
    path('<int:pk>/detail', ProductMixinsViews.as_view(), name='detail'),
    path('<int:pk>/update', ProductMixinsViews.as_view()),
    path('<int:pk>/delete', ProductMixinsViews.as_view()),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
