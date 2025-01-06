from ollama import Client
import re
import json

def word_generator_for_persona(persona):
    client = Client(host='http://10.101.10.140:3000')
    
    # Create a prompt to act as the persona and generate relevant search sentences
    prompt = f"Act as {persona['name']}, 
             a {persona['age']}-year-old 
             {persona['occupation']} 
             who is interested in {persona['primary_interest']} 
             with a preference for {persona['style_preference']} style. 
             Generate search sentences that would be relevant to {persona['name']} based on their interests and unmet needs."
    
    response = client.chat(model='llama3.1', messages=[
        {'role': 'user', 'content': prompt}
    ])
    
    # Extract the generated response text
    var = response['choices'][0]['message']['content']
    
    # Use regex to find keyword phrases in quotes, as they may represent search terms
    keywords = re.findall(r'\"(.*?)\"', var)
    
    return keywords

def select_persona_and_generate_keywords():
    # Load personas from JSON file
    with open("personas.json", "r") as file:
        personas = json.load(file)
    
    # Display persona choices to the user
    print("Available personas:")
    for idx, persona in enumerate(personas, start=1):
        print(f"{idx}. {persona['name']} - {persona['occupation']} ({persona['age']} years old)")
    
    # Ask user to select a persona by index
    selected_index = int(input("Enter the number of the persona you want to act like: ")) - 1
    
    # Ensure the index is valid
    if 0 <= selected_index < len(personas):
        selected_persona = personas[selected_index]
        keywords = word_generator_for_persona(selected_persona)
        print(f"Relevant search keywords for {selected_persona['name']}: {keywords}")
    else:
        print("Invalid selection. Please try again.")

# Run the selection and keyword generation
if __name__ == "__main__":
    select_persona_and_generate_keywords()

