# Lux Property

This project is a web application based on Python Django, using HTML, CSS, and Bootstrap. The backend part was written in Django, and the templates were downloaded for free.

The web-app has five main sections:
> Home Page
> Our Offers
> Services
> About Us
> Contact Us

In addition, there is a hidden section - Manager. Access to the Manager section is restricted to users who are part of the 'manager' group. In the Manager section, the manager can process applications from clients. After processing, the application goes to the archive, where it can be deleted.

Each offer is an independent unit that contains information about the unit and is connected with a real estate agent.

All the information on the site is dynamic and can be edited from the admin page.

Installation:

Clone the repository using the command:
```
git clone https://github.com/<username>/lux-property.git
```

Create a virtual environment and activate it.

Install the requirements using the command:
```
pip install -r requirements.txt
```

Create a database and make migrations:
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

Access the application on http://127.0.0.1:8000/

Usage:

Home Page: The home page displays a carousel of featured offers, a search bar to search for offers, and a section about the company.

Our Offers: This page displays a list of all the offers, with information about each offer, such as the name, description, location, price, and real estate agent.

Services: This page displays information about the various services offered by the company, such as property management, real estate consulting, and legal services.

About Us: This page displays information about the company, such as its history, values, and mission.

Contact Us: This page displays a form that users can fill out to contact the company.

Manager: This section is only accessible to users who are part of the 'manager' group. Here, the manager can process applications from clients, view the archive, and delete applications.

To edit the information on the site, log in as a superuser and go to the admin page.

Thank you for using Lux Property!
