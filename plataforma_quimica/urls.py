from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from .views import (
    login_view,
    dashboard_view,
    cursos_view,
    leccion_view,
    evaluacion_view,
)


admin.site.site_header = "Plataforma Educativa"
admin.site.site_title = "Administración Plataforma Educativa"
admin.site.index_title = "Panel de administración"


urlpatterns = [
    path("", login_view, name="login"),
    path("dashboard/", dashboard_view, name="dashboard"),
    path("cursos/", cursos_view, name="cursos"),
    path("leccion/<int:leccion_id>/", leccion_view, name="leccion"),
    path("evaluacion/<int:evaluacion_id>/", evaluacion_view, name="evaluacion"),

    path("admin/", admin.site.urls),

    path("api/token/", obtain_auth_token, name="api_token"),
    path("api/usuarios/", include("usuarios.urls")),
    path("api/", include("cursos.urls")),
    path("api/", include("lecciones.urls")),
    path("api/", include("evaluaciones.urls")),
]