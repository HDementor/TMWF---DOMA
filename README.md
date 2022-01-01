## TMWF DOMA
### Data Obfuscation and Masking App

#### Developers: Hamza Ansari, Omer Ansari, and Norah Khan
#### Create Date: 12.23.2021

## Summary:

This is a web application which allows the user to upload a sensitive data document from the TMWF osnium system,(or for that matter any system which has customer sensitive information), and allows the user to select the specific fields to mask and creates the masked csv format


### Setting up a VirtualEnv & Flask

    Download the repository to your local machine.
    Change directories into the repository project folder
    Set up virtual environment:

    [rent-v-buy]$
    [rent-v-buy]$ python3.7 -m venv venv

    Activate virtual environment:

    [rent-v-buy]$ . venv/bin/activate
    (venv) [rent-v-buy]$

    Install all requirements:

    (venv) [rent-v-buy]$ pip install -r requirements.txt

Note: we intentionally did not upload the virtual env directory to git. You are required to create a fresh venv/ locally.
IB. How to run (in dev environment)

(venv) [rent-v-buy]$ export FLASK_APP=rentvbuy.py
(venv) [rent-v-buy]$ flask run
 * Serving Flask app "dbtest.py"
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

For tips set up and run this in Pycharm, please watch this [video](https://www.youtube.com/watch?v=bZUokrYanFM&feature=youtu.be).
