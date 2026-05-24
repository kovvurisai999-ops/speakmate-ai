#!/usr/bin/env bash
# exit on error
set -o errexit

echo "Installing requirements..."
pip install -r requirements.txt

echo "Running migrations..."
python manage.py migrate --no-input

echo "Collecting static files..."
python manage.py collectstatic --no-input

echo "Seeding database with default roadmap levels and concepts..."
python manage.py seed_roadmap
python manage.py seed_roadmap_advanced
python manage.py seed_exercises

echo "Seeding daily challenges..."
python populate_challenges.py

echo "Build process completed successfully!"
