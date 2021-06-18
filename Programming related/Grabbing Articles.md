#todo
- [ ] Matching stings from Articles list wth Articles found in Pdf


```python
for i in 
```

- [ ] Creating a new with the same name.md
- [ ] How to read and write files in python.
	- [ ] if found, Match the title in file and create a new `<title>.md` file
	### Reading and writing to text files in Python
	- There are two types of files that can be handled in Python, normal text files and binary files.
		- **Text files:** In this type of file, each line of text is terminated with a special character called EOL (End of line), which is the new line character (`\n`) in Python by default.
		- **Binary files:** In this type of fie, there is no terminator for a line and the data is stored after converting it into machine understandble binary language.
	- Opening, closing, reading and writing data a text file.
#### File Access Mode
- Access modes govern the type of operation spossible in teh opened file.
- It refers to how the file will bes ued once its opened.
- These modes also define the location of the File Handle in the file.
- Files handle is lika a cursor, which defines from where the data has to be read or written in the file.
- There are 6 access modes in python.
- [[Read Only(r)]]
- [[Read and Write(r+)]]
- [[Write only(w)]]
- [[Wrtie and Read(w+)]]
- [[Append Only(a)]]
- [[Append and Read(a+)]]

### Python - How to search for a string in text files?
- from [GeeksforGeeks](https://www.geeksforgeeks.org/python-how-to-search-for-a-string-in-text-files/)

#### Example 1: 
- we are going to search string line by line if the string found then we will print that string and line number
- steps:
	- Open a file
	- set variables index and flag to zero.
	- Run a loop through the file line by line.
	- In that loop check condition suing the 'in' opertor for string preesent in line or not. If found flag to 0.
	- After loop again check condition for the flag is set or not.
		- if string found the print a string and line nubmer otherwise simply print the message 'Sting not found'
	- Close the file.

```python

string1 = 'coding' #we need to make an index that is found in the Constiution of India

#opening a a text file in read only mode
file1 = open('Geeks.txt', "r")

#setting flad and index to 0

flag = 0
index = 0

 # Loop through the file line by line
 
 for line in file1:
 	index + = 1
	
	# checking string is presrnt in line or not.
	if string in line:
		flag = 1
		break

# checking condition for string found or not

if flag == 0:
	print('String', string1, 'Not found')
	
else:
	print('String' , string1, "Found in Line", index)
	
# closing the fiel
file1.close()
```
```shell
String coding Found in Line 5
```

#### Example 2:
- We are just finding srting is present in the file or not.
- steps:
	- Open a file.
	- Read a file and store it in a variable.
	- Check condition using 'in' operator for string present in the file or not.
	- If the condititon true then print the message 'string in found' otherwise print 'string not found'
	- Close a file.