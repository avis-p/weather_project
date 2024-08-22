# Django Weather Application

This Django application fetches real-time weather data from a public API, processes the data, provides insights, and displays alerts if the weather conditions are extreme.

## Features

- **Fetch Real-Time Weather Data**: Integrates with the WeatherAPI to fetch the current weather for a specified city.
- **Data Processing**: Stores the weather data in a database and calculates trends such as average temperature and humidity over the last 24 hours.
- **Alerts**: Displays an alert if the weather condition is extreme (e.g., temperature above 35°C).

## Requirements

- Python 3.8+
- Django 4.2+
- `requests` library
- `django-environ` for environment variable management

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/django-weather-app.git
   cd django-weather-app

## Create a virtual environment and activate it:

- python3 -m venv env
- source env/bin/activate

## Install the dependencies:

- pip install -r requirements.txt

## Run migrations to set up the database:

- python manage.py makemigrations
- python manage.py migrate

## Run the development server:

- python manage.py runserver
