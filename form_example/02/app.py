from flask import Flask , render_template
from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField 
from wtforms.validators import InputRequired , Length
app = Flask(__name__)
app.config['SECRET_KEY'] = 'google'
class LoginForm(FlaskForm):
	username = StringField('username', validators = [InputRequired(message= "A username is required"),Length(min = 5 ,max = 10 , message ='must be between 5 and 10')])
	password = PasswordField('password' , validators = [InputRequired(message = "A pasword is required")])



@app.route('/form',methods=['post','GET'])
def form():
	form = LoginForm()
	if form.validate_on_submit():
		return "<h1> the username is {} . the password is {} </h1".format(form.username.data , form.password.data)
	return render_template('form.html',form = form)

if __name__ == '__main__':
	app.run(debug = True)