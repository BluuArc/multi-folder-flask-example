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

* By default, the server should run off of `localhost` or `127.0.0.1` on port `5000`

## Routes

* Root
  * `/` - returns "You're at root!"
  * `/json` - returns data inside `sample.json`
* Routes for `website`
  * `/website/` - returns `website/index.html`, which is a webpage that calls into the static and API endpoints for the mock `website` project
  * `/website/static/<path:filename>` - returns files in the `website/static` folder
  * `/website/api/members` - returns data in `website/apiMock/members.json` through API endpoint setup in `website/server.py`
* Routes for `my_cool_app`
  * `/my_cool_app/` - returns `my_cool_app/index.html`, which is a webpage that calls into the static and API endpoints for the mock `my_cool_app` project
  * `/my_cool_app/static/<path:filename>` - returns files in the `my_cool_app/static` folder
  * `/my_cool_app/api/members` - returns data in `my_cool_app/apiMock/members.json` through API endpoint setup in `my_cool_app/server.py`

## Adding a Project API to the Root Server

1. The project must have `__init__.py` and another `.py` file (e.g. `server.py`) that has a method that takes in a Flask instance and sets up routes. For simplicity, this example uses `server.py` and the method name `extendApplication` for `website` and `my_cool_app`, both of which represent separate projects with APIs that do different things on the same server
  * Examples: `website/server.py` and `my_cool_app/server.py`
  * Needing `__init__.py` is mentioned [here](https://stackoverflow.com/questions/4383571/importing-files-from-different-folder/48859135#48859135)
2. The `server.py` in the root repository must import the project's `.py` file with the method setup in Step 1 and call it with its Flask instance.

## Implementation Notes & Concerns

* Unknown behavior if a server subproject/submodule uses a dependency in its `server.py` file that the root server doesn't use (probably a dependency error?).
* A better solution would be to have the same `server.py` for each submodule with the same `extendApplication` method, but also include a standalone mode for running each submodule's `server.py` as the server itself.
* Compatibility and whether or not this is the "best" way to import relative modules is largely unknown to me. Many other solutions for relative imports in Python are mentioned in [this StackOverflow post](https://stackoverflow.com/questions/4383571/importing-files-from-different-folder/48859135).
* Each subproject to be added to the root server will have to be done one by one. It may be worthwhile to find a way to load the submodules programmatically.
