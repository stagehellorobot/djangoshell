# Djangoshell

A simple Django application that returns a reverse shell when deployed to the IP that is passed as a GET parameter to index.

## Usage

```
python3 index.py runserver
curl http://djangoshell/?ip=127.0.0.1
```
