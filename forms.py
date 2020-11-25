from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField 
from wtforms.validators import InputRequired, Email, Length

class RegisterForm(FlaskForm):
    """Form for both registration and authentication"""
    first_name = StringField(
        'First Name', 
        validators=[InputRequired(), Length(max=30)]
    )
    last_name = StringField(
        'Last Name', 
        validators=[InputRequired(), Length(max=30)]
    )
    username = StringField(
        'Username', 
        validators=[InputRequired(), Length(min=1, max=20)]
    )
    password = PasswordField(
        'Password', 
    validators=[InputRequired(), Length(min=8, max=55)]
    )
    email = StringField(
        'Email', 
        validators=[InputRequired(), Email(), Length(max=50)])


class LoginForm(FlaskForm):
    """Form for logins"""

    username = StringField(
        "Username",
        validators=[InputRequired(), Length(min=1, max=20)],
    )
    password = PasswordField(
        "Password",
        validators=[InputRequired(), Length(min=8, max=55)],
    )

class FeedbackForm(FlaskForm):
    """Form for feedback from logged in user"""
    title = StringField(
        'Title', 
        validators=[InputRequired(), Length(max=100)]
    )
    content = StringField('Content', validators=[InputRequired()])

class DeleteForm(FlaskForm):
    
    """Intentionally left blank"""
