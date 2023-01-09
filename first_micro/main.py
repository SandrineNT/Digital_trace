from flask import Flask, render_template, request,url_for
import logging
import sys
import requests
import matplotlib.pyplot as plt
import os
import base64
import io
import pandas as pd
from pytrends.request import TrendReq
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

app = Flask(__name__)
#app.config["DEBUG"] = True
logging.basicConfig(filename='record.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

#if __name__ == '__main__':
#    app.run(host="localhost", port=8000, debug=True)

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

@app.route("/pytrends")
def trending_searches(self, pn='song'):
        """Request data from Google's Hot Searches section and return a dataframe"""

        # make the request
        # forms become obsolete due to the new TRENDING_SEARCHES_URL
        # forms = {'ajax': 1, 'pn': pn, 'htd': '', 'htv': 'l'}
        req_json = self._get_data(
            url=TrendReq.TRENDING_SEARCHES_URL,
            method=TrendReq.GET_METHOD
        )[pn]
        result_df = pd.DataFrame(req_json)
        return result_df

def pytrends():
    
    Pytrend = TrendReq() 
    Pytrend.build_payload(kw_list=trending_searches(pn='song'), timeframe='2022-01-01 2022-12-30' , geo ='ID')
    df = Pytrend.interest_over_time()
    #generate plot
    x=trending_searches(pn='song')[:,1]
    y=trending_searches(pn='song')[:,2]
    fig=plt.figure(figsize=(8,5))
    plt.plot(df.index,x)
    plt.plot(df.index,y)
    
    pngImage = io.BytesIO()
    FigureCanvas(fig).print_png(pngImage)
     # Encode PNG image to base64 string
    pngImageB64String = "data:image/png;base64,"
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')

    return render_template("image.html", image=pngImageB64String)