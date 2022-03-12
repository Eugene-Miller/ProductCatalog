# ProductCatalog

To run run these commands from the projects main directory:

$ export FLASK_APP=flaskr
$ export FLASK_ENV=development
# run the init-db command only once to create and configure the db
$ flask init-db
$ flask run

This will start the server at http://127.0.0.1:5000/

URLS:
http://127.0.0.1:5000/create - create new products in the catalog
http://127.0.0.1:5000/search - search for existing products by product name