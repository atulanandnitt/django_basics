#https://www.geeksforgeeks.org/longest-palindromic-substring-set-2/



"""
You have a client-server architecture. In between client 
and server you have your application. Given each server has a success probability factor `x`(0 to 1), You are supposed to come up with a logic so that you decide which server among all the active servers would process your request and give back the response to your application, which in turn is displayed to the user. Design and Develop your application… 

"""
# A O(n^2) time and O(1) space program to find the 
#longest palindromic substring 

# This function prints the longest palindrome substring (LPS) 
# of str[]. It also returns the length of the longest palindrome 
def longestPalSubstr(string): 
	maxLength = 1

	start = 0
	length = len(string) 

	low = 0
	high = 0

	# One by one consider every character as center point of 
	# even and length palindromes 
	for i in range(1, length): 
		# Find the longest even length palindrome with center 
	# points as i-1 and i. 
		low = i - 1
		high = i 
		while low >= 0 and high < length and string[low] == string[high]: 
			if high - low + 1 > maxLength: 
				start = low 
				maxLength = high - low + 1
			low -= 1
			high += 1

		# Find the longest odd length palindrome with center 
		# point as i 
		low = i - 1
		high = i + 1
		while low >= 0 and high < length and string[low] == string[high]: 
			if high - low + 1 > maxLength: 
				start = low 
				maxLength = high - low + 1
			low -= 1
			high += 1

	print ("Longest palindrome substring is:", )
	print (string[start:start + maxLength] )

	return maxLength 

# Driver program to test above functions 
string = "forgeeksskeegfor"
print ("Length is: " + str(longestPalSubstr(string)) )

# This code is contributed by BHAVYA JAIN 
