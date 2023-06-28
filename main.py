#the encrypted message is copied from the gambitresearch site
encrypted = [155,86,245,191,96,181,115,52,248,193,88,251,180,101,254,191,82,253,188,96,247,198,17,239,194,99,169,198,96,245,201,90,247,186,17,253,187,86,169,154,82,246,181,90,253,115,84,241,180,93,245,184,95,240,184,31,169,163,93,238,180,100,238,115,100,238,193,85,169,204,96,254,197,17,252,194,93,254,199,90,248,193,17,234,193,85,169,150,71,169,199,96,169,188,84,234,193,84,248,183,86,201,186,82,246,181,90,253,197,86,252,184,82,251,182,89,183,182,96,246,115,98,254,194,101,242,193,88,169,197,86,239,184,99,238,193,84,238,141,17,192,138,38,188,180,87,234,184,33,192]

#plaintext = decoded message
#ciphertext = encoded message

#parameter: a number
#returns: whether or not this ascii value is printable and English 
def is_printable_char(num):
    #ascii values 31 and below are legacy and do not represent readable text
    #Gambit Research is based out of London, England, and the message is text explaining how to apply 
    #expanded ascii values 128 and above are generally for non-English characters
    #therefore valid plaintext should be printable and English, so above 31 and below 128
    return num > 31 and num < 128

#parameters: numbers a, b, c, representing the shifts of the Vigenere cipher
#returns: True if all of the plaintext found with these shifts are printable and English, False otherwise
#will print the decoded message as well if all chars valid
def shift(a, b, c):
    output = ""
    for i in range(0, len(encrypted)):
        decoded = encrypted[i]
        #reversing the code in the <script> tag with comment //You're on the right path
        #apply the correct shift depending on the position in the ciphertext
        if i % 3 == 0:
            decoded = (decoded - a) % 256
        elif i % 3 == 1:
            decoded = (decoded - b) % 256
        elif i % 3 == 2:
            decoded = (decoded - c) % 256

        #if a character is not valid, no need to look at the rest of the ciphertext
        if not is_printable_char(decoded):
            return False
        
        #add the character to the output string if it was valid
        output += chr(decoded)
    
    #if the loop has completed, the shift resulted in valid characters only
    print(output)
    return True

#parameters: plain and cipher are both numbers, ascii values of the plaintext and cipher text
def find_shift(plain, cipher):
    #return the number that was added to the plaintext character to get to the ciphertext character
    #this formula comes from the //You're on the right path code
    return (cipher - plain) % 256

#loop through the ciphertext, taking chunks of 3 characters so don't go all the way to the end
for i in range(0, len(encrypted) - 3):
    #pick a block of 3 chars
    curr_block = encrypted[i : i + 3]
    #"the" is the most common word in the English language, 
    # so I try all the shifts that result in "the" in the decoded message
    #find the shift values that would turn this 3-character block into "the"
    shift1 = find_shift(ord("t"), curr_block[0])
    shift2 = find_shift(ord("h"), curr_block[1])
    shift3 = find_shift(ord("e"), curr_block[2])
    shift_arr = [shift1, shift2, shift3]
    #the shift() function takes a, b, c, so shift1, shift2, shift3 must be passed in correctly
    param_arr = [0, 0, 0]
    for s in range(0, 3):
        #based on the value of i, one of a, b, c will be shift1
        # and the rest are assigned sequentially
        param_arr[(i + s) % 3] = shift_arr[s]
    
    #pass the correct a, b, c, into shift and see if the result is printable English
    shifts_are_right = shift(param_arr[0], param_arr[1], param_arr[2])
    if shifts_are_right:
        #note the shifts only if the results are printable English
        print("shifts for above", param_arr)