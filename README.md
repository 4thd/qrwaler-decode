
## Description

A proof of concept for QR code crawling/decoding based on images.
- Fetchs images based on selected dated and query.
- Analyse images and tries QR code decoding.
- Saving datas found in json format (db.json).
- May find personnal data related to french sanitary pass (pass_db.json).

## Installation
Install the dependencies.

```sh
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run

```python
python3 main.py
```

# Disclaimer :warning:
This tool is a poc made for educational purposes only.
You are responsible for your own actions.


# Contact
[athd92@gmail.com](mailto:athd92@gmail.com)