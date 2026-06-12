from django.contrib import admin
from django.urls import path, include

from usuarios.views import CustomAuthToken

from .views import (
    login_view,
    dashboard_view,
    cursos_view,
    leccion_view,
    evaluacion_view,
    usuarios_view,
    admin_dashboard_view,
    admin_cursos_view,
    admin_usuarios_view,
    admin_inscripciones_view,
)


admin.site.site_header = "Plataforma Educativa"
admin.site.site_title = "Administración Plataforma Educativa"
admin.site.index_title = "Panel de administración"


urlpatterns = [
    path("", login_view, name="login"),

    path("dashboard/", dashboard_view, name="dashboard"),
    path("cursos/", cursos_view, name="cursos"),
    path("leccion/", leccion_view, name="leccion"),
    path("evaluacion/", evaluacion_view, name="evaluacion"),
    path("usuarios/", usuarios_view, name="usuarios"),

    path("admin-dashboard/", admin_dashboard_view, name="admin_dashboard"),
    path("admin-cursos/", admin_cursos_view, name="admin_cursos"),
    path("admin-usuarios/", admin_usuarios_view, name="admin_usuarios"),
    path("admin-inscripciones/", admin_inscripciones_view, name="admin_inscripciones"),

    path("admin/", admin.site.urls),

    path("api/token/", CustomAuthToken.as_view(), name="api_token"),
    path("api/usuarios/", include("usuarios.urls")),
    path("api/", include("cursos.urls")),
    path("api/", include("lecciones.urls")),
    path("api/", include("evaluaciones.urls")),
]