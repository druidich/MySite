import os

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.db')
SECRET_KEY = 'hardToguessString'


class Config:
    SECRET_KEY = 'hardToguessString'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

    # email setting
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    MAIL_SERVER = 'smtp.yandex.com'
    MAIL_USE_SSL = True
    FLASKY_MAIL_SENDER = 'Flasky Admin email server '
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USERNAME = 'tests.testovich'
    MAIL_PASSWORD = 'testSite'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data.db')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir,
                                                                                                 'data-test.db')


class ProductionConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data.db')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
