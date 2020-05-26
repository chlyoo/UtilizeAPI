from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import Required, Email, Length

# 20191122
from wtforms import SelectField, ValidationError
from wtforms.validators import Regexp, EqualTo

class registerform(FlaskForm):
	email = StringField('Email', validators=[Required(), Length(1, 64), Email()])
	submit = SubmitField('Save')

"""
	def validate_email(self, field):
		collection = db.get_collection('emails')
		results = collection.find_one({'id':field.data})
		if results is not None:
			raise ValidationError('Email registered successfully.')
		pass
"""