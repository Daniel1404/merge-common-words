#####################################
#          DEVELOPER ROAD           #
#####################################



def open_file(file_path, open_mode="r"):

    try:
        file_handler = open(file_path, mode=open_mode)

    except FileNotFoundError:
        print(f"Sorry the file {file_path} doesn't exist")
        exit()

    except ValueError:
        print(f"Sorry the file {file_path} can't be opened with mode {open_mode}")
        exit()

    return file_handler            


def get_file_words(file_path):

    file_words = set()

    read_file = open_file(file_path)

    for word in read_file.read().split():
        
        file_words.add(word.lower())

    return file_words

def merge(*filenames, merge_file="merge.txt"):

    list_of_file_words = []

    for filename in filenames:

        file_words = get_file_words(filename)
        list_of_file_words.append(file_words)

    common_words = set.intersection(*list_of_file_words)

    merge_write_file = open_file(merge_file, "w")

    for word in common_words:

        word = word + ", "

        merge_write_file.write(word)
    
    merge_write_file.close()



def main():
    
    file1 = "text_one.txt"

    file2 = "text_two.txt"

    merge(file1, file2, merge_file="merge_main.txt")


if __name__ == "__main__":
    main()