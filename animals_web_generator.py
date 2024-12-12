import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')

def print_animal_details(animals):
    for animal in animals:
        if "name" in animal:
            print(f"Name: {animal['name']}")

        if "characteristics" in animal and isinstance(animal["characteristics"], dict):
            if "diet" in animal["characteristics"]:
                print(f"Diet: {animal['characteristics']['diet']}")

        if "locations" in animal and isinstance(animal["locations"], list) and animal["locations"]:
            print(f"Location: {animal['locations'][0]}")

        if "characteristics" in animal and isinstance(animal["characteristics"], dict):
            if "type" in animal["characteristics"]:
                print(f"Type: {animal['characteristics']['type']}")

print_animal_details(animals_data)