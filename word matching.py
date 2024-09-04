print("\033c")

def match_words(words):
    cnt = 0
    lst = []
    
    for word in words:
        
        if len(word) > 1 and word[0] == word[-1]:
            cnt = cnt + 1
            lst.append(word)
            
    print("List of words with the first and last characters same\n ", lst)
    return cnt

li = ['abc', 'cfc', 'xyz', 'aba', '1221', 'nahian', 'narhan', 'aditya']
count = match_words(li)
print("Number of words having first and last character same: ", count)


        
    