# import whatever modules/functions/classes that we need for our code to work as intended

from flask import Blueprint, render_template

"""
Note that in the below code, 
some arguments are specified when creating the Blueprint object. 
The first argument, "site", is the Blueprint’s name, 
which is used by Flask’s routing mechanism. 
The second argument, __name__, is the Blueprint’s import name, 
which Flask uses to locate the Blueprint’s resources.
"""
site = Blueprint('site', __name__, template_folder='site_templates')

# each webpage is defined/controlled by a flask route -> which is a python function!

# our homepage route! Hello routing :)
@site.route('/')
def home():
    return render_template('index.html')


# make second route for the profile page
@site.route('/profile')
def profile():
    return render_template('profile.html')