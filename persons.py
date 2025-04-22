import csv

def write_person_info(num_entries, filename="persons_info.csv"):

    fieldnames = ['id', 'first name', 'last name', 'age']

    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for i in range(1, num_entries+1):
                while True:
                    first_name = input(f"Please enter name {i}: ")
                    last_name = input(f"Please enter last name {i}: ")
                    age_str = input(f"Please enter age {i}: ")

                    try:
                        age = int(age_str)
                        break
                    except ValueError:
                        print(f"Please enter integer as age")

                writer.writerow({'id': i, 'first name': first_name, 'last name': last_name, 'age': age})

        print(f"Data has been successfuly uploaded: {e}")
    except Exception as e:
        print(f"Error with file: {e}")
num = int(input("How many person's data you want to store?"))
write_person_info(num)
