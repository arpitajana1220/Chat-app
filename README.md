# Realtime Chat Application

This is a realtime chat application built with Django and Tailwind CSS.

## Features

- Realtime messaging
- User authentication
- Online user count
- Responsive design

## Prerequisites

- Python 3.x
- Node.js
- npm (Node Package Manager)

## Setup and Run Locally

Follow these steps to set up and run the project locally:

Clone the repository:
```
git clone https://github.com/arpitajana1220/Chat-app.git
cd Chat-app

```

Create a virtual environment:
```
python -m venv venv
```
Activate the virtual environment:
On Windows:
```
venv\Scripts\activate
```
On macOS/Linux:
```
source venv/bin/activate
```
Install the required Python packages:
```
pip install -r requirements.txt
```
Run database migrations:
```
python manage.py migrate
```
Create a superuser:
```
python manage.py createsuperuser
```
Run the development server:
```
python manage.py runserver
```

Access the application: Open your web browser and go to http://127.0.0.1:8000.

License
This project is licensed under the MIT License.
