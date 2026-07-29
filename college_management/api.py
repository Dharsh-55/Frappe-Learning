import frappe
import google.generativeai as genai

# Replace with your API key for now
genai.configure(api_key="YOUR_API_KEY")

@frappe.whitelist()
def generate_student_summary(student_name, department, biography, skills):

    model = genai.GenerativeModel("gemini-3.1-flash-lite")

    prompt = f"""
You are an expert student profile writer.

Generate a professional student summary in 80-100 words.

Student Name:
{student_name}

Department:
{department}

Biography:
{biography}

Skills:
{skills}

Write in a professional and concise style.
"""

    response = model.generate_content(prompt)

    return response.text


def custom_logic(doc, method):
    frappe.msgprint("Hook executed!")