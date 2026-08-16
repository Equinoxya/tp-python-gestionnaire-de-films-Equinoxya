# tp-python-gestionnaire-de-films

TP réalisé dans le cadre de la formation (Metz Numeric School, via GitHub Classroom) : un gestionnaire de films en ligne de commande, écrit en Python, avec stockage des données dans un fichier CSV.

## 🎬 Fonctionnalités

L'application propose un menu interactif permettant de :

- ➕ **Ajouter un film** (titre, année de sortie, genre, statut "vu/pas vu")
- 📋 **Afficher la liste des films** enregistrés, sous forme de tableau formaté
- 🔍 **Rechercher un film** par titre
- 🗑️ **Supprimer un film** de la liste
- ✅ **Marquer un film comme vu**
- 🚪 Quitter l'application

## 🗂️ Structure du projet

```
tp-python-gestionnaire-de-films-Equinoxya/
├── movies.csv     # Base de données des films (générée/mise à jour par le script)
└── script.py      # Script principal contenant toute la logique du gestionnaire
```

## 🚀 Installation et lancement

### Prérequis

- Python 3
- La bibliothèque [`inquirer`](https://pypi.org/project/inquirer/), utilisée pour les menus interactifs en ligne de commande

### Installation

```bash
git clone https://github.com/Equinoxya/tp-python-gestionnaire-de-films-Equinoxya.git
cd tp-python-gestionnaire-de-films-Equinoxya
pip install inquirer
```

### Lancement

```bash
python script.py
```

Un menu s'affiche alors, permettant de naviguer entre les différentes actions à l'aide des flèches du clavier.

## 🧩 Détails techniques

- Les données sont stockées dans `movies.csv`, avec les colonnes : `title`, `release_year`, `genre`, `is_seen`.
- La saisie est validée : un titre ou un genre ne peut pas être vide, et l'année doit être un nombre à 4 chiffres.
- La suppression d'un film fonctionne par réécriture complète du fichier CSV, en excluant la ligne concernée.

## ✍️ Auteur

[Equinoxya](https://github.com/Equinoxya) — forké depuis [Metz-Numeric-School/tp-python-gestionnaire-de-films-Equinoxya](https://github.com/Metz-Numeric-School/tp-python-gestionnaire-de-films-Equinoxya)
