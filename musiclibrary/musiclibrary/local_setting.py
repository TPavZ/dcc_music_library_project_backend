# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-^!*(_o622s0f_h_&6-u@aypbm2&dy)fw-!^ip8tg9s2$(m634)'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'music_library_database',
        'USER': 'root',
        'PASSWORD': 'weakPassword',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}
