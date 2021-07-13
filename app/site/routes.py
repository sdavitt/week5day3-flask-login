# import whatever modules/functions/classes that we need for our code to work as intended
from flask import Blueprint, render_template, request, flash, redirect, url_for

# import any database model we're using
from app.models import Animal, db

# import our form that we're using
from app.forms import newAnimalForm

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
@site.route('/', methods=['GET', 'POST'])
def home():
    form = newAnimalForm()
    try:
        if request.method == 'POST' and form.validate_on_submit():
            namedata = form.name.data
            weightdata = form.weight.data
            heightdata = form.height.data
            climatedata = form.climate.data
            regiondata = form.region.data
            
            print(namedata, regiondata)

            # create an animal object in my database based off the form data
            new_animal = Animal(name=namedata, weight=weightdata, height=heightdata, climate=climatedata, region=regiondata)

            #add the newly created animal to our database - always a two step process
            db.session.add(new_animal)
            db.session.commit()

            # tell our user that we've added something - using flash messages!
            flash(f'You have successfully added the animal {namedata} to your database.')

            return redirect(url_for('site.home'))
    except:
        flash(f'Invalid form input, try again.')
        return redirect(url_for('site.home'))
    return render_template('index.html', form=form)


# make second route for the profile page
@site.route('/profile')
def profile():
    return render_template('profile.html')