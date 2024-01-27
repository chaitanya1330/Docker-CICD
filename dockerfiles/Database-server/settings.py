db_host = os.environ.get('DB_HOST', 'localhost')
db_port = os.environ.get('DB_PORT', '3306')
db_user = os.environ.get('DB_USER', 'root')
db_password = os.environ.get('DB_PASSWORD', '')
db_database = os.environ.get('DB_DATABASE', 'mydatabase')

# Create a MySQL connection
connection = mysql.connector.connect(
    host=db_host,
    port=db_port,
    user=db_user,
    password=db_password,
    database=db_database
)

-------------------------------------
DATABASES = {
    
        'ENGINE': 'django.db.backends.mysql',
        'NAME': db_database,
        'USER': db_user,
        'PASSWORD': db_password,
        'HOST': db_host,
        'PORT': db_port
    }
