from flask import Flask, render_template
app = Flask(__name__)

#Index route
@app.route('/')
def index():
	return render_template('index.html')

#Get started route
@app.route('/get_started')
def get_started():
	return render_template('about.html')

if __name__ == "__main__":
	app.run()