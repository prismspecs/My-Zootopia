# note: set up a venv and install requests
# python3 -m venv venv
# source venv/bin/activate
# pip install requests python-dotenv

import json
import requests
from dotenv import load_dotenv
import os

# load the .env file
load_dotenv()


def get_api_key():
    return os.getenv("API_KEY")


def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)


# animals_data = load_data("animals_data.json")


def load_data_from_api(name):
    # code to fetch data from API
    api_url = "https://api.api-ninjas.com/v1/animals?name={}".format(name)

    api_key = get_api_key()
    response = requests.get(api_url, headers={"X-Api-Key": api_key})
    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        # return an error
        return "Error fetching data from API"


def animal_data(animals):
    output = "<ul>"
    for animal in animals:
        output += '<li class="cards__item">'

        if "name" in animal:
            output += '<div class="card__title">'
            output += f"{animal['name']}"
            output += "</div>"

        output += '<p class="card__text">'

        if "characteristics" in animal and isinstance(animal["characteristics"], dict):
            if "diet" in animal["characteristics"]:
                output += (
                    f"<strong>Diet</strong>: {animal['characteristics']['diet']}<br/>\n"
                )

        if (
            "locations" in animal
            and isinstance(animal["locations"], list)
            and animal["locations"]
        ):
            output += f"<strong>Location</strong>: {animal['locations'][0]}<br/>\n"

        if "characteristics" in animal and isinstance(animal["characteristics"], dict):
            if "type" in animal["characteristics"]:
                output += (
                    f"<strong>Type</strong>: {animal['characteristics']['type']}<br/>\n"
                )

        output += "</p>"
        output += "</li>"
    output += "</ul>"
    return output


def generate_html_file(html_content, output_file):
    # write html to a file
    html_structure = f"""
    <html>
        <head>
            <title>Zootopia</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #fce4ec;
                    margin: 0;
                    padding: 16px;
                }}
                h1 {{
                    text-align: center;
                    color: #333;
                }}
                ul {{
                    list-style:none;
                }}
                .card__title {{
                    font-weight:bold;
                }}
                .cards__item {{
                    background-color: white;
                    padding: 1.5rem;
                    margin: 1.5rem 0;
                    border-radius: 8px;
                    box-shadow: 0 8px 15px rgba(0, 0, 0, 0.1);
                    text-align: left;
                }}
            </style>
        </head>
        <body>
            <h1>My Animal Repository</h1>
            {html_content}
        </body>
    </html>
    """
    with open(output_file, "w") as file:
        file.write(html_structure)
    print(f"HTML file generated successfully: {output_file}")


if __name__ == "__main__":

    # ask user for animal name
    animal_name = input("Enter the name of the animal: ")
    animals_data = load_data_from_api(animal_name)

    # if animals_data is empty
    if not animals_data:
        html_output = f"<h2>The animal {animal_name} doesn't exist.</h2>"
    else:
        html_output = animal_data(animals_data)

    generate_html_file(html_output, "animals.html")
