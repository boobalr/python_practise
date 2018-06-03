def duplicate_count(text):
    # Your code goes here
    masterCounter = 0
    str1 = ""
    #Convert all the alphabets to lower case
    text = text.lower()
    #traverse through each character in the input string
    for sub in text:
        #count(sub) will search for a character in a string
        #find its no. of occurences and returns
        counter = text.count(sub)
        if counter > 1:
            str1 = str1 + sub
            #Adding the filtered character in a string using join
            str1 = ''.join(set(str1))
    #returns the length of the filtered string
    return len(str1)
   
#Sample Inputs:
#test.assert_equals(duplicate_count("abcde"), 0)
#test.assert_equals(duplicate_count("abcdea"), 1)
#test.assert_equals(duplicate_count("indivisibility"), 1)
