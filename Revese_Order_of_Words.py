#Reverse order of Word in a string


def revOrderOfWords(s):
    p=s.split()
    k=p[::-1]
    output=' '.join(k)
    return output


s=input("Enter a string:\n")          #"Python is an amazing language"
ans=revOrderOfWords(s)                
print(ans)                            # language amazing an is Python