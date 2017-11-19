
def main():
	"""
	Main section of program
	Open words.txt as f. Turn into list 'words'. 
	Use is_palindrome to copy palindromes into list 'palindromes'
	Write 'palindromes' palindromes.txt
	
	"""
	with open("words.txt") as words:
		# if line (without \n) is palindrome, add to palindrome list
		palindrome = [line.rstrip('\n') for line in words if is_palindrome(line.rstrip('\n')) == True]
		
	#create output file palindromes.txt
	output = open("palindromes.txt", "w")
	
	#write palindromes list to output file, one per line, and close the file
	with open("palindromes.txt", "w") as output:
		output.writelines("%s\n" % i  for i in palindrome)
		
	print ("Palindromes written to palindromes.txt")

def is_palindrome(word):
	"""
	Function reverses word, saves it as drow and checks if the two are the same
	If same, returns true; if not, returns false
	
	>>> is_palindrome("hannah")
	True
	>>> is_palindrome("james")
	False
	"""
	
	drow = word[::-1]
	if word==drow:
		return True
	else: return False

# Run program

if __name__ == "__main__": main()
	#import doctest
	#doctest.testmod()    