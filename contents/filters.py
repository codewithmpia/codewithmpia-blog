import markdown
from pygments.formatters import HtmlFormatter

def format_markdown(object):
    md_template_string = markdown.markdown(object, extensions=["fenced_code", "codehilite"])
    formatter = HtmlFormatter(style="vim", full=True, cssclass="codehilite")
    css_string = formatter.get_style_defs()
    md_css_string = "<style>" + css_string + "</style>"
    md_template = md_css_string + md_template_string
    return md_template


def pluralize(object, singular="", plural="s"):
    if object.count() <= 1:
        return singular
    return plural