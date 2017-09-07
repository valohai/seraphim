Seraphim
========

Tools for dealing with AngelList.

Usage
-----

* Create and enter a Python 3 virtualenv.
* Install the requirements from `requirements.txt`.
* Log in on AngelList on your browser.
* Copy the value of the `_angellist` cookie (a hex string); this is your *session ID*. You'll need it below.

### Download startups who are looking for marketing specialists

The first command runs a search and outputs matching Startup IDs as a JSON list.
The second command ingests the JSON list and downloads JSON documents of each company to the directory specified.

```
$ python seraphim_cli.py -s SESSION_ID_HERE search -k "marketing specialist" > marketing-specialists.json
$ python seraphim_cli.py -s SESSION_ID_HERE download -d marketing-specialist-companies -f marketing-specialists.json
```

