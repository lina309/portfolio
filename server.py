from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__) #creating an instance of Flask
#print(__name__)
# @app.route("/<username>/<int:post_id>") #decorater
# def hello_world(username=None, post_id=None):
#     return render_template('index.html', name=username, post_id=post_id)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/<string>')
def my_page(string):
    return render_template(string)

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thank_you.html')
        except:
            return 'Could not save to database.'
    else:
        return "Oops! Something went wrong..."

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject=data['subject']
        message=data['message']
        file= database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database:
        email = data['email']
        subject=data['subject']
        message=data['message']
        file= csv.writer(database, delimiter=',', quotechar='|')
        file.writerow([email,subject,message])

