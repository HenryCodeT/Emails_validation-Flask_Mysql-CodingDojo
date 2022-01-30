from flask import redirect, render_template, request
from email_app import app
from email_app.models.email_model import Email

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/results",methods=['GET','post'])
def results():
    if request.method == 'POST':
        data = {
            'email':request.form['email']
        }

        if not Email.validate_email(data):
            return redirect("/")

        method_response_create_email = Email.create_email(data)
        print("el correo ha sido creado",method_response_create_email)
        return redirect("/results")
    else:
        emails_models = Email.get_all_emails()
        return render_template("results.html",emails = emails_models)
@app.route("/delete/<int:id>")
def delete(id):
    data = {
        'id':id
    }
    Email.delete_email(data)    
    return redirect("/results")