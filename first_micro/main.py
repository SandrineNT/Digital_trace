from flask import Flask
import logging

app = Flask(__name__)

LOGGER = logging.getLogger(__name__)
#logging.basicConfig(filename='record.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

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

#Afficher les log @app.route('/', methods = ['POST'])
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