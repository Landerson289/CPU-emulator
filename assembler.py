def writeToRam(data, loc):
  ram = open("RAM.txt", "r")
  ramStr = ram.read()
  ramList = []
  #print(data)
  for i in ramStr:
    ramList.append(i)
  for i in range(8):
    #print(data[i])
    ramList[loc*8+i] = data[i]
  ramStr = ""
  for i in ramList:
    ramStr += i
  ram.close()
  ram = open("RAM.txt", "w")
  ram.write(ramStr)
  ram.close()


def assemble(startByte):
  code = open("assembly.ass", "r").read().splitlines()
  

  print("assembling")

  currentByte = startByte #+ 1
  lineNum = 0
  for line in code:
    if line != "":
      if line[0] != "#":
        lineNum += 1
        parts = line.split(" ")
        if len(parts) == 0:
          continue
        elif len(parts) == 1:
          instruction = parts[0]
          #if instruction == "EXT":
          #  print(instruction)
          location = None
          location2 = None
        elif len(parts) == 2:
          instruction = parts[0]
          location = parts[1]
          location2 = None
        elif len(parts) == 3:
          instruction = parts[0]
          location = parts[1]
          location2 = parts[2]
        else:
          print("ERROR: LINE FORMAT WRONG ON LINE " + str(lineNum))
          print("\t" + line)
    
        commands = open("commands.txt").read().splitlines()
        for command in commands:
          command = command.split(" ")
          assemblyCode = command[0]
          machineCode = command[2]
          detail = command[3:]
    
          #if assemblyCode == "EXT":
          #  print("FFFFF")
          
          if instruction == assemblyCode:
            #print(assemblyCode)
            #print(machineCode)
            #print(detail)
          #  if instruction == "EXT":
          #    print(machineCode, currentByte)
            writeToRam(machineCode, currentByte)
            currentByte += 1
            if location != None:
              
              writeToRam(location, currentByte)
              currentByte += 1
            if location2 != None:
              writeToRam(location2, currentByte)
              currentByte+= 1
            break
