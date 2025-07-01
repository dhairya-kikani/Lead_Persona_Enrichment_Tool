from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

#Prompt Function

def generate_persona(lead):
    prompt = f"""Based on this lead's info, describe their likely goals, responsibilities, and mindset in 2-3 lines.

Name : {lead['Name']}
Job Title : {lead['Job Title']}
Company : {lead['Company']}
Industry : {lead['Industry']}
LinkedIn : {lead['LinkedIn']}
"""
    return gpt_call(prompt)

def generate_pitch_angle(lead):
    prompt = f"""Suggest a personalized value pitch angle for this lead's company role.

Job Title : {lead['Job Title']}
Company : {lead['Company']}
Industry : {lead['Industry']}
"""
    return gpt_call(prompt)

def generate_icebreaker(lead):
    prompt = f"""Write a short icebraker or opener that feels personalized and warm for this LinkedIn lead.

Name : {lead['Name']}
Job Title : {lead['Job Title']}
Company : {lead['Company']}
"""
    return gpt_call(prompt)



#GPT handler

def gpt_call(prompt, model="llama3-70b-8192"):
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=200,
    )
    return response.choices[0].message.content.strip()