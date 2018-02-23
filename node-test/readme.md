# Support Engineer Assignment

This example project shows some of the basic functionality of the CBT API which will test websites behind a firewall.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites
Install virtualenv

```
pip install virtualenv
```

And the CBT Node Module

```
npm install -g cbt_tunnels
```

### Setup

Download the project, and cd into the root.

Type the following command:

```
python server/server.py
```
to start the HTTP server.

Also,

```
cbt_tunnels --username USERNAME --authkey AUTHKEY
```
to get the CBT Tunnels running.

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
