
# pyTest Framework with

## Installation

This project requires python 3.8 To install:

```
Download and install python 3.8 from https://www.python.org/downloads/
```

Use pip to install Pipenv:

```
pip install --user pipenv
```

Install all dependencies:

```
cd <project-folder>
pipenv install
```

# End-to-end tests

The `test-e2e` command runs Selenium using the production configuration. Among other things, this will run the tests in headless mode (so no browser visible). When developing, we provide a different configuration that gives you more insight into the test run:
    $ pipenv run test-e2e
	

## Development

To run the mytestinglab tests in local machine:

    $ pipenv run test-e2e_dev

Running a specific test file:

    $ pipenv run test-e2e_dev <path/file-name.py>


Running a specific test:

    $ pipenv run test-e2e_dev -m=app
	
	$ pipenv run test-e2e_dev -k=app



## Environment variables

There are a number of environment variables you can set:

  * `TEST_URL`: The application URL [default=http://mytestinglabs.in]
  * `BROWSER`: Browser to run tests  [default=chrome]
  * `BROWSER_MODE`: Browser mode to run tests [default=None] set to `headless` to run tests in headless mode (so no browser visible).
