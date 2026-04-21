import csv
import inquirer
from inquirer.errors import ValidationError
def no_empty(_, x):
    """Vérifie que le champ n'est pas vide"""
    if not x.strip():
        raise ValidationError("", reason= "Ce champ ne peut pas être vide ! ")
    return True
def valid_year(_ , x):
    """Vérifie que le champ n'est pas vide et que c'est un nombre"""
    if not x.strip().isdigit() and len(x.strip()) != 4: 
        raise ValidationError("", reason= "La saisie de l'année n'est pas valide")
    return True
def menu():
    """Fonction qui fait le menu"""
    while True:
        menu = [
            inquirer.List('Menu', message='What do you want to do ?', choices=["Add a movie", "See the list","Search a movie", "Delete a movie", "I have see a movie", "Exit"])
        ]
        result = inquirer.prompt(menu)
        if result['Menu'] == "Add a movie":
            add_movie()
        elif result['Menu'] == "See the list":
            list_movies()
        elif result['Menu'] == "Search a movie":
            search_movie()
        elif result['Menu'] == "Delete a movie":
            delete_movie()
        elif result['Menu'] == "I have see a movie":
            mark_movie_as_seen()
        elif result['Menu'] == "Exit":
            exit()
def add_movie(path = "movies.csv"):
    """Ajout de film dans le .csv"""
    q = [
        inquirer.Text("title", message = "What's the movie's name ? ", validate= no_empty),
        inquirer.Text("release_year", message = "When has released the movie ? ",validate= valid_year),
        inquirer.Text("genre", message = "What's the genre of movie ? ", validate= no_empty),
        inquirer.List("is_seen", message ="Do you have seen the movie ? ", choices = ["Yes", "No"], default= "No"),
    ]
    answers = inquirer.prompt(q)
    with open(path, "a", encoding= 'utf-8', newline='') as f:
        fieldnames = ['title', 'release_year', 'genre', 'is_seen']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if f.tell() == 0: #Empêche de réécrire l'entête à chaque fois
            writer.writeheader()
        writer.writerow(answers)
    return answers
def list_movies(path = "movies.csv"):
    """Affiche la liste des films du .csv"""
    q = [
        inquirer.List('path', message='What list do you want to see ?', choices=["Read the list : movies.csv", "Exit"])
        ]
    result = inquirer.prompt(q)
    if result['path'] == "Read the list : movies.csv":
        with open(path, "r", encoding= 'utf-8') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        headers = list(rows[0].keys())
        col_widths = {h: max(len(h), max(len(str(row.get(h, ""))) for row in rows)) for h in headers}
        print("  ".join(h.ljust(col_widths[h]) for h in headers))
        print("  ".join("-" * col_widths[h] for h in headers))
        for row in rows:
            print("   ".join(str(row.get(h, "")).ljust(col_widths[h]) for h in headers))
    elif result['path'] == "Exit":
        exit()
def search_movie(path = "movies.csv"):
    """Permet la recherche d'un film et de ses éléments"""
    q = [
        inquirer.Text("movie", message="What movie do you want to consult ? ")
    ]
    result = inquirer.prompt(q)
    with open(path, "r", encoding= 'utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
                if row['title'] == result['movie']:
                    print(row)
def delete_movie(path = "movies.csv"): #REVOIR CE CONCEPT
    """Permet la suppression d'une ligne en lisant, en ignorant la ligne en question et en réécrivant le .csv"""
    q = [
        inquirer.Text('Del', message=" What movie do you want to delete ?")
    ]
    result = inquirer.prompt(q)
    with open(path, 'r', encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f)
        rows = [row for row in reader if row['title'] != result['Del']] #on exclu le choix s'il est dans la section titre
        fieldnames = reader.fieldnames
    with open(path, "w", encoding= 'utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames= fieldnames)
        writer.writeheader()
        writer.writerows(rows)
        print("Deleted.")
def mark_movie_as_seen(path= "movies.csv"):
    """Permet de changer le No en Yes une fois le film vu"""
    q = [
        inquirer.Text('is_seen', message='What movie did you see ?')
    ]
    result = inquirer.prompt(q)
    with open(path, "r+", encoding= 'utf-8', newline='') as f:
        rows = list(csv.DictReader(f))
        for row in rows:
            if row['title'] == result['is_seen']:
                row['is_seen'] = "Yes"
        f.seek(0)
        writer = csv.DictWriter(f, fieldnames= rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
menu()
