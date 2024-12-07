def main():
    file_name = input("Enter the file name: ")
    
    try:
        with open(file_name, 'r') as file:
            count = 0
            total = 0
            
            for line in file:
                line = line.strip()
                if line.startswith("X-DSPAM-Confidence:"):
                    try:
                        value = float(line.split(":")[1].strip())
                        total += value
                        count += 1
                    except ValueError:
                        print(f"Skipping invalid line: {line}")
            
            if count > 0:
                average = total / count
                print(f"Average spam confidence: {average}")
            else:
                print("No lines with 'X-DSPAM-Confidence:' found.")

    except FileNotFoundError:
        print(f"File not found: {file_name}")
        
if __name__ == "__main__":
    main()