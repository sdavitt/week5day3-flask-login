# import whatever modules/functions/classes that we need for our code to work as intended
from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify

from flask_login import current_user, login_required

# import any database model we're using
from app.models import Animal, db

# import our form that we're using
from app.forms import newAnimalForm, updateAnimalForm

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
    if current_user.is_authenticated:
        username = current_user.username
    else:
        username = "GUEST"
    form = newAnimalForm()
    try:
        if request.method == 'POST' and form.validate_on_submit():
            namedata = form.name.data
            pricedata = form.price.data
            descdata = form.desc.data
            imgdata = form.img.data
            
            print(namedata, descdata)

            # create an animal object in my database based off the form data
            new_animal = Animal(name=namedata, price=pricedata, desc=descdata, img=imgdata)

            #add the newly created animal to our database - always a two step process
            db.session.add(new_animal)
            db.session.commit()

            # tell our user that we've added something - using flash messages!
            flash(f'You have successfully added the animal {namedata} to your database.')

            return redirect(url_for('site.home'))
    except:
        flash(f'Invalid form input, try again.')
        return redirect(url_for('site.home'))
    return render_template('index.html', form=form, user=username)


# make second route for the profile page
@site.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

@site.route('/animals')
def displayAnimals():
    a = Animal.query.all()
    # print('all animals: ', animals)
    # animal = Animal.query.filter_by(region = 'Tundra').first()
    # print('Tundra animals: ', animal)
    # try_me = Animal.query.get_or_404(6)
    # print("get or 404: ", try_me)
    return render_template('display_animals.html', animals=a)

@site.route('/animals/<int:animal_id>')
def individualAnimal(animal_id):
    a = Animal.query.get_or_404(animal_id)
    return render_template('individual_animal.html', animal = a)


@site.route('/animals/update/<int:animal_id>', methods=["GET","POST"])
@login_required
def updateIndividualAnimal(animal_id):
    a = Animal.query.get_or_404(animal_id)
    updateAnimal = updateAnimalForm()
    if request.method =="POST" and updateAnimal.validate_on_submit():
        namedata = updateAnimal.name.data
        descdata = updateAnimal.desc.data
        imgdata = updateAnimal.img.data

        # deal with price being a string and needing conversion
        if updateAnimal.price.data:
            try:
                a.price = float(updateAnimal.price.data)
                print('changed price')
            except:
                flash(f"Invalid Price, couldn't update.")
                return redirect(url_for('site.individualAnimal', animal_id=animal_id))
        print('got past form data')
        # fixed update to actually update the animal if data present from the form
        if namedata:
            a.name = namedata
            print('changed name')
        if descdata:
            a.desc = descdata
            print('changed desc')
        if imgdata:
            a.img = imgdata
            print('changed img')

        print(namedata, descdata, updateAnimal.price.data)

        db.session.commit()

        flash(f"{a.name} has been updated!")
        return redirect(url_for('site.individualAnimal', animal_id=animal_id))
      
    return render_template('update_individual_animal.html', animal = a, form=updateAnimal)

@site.route('/animals/delete/<int:animal_id>')
def deleteIndividualAnimal(animal_id):
    a = Animal.query.get_or_404(animal_id)

    db.session.delete(a)
    db.session.commit()

    flash(f"Successfully deleted {a.name}")
    return redirect(url_for('site.displayAnimals'))



# Add a Public API endpoint that anyone can access to get my product information
# Note: be careful about using public API endpoints -> we can talk about authentication required api endpoints another day
# a public api endpoint can lead to unintentionally large cloud hosting costs if not set up properly
# this is a simplified and improper implementation below
@site.route('/products', methods=['GET'])
def get_products():
    """
    [GET] /products returns jsonified data on the animals within our database
    """
    # query database to get the animals
    animals = Animal.query.all()
    print(animals)
    # turn the list of animal objects into a list of animal dictionaries
    animals = [animal.to_dict() for animal in animals]
    # jsonify that list
    animals = jsonify(animals)
    # return that list
    return animals