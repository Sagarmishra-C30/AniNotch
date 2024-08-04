import logging.config
import os

def setup_logging(environment='DEVELOPMENT'):
    log_dir = 'logs/development' if environment == 'DEVELOPMENT' else 'logs/production'

    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_file = os.path.join(log_dir, 'app.log')
    error_file = os.path.join(log_dir, 'error.log')
    access_file = os.path.join(log_dir, 'access.log')
    data_file = os.path.join(log_dir, 'data.log')

    handlers = {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': log_file,
            'maxBytes': 5 * 1024 * 1024,
            'backupCount': 5,
            'formatter': 'detailed',
        },
        'error_file': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': error_file,
            'maxBytes': 5 * 1024 * 1024,
            'backupCount': 5,
            'formatter': 'detailed',
        },
        'access_file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': access_file,
            'maxBytes': 5 * 1024 * 1024,
            'backupCount': 5,
            'formatter': 'simple',
        },
        'data_file': { 
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': data_file,
            'maxBytes': 5 * 1024 * 1024,
            'backupCount': 5,
            'formatter': 'simple',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    }

    formatters = {
        'detailed': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        },
        'simple': {
            'format': '%(levelname)s - %(message)s',
        },
    }

    logging.config.dictConfig({
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': formatters,
        'handlers': handlers,
        'loggers': {
            '': {
                'level': 'DEBUG',
                'handlers': ['file', 'console'],
            },
            'error': {
                'level': 'ERROR',
                'handlers': ['error_file'],
                'propagate': False,
            },
            'access': {
                'level': 'INFO',
                'handlers': ['access_file'],
                'propagate': False,
            },
            'data': { 
                'level': 'INFO',
                'handlers': ['data_file'],
                'propagate': False,
            },
        },
        'root': {
            'level': 'DEBUG',
            'handlers': ['file', 'console'],
        },
    })

    logging.debug("Logging is set up.")

# initialize different loggers
app_logger = logging.getLogger()
error_logger = logging.getLogger('error')
access_logger = logging.getLogger('access')
data_logger = logging.getLogger('data')