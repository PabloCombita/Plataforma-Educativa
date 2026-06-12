from django.shortcuts import render


def login_view(request):
    return render(request, "login.html")


def dashboard_view(request):
    return render(request, "dashboard.html")


def cursos_view(request):
    return render(request, "cursos.html")


def leccion_view(request):
    return render(request, "leccion.html")


def evaluacion_view(request):
    return render(request, "evaluacion.html")


def usuarios_view(request):
    return render(request, "usuarios.html")


def admin_dashboard_view(request):
    return render(request, "admin_dashboard.html")


def admin_cursos_view(request):
    return render(request, "admin_cursos.html")


def admin_usuarios_view(request):
    return render(request, "admin_usuarios.html")


def admin_inscripciones_view(request):
    return render(request, "admin_inscripciones.html")


def admin_lecciones_view(request):
    return render(request, "admin_lecciones.html")