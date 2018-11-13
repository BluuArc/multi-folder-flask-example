# Multi Folder Flask Example

## What is it?

This is an example of using multiple modules with a single `server.py` file. The intention was to showcase one way of splitting up APIs for a server into different repositories. Originally made as an example for the [lug.cs.uic.edu website redesign project](https://github.com/lugatuic/lug.cs.uic.edu-2018). Basic structure of the server used here and some instructions for this README is from that project.

## Requirements

* Python 3.7.1+
* Pipenv

## Installation

1. Clone the repository
2. Initialize the environment with `pipenv install --dev`

## Running

* Windows Powershell

  ```posh
  pipenv shell
  $env:FLASK_APP = 'server.py'
  $env:FLASK_ENV = 'development'
  flask run
  ```
* Bash (MacOS and Linux):

  ```bash
  pipenv shell
  export FLASK_APP=server.py
  export FLASK_ENV=development
  flask run
  ```

* By default, the server should run off of `localhost` on port `5000`

## Routes

* Root
  * `/` - returns "You're at root!"
  * `/json` - returns data inside `sample.json`
