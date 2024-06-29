#!/usr/bin/env python
# coding: utf-8

# In[7]:


def bin_to_dec(number):

    #Initialize 
    integer_conversion = []
    exponent = len(str(number)) -1 

    if number == 0: #If number = 0, conversion = 0
        return "0"
    
    for digit in number: #Loop conversion until last digit

        digit_conversion = int(digit)*(2**exponent) #Convert into binary
        exponent -= 1 #Subtract 1 from exponent for every digit converted
        integer_conversion.append(digit_conversion) # Add conversion to end of list 
        
    return sum(integer_conversion) #Get the sum of the elements in the list to get final output
        
bin_to_dec("1010")       


# In[1]:


def dec_to_bin(number):

    #Initialize
    binary_conversion = []
    integer = int(number)

    while integer > 0: # Loop while greater than 0 
        remainder = str(integer % 2) # Get the remainder of the integer 
        integer = integer // 2 # Divide the integer by 2 
        binary_conversion.append(remainder) # Add the remainder to the list (as a digit of the binary number)
    
    binary_conversion.reverse() # Reverse the list 
    return ''.join(binary_conversion) # Concatenate all elements of the list to get binary number

dec_to_bin("5")


# In[19]:


def telephone_cipher(message):

    encoder_dict = {
                " ":"0",
                "A":"2",
                "B":"22",
                "C":"222",
                "D":"3",
                "E":"33",
                "F":"333",
                "G":"4",
                "H":"44",
                "I":"444",
                "J":"5",
                "K":"55",
                "L":"555",
                "M":"6",
                "N":"66",
                "O":"666",
                "P":"7",
                "Q":"77",
                "R":"777",
                "S":"7777",
                "T":"8",
                "U":"88",
                "V":"888",
                "W":"9",
                "X":"99",
                "Y":"999",
                "Z":"9999"
            }
    
    encrypted_message = [] # Initialize
    
    for letter in message: # Loop the conversion of each letter according to dict 
        new_number = encoder_dict[letter] 

        # Use "and" function to put the list in the range
        # if first digit of previous number = first digit of new number, add "_"
        if encrypted_message and encrypted_message [-1][0] == new_number [0]: 
            encrypted_message.append("_") 
            
        encrypted_message.append(new_number) # Add the new number to the list
        
    return ''.join(encrypted_message) # Concatenate all numbers in the list into a single string

telephone_cipher("WXYZ")


# In[7]:


def telephone_decipher(telephone_string):
    
    decipher_dict = {
        "0":" ",
        '2': 'A',
        '22': 'B',
        '222': 'C',
        '3': 'D',
        '33': 'E',
        '333': 'F',
        '4': 'G',
        '44': 'H',
        '444': 'I',
        '5': 'J',
        '55': 'K',
        '555': 'L',
        '6': 'M',
        '66': 'N',
        '666': 'O',
        '7': 'P',
        '77': 'Q',
        '777': 'R',
        '7777': 'S',
        '8': 'T',
        '88': 'U',
        '888': 'V',
        '9': 'W',
        '99': 'X',
        '999': 'Y',
        '9999': 'Z'
    }
    # Initialize
    decrypted_message = []
    i = 0
    
    while i < len(telephone_string): # Loop while the the character index is less than the length of the string
        index_start = i 
        while i < len(telephone_string) - 1 and telephone_string[i] == telephone_string[i + 1]:# Loop from start to end index
            i += 1
        index_end = i + 1
        number_key = telephone_string[index_start:index_end]
        if "_" not in number_key: #Ignore the underscore and add the letter conversion to the message
            decrypted_message.append(decipher_dict[number_key])
            
        i += 1 # Check the next number
    
    return "".join(decrypted_message) #Concatenate the letters in the list

telephone_decipher("2_22")


# In[ ]:




