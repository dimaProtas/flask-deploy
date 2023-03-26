import os
# from dotenv import load_dotenv
# from blog.enums import EnvType
#
# load_dotenv()
#
#
# ENV = os.getenv('FLASK_ENV', default=EnvType.production)
# DEBUG = ENV == EnvType.development
#
# SECRET_KEY = os.getenv('SECRET_KEY')
#
# SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
# SQLALCHEMY_TRACK_MODIFICATIONS = False
file_path = os.path.abspath(os.getcwd())+'/instance/blog.db'


class BaseConfig(object):
    DEBUG = False
    Testing = False
    # SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+file_path
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "abcdefg123456"
    WTF_CSRF_ENABLED = True
    FLASK_ADMIN_SWATCH = 'cosmo'
    OPENAPI_URL_PREFIX = '/api/swagger'
    OPENAPI_SWAGGER_UI_PATH = '/'
    OPENAPI_SWAGGER_UI_VERSION = '3.22.0'


class DevConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")


class TestConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    pass
