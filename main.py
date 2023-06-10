f = open("RAM.txt", "w")
#f.write("00001011"+"0"*(256*8-48)+"0100100001001001001000010000000000000000")
f.write("00001011"+ "0"*(256*8-8))
f.close()


#print(len("00001011"+"0"*(256*8-48)+"100100001001000100100001000000000000000000"))

ram = open("RAM.txt").read()

def get_byte(byteNum):
  return ram[byteNum*8:byteNum*8+8]
def binToInt(byte):
  num = 0
  for i in range(len(byte)):
    num += 2**(len(byte)-i-1)*int(byte[i])
  return num
def intToBin(number):
  bitList = ["0","0","0","0","0","0","0","0"]
  number = number % 256
  while number != 0:
    count = 0
    powerOfTwo = 1
    while powerOfTwo <= number:
      powerOfTwo *= 2
      count += 1
      
    powerOfTwo /= 2
    if count <= 8:
      bitList[len(bitList)-count] = "1"
      

    number -= powerOfTwo

  bitString = ""
  for i in bitList:
    bitString += i

  return bitString

stop = False
byteNum = 0
register = "0"*8

output = ""

while stop == False:
  byte = get_byte(byteNum)
  #print(byte)
  print("Reg", register)
  if byte == "00000000": # Stop
    stop = True
    print("EXT")
    print()
    print(output)
  elif byte == "00000001": # Load
    byteNum += 1
    location = get_byte(byteNum)
    print("LDA", location)
    byte = get_byte(binToInt(location))
    
    register = byte
  elif byte == "00000010": # Store
    byteNum += 1
    location = get_byte(byteNum)
    print("STO", location)
    #print("STORED BYTE ==", register)

    ramList = []
    for i in ram:
      ramList.append(i)

    for i in range(0,8):
      #try:
      ramList[binToInt(location)*8+i] = register[i]
      #except:
        #print(binToInt(byte)*8+i)
    ram = ""
    for i in ramList:
      ram += i

    RAM = open("RAM.txt","w")
    RAM.write(ram)
    RAM.close()  
  elif byte == "00000011": # Input
    print("INP")
    rawInput = input(">>>")
    validInput = True
    for i in rawInput:
      if i != "0" or i != "1":
        ValidInput = False

    if len(rawInput) != 8:
      validInput = False

    if validInput == True:
      register = rawInput
    else:
      quit()
  elif byte == "00000100": # Output
    print("OUT")
    print(register)
    output += register
  elif byte == "00000101": # Break if 0
    print("BRO")
    #print(byteNum,byte)
    if register == "00000000":
      print("True")
      byteNum += 1
      byte = get_byte(byteNum)
      byteNum = binToInt(byte)-1
      
    else:
      print("False")
      byteNum+=1
  elif byte == "00000110": # equate
    byteNum += 1
    location = get_byte(byteNum)
    print("EQU", location)
    byte = get_byte(binToInt(location))
    if byte == register:
      register = "00000001"
    else:
      register = "00000000"
  elif byte == "00000111": # Set
    print("SET")
    byteNum += 1
    byte = get_byte(byteNum)
    register = byte
  elif byte == "00001000": # Add
    print("ADD")
    byteNum += 1
    location = get_byte(byteNum)
    byte = get_byte(binToInt(location))
    number1 = binToInt(byte)
    number2 = binToInt(register)
    number3 = number1+number2
    register = intToBin(number3)
  elif byte == "00001001": # Go To
    
    byteNum+=1
    location = binToInt(get_byte(byteNum))
    print("GTO", location)
    byteNum = location - 1
  elif byte == "00001010": # subtract
    print("SUB")
    byteNum += 1
    location = get_byte(byteNum)
    byte = get_byte(binToInt(location))
    number1 = binToInt(byte)
    number2 = binToInt(register)
    number3 = number1-number2
    register = intToBin(number3)
  elif byte == "00001011": #assemble code
    print("ASS")
    import assembler
    assembler.assemble(byteNum+1)
    #byteNum += 1
    ram= open("RAM.txt").read()
  elif byte == "00001100":
    print("OPC")
    print(chr(binToInt(register)))
    output += chr(binToInt(register))
  elif byte == "00001101":
    print("LDR")
    #byteNum += 1
    location = register
    byte = get_byte(binToInt(location))
    
    register = byte
  elif byte == "00001110":
    print("LDD")
    byteNum += 1
    byte = get_byte(byteNum)
    register = byte
  elif byte == "00001111":
    print("GTR")
    location = binToInt(register)
    byteNum = location - 1
  elif byte == "00010000":
    print("LDL")
    register = intToBin(byteNum)
  elif byte == "00010001":
    byteNum += 1
    byte = get_byte(byteNum)
    location = register
    print("STR", location)
    print(location, byte)
    #print("STORED BYTE ==", register)

    ramList = []
    for i in ram:
      ramList.append(i)

    for i in range(0,8):
      #try:
      ramList[binToInt(location)*8+i] = byte[i]
      #except:
        #print(binToInt(byte)*8+i)
    ram = ""
    for i in ramList:
      ram += i

    RAM = open("RAM.txt","w")
    RAM.write(ram)
    RAM.close()  
  elif byte == "00010010":
    byteNum += 1
    byte = get_byte(byteNum)
    
    #print("STORED BYTE ==", register)

    byteNum += 1
    location = get_byte(byteNum)

    print("STT", location)
    print(location, byte)

    ramList = []
    for i in ram:
      ramList.append(i)

    for i in range(0,8):
      #try:
      ramList[binToInt(location)*8+i] = byte[i]
      #except:
        #print(binToInt(byte)*8+i)
    ram = ""
    for i in ramList:
      ram += i

    RAM = open("RAM.txt","w")
    RAM.write(ram)
    RAM.close()
  elif byte == "00010011":
    byteNum += 1
    location = get_byte(binToInt(get_byte(byteNum)))
    print("STV", location)
    #print("STORED BYTE ==", register)

    ramList = []
    for i in ram:
      ramList.append(i)

    for i in range(0,8):
      #try:
      ramList[binToInt(location)*8+i] = register[i]
      #except:
        #print(binToInt(byte)*8+i)
    ram = ""
    for i in ramList:
      ram += i

    RAM = open("RAM.txt","w")
    RAM.write(ram)
    RAM.close()
  elif byte == "00010100":
    rawInput = input(">>>")
    if len(rawInput) > 1:
      quit()
    elif len(rawInput) == 0:
      register = "00000000"
    else:
      register = intToBin(ord(rawInput))
  byteNum +=1
