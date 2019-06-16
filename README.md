# quickcerts

Quick and easy X.509 certificate generator for SSL/TLS utilizing local PKI

## Requirements

* Python 3.4+
* cryptography 1.6+

## Installation

```
pip3 install .
```

## Usage example

```
quickcerts -D *.example.com example.com -D www.example2.com example2.com mx.example2.com
```

This command will produce following files in current directory:
* CA certificate and key
* Two certificates with keys having multiple DNS names in SubjectAlternativeName fields.

Consequent invokations will reuse created CA.

## Synopsis

```
$ quickcerts --help
usage: quickcerts [-h] [-o OUTPUT_DIR] [-k KEY_SIZE] -D DOMAINS [DOMAINS ...]

Generate RSA certificates signed by common self-signed CA

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT_DIR, --output-dir OUTPUT_DIR
                        location of certificates output (default: .)
  -k KEY_SIZE, --key-size KEY_SIZE
                        RSA key size used for all certificates (default: 2048)
  -D DOMAINS [DOMAINS ...], --domains DOMAINS [DOMAINS ...]
                        domain names covered by certificate. First one will be
                        set as CN. Option can be used multiple times (default:
                        None)
```
