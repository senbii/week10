def main():
    file_name = input("Enter the filename: ")
    
    try:
        with open(file_name) as file:
            for line in file:
                line = line.strip()
                line = line.upper()
                print(line)
    except FileNotFoundError:
        print(f"File not found: {file_name}")
        
if __name__ == "__main__":
    main()