# Support Engineer Assignment

This example project shows some of the basic functionality of the CBT API which will test websites behind a firewall.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

## Prerequisites
First, download the project and CD into root. All commands are assuming presence in topmost directory.
### Install virtualenv

```
pip install virtualenv
```
Then, to setup the virtualenv, type:
```
virtualenv env
```
to create a local python installation.
### Install dependencies
```
env/bin/pip install selenium
```
```
env/bin/pip install urllib2
```

### Install the CBT Node Module

```
npm install -g cbt_tunnels
```

## Setup
### HTTP Server
Type the following command to start the HTTP server:

```
python server/server.py
```

### CBT Tunnels
Type the following to get the CBT Tunnels running.
```
cbt_tunnels --username USERNAME --authkey AUTHKEY
```
Where USERNAME is your login, and AUTHKEY is your API auth key.
## Running the tests

With this project, you may run tests on Windows, Android, and Mac devices.

### Test a Windows machine

Run a Windows test (most heavily commented) with:

```
python tests/TestWindows.py
```
upon success, this will set the result as 'pass' with the CBT PUT API endpoint.

### Test all machines

Running the following command:
```
python -m unittest discover tests/ -p '*.py'
```
will test all machines in the 'tests' folder.

## Authors

* **Joshua Hatcher** - *Initial work* - (https://github.com/jbjbhatcher)
