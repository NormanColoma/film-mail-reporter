import os

EMAIL_CREDENTIALS = {
    'account': os.environ.get('EMAIL_USER'),
    'password': os.environ.get('EMAIL_PASSWORD'),
    'to': os.environ.get('TO_USER_EMAIL')
}

EMAIL_SERVER = {
    'host': 'smtp.gmail.com',
    'port': 465
}

GOOGLE_CLOUD_STORAGE = {
    'bucket': 'film-reports'
}
