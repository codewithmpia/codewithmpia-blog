from flask import render_template, redirect, request, url_for, flash
from flask.views import MethodView

from .errors import get_form_errors
from .models import db, Post, Comment
from .forms import SearchForm, CommentForm


class IndexView(MethodView):
  template_name = "index.html"
  form_class = SearchForm

  def get(self):
    form = self.form_class()
    search = request.args.get("search")

    if search:
      posts = Post.query.filter(
        Post.title.contains(search)|
        Post.resume.contains(search)|
        Post.content.contains(search)
      ).filter_by(publish=True).order_by(Post.created_at.desc())
    else:
      posts = Post.query.filter_by(publish=True).order_by(Post.created_at.desc())

    if posts.count() == 0 and search is None:
      flash("Aucun article n'est disponible pour l'instant.", "info")
    elif search is not None and posts.count() <= 0:
      flash("Aucun article ne correspond à votre recherche.", "info")

    return render_template(self.template_name, posts=posts, form=form, search=search)

  

class PostDetailView(MethodView):
  template_name = "detail.html"
  form_class = CommentForm

  def get(self, slug):
    post = Post.query.filter_by(publish=True, slug=slug).first_or_404()
    print(dir(post))
    post.views += 1
    db.session.commit()
    comments = Comment.query.filter_by(post_slug=post.slug, active=True)
    form = self.form_class()
    return render_template(self.template_name, post=post, comments=comments, form=form)

  def post(self, slug):
    post = Post.query.filter_by(publish=True, slug=slug).first_or_404()
    form = self.form_class()

    if form.validate_on_submit():
      name = form.name.data
      email = form.email.data
      message = form.message.data
      new_comment = Comment(
        post_slug=post.slug,
        name=name,
        email=email,
        message=message
      )
      db.session.add(new_comment)
      db.session.commit()
      flash("Merci d'avoir commenter.", "success")
      return redirect(url_for("detail", slug=post.slug))
    elif form.errors:
      get_form_errors(form)
    return render_template(self.template_name, post=post, form=form)
  