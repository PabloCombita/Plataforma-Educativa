from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from rest_framework.authtoken.views import obtain_auth_token

def login_view(request):
    return render(request, 'login.html')

def dashboard_view(request):
    return render(request, 'dashboard.html')

def cursos_view(request):
    return render(request, 'cursos.html')

def detalle_curso_view(request):
    return render(request, 'detalle-curso.html')

def leccion_view(request):
    return render(request, 'leccion.html')

def evaluacion_view(request):
    return render(request, 'evaluacion.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='login'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('cursos/', cursos_view, name='cursos'),
    path('detalle-curso/', detalle_curso_view, name='detalle-curso'),
    path('leccion/', leccion_view, name='leccion'),
    path('evaluacion/', evaluacion_view, name='evaluacion'),
    path('api/token/', obtain_auth_token, name='api_token'),
    path('api/usuarios/', include('usuarios.urls')),
    path('api/', include('cursos.urls')),
    path('api/', include('lecciones.urls')),
    path('api/', include('evaluaciones.urls')),
]