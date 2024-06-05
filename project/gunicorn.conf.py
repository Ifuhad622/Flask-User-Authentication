# gunicorn.conf

# Number of worker processes
workers = 4

# Bind address and port
bind = '0.0.0.0:9000'

# Logging
errorlog = '/var/log/gunicorn/project1_error.log'

accesslog = '/var/log/gunicorn/project1_access.log'
loglevel = 'info'

# Timeout
timeout = 60
