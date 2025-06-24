import csv
from geo import get_coordinates

def is_valid_row(row):
    required_fields = [
        row['email'], row['first_name'], row['last_name'],
        row['res_street'], row['res_city'], row['res_state'], row['res_postcode'],
        row['post_street'], row['post_city'], row['post_state'], row['post_postcode']
    ]
    return all(required_fields)

def clean_postcode(value):
    try:
        return str(int(float(value))) 
    except ValueError:
        return ''

def parse_and_validate_csv(input_path, output_path):
    with open(input_path, 'r', newline='', encoding='utf-8') as infile, \
         open(output_path, 'w', newline='', encoding='utf-8') as outfile:

        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames + ['latitude', 'longitude']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        count = 0
        for row in reader:
            if count >= 100:
                break

            if not is_valid_row(row):
                print("Invalid row (missing required fields):", row)
                continue

            postcode = clean_postcode(row['res_postcode'])

            address = f"{row['res_city']}, {row['res_state']} {postcode}, Australia"
            print("Looking up address:", address)

            coords = get_coordinates(address)
            if coords:
                row['latitude'], row['longitude'] = coords
                writer.writerow(row)
                count += 1
            else:
                print("Geolocation failed for:", address)
