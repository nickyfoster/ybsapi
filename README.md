##Heroku logs
```
heroku logs --tail --app ybsapi
```
##Migrations
```
heroku run python manage.py db upgrade --app
```
##Exporting environment variables
```
export APP_SETTINGS="config.DevelopmentConfig"
export DATABASE_URL="postgresql://localhost/ybs"
```
##Database creation
```
sudo -u name_of_user createdb ybs #to create
psql -U name_of_user -d ybs #to check
```
##Database updates.
1. Edit database schemas.
2. Delete migrations folder.
3. Remember to mkdir versions with ".keep" file
```
python3.7 manage.py db init
python3.7 manage.py db migrate
python3.7 manage.py db upgrade
```
##Heroku setup
```
heroku create name_of_your_application
heroku config:set APP_SETTINGS=config.ProductionConfig --remote prod
heroku config --app name_of_your_application
heroku run python manage.py db upgrade --app name_of_your_application # migrations
```
##Heroku logs
```
heroku logs --tail --app ybsapi
```
###Flask and Heroku tutorial
https://medium.com/@dushan14/create-a-web-application-with-python-flask-postgresql-and-deploy-on-heroku-243d548335cc
###VK verify user ID
https://vk.com/dev/vk_apps_launch_params


