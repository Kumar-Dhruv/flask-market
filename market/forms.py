# Initialization for all the forms to be used
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User

# Class for Register Form
class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists')
    
    def validate_email_address(self, email_to_check):
        email_address = User.query.filter_by(email_address=email_to_check.data).first()
        if email_address:
            raise ValidationError('Email Address already exists')
    # Automatic validation for username and email existence by getting user object

    username = StringField(label='User Name:', validators=[Length(min=2, max=30), DataRequired()]) 
    email_address = StringField(label='Email Address:', validators=[Email(), DataRequired()]) 
    password1 = PasswordField(label='Password:', validators=[Length(min=3), DataRequired()]) 
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')
# RegisterForm containing fields - username, email, password, confirm password and submit with Length, Email, DataRequired and EqualTo validators

class LoginForm(FlaskForm):
    username = StringField(label='User Name:', validators=[DataRequired()])
    password = StringField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign In')
# LoginForm containing fields - username, password and submit with DataRequired validator