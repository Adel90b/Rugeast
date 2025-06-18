# Rugeast Backend - Django E-commerce Platform

A comprehensive Django-based e-commerce backend for carpet/rug sales, built with Django Oscar framework.

## 🚀 Features

- **E-commerce Core**: Built on Django Oscar for robust e-commerce functionality
- **Multilingual Support**: German and English language support
- **Product Management**: Advanced catalog with categories, attributes, and variants
- **Order Processing**: Complete order management system
- **API Integration**: RESTful API with multiple versions (V0.1, V1.0, V2.1)
- **User Management**: Customer accounts and authentication
- **Content Management**: Blog, newsletter, and contact systems
- **Import System**: Bulk product import functionality
- **Task Queue**: Celery integration for background tasks

## 🛠 Technology Stack

- **Framework**: Django 2.2.13
- **E-commerce**: Django Oscar 2.1
- **API**: Django REST Framework 3.11.0
- **Database**: PostgreSQL (recommended)
- **Task Queue**: Celery 4.4.6
- **Cache**: Redis (django-redis 4.12.1)
- **Search**: Django Haystack 3.0b2
- **Internationalization**: Django Rosetta 0.9.4

## 📁 Project Structure

```
backend/
├── apps/                    # Custom Django applications
│   ├── api/                # API endpoints and serializers
│   ├── catalogue/          # Product catalog management
│   ├── checkout/           # Checkout process
│   ├── contact/            # Contact forms
│   ├── customer/           # Customer management
│   ├── dashboard/          # Admin dashboard
│   ├── importer/           # Product import system
│   ├── newsletter/         # Newsletter management
│   ├── order/              # Order processing
│   ├── partner/            # Partner/supplier management
│   ├── shipping/           # Shipping calculations
│   └── slider/             # Homepage sliders
├── core/                   # Core functionality
├── teemche/                # Main Django project settings
├── templates/              # Django templates
├── locale/                 # Translation files
└── manage.py              # Django management script
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- PostgreSQL
- Redis
- Virtual environment tool (venv, virtualenv, or conda)

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd rugeast-backend
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp teemche/local_settings.py.example teemche/local_settings.py
   # Edit local_settings.py with your database and other configurations
   ```

5. **Database setup**
   ```bash
   python manage.py migrate
   python manage.py oscar_populate_countries
   python manage.py init <https://your-site-url.com> <product-type:rugs>
   python manage.py create_socials
   python manage.py set_tax
   ```

6. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run development server**
   ```bash
   python manage.py runserver
   ```

## 🔧 Configuration

### Database Configuration

Update `teemche/local_settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Redis Configuration

```python
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}
```

### Celery Configuration

Start Celery worker:
```bash
celery -A teemche worker -l info
```

Start Celery beat (for scheduled tasks):
```bash
celery -A teemche beat -l info
```

## 📚 API Documentation

The project includes multiple API versions:

- **API V0.1**: `/api/v0.1/`
- **API V1.0**: `/api/v1.0/`
- **API V2.1**: `/api/v2.1/`

Key endpoints:
- Products: `/api/products/`
- Categories: `/api/categories/`
- Orders: `/api/orders/`
- Basket: `/api/basket/`
- Users: `/api/users/`

## 🌍 Internationalization

The project supports German (primary) and English:

1. **Update translations**
   ```bash
   python manage.py makemessages -l de
   python manage.py makemessages -l en
   ```

2. **Compile translations**
   ```bash
   python manage.py compilemessages
   ```

3. **Use Rosetta for web-based translation management**
   Visit `/rosetta/` in your browser

## 🚀 Deployment

### Production Settings

1. Set `DEBUG = False` in production
2. Configure proper `ALLOWED_HOSTS`
3. Use environment variables for sensitive data
4. Set up proper logging
5. Configure static file serving
6. Set up SSL/HTTPS

### Recommended Stack

- **Web Server**: Nginx
- **Application Server**: Gunicorn
- **Process Manager**: Supervisor
- **Database**: PostgreSQL
- **Cache**: Redis
- **Task Queue**: Celery with Redis broker

## 📝 Management Commands

```bash
# Initialize the site
python manage.py init <site-url> <product-type>

# Create social media links
python manage.py create_socials

# Set up tax configuration
python manage.py set_tax

# Import products (if you have import functionality)
python manage.py import_products <file-path>

# Clear cache
python manage.py clear_cache
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is proprietary. All rights reserved.

## 🆘 Support

For support and questions, please contact the development team.

---

**Note**: This repository excludes media files, product images, and database dumps to keep the repository size manageable. In production, these files should be stored separately (e.g., AWS S3, CDN) and not in the Git repository.