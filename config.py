class Config(object):
    DEBUG = True
    DEVELOPMENT = True
    TESTING = True
    PORT = 8080
    ATLAS_URI = 'mongodb://user:password@localhost'

class ProductionConfig(Config):
    DEVELOPMENT = False
    DEBUG = False
    PORT = 80
    ATLAS_URI = 'mongodb://user:password@localhost'