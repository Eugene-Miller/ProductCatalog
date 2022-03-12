# ProductCatalog

The project was done using python with the flask framework and a sqlite database in a linux environment.

To start the application run these commands from the projects main directory:
```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask init-db
flask run
```
This will start a http server at http://127.0.0.1:5000/

URLs:

http://127.0.0.1:5000/create - create new products in the catalog

http://127.0.0.1:5000/search - search for existing products by product name
