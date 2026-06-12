from django.shortcuts import render


def login_view(request):
    return render(request, "login.html")


def dashboard_view(request):
    return render(request, "dashboard.html")


def cursos_view(request):
    return render(request, "cursos.html")


def leccion_view(request, leccion_id):
    return render(request, "leccion.html", {"leccion_id": leccion_id})


def evaluacion_view(request, evaluacion_id):
    return render(request, "evaluacion.html", {"evaluacion_id": evaluacion_id})