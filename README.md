# Getting Started

## Pre-requisites
* python 3.X

#### ensure you are navigated into this project in your terminal.
```shell script
> cd /path/to/this/project/on/your/machine
```

#### create and use a python virtual environment
```shell script
> python3 -m venv venv
> source venv/bin/activate
```

#### install all dependencies
```shell script
> pip install -r requirements.txt
```

## Running Locally
To run the application run the `statshow.py`
In a command terminal enter the following command.
```shell script
> python statshow.py
```

## Running tests
All tests should be named the same as the module but suffixed with `_test.py`
You can run all tests by running the following command in a terminal. 
```shell script
> python -m unittest discover -p "*_test.py"
```

#### Our notes on how to get started with Wiz Pyrow
Reference the original readme file [here](original_docs/README.md)


## Other Notes:
##### Commands i store in my ~/.bash_profile to help me create and use my venvs
```shell script
alias cenv="python3 -m venv"
alias pact="source ~/projects/pyrow/pyrow/bin/activate"
```