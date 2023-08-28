from flask import Flask,render_template,request,redirect
import csv

app = Flask(__name__)

@app.route("/")
def my_home():

    return 	render_template('index.html')


@app.route("/<string:html_page>")
def about(html_page):

    return 	render_template(html_page)

def write_to_file(data):
	with open('database.txt',mode='a') as database:
		email = data['email']
		subject = data['subject']
		message = data['message']
		file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
	with open('database.csv',mode='a',newline='') as database_csv:
		email = data['email']
		subject = data['subject']
		message = data['message']
		csv_writter= csv.writer(database_csv, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL,)
		csv_writter.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		data = request.form.to_dict()
		write_to_csv(data)
		return redirect('/thankyou.html')
	else:
		return 'THE FORM IS NOT SUBMITTED'