# Pendulum

<img src="./pendulum-logo.png" align="left" width="192px" height="192px"/>
<img align="left" width="0" height="192px" hspace="10"/>

> **Pendulum** is an intelligent text parsing utility with a focus on time.

[![License: LGPL v3](https://img.shields.io/badge/License-LGPL%20v3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0) [![Under Development](https://img.shields.io/badge/under-development-orange.svg)](https://github.com/cez-aug/github-project-boilerplate)

> Through the use of Natural Language Processing (NLP), Pendulum is able to take in a blob of text and extract context along with fuzzy dates and times. Through this extraction and evaluation the system can determine whether the given text contains any reminders, due dates, or past dates.

> Combining the extracted context with the extracted dates allows for the generation of a Smart Note that automatically attaches reminders and dates that are relevant to the notes content.

<br>
<br>

## Prerequisites

* Python >= 3.7.x
* virtualenv >= 16.1.x

## Installing

```sh
$ source ./env/bin/activate
$ pip install -r requirements.txt
$ python setup.py install

```

# Getting Started
> There are two ways to run Pendulum:
1. In demo mode with preset text:
```python pendulum/```

2. Running it as an API:
```python pendulum/api.py```
```curl --request POST \
  --url http://localhost:8000/SmartNote \
  --header 'Cache-Control: no-cache' \
  --header 'Content-Type: application/json' \
  --header 'Postman-Token: f334235d-c5c6-4490-8d8f-0c35ea130042' \
  --data '{\n	"note": "Finish the homework for Artificial intelligence by this friday"\n}'```


<!--
## Usage

> **[?]** Tell contributors how to use it.

-->
