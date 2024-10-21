import csv
import load_json

def save_contacts_to_csv(data, csv_filename):
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Order', 'Gender', 'First Name', 'Last Name', 'University ID'])
        for record in data:
            university_id = record.get('university', {}).get('id', 'N/A')
            contacts = record.get('contacts', [])
            for contact in contacts:
                writer.writerow([contact.get('order', 'N/A'),contact.get('gender', 'N/A'),contact.get('firstname', 'N/A'),contact.get('lastname', 'N/A'),university_id])


save_contacts_to_csv(load_json.data, 'contacts.csv')
