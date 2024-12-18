YAML and OpenAPI auto-generated client for GLS API
==================================================

[GLS](https://gls-group.com) is a delivery company operating in middle Europe.
In this repository there's a gls.yaml file and a simple code for use [GLS API described here:](https://api.mygls.cz/) 
I've developed this code because GLS company currently doesn't provide yaml.
Gls.yaml file is generated from the provided documentation by AI and heavily modified by myself.
Rest of the client is autogenerated from gls.yaml with [OpenAPI generator](https://opencollective.com/openapi_generator)

getprintedlabels.py is a CLI implementation of getPrintedLabels. It can create PDF from:
* Package Nr. (that code printed on the label)
* Package ID (internal number in GLS database. It's the number you get from PrepareLabels API call)

Features
--------
* The behavior can be configured via settings.local.toml
* Secrets are stored in .secrets.toml (you must create it)

Dependencies
------------

* urllib3
* python_dateutil
* pydantic
* typing-extensions
* dynaconf
* hashlib
* argparse

Installation
------------
* clone the repository
* create venv (python -m venv .venv)
* install the main package (.venv/bin/pip install -e glslabelapi)
* install the openapi_client generated package (.venv/bin/pip install -e glslabelapi/openapi_client)
* check, add or modify settings.local.toml and .secrets.toml

Usage
-----

`python getprintedlabels.py -id <your-package-id> -o label.pdf`
Expected behavior is you get PDF with label(s) or API error.

Current state
-------------
* DeleteLabels and PrepareLabels weren't tested. Check it before you use it.
* There may be glitches in yaml definition caused by lack of documentation. 