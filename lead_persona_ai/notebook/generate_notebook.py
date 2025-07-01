from pathlib import Path
from nbformat import v4 as nbf

# Create notebook cells
cells = []

cells.append(nbf.new_markdown_cell("# Lead Enrichment Demo using LLMs (Groq API)\n\nThis notebook demonstrates the process of enriching a single lead with a persona, pitch angle, and icebreaker."))

cells.append(nbf.new_code_cell(
'''import pandas as pd
from groq_prompts import generate_persona, generate_pitch_angle, generate_icebreaker

# Load leads
leads = pd.read_csv("leads.csv")
sample_lead = leads.iloc[0].to_dict()
sample_lead'''
))

cells.append(nbf.new_code_cell(
'''# Generate enriched outputs
persona = generate_persona(sample_lead)
pitch = generate_pitch_angle(sample_lead)
icebreaker = generate_icebreaker(sample_lead)

print("Persona:\\n", persona)
print("\\nPitch Angle:\\n", pitch)
print("\\nIcebreaker:\\n", icebreaker)'''
))

cells.append(nbf.new_markdown_cell("### Summary\n\nThis notebook successfully enriches a LinkedIn lead using LLMs to generate content that enhances sales outreach. The approach saves time and improves quality."))

# Create notebook
notebook = nbf.new_notebook(cells=cells)

# Save notebook 
output_path = Path("Lead_Enrichment_Demo.ipynb")
with output_path.open("w", encoding="utf-8") as f:
    f.write(nbf.writes(notebook))

print("Notebook created:", output_path.name)
