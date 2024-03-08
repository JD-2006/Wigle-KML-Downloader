import os

def search_in_files(keyword):
    files_with_keyword = []
    current_directory = os.getcwd()

    for filename in os.listdir(current_directory):
        if filename.endswith(".kml"):
            with open(filename, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                for line_number, line in enumerate(lines, start=1):
                    if keyword.lower() in line.lower():
                        files_with_keyword.append((filename, line_number))
                        break

    return files_with_keyword

def main():
    keyword = input("Enter the search term: ")
    found_files = search_in_files(keyword)

    if found_files:
        print("Files containing the keyword:")
        for filename, line_number in found_files:
            print(f"{filename}: Line {line_number}")
    else:
        print("No files found containing the keyword.")

if __name__ == "__main__":
    main()
