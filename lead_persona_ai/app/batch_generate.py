import csv
from groq_prompts import generate_persona, generate_pitch_angle, generate_icebreaker

#INPUT & OUTPUT file paths
Input_File = "data/leads.csv"
Output_File = "data/enriched_leads.csv"

def process_leads():
    leads = []

    #Read leads from CSV
    with open(Input_File, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            leads.append(row)

    enriched_data = []

    print(f"Processing {len(leads)} leads...")

    for i, lead in enumerate(leads):
        print(f"Processing lead {i+1}/{len(leads)}: {lead['Name']} at {lead['Company']}")

        try:
            persona = generate_persona(lead)
            pitch = generate_pitch_angle(lead)
            icebreaker = generate_icebreaker(lead)
        except Exception as e:
            print(f"Error processing lead {lead['Name']}: {e}")
            persona, pitch, icebreaker = 'Error', 'Error', 'Error'

        enriched_data.append({
                "Name": lead['Name'],
                "Job Title": lead['Job Title'],
                "Company": lead['Company'],
                "Industry": lead['Industry'],
                "LinkedIn": lead['LinkedIn'],
                "Persona": persona,
                "Pitch Angle": pitch,
                "Icebreaker": icebreaker,
            })

    #write to enriched CSV
    with open(Output_File, mode='w', encoding='utf-8', newline='') as file:
        fieldnames = [
            "Name", "Job Title", "Company", "Industry", "LinkedIn",
            "Persona", "Pitch Angle", "Icebreaker"
        ]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(enriched_data)

print(f"Enriched leads saved to: {Output_File}")

if __name__ == "__main__":
    process_leads()
        



















            