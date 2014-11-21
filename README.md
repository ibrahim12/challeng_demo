challeng_demo
=============

Demo Project For challeng

## Installation

- Create a folder name **project**

- Clone git repo inside the folder as 
    
```

git@github.com:ibrahim12/challeng_demo.git

```

- Create VirtualEnv and Install dependencies

```
virtualenv ve
pip install -r challeng_demo/requirements.txt

```

- Init Database

```

cd challeng_demo
python manage.py db init
python manage.py db migrate
python manage.py db upgrade

```

- Run the Server

```

python manage.py runserver

# In Debug Mode
python manage.py runserver --debug

```



