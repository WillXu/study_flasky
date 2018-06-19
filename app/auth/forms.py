
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email

class LoginForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
	
	password = PasswordField('密码', validators=[DataRequired()])
	remember_me = BooleanField('让我保持登录')
	submit = SubmitField('登录')