#!/usr/bin/env bash
# Exit on error - (Salir si hay un error)
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.) - (Instalar dependencias)
pip install -r requirements.txt

# Convert static asset files () - (Recopilar archivos estáticos)
python manage.py collectstatic --no-input

# Apply any outstanding database migrations - (Aplicar migraciones de la base de datos)
python manage.py migrate