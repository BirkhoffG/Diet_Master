# Get Started

## Create Users

Migrate first:

```
> python manage.py migrate
```

### Create Superusers/Admin

```
> python manage.py createsuperuser 
```



## Create Apps

```
> python manage.py startapp [app-name]
```



## Make Migration

Make migration after new models.

```
> python manage.py makemigrations [app-name]
```

Then migrate:

```
> python manage.py migrate
```



## Create new Models

Enable `shell`

```
> python manage.py shell
```

