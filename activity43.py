def match_word (words):
    ctr=0
    lst=[]
    for word in words:
        if len (word) > 1 and word[0]==word[-1]:
            ctr=ctr+1
            lst.append(word)
    print ("list a words with same first and last letter", lst)
    return ctr
count=match_word(['apple', 'mango', 'aba', 'palendromic'])
print ("number of words having same first and last character", count)