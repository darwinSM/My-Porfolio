# Personal Portfolio - Django Project

This is my personal portfolio website, built with Django and Bootstrap 5.  
It showcases my personal projects, technologies I've worked with, and includes a contact form with email integration.

## Features

- About Me section
- Project list and detail pages
- Technologies used (grouped by category)
- Contact form with email notifications
- Admin panel for content management
- Responsive design using Bootstrap 5

## Stack

- Python 3
- Django 5.2.1
- Bootstrap 5
- SQLite (local development)
- Email: Gmail SMTP (using Django email backend)

## Setup Instructions

1. Clone this repository:

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name


2. Create a virtual environment and install dependencies:

python -m venv venv
source venv\Scripts\activate  # on Mac: venv/bin/activate
pip install -r requirements.txt


3. Set up your .env file:

SECRET_KEY=your-secret-key
DEBUG=True
EMAIL_HOST_USER=your-gmail@example.com
EMAIL_HOST_PASSWORD=your-gmail-app-password


4. Run migrations and start server:

python manage.py migrate
python manage.py runserver


5. Visit http://127.0.0.1:8000/ in your browser.


License
This project is open-source and available under the MIT License.