#https://www.geeksforgeeks.org/given-a-string-find-its-first-non-repeating-character/

def find_first_non_repeating_character_fromGivenString(str1):
    dict1={key:str1.count(key) for key in str1}
    print(dict1)
    for item in str1:
        if dict1[item] ==1:
            return item
    

str1="GeeksforGeeks"
print(find_first_non_repeating_character_fromGivenString(str1) )






def findFirstNonRepeating_FromGivenStream(stream1):
    repeated=[]
    inDLL=[]
    
    while len(stream1)>0:
        print("reading ",stream1[0] ,"from stream")
        if stream1[0] not in repeated:
            if stream1[0] not in inDLL:
                inDLL.append(stream1[0])
                
            else:
                inDLL.remove(stream1[0])
        
        stream1 = stream1[1:]
        
        if len(inDLL) !=0:
            print("first non-repeating element till now :",inDLL[0])
    




stream1="geeksforgeeksandgeeksquizfor"
print(findFirstNonRepeating_FromGivenStream(stream1) )





#https://www.geeksforgeeks.org/find-first-non-repeating-character-stream-characters/

# A Python program to find first non-repeating character from
# a stream of characters
MAX_CHAR = 256
 
def findFirstNonRepeating():
 
    # inDLL[x] contains pointer to a DLL node if x is present
    # in DLL. If x is not present, then inDLL[x] is NULL
    inDLL = [] * MAX_CHAR
 
    # repeated[x] is true if x is repeated two or more times.
    #  If x is not seen so far or x is seen only once. then
    # repeated[x] is false
    repeated = [False] * MAX_CHAR
 
    # Let us consider following stream and see the process
    stream = "geeksforgeeksandgeeksquizfor"
    for i in range(len(stream)):
        x = stream[i]
        print ("Reading " + x + " from stream")
 
        # We process this character only if it has not occurred
        # or occurred only once. repeated[x] is true if x is
        # repeated twice or more.s
        if not repeated[ord(x)]:
 
            # If the character is not in DLL, then add this
            # at the end of DLL
            if not x in inDLL:
                inDLL.append(x)
            else:
                inDLL.remove(x)
 
        if len(inDLL) != 0:
            print ("First non-repeating character so far is "),
            print (str(inDLL[0]))
 
# Driver program
findFirstNonRepeating()
     