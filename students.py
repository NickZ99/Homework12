import csv

def filter_students(input_filename="students.csv", failed_filename="failed_students.csv", passed_filename="passed_students.csv"):
    try:
        with open(input_filename, 'r', newline='', encoding='utf-8') as infile, \
                open(failed_filename, 'w', newline='', encoding='utf-8') as failedfile, \
                open(passed_filename, 'w', newline='', encoding='utf-8') as passedfile:
            reader = csv.DictReader(infile)
            failed_writer = csv.DictWriter(failedfile, fieldnames=reader.fieldnames)
            passed_writer = csv.DictWriter(passedfile, fieldnames=reader.fieldnames)

            failed_writer.writeheader()
            passed_writer.writeheader()

            for row in reader:
                try:
                    grade = int(row['Grade'])
                    if grade < 50:
                        failed_writer.writerow(row)
                    else:
                        passed_writer.writerow(row)
                except ValueError:
                    print(f"Warning: Grade in a wrong format: {row['Name']}")
                except KeyError:
                    print(f"Warning: No 'Grade' column found in the file.")
                    return

        print(f"Students successfully filtered and uploaded in Files: {failed_filename}, {passed_filename}")
    except FileNotFoundError:
        print(f"Error: file '{input_filename}' has not found")
    except Exception as e:
        print(f"Unexpected Error: {e}")

filter_students()
