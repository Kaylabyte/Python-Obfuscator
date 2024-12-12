"""( ͡° ͜ʖ ͡°)"""

import os

"""CHANGE THESE VALUES"""
my_own_file_path = "" # leave empty if not using your own file path
INPUT_DIR = "convert" # puts the folder in the working directory by default, not necessarily the same location as this file
OUTPUT_DIR = "converted" # puts the folder in the working directory by default, not necessarily the same location as this file
obfuscation_char = "⠀" # empty braille character by default, makes the "code" look funny that way - can be set to a string

"""DON'T CHANGE THESE VALUES"""
dir_list = []
SUPPORTED_FORMATS = [".py"]

if my_own_file_path != "":
    if os.path.exists(my_own_file_path): # makes sure you're not stupid
        dir_list.append(my_own_file_path)
else:
    try: # scans every file in the input directory and adds all files with supported formats to a list
        for x in os.scandir(INPUT_DIR):
            if os.path.splitext(x)[1] in SUPPORTED_FORMATS:
                dir_list.append(x.path)
    except FileNotFoundError: # creates a new directory to put the to-be obfuscated files into upon first time running the program
        os.mkdir(INPUT_DIR)
        exit(f"""Convert folder successfully made! Please put all the files you want to obfuscate into the \"{INPUT_DIR}\" folder!
(Hint: you should find the folder in the working directory :D)""")

if obfuscation_char.strip() == "":
    exit("Space as obfuscation character is not supported. Please set the obfuscation character to something other than space and try again...")
obfuscation_char = str(obfuscation_char) # just in case obfuscation_char is set to an integer or something

def save_file(converted, path):
    try: # creates the output directory if it doesn't already exist
        os.mkdir(OUTPUT_DIR)
    except FileExistsError:
        pass

    file = path.split("/")[-1] # grabs the file name + extension (to be used in the new file name)
    file_extension = file.split(".")[-1]
    file_name = file.replace(f".{file_extension}", "")
    output_file = open(f"./{OUTPUT_DIR}/{file_name}_obfuscated.{file_extension}", "w") # creates the new file and then writes to it
    output_file.write(f'unobfuscated = "{converted}".replace(f"{obfuscation_char * 3} ", " ").replace(f"{obfuscation_char * 2} ", "1").replace(f"{obfuscation_char} ", "0").split(); unobfuscated = "".join(chr(int(binary, 2)) for binary in unobfuscated); exec(unobfuscated)')
    output_file.close()

def obfuscate(bin_char): # converts the binary to the obfuscation character so that one "character" represents 0, two "characters" represents 1, and three "characters" is a null terminator
    obfuscated = ""
    for byte in bin_char:
        if byte == "1":
            obfuscated += f"{obfuscation_char * 2} "
        elif byte== "0":
            obfuscated += f"{obfuscation_char} "
        else:
            raise Exception("Binary has byte value other than 0 or 1. If this happens, please tell me what you did as this isn't supposed to happen ever.")

    obfuscated += f"{obfuscation_char * 3} "
    return obfuscated

def file_convert_to_bin(path): # reads the contents of the entire file and converts it all to binary
    converted = ""
    input_file = open(path, "r")
    f_contents = input_file.read()

    for char in f_contents: # loops through each character and individually converts each to binary (then the obfuscation character)
        bin_char = bin(ord(char)).replace("0b", "")
        converted += obfuscate(bin_char)

    save_file(converted, path) # self explanatory, creates a new file to save the obfuscated output
    input_file.close()

if len(dir_list) == 0: # if there are no files to be obfuscated
    if my_own_file_path != "":
        exit("Please provide a valid directory to the \"my_own_file_path\" variable and try again...")
    else:
        exit(f"""Please provide a file to be obfuscated and try again...
(Hint: put the files to be obfuscated into the "{INPUT_DIR}" folder located in the working directory :D)""")

for path in dir_list: # loops over every file to be obfuscated
    file_convert_to_bin(path)

print("Successfully obfuscated file(s)!!!")
