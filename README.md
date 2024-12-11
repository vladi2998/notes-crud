Running the app locally
=============
1. Creating python virtual enviroment (optional):
```bash
python -m venv <enviroment-name>
source <enviroment-name>/bin/activate
```

2. Intalling dependencies:
```bash
cd notes-crud
pip install -r requirements.txt
```

3. Running the app:
```bash
flask --app main run
```

4. Running the app with debug mode on (optional):
```bash
flask --debug --app main run
```

Running the app via Docker Compose
=============
1. Build the Docker image:
```bash
docker-compose build
```

2. Run the Docker container:
```bash
docker-compose up
```

3. Stop the Docker container:
```bash
docker-compose down
```

4. Run the Docker container with debug mode on (optional):
```bash
docker-compose -f docker-compose.yml -f docker-compose.debug.yml up
```

Running the app via Dockerfile
=============

1. Build the Docker image:
```bash
docker build -t austrian-notes-crud .
```

2.Run the Docker container:
```bash
docker run -p 5000:5000 austrian-notes-crud:latest
```

Handling migrations
=============
The following commands are used to handle the database migrations and only work when the app is running and the database is connected:

1. Creating a new migration:
```bash
flask db migrate
```

2. Applying the migration:
```bash
flask db upgrade
```

3. Downgrading the migration:
```bash
flask db downgrade
```

Running tests
=============
```bash
python -m unittest discover tests
```
