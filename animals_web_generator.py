import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')

def animal_data(animals):
    output = ''
    for animal in animals:
        # oh dear this is a misuse of li ....
        output += '<li class="cards__item">'
        if "name" in animal:
            output += f"Name: {animal['name']}\n"

        if "characteristics" in animal and isinstance(animal["characteristics"], dict):
            if "diet" in animal["characteristics"]:
                output += f"Diet: {animal['characteristics']['diet']}<br/>\n"

        if "locations" in animal and isinstance(animal["locations"], list) and animal["locations"]:
            output += f"Location: {animal['locations'][0]}<br/>\n"

        if "characteristics" in animal and isinstance(animal["characteristics"], dict):
            if "type" in animal["characteristics"]:
                output += f"Type: {animal['characteristics']['type']}<br/>\n"
        output += '</li>'
    return output
#animal_data(animals_data)

print(animal_data(animals_data))
