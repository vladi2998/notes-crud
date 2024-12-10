# Using lightweight alpine image
FROM python:3.12-alpine

# Update packages and run virtual enviroment
RUN apk update
RUN python -m venv /usr/src/notes-crud-venv

# Defining working directory and adding source code
WORKDIR /usr/src/
COPY requirements.txt ./
COPY main.py ./
COPY config.py ./
COPY ./tests ./tests
COPY ./app ./app

# Install API dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Start app
EXPOSE 5000
CMD ["flask", "--debug", "--app", "main.py", "run", "--host=0.0.0.0"]
