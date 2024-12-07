import re

def main():
    file_name = input("Enter the file name: ")
    
    try:
        with open(file_name, 'r') as file:
            for line in file:
                emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', line)
                for email in emails:
                    print(email)
    except FileNotFoundError:
        print(f"File not found: {file_name}")
        
if __name__ == "__main__":
    main()