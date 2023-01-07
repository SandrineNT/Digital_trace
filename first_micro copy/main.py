from flask import Flask
import logging

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
 return prefix_google + "Hello World"

analytics = initialize_analyticsreporting()
response = get_report(analytics)
nb_visitor = print_response(response)
logging.info("Test gdx") 
return prefix_google + render_template('index.html', visitors=str(nb_visitor))

@app.route('/', methods = ['POST'])
def redirect_response():
    if request.form["submit"] == "Logger":
        return redirect(url_for("logger"))
    return "Connecté!"

# Define logger on deta
@app.route('/logger', methods = ['GET', 'POST'])
def logger():

    global user_input

    print('Back-end log!', file=sys.stderr)
    logging.info("Logging test")
    value = request.form.get("textbox_input")

    return render_template("logger.html",text=value) 

# Cookies
@app.route('/cookies', methods = ['GET', 'POST'])
def get_cookies():       
    req = requests.get("https://www.google.com/")

    return req.cookies.get_dict()

@app.route('/ganalytics', methods = ['GET', 'POST'])
def get_analytics():

    mail = os.getenv("Google_mail")
    password = os.getenv("Google_password")

    payload = {'inUserName': mail, 'inUserPass': password}
    # url = 'http://www.example.com'
    other_url = "https://analytics.google.com/analytics/web/#/report-home/a164062586w272485488p243020933"
    r = requests.post(other_url, data=payload)
    req = requests.get(other_url, cookies=r.cookies)
    return req.text

@app.route('/test', methods = ['GET', 'POST'])
def get_test():

    analytics = initialize_analyticsreporting()
    response = get_report(analytics)
    nb_visitor = print_response(response)
    print("test visitor", nb_visitor)
    logging.info("Test gdx")
    return render_template('index.html', visitors=str(nb_visitor))

if __name__ == '__main__':
    app.run(debug = True)