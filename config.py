import os
base_dir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECREY_KEY') or 'test_key'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    TLDRMED_MAIL_SUBJECT_PREFIX = '[TLDRMed] '
    TLDRMED_MAIL_SENDER = 'TLDRMed Admin <contact@georg.io>'
    TLDRMED_ADMIN = os.environ.get('TLDRMED_ADMIN')

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(base_dir, 'data-dev.sqlite')

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
    }
