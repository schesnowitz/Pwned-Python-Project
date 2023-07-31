from flask import Flask, render_template, request
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
from pwned_functions import get_user_input

app = Flask(__name__)
app.secret_key = "jasjf3458asg09435g]"
csrf = CSRFProtect(app)

class PasswordCheckerForm(FlaskForm):
    password_field = StringField("Enter a password to check", validators=[DataRequired(), Length(3, 100)])
    submit = SubmitField("Submit")



# @app.route("/contact")
# def contact():
   
#     return render_template("contact.html")

@app.route("/<string:path>")
def pages(path):
   
    return render_template(path)

@app.route("/", methods=["GET", "POST"])
def index():
    form = PasswordCheckerForm()
    if form.validate_on_submit():
        form_data = request.form.to_dict()
        # print(form_data)
        pass_field = form_data['password_field']
        result = get_user_input(pass_field)

        return render_template("index.html", form=form, form_data=form_data, result=result)
    return render_template("index.html", form=form)