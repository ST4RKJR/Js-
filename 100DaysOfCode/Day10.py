#Find Smallest Letter Greater Than Target
def nextGreatestLetter(letters, y):

    for x in letters:
        if y < x:
            return(x)
    else:
        return(letters[0])
    