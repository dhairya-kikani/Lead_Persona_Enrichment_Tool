import pandas as pd
from groq_prompts import generate_persona, generate_pitch_angle, generate_icebreaker

df = pd.read_csv("data/leads.csv")

lead = df.iloc[0]

print("Persona:")
print(generate_persona(lead))

print("Pitch Angle:")
print(generate_pitch_angle(lead))

print("Icebreaker:")
print(generate_icebreaker(lead))