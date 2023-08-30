import string

def main():
    file_name = input("File: ")

    try:
        with open(file_name, 'r') as file:
            word_count = {}
            
            for line in file:
                words = line.lower().split()

                for word in words:
                    word = word.strip(string.punctuation)
                    
                    if word in word_count:
                        word_count[word] += 1
                    else:
                        word_count[word] = 1

            print("Word frequency:", word_count)
    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    main()
