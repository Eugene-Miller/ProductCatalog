# ProductCatalog

The project was done using python 3.9.2 with the Flask framework and a sqlite database in a linux environment.

To download run:
```bash
git clone https://github.com/Eugene-Miller/ProductCatalog.git
```

To install flask run:
```bash
pip install Flask
```

To start the application run these commands from the projects main directory:
```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```
This will start a http server at http://127.0.0.1:5000/

URLs:

http://127.0.0.1:5000/create - create new products in the catalog

http://127.0.0.1:5000/search - search for existing products by product name
