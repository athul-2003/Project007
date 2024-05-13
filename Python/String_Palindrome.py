# Python program to check if a string is palindrome or not

x_str = input("Enter a string: ")

rev_str = ""
for i in x_str:
	rev_str = i + rev_str

if (x_str == rev_str):
	print("Yes,the entered string is a palindrome.")
else:
	print("No,the entered string is not a palindrome.")
