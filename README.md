# CPU-emulator

## Storage
The RAM.txt file functions as the memory of the computer. It is stored with 2040 zeros and the machine code to load the assembly.ass file into the ram. Although it is a .txt file, it can only hold 1s and 0s. 


## Execution
The code reads through the code one byte at a time, performing the fetch, decode, execute cycle upon it. It checks the byte with a series of elif statements in the main file. It will then execute some code that will alter the RAM file in someway or interact with the user. A list of the commands. their assembly and machine code values and a description of their function can be found at the command.txt file. 

## Assembling
This code runs through the assembly.ass file to convert it to machine code by using the commands.txt file to convert keywords to its corresponding byte. 
