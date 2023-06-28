# This is my solution to the Gambit challenge
[https://gambitresearch.com/quiz](https://gambitresearch.com/quiz)
## Step 1: I found the method used to encode the message (ASCII variation on Vigenere cipher) hidden on the site. 
## Step 2: I copied the encoded message and changed it to an array.
## Step 3: I took 3-character blocks and found the shifts that decoded the particular block to "the". I then aplied thesee shifts across the whole message. If the shifts resulted in any non-printable non-English ASCII characters, then I moved to the next block. Otherwise, I printed the decoded message that used the particular shift.
## Step 4: Looking at the results in results.txt, it is obvious which one is the correct decryption. 

### main.py contains the code with comments that I used to implement my solution.
### results.txt contains the output of running this code
