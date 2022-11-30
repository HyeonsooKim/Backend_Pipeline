import json_log_formatter
from datetime import datetime

class CustomisedJSONFormatter(json_log_formatter.JSONFormatter):
    def json_record(self, message, extra, record):
        # breakpoint()
        if extra.get('request',0):
            _request = extra['request']
            extra['url'] = _request.__str__().split("'")[-2]
            extra['method'] = _request.method
            if not extra['url'].replace('/api/boards/', ''):
                pass
            else:
                extra['board_id'] = int(extra['url'].replace('/api/boards/', ''))

            if _request.__dict__['_auth']:
                extra['user_id'] = _request.__dict__['_auth']['user_id'] ^ 0
            else:
                extra['user_id'] = None

        extra['name'] = record.__dict__['name']
        extra['inDate'] = datetime.fromtimestamp(record.__dict__['created']).strftime('%Y-%m-%dT%X.%f')[:-3]+'Z'
        extra['detail'] = {'message': message, 'levelname':record.__dict__['levelname']}
        request = extra.pop('request', None)
        if request:
            extra['x_forward_for'] = request.META.get('X-FORWARD-FOR')
        return extra

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'standard': {
#             'format' : "[%(asctime)s] %(levelname)s %(name)s:%(lineno)s %(message)s",
#             'datefmt' : "%Y-%m-%d %H:%M:%S"
#         },
#         'json': {
#             '()': CustomisedJSONFormatter,
#         }
#     },
#     'handlers': {
#         'null': {
#             'level': 'DEBUG',
#             'class': 'logging.NullHandler',
#         },
#          'console': {
#             'level': 'INFO',
#             'class': 'logging.StreamHandler',
#             'formatter': 'standard',
#         },
#           'log_file1': {
#             'level': 'INFO',
#             'class': 'logging.FileHandler',
#             'filename': os.path.join(LOG_DIR, 'log_file1.log'),
#             'formatter': 'standard',
#         },
#         'log_file2': {
#             'level': 'INFO',
#             'class': 'logging.FileHandler',
#             'filename': os.path.join(LOG_DIR, 'log_file2.log'),
#             'formatter': 'json',
#         },
#       },
#     'loggers': {
#          'log_file1': {
#             'handlers': ['log_file1'],
#             'level': 'INFO',
#             'propagate': False,
#         },
#         'log_file2': {
#             'handlers': ['log_file2'],
#             'level': 'INFO',
#             'propagate': False,
#         }
#       }
# }