# Mini Blog - Plataforma de Publicación Ligera

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
![Django Version](https://img.shields.io/badge/django-4.2-brightgreen)

Un sistema de blogging minimalista y responsivo, optimizado para dispositivos móviles y de fácil implementación.

Backend creado con Django | Python.
Frontend creado con ayuda de la IA de Deepseek usando Bootstrap y JS.

![Captura de Pantalla del Blog](url-de-tu-captura.jpg)

## Características Principales

- 🚀 **Publicación Rápida**: Interfaz de administración intuitiva
- 📱 **Primero Móvil**: Diseño responsivo priorizado para smartphones
- 🔒 **Autenticación Segura**: Sistema de usuarios con permisos
- 📑 **Gestión de Contenidos**:
  - Posts con categorías y etiquetas
  - Búsqueda y filtrado básico
  - Paginación optimizada
- 🛠 **Tecnologías Clave**:
  - Django 4.2
  - Bootstrap 5
  - PostgreSQL (configurable)

## Requisitos del Sistema

- Python 3.9+
- PostgreSQL 12+ (o SQLite para desarrollo)
- Node.js (opcional para assets)

## Instalación Rápida

1. **Clonar Repositorio**
```bash
git clone https://github.com/tu-usuario/mini-blog.git
cd mini-blog

2. **Configurar Entorno Virtual**
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows

3. **Instalar Dependencias**
pip install pillow
pip install django-ckeditor

4. **Migraciones Iniciales**
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

5. **Ejecutar Servidor**
python manage.py runserver

