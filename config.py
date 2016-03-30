import os

# 根目录
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# 数据库名
DB_NAME = 'flasky'


# 基本配置
class Config:
    # 安全密钥
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'I am sleeping!'

    # 邮件服务
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USER')
    MAIL_PASSWORD = os.environ.get('MAIL_PASS')

    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'FLASK ADMIN <no-reply@flasky.com>'
    FLASKY_ADMIN = os.environ.get('MAIL_USER')

    # 数据库
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True

    @staticmethod
    def init_app(app):
        pass


# 开发配置
class DevelopmentConfig(Config):
    # 开启调试
    DEBUG = True
    # 开发数据库配置
    SQLALCHEMY_DATABASE_URI = os.environ.get('MYSQL_URL') + DB_NAME + '_dev'


# 测试配置
class TestingConfig(Config):
    # 开启测试
    TESTING = True
    # 测试数据库配置
    SQLALCHEMY_DATABASE_URI = os.environ.get('MYSQL_URL') + DB_NAME + '_test'


# 上线配置
class ProductionConfig(Config):
    # 上线数据库配置
    SQLALCHEMY_DATABASE_URI = os.environ.get('MYSQL_URL') + DB_NAME


# 配置字典
config = dict(
    development = DevelopmentConfig,
    testing = TestingConfig,
    production = ProductionConfig,

    default = DevelopmentConfig
)
