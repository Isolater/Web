from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms import validators, ValidationError
from ..models import User

class LoginForm(Form):
    email = StringField('Email', [validators.required, validators.length(min=1, max=64), validators.Email])
    password = PasswordField('Password', [validators.required])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log in')
    

class RegistrationForm(Form):
    email = StringField('Email', [validators.required, validators.length(min=1, max=6), validators.Email])
    username = StringField('Username', [validators.required, validators.length(min=1,max=64),
                                        validators.regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                                          'Usernames must have only letters,''numbers, dots or underscores')])
    password = PasswordField('Password', [validators.required, validators.equal_to('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm password', [validators.required])
    submit = SubmitField('Register')
    
    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')
        
    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')