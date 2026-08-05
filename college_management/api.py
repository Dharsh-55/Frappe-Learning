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

@frappe.whitelist()
def create_task(task_subject):

    task = frappe.new_doc("Task")
    task.subject = task_subject
    task.save()

    return task.name

from frappe.query_builder import DocType

@frappe.whitelist()
def update_students():
    stu = DocType("Student")
    dept = DocType("DepartmentX")

    stus = (
        frappe.qb.from_(stu)
        .join(dept)
        .on(stu.department == dept.dept_name)
        .select(
            stu.name,
            stu.s_name,
            stu.department
        )
        .limit(5)
        .run(as_dict = True)
    )

    if stus:
        doc = frappe.get_doc("Student", stus[0]['name'])
        doc.title = "updates using document api"
        doc.save()

    for s in stus:
        frappe.db.set_value(
            "Student",
            stu["s_name"],
            "title",
            "updated using db api"
        )

    return stus