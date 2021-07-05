- Open the file for writing.
- For existing file, the data is truncated and over-written.
- The handle is positioned at the beginning of the file
- Creates the file, if the file doesn't exists.

### Problem Description

- The program copies the contents of one file and writes it into another.

- Problem Solution
	1. Open one file called `test.txt` in read mode.  
	2. Open another file `out.txt` in write mode.  
	3. Read each line from the input file and write it into the output file.  
	4. Exit.

#### Program/Source Code

Here is source code of the Python Program to copy the contents of one file into another. The program output is also shown below.

```python
with open("test.txt") as f:
    with open("out.txt", "w") as f1:
        for line in f:
            f1.write(line)
```

#### Program Explanation

1. The file test.txt is opened using the open() function using the f stream.  
2. Another file out.txt is opened using the open() function in the write mode using the f1 stream.  
3. Each line in the file is iterated over using a for loop (in the input stream).  
4. Each of the iterated lines is written into the output file.


##### Test Cases
```shell
Case 1:
Contents of file(test.txt): 
Hello world
 
Output(out.text): 
Hello world
 
Case 2:
Contents of file(test.txt): 
Sanfoundry
 
Output(out.text): 
Sanfoundry
```
