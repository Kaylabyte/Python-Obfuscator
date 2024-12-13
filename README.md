# Python-Obfuscator

Obfuscated any .py file into an unreadable one-liner. Not useful in the slightest, but it is funny :D

## What it does:

This program converts any python file into a functional piece of code unreadable to any normal human. 

###### From:

![image](https://github.com/user-attachments/assets/36add455-78a0-467e-9433-4d47f77d02e2)

###### To:

![image](https://github.com/user-attachments/assets/bf4913bd-99c3-4846-83be-6a3e14927a6d)

Essentially, the contents of the Python file when run through my program is converted to ASCII, converted from decimal to binary, then the ones and zeros are each replaced with an "obfuscation character". All of this is then put into a new file alongside an additional piece of code that converts it all back and lets Python run the code. This allows for the code to all be on one VERY long line and simultaneously be completely unreadable to anyone.

## How to use:

These steps are mainly going to be for me as I tend to forget how to use my own programs, but it should also hopefully be useful on the off-chance someone else finds this.

### 1. Change Default Values

By default, the code creates a folder in the working directory called "convert" for you to put the files you want to convert into, a folder in the working directory called "coverted" where the converted files are located, and it sets the obfuscation character to an empty braille character. All defaults are near the top of the code for easy access.

![image](https://github.com/user-attachments/assets/190b4aa1-8bc8-4d35-a177-189cd08ba948)

#### 1.1. Specify your own file path

If you want to specify a file rather than convert multiple files, put the exact path in the ***my_own_file_path*** variable. File paths can be relative to the working directory.

*NOTE: only .py files are supported in the meantime.*

###### Example 1:

![image](https://github.com/user-attachments/assets/1d636191-14b3-4ee2-b90d-3fe6276a4d5c)

###### Example 2:

![image](https://github.com/user-attachments/assets/91448261-8f96-4d9c-9456-3a7728c22c85)

#### 1.2. Specify input/output folders

If you want to specify pre-existing input and output folders or would like to change the name of the generated ones, put the exact directory in the ***INPUT_DIR*** and ***OUTPUT_DIR*** variables respectively. Folder paths can be relative to the working directory.

###### Example 1:

![image](https://github.com/user-attachments/assets/cefabc6a-6b3e-4404-ac68-b1d84f0fd426)

###### Example 2:

![image](https://github.com/user-attachments/assets/03477da3-a04c-4707-8b08-092160f8f626)

#### 1.3. Specify obfuscation character

If you want to change the obfuscation character from the default, put the new obfuscation character in the ***obfuscation_char*** variable. The obfuscation character may be a string, however it cannot be a space (although, the empty braille character "⠀" may be used instead.)

###### Example 1:

![image](https://github.com/user-attachments/assets/3cbdd2f6-9382-4271-b714-e37ff9982000)

###### Example 2:

![image](https://github.com/user-attachments/assets/7e7304a0-a1fb-4e1c-be01-f9f4d3327965)

---

### 2. Choosing Files to Obfuscate

#### 2a. Obscuring folder of files

If you didn't do [step 1.1](#11-specify-your-own-file-path), then follow these steps

##### 2a.1. Creating input folder

If the input folder doesn't already exist, the program will create the input folder for you at the location given in the ***INPUT_DIR*** variable. Just run the program once and the folder will be created. The program will then tell you the name of the folder.

###### Message if successful:

![image](https://github.com/user-attachments/assets/5a87012f-d58d-455c-882a-ab8d4c3bbf66)

##### 2a.2. Choosing the files

After the convert folder is created, put any file you want to obfuscate into the folder created in the previous step.

###### Example:

![image](https://github.com/user-attachments/assets/aeaf034b-e9e8-4956-afe0-13755e6daaac)

#### 2b. Specifying your own file

If you followed [step 1.1](#11-specify-your-own-file-path), then no additional steps need to be taken here.

---

### 3. Obfuscating Files

Run the program once you've finished step 2. If all has gone correctly, an output folder should be created with the obfuscated files at the location given in the ***OUTPUT_DIR*** variable. 

###### Message if successful:

![image](https://github.com/user-attachments/assets/9f8e4186-94a3-4699-8c79-8e48d0b91f39)

###### Example:

![image](https://github.com/user-attachments/assets/7cace1b9-9826-447a-8ea1-a83a6668ba4c)
