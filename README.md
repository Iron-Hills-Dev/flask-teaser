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
export CAR_PORT={DUMMY / IN_MEMORY}
flask run
```

#### More about CAR_PORT
Before running an application you need to choose car port - implementation of car service:\
DUMMY - dummy implementation, no real actions, returns always fake data.\
IN_MEMORY - saves cars in dictionary in memory - all data will disappear after restart of application.