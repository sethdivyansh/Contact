from flask import Flask, render_template, request
import mysql.connector
import requests


app = Flask(__name__)

con = mysql.connector.connect(host = "localhost", user = "root", password = "Divyansh@08", database = "contact_form")
cur = con.cursor()

@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == 'POST':
        fname = request.form.get('first_name')
        lname = request.form.get('last_name')
        mail = request.form.get('mail')
        subject = request.form.get('subject')
        message = request.form.get('message')
        print ("Your name is " + fname + lname)
        print("Email: "+mail)
        print("subject : "+subject)
        print(message)

        
        query = "insert into data values('%s' , '%s', '%s', '%s', '%s')" %(fname,lname,mail,subject,message)
        cur.execute(query)
        con.commit()
    return render_template('submit.html')

@app.route("/")
def index_page():
    return "Hello world"

@app.route("/contact")
def contact_form():
    print("Rendering page")
    return render_template("form.html")

@app.route("/responses")
def response():
    query = "select * from data"
    cur.execute(query)
    data=cur.fetchall()
    return render_template('responses.html',data = data)



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5050")




