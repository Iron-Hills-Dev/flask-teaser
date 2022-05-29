# Flask teaser

## Prerequisites
* Python 3.10 with pipenv installed

## How to run locally

Install python 3.10
```
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.10
```

Install pip & pipenv
```
sudo apt install python3.10-distutils
pip install pipenv==2022.4.8
```

Run inside pipenv shell
```
pipenv shell
pipenv install
flask run
```

Run application
```
export TEASER_CAR_PORT={DUMMY / IN_MEMORY / FILE/ DATABASE}


flask run
```

#### TEASER_CAR_PORT
Before running an application you need to choose `TEASER_CAR_PORT` - implementation of car service:\
**DUMMY** - dummy implementation, no real actions, returns always fake data.\
**IN_MEMORY** - saves cars in dictionary in memory - all data will disappear after restart of application.\
**FILE** - saves cars in data folder chosen with env variable:

`export TEASER_CAR_DATA_DIR={your path}`

If folder does not exist, app will create it\
If folder already has up-to-date data structure - app will use this data structure\
If folder is full, but it's not data structure - app will refuse to init\
If folder has data structure, but it's outdated - app will refuse to init\
**DATABASE** - saves cars in postgresql database. To use that port you will need to export env variables with creds:
```
export TEASER_DB_USER={your db username} 
export TEASER_DB_PASS={your db password} 
export TEASER_DB_NAME={your database name} 
export TEASER_DB_HOST={your db host} 
export TEASER_DB_PORT={your db port}
```


## How to run locally in docker container

Navigate to `.docker` directory
```
cd .docker
```

and then simply run with command
```
docker-compose up
```

Rebuild docker container after code changes
```
docker-compose build
```

or run with force rebuilding
```
docker-compose up --build
```

### Dockerized Postgres

To run postgres and pgadmin services use this command:
```
cd .docker
docker-compose -f docker-compose-services.yml up
```

Postgres:
- user: `postgres`
- pass: `postgres` 
- access from host: `localhost:5432` 
- access from container: `teaser-postgres:5432`

Pgadmin:
- portal: http://localhost:5480
- user: `codebusters@ironhills.dev`
- pass: `postgres`
