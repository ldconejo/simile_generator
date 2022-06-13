'''
ldconejo - Generates random similes (yeah, just that :-))
'''
import os
from warnings import simplefilter
from flask import Flask, render_template
from random import choice

app = Flask(__name__)

ADJECTIVES = "adjectives.txt"
NOUNS = "nouns.txt"
PRONOUN_TUPLES = [
    ("She", "is"),
    ("He", "is"),
    ("It", "is"),
    ("You", "are"),
    ("Thou", "art"),
    ("We", "are"),
    ("They", "are")
]

CONNECTORS_SINGULAR = [
    "this",
    "that",
    "one"
]

CONNECTORS_PLURAL = [
    "these",
    "those",
    "two"
]

'''
Selects a pronoun tuple, and adjective and a noun
'''
def select_simile_components(adjectives=ADJECTIVES, nouns=NOUNS, pronoun_tuple=PRONOUN_TUPLES, connectors_singular=CONNECTORS_SINGULAR, connectors_plural=CONNECTORS_PLURAL):
    with open(adjectives) as file:
        list_of_adjectives = file.readlines()

    with open(nouns) as file:
        list_of_nouns = file.readlines()

    selected_noun = choice(list_of_nouns).strip()

    if selected_noun.endswith("s"):
        selected_connector = choice(connectors_plural)
    else:
        selected_connector = choice(connectors_singular)
    
    return choice(pronoun_tuple), choice(list_of_adjectives).strip(), selected_connector, selected_noun

'''
Generates the actual simile
'''
def generate_simile(pronoun_tuple, adjective, connector, noun):
    return f"{pronoun_tuple[0]} {pronoun_tuple[1]} as {adjective} as {connector} {noun}"

@app.route('/', methods=['GET'])
def main_page():
    pronoun_tuple, adjective, connector, noun = select_simile_components()
    simile = generate_simile(pronoun_tuple, adjective, connector, noun)
    return render_template('base.jinja2', simile=simile)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 50000))
    app.run(host='0.0.0.0', port=port)