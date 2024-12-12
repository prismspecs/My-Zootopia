import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')

def animal_data(animals):
    output = '<ul>'
    for animal in animals:
        output += '<li class="cards__item">'

        if "name" in animal:
            output += '<div class="card__title">'
            output += f"{animal['name']}"
            output += '</div>'

        output += '<p class="card__text">'

        if "characteristics" in animal and isinstance(animal["characteristics"], dict):
            if "diet" in animal["characteristics"]:
                output += f"<strong>Diet</strong>: {animal['characteristics']['diet']}<br/>\n"

        if "locations" in animal and isinstance(animal["locations"], list) and animal["locations"]:
            output += f"<strong>Location</strong>: {animal['locations'][0]}<br/>\n"

        if "characteristics" in animal and isinstance(animal["characteristics"], dict):
            if "type" in animal["characteristics"]:
                output += f"<strong>Type</strong>: {animal['characteristics']['type']}<br/>\n"

        output += '</p>'
        output += '</li>'
    output += '</ul>'
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
    animals_data = load_data("animals_data.json")
    html_output = animal_data(animals_data)
    generate_html_file(html_output, "animals.html")


