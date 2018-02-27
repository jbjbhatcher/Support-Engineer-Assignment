# Support Engineer Assignment

This example project shows some of the basic functionality of the CBT API which will test websites behind a firewall. It will begin with showing how to test on a single machine (Windows) while setting the pass/fail result through the Cross Browser Testing API.

Then, this documentation will show how to test multiple tests sequentially.

## Prerequisites
### Install the following python modules:
```
pip install selenium
```
```
pip install urllib2
```

### Install the CBT Node Module: 

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
Windows is the file which is most heavily commented, so this will be the first one we test with. If you understand this file, the others should follow suit.

Run a test on a Cross Browser Testing Windows machine by executing the command:

```
python tests/TestWindows.py
```
upon success, this will set the result as 'pass' with the CBT PUT API endpoint.

### Test multiple machines

Running the following command:
```
python -m unittest discover tests/ -p '*.py'
```
will test all machines in the 'tests' folder.

## Authors

* **Joshua Hatcher** - *Initial work* - (https://github.com/jbjbhatcher)
