from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core import views


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

router = routers.DefaultRouter()
router.register(r"autores", views.AutorViewSet)
router.register(r"categorias", views.CategoriaViewset)
router.register(r"editoras", views.EditoraViewSet)
router.register(r"livros", views.LivroViewSet)
router.register(r"compras", views.CompraViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    # OpenAPI 3
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    #Autenticação
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('teste/', views.teste),
    # Outros endpoints
    path('categorias-class/', views.CategoriaView.as_view()),
    path('categorias-class/<int:id>', views.CategoriaView.as_view()),
    path('categorias-apiview/', views.CategoriasList.as_view()),
    path('categorias-apiview/<int:id>/', views.CategoriaDetail.as_view()),
    path('categorias-generic/', views.CategoriasLisGeneric.as_view()),
    path('categorias-generic/<int:id>/',
         views.CategoriaDetailGeneric.as_view()),
    path('api/', include(router.urls)),


    ]
