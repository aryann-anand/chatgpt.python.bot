import openai
import PySimpleGUI as sg

# Set up OpenAI API key
openai.api_key = "YOUR_API_KEY_HERE"

# Define function to generate OpenAI response
def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.7,
        max_tokens=1024,
        n_top=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text.strip()

# Define the GUI layout
layout = [
    [sg.Text("Welcome to ChatGPT!")],
    [sg.Output(size=(60, 20))],
    [sg.InputText(key="-INPUT-"), sg.Button("Send"), sg.Button("Quit")],
]

# Create the window
window = sg.Window("ChatGPT", layout)

# Event loop
while True:
    event, values = window.read()
    if event == "Quit":
        break
    elif event == "Send":
        # Get user input
        input_text = values["-INPUT-"]
        
        # Generate OpenAI response
        response_text = generate_response(input_text)
        
        # Display response in GUI
        print(f"You: {input_text}")
        print(f"ChatGPT: {response_text}")

# Close the window
window.close()
