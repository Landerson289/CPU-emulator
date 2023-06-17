# CPU-emulator

## Storage
The RAM.txt file functions as the memory of the computer. It is stored with 2040 zeros and the machine code to load the assembly.ass file into the ram. Although it is a .txt file, it can only hold 1s and 0s. 


## Execution
The code reads through the code one byte at a time, performing the fetch, decode, execute cycle upon it. It checks the byte with a series of elif statements in the main file. It will then execute some code that will alter the RAM file in someway or interact with the user. A list of the commands. their assembly and machine code values and a description of their function can be found at the command.txt file. 

## Assembling
This code runs through the assembly.ass file to convert it to machine code by using the commands.txt file to convert keywords to its corresponding byte. 

## CURRENT FRAMEWORK
* Code starts at 00000000
* Variables are stored at 10000000 for the language
* Addresses at the end of the memory are being used for temporary values.

## PLANNED FRAMEWORK
* Some sections of the Memory should be presaved for programmes like reading and writing to variables for the language etc. These should perhaps be a certain length, ei 255 bytes. This should  allow the user to pass in 'parameters' by storing values in specific slots. It should also return values and continue the code being run before.
* File system which can store .txt files. The code for this is already written but should be updated to be more dynamic and to intergrate with updated framework.
* A system to convert .ass files stored like text files to executable machine code.
