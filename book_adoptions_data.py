import load_json
import csv


def save_adoptions_to_csv(data, csv_filename):
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Adoption ID', 'Date', 'Quantity', 'Book ID', 'Title', 'ISBN-10', 'ISBN-13', 'Category', 'University ID'])
        for record in data:
            university_id = record.get('university', {}).get('id', 'N/A')
            adoptions = record.get('adoptions', [])
            for adoption in adoptions:
                book = adoption.get('book', {})
                writer.writerow([adoption.get('id', 'N/A'),adoption.get('date', 'N/A'),adoption.get('quantity', 'N/A'),book.get('id', 'N/A'),book.get('title', 'N/A'),book.get('isbn10', 'N/A'),book.get('isbn13', 'N/A'),book.get('category', 'N/A'),university_id])

save_adoptions_to_csv(load_json.data, 'adoptions.csv')
