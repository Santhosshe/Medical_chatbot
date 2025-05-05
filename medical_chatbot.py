import tkinter as tk
from tkinter import messagebox
import datetime

def get_response(user_input):
    user_input = user_input.lower()

    if "fever" in user_input:
        return "Fever could indicate infection. Stay hydrated and rest. Consult a doctor if it lasts more than 2 days."
    elif "cough" in user_input:
        return "A dry cough may be a sign of allergies or infection. Drink warm fluids and rest."
    elif "headache" in user_input:
        return "Try resting in a dark, quiet room. If it’s severe or recurring, consult a physician."
    elif "cold" in user_input:
        return "Common cold can be managed with rest, hydration, and warm fluids."
    elif "covid" in user_input:
        return "COVID-19 symptoms include fever, cough, fatigue, and loss of smell. Consider getting tested."

    elif "tip" in user_input or "tips" in user_input:
        return " Health Tip: Drink at least 2 liters of water daily, sleep 7–8 hours, and walk 30 mins a day."

    elif "burn" in user_input:
        return "For minor burns, cool the area with water, avoid ice, and cover it with a clean cloth."
    elif "cut" in user_input:
        return "Clean the wound, apply pressure to stop bleeding, and cover it with a sterile bandage."

        # Extended Symptom Checker (30+ Symptoms)
    if "fever" in user_input:
        return "Fever may indicate infection. Stay hydrated and rest. If high or persistent, consult a doctor."
    elif "cough" in user_input:
        return "Persistent cough can be due to cold, allergies, or infections. Stay warm and drink hot fluids."
    elif "cold" in user_input:
        return "Cold includes sneezing, sore throat, and runny nose. Rest, hydration, and warm fluids help."
    elif "headache" in user_input:
        return "Headaches can be due to stress or dehydration. Rest and avoid screen time."
    elif "nausea" in user_input or "vomiting" in user_input:
        return "Avoid solid food temporarily, hydrate with ORS, and rest. Seek help if it persists."
    elif "diarrhea" in user_input:
        return "Drink ORS or clean fluids. Avoid spicy food. Consult a doctor if symptoms persist."
    elif "sore throat" in user_input:
        return "Gargle with warm salt water. Avoid cold drinks and rest your voice."
    elif "chest pain" in user_input:
        return "If severe, with shortness of breath, seek emergency care immediately."
    elif "fatigue" in user_input or "tiredness" in user_input:
        return "Could be due to overwork, poor sleep, or illness. Sleep well and eat nutritious food."
    elif "dizziness" in user_input or "lightheaded" in user_input:
        return "Sit or lie down, breathe deeply. May be due to dehydration or low BP."
    elif "rash" in user_input or "itching" in user_input:
        return "Apply a soothing lotion or aloe vera. Avoid scratching. May be allergic or fungal."
    elif "eye pain" in user_input or "red eye" in user_input:
        return "May be due to strain or infection. Use clean water to rinse and reduce screen time."
    elif "stomach pain" in user_input or "abdominal pain" in user_input:
        return "Could be gas, cramps, or indigestion. Avoid oily food and rest."
    elif "back pain" in user_input:
        return "Maintain posture, avoid lifting heavy items, and use hot compress."
    elif "ear pain" in user_input:
        return "Could be infection or wax build-up. Avoid inserting objects. See a doctor if severe."
    elif "toothache" in user_input:
        return "Rinse with salt water, apply a cold compress, and avoid sweet food."
    elif "burning sensation" in user_input:
        return "If on skin, cool with water and cover lightly. If in chest, it may be acidity."
    elif "breathlessness" in user_input:
        return "Take deep breaths and rest. If continues, especially with chest pain, seek help immediately."
    elif "constipation" in user_input:
        return "Eat fiber-rich food, drink water, and exercise lightly."
    elif "acidity" in user_input or "heartburn" in user_input:
        return "Avoid spicy food, eat small meals, and stay upright after eating."
    elif "gas" in user_input or "bloating" in user_input:
        return "Avoid carbonated drinks and heavy meals. Ginger tea may help."
    elif "leg pain" in user_input:
        return "Could be due to fatigue or cramps. Try gentle massage or stretching."
    elif "hand pain" in user_input or "wrist pain" in user_input:
        return "May be due to overuse. Rest the hand and use ice packs."
    elif "joint pain" in user_input:
        return "Common with aging or arthritis. Warm compress and light movement may help."
    elif "muscle pain" in user_input:
        return "Can follow exertion. Use hot/cold packs and stay hydrated."
    elif "nose bleed" in user_input:
        return "Lean forward, pinch the nose, and apply ice. Seek help if frequent."
    elif "urine burning" in user_input or "painful urination" in user_input:
        return "May indicate UTI. Drink water and consider medical checkup."
    elif "sweating" in user_input:
        return "Can be normal or due to fever/stress. If excessive or with chest pain, consult doctor."
    elif "shivering" in user_input:
        return "Often with fever. Keep warm and monitor temperature."
    elif "blurred vision" in user_input:
        return "Could be eye strain, low BP, or serious issues. Rest eyes and consult if persistent."
    elif "palpitations" in user_input or "fast heartbeat" in user_input:
        return "Could be due to anxiety or heart issues. Sit and breathe. Seek help if persistent."

    elif "appointment" in user_input:
        now = datetime.datetime.now().strftime("%A, %d %B %Y, %I:%M %p")
        return f"🩺 Appointment booked successfully!\n📅 Date: {now}"

    elif "hello" in user_input or "hi" in user_input:
        return "Hello! I’m your medical assistant chatbot. Ask me about symptoms, health tips, or first-aid!"

    elif "thank" in user_input:
        return "You're welcome! Stay safe and healthy. 😊"

    elif "emergency" in user_input:
        return "🚨 Please call your local emergency number or go to the nearest hospital immediately."

    else:
        return "I'm not trained for that topic. Please consult a real doctor for detailed advice."

def send():
    user_input = entry.get()
    if not user_input.strip():
        return
    chat_log.insert(tk.END, "You: " + user_input + "\n")
    response = get_response(user_input)
    chat_log.insert(tk.END, "Bot: " + response + "\n\n")
    entry.delete(0, tk.END)

def clear_chat():
    chat_log.delete(1.0, tk.END)

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to exit the chatbot?"):
        root.destroy()

root = tk.Tk()
root.title("Advanced Medical Assistant Chatbot")
root.geometry("500x500")

chat_log = tk.Text(root, height=20, width=60, font=("Arial", 11))
chat_log.pack(pady=10)

entry_frame = tk.Frame(root)
entry_frame.pack(pady=5)

entry = tk.Entry(entry_frame, width=40, font=("Arial", 12))
entry.pack(side=tk.LEFT, padx=5)

send_button = tk.Button(entry_frame, text="Send", command=send)
send_button.pack(side=tk.LEFT)

clear_button = tk.Button(root, text="Clear Chat", command=clear_chat)
clear_button.pack()

chat_log.insert(tk.END, "🤖 Bot: Hello! I’m your medical assistant chatbot.\nAsk me about symptoms, health tips, or first-aid.\n\n")

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
