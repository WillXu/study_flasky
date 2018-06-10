from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment

from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)
moment = Moment(app)


class NameForm(FlaskForm):
	name = StringField('你叫什么名字？', validators=[DataRequired()])
	submit = SubmitField('提交')
		

@app.route('/', methods=['GET', 'POST'])
def index():
	name = None
	form = NameForm()
	if form.validate_on_submit():
		name = form.name.data
		form.name.data = ''
	return render_template('index.html', form=form, name=name, current_time=datetime.utcnow())


@app.route('/user/<name>')
def user(name):
	return render_template('user.html', name=name) 

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'),404 

@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'),500
