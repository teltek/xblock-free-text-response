import pkg_resources

from django.template import Template

def load_resource(resource_path):
    """
    Gets the content of a resource
    """
    resource_content = pkg_resources.resource_string(__name__, resource_path)

    return unicode(resource_content)


def render_template(template_path):
    """
    Returns a template which matches template_path
    """
    template_str = load_resource(template_path)
    template = Template(template_str)

    return template
