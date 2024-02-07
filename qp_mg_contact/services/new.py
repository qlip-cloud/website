import frappe
from frappe.utils import validate_email_address, validate_phone_number
@frappe.whitelist(allow_guest=True)
def handler():

    try:

        args = frappe.form_dict

        contact = frappe.new_doc("qp_mg_Contact")
        contact.fullname = args.get("fullname")
        contact.position = args.get("position")
        contact.phone = __is_phone_valid(args.get("phone")) 
        contact.email = __is_email_valid(args.get("email"))
        contact.company_name = args.get("company_name")
        contact.subject = args.get("subject")
        contact.insert()
        frappe.db.commit()
        frappe.response['message'] = "Los datos han sido almacenado correctamente"
        frappe.response['http_status_code'] = 200
        
    except Exception as error:

        frappe.response['message'] = str(error)
        frappe.response['http_status_code'] = 500

def __is_email_valid(email):

    if not validate_email_address(email):
        
        raise Exception("Formato de Correo electrónico incorrecto")
    
    return email

def __is_phone_valid(phone):

    if not validate_phone_number(phone):
        
        raise Exception("Formato de Teléfono incorrecto")
    
    return phone

