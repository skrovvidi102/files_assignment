import load_json
import csv


def book_catogery_to_csv(data, csv_filename):
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Book ID', 'Title','Category', 'University ID'])
        for record in data:
            university_id = record.get('university', {}).get('id', 'N/A')
            adoptions = record.get('adoptions', [])
            for adoption in adoptions:
                book = adoption.get('book', {})
                writer.writerow([book.get('id', 'N/A'),book.get('title', 'N/A'),book.get('category', 'N/A'),university_id])

book_catogery_to_csv(load_json.data, 'book_catogary.csv')
