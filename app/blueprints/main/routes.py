from flask import render_template, request, flash
import requests
from flask_login import login_required
from .import bp as main 

#Routes
@main.route('/', methods=['GET'])
@login_required
def index():
#this index function will be passed through the route function
    return render_template('index.html.j2')

@main.route('/students', methods=['GET'])
@login_required
def students(): 
    the_students = ["Thu", "Leo", "Sydney", "Josh", "Chris", "Fernando", "Benny", "Vicky", "Bradley"]
    return render_template('students.html.j2', students=the_students)

@main.route('/pokemon', methods=['GET', 'POST'])
@login_required
def pokemon():
    if request.method == 'POST':
        name = request.form.get('name')
        url = f"https://pokeapi.co/api/v2/pokemon/{name}" 
        response = requests.get(url)
        if response.ok:
            try:
                data = response.json()
            except:
                flash(f'There is no pokemon named {name}', 'warning')
                return render_template("pokemon.html.j2")
            # pokemon_data = []
            # for data in data:
            pokemon_data={ # renamed pokemon data
                "Name" : data['forms'][0]['name'],
                "Ability": data['abilities'][0]['ability']['name'],
                "Base Experience" : data['base_experience'], # Fixed typo in name
                "Sprite URL" : data['sprites']['front_shiny']
                }
                # pokemon_data.append(pokemon_data_dict)
            return render_template("pokemon.html.j2", data =pokemon_data)
        else: 
            flash('Something is Wrong', 'danger')
            render_template("pokemon.html.j2")
    return render_template("pokemon.html.j2")