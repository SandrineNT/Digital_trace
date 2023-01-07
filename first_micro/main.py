from flask import Flask, render_template, request
import logging
import sys
import requests


app = Flask(__name__)

logging.basicConfig(filename='record.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

@app.route('/', methods=["GET"])
def hello_world():
 prefix_google = """
 <!-- Google tag (gtag.js) -->
<script async
src="https://www.googletagmanager.com/gtag/js?id=UA-250994065-2"></script>
<script>
 window.dataLayer = window.dataLayer || [];
 function gtag(){dataLayer.push(arguments);}
 gtag('js', new Date());
 gtag('config', 'UA-250994065-2');
</script>
 """

 return prefix_google + "Hello Word"

 # Define logger on deta
@app.route('/Logs', methods = ['GET', 'POST'])
def Logs():
 app.logger.info(' log')
 with open('record.log','r') as file:
    content_log=file.read()
    print(content_log)
 return content_log


@app.route('/Cookies', methods=["GET","POST"])
def Cookies():
    req=requests.get("https://www.google.com/")
    return req.cookies.get_dict()


@app.route('/Analitics', methods=["GET","POST"])
def Analytics():
    req=requests.get("https://analytics.google.com/analytics/web/#/report-home/a250994065w345182162p281264556")
    return req.text


@app.route('/Utilisateur')
def fetch_users():
    
    return "the number of visitors fetched is : 2 "
