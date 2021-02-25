# Example Bank Account app

### To run this up using docker-compose:
* Set environment variables as .env file based on .env-example
* Run:
```
  docker-compose up -d --build
  docker-compose exec web python manage.py migrate
```
### For using this app You have to create super user
```
docker-compose exec web python manage.py createsuperuser
```
### To load mock data:
```
docker-compose exec web  python manage.py loaddata account.json
docker-compose exec web python manage.py loaddata transactions.json
```

### To app login as superuser:
```
http://localhost:8009/admin/
```

### After login You can add transactions in admin panel 

### App urls:
* Show specific Account: account\<int:pk> ex:
```
http://localhost:8009/account/1/
```
* Show all transactions:
```
http://localhost:8009/transaction
```