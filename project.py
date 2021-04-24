from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')
	
#@app.route('/sample')
#def sample():
#	return render_template('sample.html')

app.run()
