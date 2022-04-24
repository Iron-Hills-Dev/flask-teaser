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
export TEASER_CAR_PORT={DUMMY / IN_MEMORY / FILE}
export TEASER_CAR_DATA_DIR={file-path}
flask run
```

#### More about env variables
Before running an application you need to choose **car port** - implementation of car service:\
**DUMMY** - dummy implementation, no real actions, returns always fake data.\
**IN_MEMORY** - saves cars in dictionary in memory - all data will disappear after restart of application.\
**FILE** - saves cars in data folder chosen with TEASER_CAR_DATA_DIR:\
If folder does not exist, app will create it\
If folder already has up-to-date data structure - app will use this data structure\
If folder is full, but it's not data structure - app will refuse to init\
If folder has data structure, but it's outdated - app will refuse to init\
App won't delete data folder by itself
