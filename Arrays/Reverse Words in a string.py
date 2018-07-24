
def rev(s):
    n = len(s)
    def reverse(i,j):
        while i<j:
            s[i],s[j] = s[j],s[i]
            i+=1
            j-=1

    i = 0
    for j in range(n):
        if s[j].isalpha() == False:
            reverse(i,j-1)
            i = j + 1

    reverse(i,n-1)
    reverse(0,n-1)
    return "".join(s)



s = "This is a girl"
print("Original String: ", s)
print("Reversed Order String: ",rev(list(s)))