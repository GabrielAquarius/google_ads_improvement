from ollama import Client
import json

# Function to collect inputs for each persona with language support
def create_persona(language="English"):
    # English and Portuguese questions
    questions = {
        "English": {
            "name": "Enter the persona's name: ",
            "age": "Enter {name}'s age: ",
            "size": "Enter {name}'s clothing size: ",
            "occupation": "What is {name}'s occupation or lifestyle role? ",
            "primary_interest": "What market is {name} interested in (e.g., sleepwear, lingerie)? ",
            "style_preference": "What is {name}'s preferred style (e.g., elegant, trendy, minimalist)? ",
            "profile": "Describe {name}'s overall profile and lifestyle (e.g., 'Trend-Savvy Professional'): ",
            "buying_behavior": "Describe {name}'s buying behavior (e.g., 'prefers trendy and affordable options'): ",
            "shopping_platforms": "Where does {name} primarily shop (e.g., social media, e-commerce sites)? ",
            "jobs_to_be_done": "What does {name} need to accomplish when buying? (e.g., 'Find trendy, comfortable pieces'): ",
            "unmet_needs": "What are {name}'s unmet needs or pain points? (e.g., 'Limited stylish options in larger sizes'): ",
            "price_sensitivity": "What is {name}'s price sensitivity (e.g., budget-conscious, willing to invest)? ",
            "triggers": "What sales triggers influence {name} (e.g., discounts, limited edition)? "
        },
        "Portuguese": {
            "name": "Digite o nome da persona: ",
            "age": "Digite a idade de {name}: ",
            "size": "Digite o tamanho de roupa de {name}: ",
            "occupation": "Qual é a ocupação ou estilo de vida de {name}? ",
            "primary_interest": "Em qual mercado {name} está interessado (por exemplo, roupa de dormir, lingerie)? ",
            "style_preference": "Qual é o estilo preferido de {name} (por exemplo, elegante, moderno, minimalista)? ",
            "profile": "Descreva o perfil e o estilo de vida de {name} (por exemplo, 'Profissional antenado'): ",
            "buying_behavior": "Descreva o comportamento de compra de {name} (por exemplo, 'prefere opções modernas e acessíveis'): ",
            "shopping_platforms": "Onde {name} costuma fazer compras (por exemplo, redes sociais, sites de e-commerce)? ",
            "jobs_to_be_done": "O que {name} precisa realizar ao comprar? (por exemplo, 'Encontrar peças confortáveis e modernas'): ",
            "unmet_needs": "Quais são as necessidades não atendidas ou pontos de dor de {name}? (por exemplo, 'Opções estilosas limitadas em tamanhos maiores'): ",
            "price_sensitivity": "Qual é a sensibilidade ao preço de {name} (por exemplo, econômico, disposto a investir)? ",
            "triggers": "Quais gatilhos de venda influenciam {name} (por exemplo, descontos, edição limitada)? "
        }
    }
    
    # Select questions based on language
    q = questions[language]

    # Collect data with selected questions
    name = input(q["name"])
    age = int(input(q["age"].format(name=name)))
    size = input(q["size"].format(name=name))
    occupation = input(q["occupation"].format(name=name))
    primary_interest = input(q["primary_interest"].format(name=name))
    style_preference = input(q["style_preference"].format(name=name))
    profile = input(q["profile"].format(name=name))
    buying_behavior = input(q["buying_behavior"].format(name=name))
    shopping_platforms = input(q["shopping_platforms"].format(name=name))
    jobs_to_be_done = input(q["jobs_to_be_done"].format(name=name))
    unmet_needs = input(q["unmet_needs"].format(name=name))
    price_sensitivity = input(q["price_sensitivity"].format(name=name))
    triggers = input(q["triggers"].format(name=name))

    persona = {
        "name": name,
        "age": age,
        "size": size,
        "occupation": occupation,
        "primary_interest": primary_interest,
        "style_preference": style_preference,
        "profile": profile,
        "buying_behavior": buying_behavior,
        "shopping_platforms": shopping_platforms,
        "jobs_to_be_done": jobs_to_be_done,
        "unmet_needs": unmet_needs,
        "price_sensitivity": price_sensitivity,
        "triggers": triggers
    }
    
    return persona

# Generate detailed persona with AI
def persona_generator(prompt):
    client = Client(host='http://10.101.10.140:3000')
    response = client.chat(model='llama3.1', messages=[{'role': 'user', 'content': prompt}])
    detailed_persona = response['choices'][0]['message']['content']
    return detailed_persona

# Collect personas and store them
# Collect personas and store them
def collect_personas():
    personas = []
    language = input("Select language (English/Portuguese): ").capitalize()
    
    # Language-specific prompt for the number of personas
    num_personas_prompt = {
        "English": "How many personas would you like to create? ",
        "Portuguese": "Quantas personas você gostaria de criar? "
    }
    
    num_personas = int(input(num_personas_prompt.get(language, num_personas_prompt["English"])))
    
    for i in range(num_personas):
        print(f"\nCreating persona {i+1}/{num_personas}")
        persona = create_persona(language)
        
        # Generate prompt for AI based on simplified persona data
        prompt = f"Create a detailed persona profile for: {json.dumps(persona)}"
        persona['detailed_profile'] = persona_generator(prompt)
        
        personas.append(persona)
    
    # Saving personas to a JSON file
    with open("personas.json", "w") as file:
        json.dump(personas, file, indent=4, ensure_ascii=False)
    
    print("Personas saved to 'personas.json'.")


# Run the persona collection
if __name__ == "__main__":
    collect_personas()