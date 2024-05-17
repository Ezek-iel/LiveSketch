from . import user_blueprint


@user_blueprint.route("/")
def home():
    return '<h1> Hello World </h1>'