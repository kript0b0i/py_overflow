# py_overflow

# Vulnerable Python Server
This server application is provided for educational purposes to demonstrate vulnerabilities. It should NOT be used in production environments.

## Overview
Binds to port `9999` by default
Multi-threaded to handle concurrent connections
Contains several intentional vulnerabilities:
Command injection in `COMMAND` route
Format string bug in `PRINT` route
Buffer overflow in `func1()` via OVERFLOW route
Plaintext communication without SSL
## Setup
Requires Python 3
Run `vuln_server.py` to start the server
Optionally change `BIND_ADDR` and `BIND_PORT`
## Disclaimer
This application is strictly for educational purposes. It intentionally contains security flaws. Do not run it on systems connected to a public network or containing sensitive information.

## Exploit Script
This Python script is designed to test vulnerabilities in the example vulnerable server application.

## Usage
Update `target_host` and `target_port` to point to the vulnerable server
Run `exploit.py`
This will:
Attempt command injection
Test format string bug
Trigger buffer overflow
Spawn interactive shell if exploits succeed
## Disclaimer
This exploit is for testing purposes only. Do not use against systems you do not own or have permission to test.

## Disabling Exploits
Comment out relevant sections to disable individual exploits
Review code to understand each vulnerability
## Improving Exploits
The buffer overflow uses a dummy RET address. Find exact offset and RETURN pointer.
The command injection can be expanded to execute other commands.
Format string bug can be used to write arbitrary memory.
