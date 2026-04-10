# Plataforma Química - API de Usuarios

Este proyecto es una API desarrollada en *Django + Django REST Framework*, que permite gestionar usuarios mediante operaciones CRUD (Crear, Leer, Actualizar y Eliminar).  
La base de datos usada es *MySQL*.

---

##  Requisitos

Antes de comenzar, tener instalado:

- Python 3.10 o superior  
- MySQL 8 o superior  
- Virtualenv (opcional, pero recomendado)

---

##  Instalación

1. *Clonar el repositorio*
   ```bash
   git clone https://github.com/tu-usuario/plataforma_quimica.git
   cd plataforma_quimica

2. crear un entorno virtual
  python -m venv venv

3. activar el entorno virtual (en powershell)
 .\venv\Scripts\activate

4. instalar dependencias 
  pip install-r requirements.txt

5. ejecutar migraciones 
 python manage.py migrate

6. iniciar el servidor de desarrollo
 python manage.py runserver
 
 el servidor estara corriendo en: https://127.0.0.1:8000/

## Endopints de la API:
 
 listar usuarios 
 GET/usuarios/

 crear usuarios
 POST/usuarios/

Json 
{
    "nombre": "juan"
    "email": "juan@example.com
    "edad": "23"
}

Obtener usuario por ID 
 
 GET/usuarios/(id)/

Actualizar usuarios

 PUT/usuarios/(id)/

Eliminar usuarios
 
 DELETE/usuarios/(id)/

## Tecnologias usadas
 
 Python 3.13
 Django 5.x
 Django rest framework
 MYSQL (como base de datos)

## Notas

Asegurate de tener MySQL corriendo en tu maquina antes de iniciar el proyecto 

el archivo requirement.txt debe contener las dependencias instaladas

si quieres generar el archivo requeriment.txt usa:
 
 pip freeze > requirements.txt
