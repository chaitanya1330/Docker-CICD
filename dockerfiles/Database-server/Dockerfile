FROM ubuntu:18.04
LABEL maintainer="chaitanya@gmail.com"

RUN apt-get update && apt-get -y install apache2
EXPOSE 80

ENTRYPOINT ["/usr/sbin/apachectl"]
CMD ["-D", "FOREGROUND"]

-----------------------------------------------

FROM ubuntu:18.04

LABEL maintainer="chaitanyachaitu@gmail.com"

docker run -d --name docker-database -e MYSQL_ROOT_PASSWORD=chay1234 -p 3306:3306 docker_image:latest
docker exec -it mysql-container bash

created a database inside that: host is localhost
user is root
port is 3306
database name  = new_chatapp

-------------
# Use the official MySQL image from Docker Hub
FROM mysql:latest

# Set environment variables to configure MySQL
ENV MYSQL_ROOT_PASSWORD=chay1234
ENV MYSQL_DATABASE=chatapp_db
ENV MYSQL_USER=chay
ENV MYSQL_PASSWORD=chay@1234
ENV MYSQL_HOST=localhost  
-----------------
mysql -h localhost -u chay -p

docker exec -it mysql-database bash
----------------------------------------------------------

in settings.py file im giving like this.....

 'NAME': 'chatapp_db',
        'database_host' = os.environ.get('DATABASE_HOST', 'custom-con'),
        'database_user' = os.environ.get('DATABASE_USER', 'chay'),
        'database_password' = os.environ.get('DATABASE_PASSWORD', 'chay@1234'),
        'PORT': '3306',
    }
}

docker run -d --name=app_cont -e MYSQL_PASSWORD=chay@1234 --network=docker_network_comp -p 8000:8000 d13feb504713

docker run -d --name=app_cont --network=docker_network_comp -p 8000:8000 -e DATABASE_USER=chay -e DATABASE_PASSWORD=chay@1234 81b74e2ef17c

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'chatapp_db',
        #'USER': 'chay',
        'USER' : os.environ.get('DATABASE_USER'),
        'PASSWORD' : os.environ.get('DATABASE_PASSWORD'),
        #'PASSWORD': 'chay@1234',
        'HOST': 'custom-con',
        'PORT': '3306',
    }
}
---------------------------------------------------
FROM python:3.6

ENV DATABASE_USER=chay
ENV DATABASE_PASSWORD=chay@1234

RUN apt-get update
RUN apt-get install --yes python3-pip

RUN mkdir /new_chatapp
COPY /new_chatapp  /new_chatapp
WORKDIR /new_chatapp
RUN pip3 install -r requirements.txt
RUN pip3 install mysqlclient
EXPOSE 8000
WORKDIR /new_chatapp/fundoo/
ENTRYPOINT  python3 manage.py migrate && python3 manage.py runserver 0.0.0.0:8000
-----------------------------------------------------------------------------------------------
To create a Docker Volume use the command:

docker volume create testvol1
docker volume ls
docker volume inspect testvol1
---------------------------------------
Mounting a Volume using -v or --mount
---------------------------------------
docker run -it --name=srv01 --mount source=testvol1,destination=/data centos
docker run -it --name srv04 -v testvol1:/data centos
docker run -it --volumes-from srv01 --name srv02 centos /bin/bash
---------------------------------------
Mounting a Host Directory as a Data volume 
---------------------------------------
mkdir files
cd files
touch file.txt
docker run -it –-name srv05 -v "$(pwd)":/data1 centos
---------------------------------------------
To remove a volume:
docker volume rm [volume_name]
	