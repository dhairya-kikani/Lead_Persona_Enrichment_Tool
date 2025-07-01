Lead Persona Enrichment Tool

1. Overview

This model is created and design through an idea to improve features and help sale and marketing professionals enrich LinkedIn lead data, also it is purposely created from a website called saasquatchleads, which is a scraping tool website. Just through taking basic information such as Lead's Name, Job Title, Company, LinkedIn profile and Industry, it generates:

a.) Persona : 2-3 line summary of their goals, responsibilities, and mindset

b.) Pitch Angle : Personalized value preposition tailored to their roles and company

c.) Icebreaker : Warm, engaging opener to use in outreach

Project Structure 

lead_persona_ai/
├── app/                     # Python scripts
│   ├── app.py
│   ├── batch_generate.py
│   ├── groq_prompts.py
│   ├── test_prompt.py
├── data/                    # Data files
│   ├── leads.csv
│   ├── enriched_leads.csv
├── notebook/                # Jupyter demo
│   ├── Lead_Enrichment_Demo.ipynb
│   ├── generate_notebook.py
├── docs/
│   ├── lead_persona_report.pdf
│   ├── README.md
├── .env
├── requirements.txt

2. Setup Instruction

a. Clone the repo

git clone https://github.com/dhairya-kikani/Lead_Persona_Enrichment_Tool.git

b. Install Dependencies

    pip install -r requirements.txt

c. Set API Key

     Export your Groq API key (or use .env):
     export GROQ_API_KEY=your_groq_api_key

d. Run via Streamlit

    streamlit run app.py

e.  Run CLI to test single lead

    python test_prompt.py

3. How it works

Inputs:
-Name
-Job Title
-Company
-Industry
-LinkedIn URL

"Prompts" (groq_prompts.py):
Each lead goes through 3 distinct groq call with prompt engineering;

- generate_persona(lead) → Summarizes goals/mindset
- generate_pitch_angle(lead) → Business pain-points + value
- generate_icebreaker(lead) → Warm, contextual message

Output:
Saved as enriched_leads.csv and display it as:

Name | Job Title | Company | Industry | LinkedIn | Persona | Pitch Angle | Icebreaker

4. Streamlit Features

a.) Sidebar filters by Industry, Name and Company.
b.) Table view with search
c.) Auto preview of first lead
d.) Download filter as CSV

5. Demo Video

Available upon request.

6. Evaluation

Criteria                                       What We've Done
-------------------------------------------------------------------------------------------------------------
Business Use                                   LLM enrich leads with persona level insights
UX/UI                                          Streamlit app with filters, preview, search and download option
Tech                                           Groq Integration, prompt-based model, fallback handling
Design                                         Clean Layout, readable enriched summaries
Other                                          CSV automation, safe error catching