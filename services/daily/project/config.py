import os


class BaseConfig:
    """Base configuration"""
    TESTING = False
    SECRET_KEY = os.getenv("SECRET_KEY")


class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    pass


class TestingConfig(BaseConfig):
    """Testing configuration"""
    TESTING = True


class ProductionConfig(BaseConfig):
    """Production configuration"""
    pass
