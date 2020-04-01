'''
Created on Mar 31, 2020

@author: bvikram2
'''
'''
Decrypting the program

    Fortunately for you, the minions aren't exactly advanced cryptographers.
    In their code, every lowercase letter [a..z] is replaced with the corresponding one in [z..a],
    while every other character (including uppercase letters and punctuation) is left untouched.
    That is, 'a' becomes 'z', 'b' becomes 'y', 'c' becomes 'x', etc.
    For instance, the word ""vmxibkgrlm"", when decoded, would become ""encryption"".
    
Input:
    wrw blf hvv ozhg mrtsg'h vkrhlwv?
Output:
    did you see last night's episode?
    
Input:
    Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!
Output:
    Yeah! I can't believe Lance lost his job at the colony!!
'''

def decrypting(x):
    decoded_list=[]
    for letter in x:
        if ord(letter) >=97 and ord(letter) <=122:
            front = ord(letter)-97
            back = 122 - front
            decoded_list.append(chr(back))
        else:
            decoded_list.append(letter)
    decoded_str="".join(decoded_list)
    return decoded_str
 
decryptedString = decrypting(input("Enter the String to be decrypted : "))
print("Decrypted String : " + decryptedString)