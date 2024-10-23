import load_json
import csv

def save_messages_to_csv(data, csv_filename):
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Message ID', 'Date', 'Content', 'Category', 'University ID'])
        for record in data:
            university_id = record.get('university', {}).get('id', 'N/A')
            messages = record.get('messages', [])
            for message in messages:
                writer.writerow([message.get('id', 'N/A'),message.get('date', 'N/A'),message.get('content', 'N/A'),message.get('category', 'N/A'),university_id])


save_messages_to_csv(load_json.data, 'messages.csv')