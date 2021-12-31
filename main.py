def delete_extra_spaces(arr):
    s = "" # We want an empty string that we can add to.

    for k in range(len(arr)): # I want to treat this like an index so I can deal with previous elements.
        if arr[k] == " " and arr[k-1] == " ": # If there is a space before your current space, replace that space with nothing.
            arr.replace(arr[k-1],"") # This replaces previous element with nothing.
        else:
            s+=arr[k] # If you don't have to replace a space, add the character to your string.

    return s

def decodeMorse(morse_code):
    # ToDo: Accept dots, dashes and spaces, return human-readable message

    MORSE_CODE = {

        '..-.': 'F', '-..-': 'X',
         '.--.': 'P', '-': 'T', '..---': '2',
         '....-': '4', '-----': '0', '--...': '7',
         '...-': 'V', '-.-.': 'C', '.': 'E', '.---': 'J',
         '---': 'O', '-.-': 'K', '----.': '9', '..': 'I',
         '.-..': 'L', '.....': '5', '...--': '3', '-.--': 'Y',
         '-....': '6', '.--': 'W', '....': 'H', '-.': 'N', '.-.': 'R',
         '-...': 'B', '---..': '8', '--..': 'Z', '-..': 'D', '--.-': 'Q',
         '--.': 'G', '--': 'M', '..-': 'U', '.-': 'A', '...': 'S', '.----': '1', " " : " "}

    #  print(MORSE_CODE.get("   "))

    # morse_code = ".... . -.--   .--- ..- -.. . "
    morse_code+=" " # Need to add extra space because our loop seems to have issues appending a string the way we wrote
    # it...
    s=""
    g = ""
    mc = []

    for k in range(len(morse_code)):
      if morse_code[k] != " ":
          s+=morse_code[k]
      elif morse_code[k] == " " and morse_code[k-1] == " ":
          mc.append(morse_code[k])
      else:
          mc.append(MORSE_CODE.get(s))
          s=""

    # print(s +" ")
    s=""
    for k in mc:
        s+=k

    return s

morse_code = input("Input some morse code: ") # '... --- ...  .-.. .    . .... ...  ..'



print(delete_extra_spaces(decodeMorse(morse_code)))

#delete_extra_spaces(morse_code)