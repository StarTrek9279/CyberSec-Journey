## Command: ls
What it does: Lists files and directories  
Syntax: ls [options] [path]  
Example: ls -la /home/user  
Useful flags: -l (long format), -a (show hidden), -h (human readable sizes)

## Command: pwd
What it does: Prints name of the current working directory  
Syntax: pwd [options]  
Example: pwd  

## Command: cat
What it does: Concatenate file and print the contents of the file  
Syntax: cat [options] [file]  
Example: cat data.txt (prints the content of data.txt in std o/p), cat data.txt - file.txt (prints content of data.txt then waits for user input then prints content of file.txt)
Useful flags: -n (number all output lines), -T (display tab characters)

## Command: grep
What it does: Prints line that matches pattern  
Syntax: grep [options] [path]  
Example: grep -la /home/user  
Useful flags: -F(interpret as fixed string not pattern), -i (ignore case), -v (invert match {print the lines which do not match}), -c (count of matching line)

## Command: find
What it does: Search for file in a directory hierarchy  
Syntax: find [options] [path] [expression] 
Example: find ./foldernew -name "README.txt"  
Useful flags: -name (to look for the file with a particular name), -empty (search for empty files in directory), -perm (to identify file with the mode bits)

## Command: file
What it does: Determine File type  
Syntax: file [options] [filename]  
Example: file "README.txt"
Useful flags: -b (file type in brief mode), * (displays all file's file type), -i (to view mimetype of file)

## Command: cd
What it does: Change the working directory  
Syntax: cd [directory_name]  
Example: cd "new folder"
Useful flags: .. (go to previous directory), \ (can be used to escape the space (example: cd new\ folder ))

## Command: du
What it does: Change the working directory  
Syntax: du [option] [directory/file]  
Example: du -sh /var/log
Useful flags: -0 (end each o/p line with NULL), -c (shows the total disk usage), -h (displays size in human readable format), -s (provides a summary of disk usage)

## Command: man
What it does: Change the working directory  
Syntax: man [option] [command]  
Example: man man
Useful flags: -f (displays concise one line description of command), -a (display all matching man page), -k or --apropos (search for command related to a keyword)

## Command: sort
What it does: Change the working directory  
Syntax: sort [option] [file]  
Example: sort -u "README.txt" 
Useful flags: -o (specifies output file for the sorted data), -r (sorts data in reverse order), -n (sort a file numerically), -nr (numrically and reverese sort),
-c (checks if file is already sorted), -u (sorts and removes duplicate lines)




