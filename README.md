# TLDRMed

## Install Dependencies

```bash
$ mkdir venv
$ virtualenv venv/ --no-site-packages
$ source venv/bin/activate
$ pip install -r requirements.txt
```

## Run Application in Development Mode

```bash
$ python config.py runserver
```

As the development environment is the only one implemented so far this should
start the application on a local development server and is then accessible
in your web browser at `http://localhost:5000`.
