#!/usr/bin/env python
# coding: utf-8

# In[201]:


def shift_letter(letter, shift):
    
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    if letter == " ":
        return " "
        
    else:
        not_looped = ((ord(letter) + shift))
        looped = (not_looped - 65 ) % 26
        return alphabet[looped]
    
shift_letter("A", 2)


# In[22]:


def caesar_cipher(message, shift):

    def shift_letter(letter, shift):
    
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        not_looped = ((ord(letter) + shift))
        looped = (not_looped - 65 ) % 26
        return alphabet[looped]

    final = " "
    for char in message:
        if char == ' ':
            final += ' '
        else: 
            final += shift_letter(char,shift)

    return final

caesar_cipher ("A B C",2)


# In[228]:


def shift_by_letter(letter, letter_shift):
   
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if letter == " ":
        return " "

    else: 
        not_looped = ord(letter) - 65 + ord(letter_shift) - 65
        looped = not_looped % 26
        return alphabet[looped]

shift_by_letter("Z","B")


# In[46]:


def vigenere_cipher(message, key):
    
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    final_message = "" 
    
    if len(key) != len(message):
        key = key*(int(len(message) // len(key)))
        
        if len(key) != len(message):
            
            for i in range(len(message)-len(key)):
                key = key + key[i]
    
    for i in range(len(message)):
        
        if message[i] == " ":
            final_message += " "
            
        else:
            key_index = alphabet.index(key[i])
            index = alphabet.index(message[i])
            new_index = (index + key_index) % len(alphabet)
            final_message += alphabet[new_index] 
            
    return final_message


# In[48]:


def scytale_cipher(message, shift):
   
    if len(message) % shift == 0:
        message = message
        
    else:
        while len(message) % shift != 0:
            message = message + "_"
        
    new_message = ""
    for i in range(len(message)):
        index = (i // shift) + (len(message) // shift) * (i % shift)
        new_message = new_message + message[index] 
        
    return new_message


# In[50]:


def scytale_decipher(message, shift):

    new_message = ""
    
    for i in range(len(message)):        
        index = (i // (len(message) // shift)) + (i % (len(message) // shift)) * shift
        new_message +=message[index]
        
    return new_message


# In[ ]:




