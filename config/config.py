import os

EMAIL_CREDENTIALS = {
    'account': os.environ.get('EMAIL_USER'),
    'password': os.environ.get('EMAIL_PASSWORD')
}

EMAIL_SERVER = {
    'host': 'smtp.gmail.com',
    'port': 465
}

GOOGLE_CLOUD_STORAGE = {
    'bucket': 'film-reports'
}
