words = ['aardvark', 'abaci', 'aback', 'abacus']

def search( prefix ):
    """Search for a prefix string in the dictionary.
    Args:
        str:  A string to look for in the dictionary
    Returns:
        code WORD if str exactly matches a word in the dictionary,
            PREFIX if str does not match a word exactly but is a prefix
                of a word in the dictionary, or
        NO_MATCH if str is not a prefix of any word in the dictionary
    """
    global words
    print("words at start of search is: ", words)
    #for i in range(len(words)):
     #   if words[i] == prefix:
     #       print("words[i] at i if is {}, searching for {}  ".format(words[i], prefix))
     #       return "WORD"
    if [1 for word in words if word == prefix]:
        return 1
    #    elif words[i].startswith(prefix):
    #        print("words[i] at i elif is {}, searching for {}  ".format(words[i], prefix))
    #        return "PREFIX"
    if [ 2 for word in words if word.startswith(prefix)]:
        return 2
    #    else:
    #        print("words[i] at i else is:  ", words[i] )
    #        result =  "NO_MATCH"
    return 0

    return result
    # FIXME: I suggest using a linear search first, checking for exact matches
    # with == and then for partial matches with the "startswith" function, e.g.,
    # words[i].startswith(prefix). 
    # Once you get the whole program working, you can make it much, much faster
    # using a binary search (which we will discuss in class). 
    
def main():
    print("aba returns:  ", search("aba"))
    print("abacus returns:  ", search("abacus"))
    print("dodo returns", search("dodo"))
main()
