"""TODO: Add module docstring"""

from flask_login import current_user
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

from flaskblog.models import User

class RegistrationForm(FlaskForm):
    """TODO: Add class docstring"""
    username = StringField(
        'Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField(
        'Email', validators=[DataRequired(), Email()])
    password = PasswordField(
        'Password', validators=[DataRequired()])
    confirm_password = PasswordField(
        'Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        """TODO: Add method docstring"""
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(
                f'Username "{user.username}" is taken. Log in, or choose another.')

    def validate_email(self, email):
        """TODO: Add method docstring"""
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(
                f'Email "{user.email}" is taken. Log in, or use another.')


class LoginForm(FlaskForm):
    """TODO: Add class docstring"""
    email = StringField(
        'Email', validators=[DataRequired(), Email()])
    password = PasswordField(
        'Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log In')


class UpdateAccountForm(FlaskForm):
    """TODO: Add class docstring"""
    username = StringField(
        'Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField(
        'Email', validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[
                        FileAllowed(['jpg', 'png', 'gif'])])
    submit = SubmitField('Update Profile')

    def validate_username(self, username):
        """TODO: Add method docstring"""
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError(
                    f'Username "{user.username}" is taken. Log in, or choose another.')

    def validate_email(self, email):
        """TODO: Add method docstring"""
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError(
                    f'Email "{user.email}" is taken. Log in, or use another.')


class RequestResetForm(FlaskForm):
    """TODO: Add class docstring"""
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        """TODO: Add module docstring"""
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError(
                'There is no account with that email. You must register first.')


class ResetPasswordForm(FlaskForm):
    """TODO: Add class docstring"""
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[
                                     DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')
