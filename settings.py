# PostgreSQL Database Configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',  # Database engine
        'NAME': 'postgres',  # Database name
        'USER': 'postgres',  # Database user
        'PASSWORD': 'Mjk2MjUtc2hwZWFy',  # Database password
        'HOST': 'localhost',  # Database host
        'PORT': '5432',  # Database port
    }
}

# Installed Apps for Django
INSTALLED_APPS = (
    'crud',  # Installed app 'crud'
)

# Secret key for this Django project
SECRET_KEY = 'SECRET KEY for this Django Project'
