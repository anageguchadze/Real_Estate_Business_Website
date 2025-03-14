# Real_Estate_Business_Website

This is a Django REST Framework (DRF) project designed for managing and displaying real estate properties. It includes features such as property listings, property types, property images, client testimonials, FAQs, and inquiries. The platform is fully API-driven, providing endpoints to interact with real estate data.

This project is ideal for real estate businesses, property managers, or anyone wanting to build a platform to manage property listings and client interactions.

Key Features:
Property Management: Create, read, update, and delete property listings.
Property Types: Manage different types of properties (e.g., residential, commercial).
Property Filters: Filter properties based on location, price, size, etc.
Inquiries: Collect and manage inquiries from potential clients.
Client Testimonials & FAQs: Display testimonials and frequently asked questions.
Admin Interface: Full integration with Django's built-in admin panel.


Live Demo
You can explore the live demo of the project hosted on DigitalOcean:

Live Demo http://104.248.242.53:8000/swagger/

Setup Instructions
Prerequisites:
Python 3.8+
Django 5.1+
Django REST Framework
SQLite (or any other database system you prefer)


Installation:
Clone the repository:
git clone https://github.com/anageguchadze/Real_Estate_Business_Website.git
cd Real_Estate_Business_Website


Install dependencies:
pip install -r requirements.txt

Apply migrations:
python manage.py migrate


Create a superuser for the Django admin panel:
python manage.py createsuperuser


Run the development server:
python manage.py runserver
Access the API at http://127.0.0.1:8000/ and the Django admin at http://127.0.0.1:8000/admin/.

API Endpoints:
Properties:
GET /api/property/: List all properties
POST /api/property/: Create a new property
GET /api/property/{id}/: View a single property
PUT /api/property/{id}/: Update a property
DELETE /api/property/{id}/: Delete a property
Property Types:
GET /api/property-type/: List all property types
POST /api/property-type/: Create a new property type
Inquiries:
GET /api/inquiry/: List all inquiries
POST /api/inquiry/: Create a new inquiry
Testimonials & FAQs:
GET /api/testimonal/: List all testimonials
POST /api/testimonal/: Create a new testimonial
GET /api/faq/: List all FAQs
POST /api/faq/: Create a new FAQ
Property Filters:
GET /api/property-filter-options/: Get filter options for properties (e.g., locations, price ranges)
Technologies Used:
Django 5.1
Django REST Framework
SQLite (for development)
DigitalOcean (for hosting)


License:
This project is licensed under the MIT License - see the LICENSE file for details.