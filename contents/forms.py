from flask_wtf import FlaskForm
from wtforms.fields import SearchField, StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
  search = SearchField("", render_kw={"placeholder": "taper votre recherche ici..."})


class CommentForm(FlaskForm):
  name = StringField(
    label="Notre nom", 
    validators=[DataRequired(message="Le nom est obligatoire")])
  message = TextAreaField(
    label="Votre message",
    validators=[DataRequired(message="Le message est obligatoire")]
  )
  submit = SubmitField(label="Soumettre")