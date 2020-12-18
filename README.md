# flask-random-words
Using Random word library in Flask to get Word and Definitions

## About

Using the [remaudcorentin-dev/python-randomword](https://github.com/remaudcorentin-dev/python-randomword) library in Python Flask to get the word and definition on a GET request.

## Usage

Build and run:

```
$ docker-compose build
$ docker-compose up
```

Test:

```
$ curl http://localhost:5000
{"word":"auxiliary","definition":"helping supporting"}
```

Using render template:

![image](https://user-images.githubusercontent.com/567298/102627850-7bcb2780-4151-11eb-872a-bfe57b024528.png)
