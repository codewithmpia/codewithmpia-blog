from flask_admin.form import ImageUploadField
from flask_admin.contrib.sqla import ModelView

from .utils import BASE_DIR


class PostAdminView(ModelView):
  column_list = ["title", "created_at", "publish"]
  form_extra_fields = {
    "image": ImageUploadField(
      label="Image",
      base_path=BASE_DIR / "assets",
      relative_path="static/images/posts/"
    )
  }
  
  def on_model_change(self, form, model, is_created):
    if is_created:
      model.generate_slug()
    return super().on_model_change(form, model, is_created)
  

class CommentAdminView(ModelView):
  column_list = ["name", "created_at", "active"]