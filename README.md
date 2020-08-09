# quickcerts

[![quickcerts](https://snapcraft.io//quickcerts/badge.svg)](https://snapcraft.io/quickcerts)

Quick and easy X.509 certificate generator for SSL/TLS utilizing local PKI

---

:heart: :heart: :heart:

You can say thanks to the author by donations to these wallets:

- ETH: `0xB71250010e8beC90C5f9ddF408251eBA9dD7320e`
- BTC:
  - Legacy: `1N89PRvG1CSsUk9sxKwBwudN6TjTPQ1N8a`
  - Segwit: `bc1qc0hcyxc000qf0ketv4r44ld7dlgmmu73rtlntw`

---

## Features

* Easy to use.
* Genarates both client and server certificates.
* Produces certificates with proper attributes (Key Usage, Extended Key Usage, Authority Key Identifier, Subject Key Identifier and so on).
* Supports certificates with multiple domain names (SAN, SubjectAlternativeName).
* Supports wildcard certificates.

## Requirements

* Python 3.4+
* cryptography 1.6+

## Installation

#### From source

Run this command within source directory:

```sh
pip3 install .
```

#### From PyPI

```sh
pip3 install quickcerts
```

#### Snap Store

[![Get it from the Snap Store](https://snapcraft.io/static/images/badges/en/snap-store-black.svg)](https://snapcraft.io/quickcerts)

```sh
sudo snap install quickcerts
```

#### Docker

For deployment with Docker see "Docker" section below.

## Usage example

```bash
quickcerts -D *.example.com example.com -D www.example2.com example2.com mx.example2.com -C "John Doe" -C "Jane Doe"
```

This command will produce following files in current directory:
* CA certificate and key
* Two server certificates having multiple DNS names in SubjectAlternativeName fields and keys for that certificates.
* Two client certificates for CN="John Doe" and CN="Jane Doe" (and keys for them).

Consequent invokations will reuse created CA.

## Docker

Also you may run this application with Docker:

```sh
docker run -it --rm -v "$(pwd)/certs:/certs" \
    yarmak/quickcerts -D server -C client1 -C client2 -C client3
```

In this example CA and certificates will be created in `./certs` directory.

## Synopsis

```
$ quickcerts --help
usage: quickcerts [-h] [-o OUTPUT_DIR] [-k KEY_SIZE]
                  [-D DOMAINS [DOMAINS ...]] [-C CLIENT]

Generate RSA certificates signed by common self-signed CA

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT_DIR, --output-dir OUTPUT_DIR
                        location of certificates output (default: .)
  -k KEY_SIZE, --key-size KEY_SIZE
                        RSA key size used for all certificates (default: 2048)
  -D DOMAINS [DOMAINS ...], --domains DOMAINS [DOMAINS ...]
                        Generate server certificate which covers following
                        domains delimited by spaces. First one will be set as
                        CN. Option can be used multiple times. (default: None)
  -C CLIENT, --client CLIENT
                        Generate client certificate with following name.
                        (default: None)
```
