#!/bin/bash

mkdir -p /var/log/trackme/

# Put nginx file for both django and node into mounted volume folder /opt/data/conf
echo "DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE" >> /tmp/env.ini
echo "project_name=dexterhive" >> /tmp/env.ini

case "$1" in 
    -a | --app-server)
        echo "Running Gunicorn"

	# Run collectstatic
	python manage.py collectstatic --noinput

        # Run DB Migrate & Load Fixture
        python manage.py migrate --noinput
	
	
        #copy nginx conf and restart
        cp deploy/templates/nginx_ecs.conf /etc/nginx/sites-enabled/app.conf
        service nginx restart
        j2 --format=env deploy/templates/supervisor_ecs.conf /tmp/env.ini > /etc/supervisor/conf.d/gunicorn.conf

    *)
      echo "Invalid option, please specify one of these (-a)"
      exit
    ;;
esac
service supervisor restart
