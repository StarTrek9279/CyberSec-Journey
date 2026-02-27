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

## Command: chmod
What it does: Change mode bits / change the permissions of the file 
Syntax: chmod [option] [mode] [file]  
Example: chmod u+x "README.php" 
Useful flags: -R (recursive: applies the change of mode bits of all the files of the specified directory), -v (verbose: gives diagnostic message), -f (suppress error messages)

## Command: mkdir
What it does: Make directory (create folder) 
Syntax: mkdir [option] [directory_name]  
Example: mkdir -p dir1/dir2/dir3
Useful flags: -v (prints verbose msg for each directory created), -p (create parent directory if they dont exist), -m (set permission for new directory)

## Command: rm
What it does: Delete files and directories 
Syntax: rm [option] [directory/file_name]  
Example: rm -i file.txt , rm -r newfolder/
Useful flags: -v (detail of each file as it is deleted), -d (delete empty directory), -r (recurisively delete content inside a directory), -rf (deletes files and directories without any confirmation), -i (interactive mode, prompts user once before deleting multiple files)

## Command: touch
What it does: Create new empty files 
Syntax: touch [option] [file]  
Example: touch file1.txt file2.txt file3.txt
Useful flags: -c (do not create new file), -r (use reference file's timestamp), -t (set a custom timestamp), -m (change modification time only)

## Command: cp
What it does: Used to copy files and directories from one location to another 
Syntax: cp [option] [source_file/dir] [destination_file/dir]  
Example: cp -R folder_src folder_dest
Useful flags: -R (copying directory structure recursively), -i (interactive mode, system warns user before overwriting the destination file), -f (forced copy),
-p (preserves some of the characteristics)

## Command: mv
What it does: Used to move or rename files and directories
Syntax: cp [option] [source_file/dir] [destination_file/dir]  
Example: mv file1.txt <path>/newfolder/
Useful flags: -i (interactive mode, prompts for confirmation), -f (overwrites an existing file without prompting, forced), -n (prevents overwriting), -v (shows the name of each file as it is moved), -u (moves a file only if the source file is newer that the destination file or if the destination file is missing)

## Command: chown
What it does: Change the group/user ownershif of file or directories
Syntax: chown chown [OPTIONS] OWNER[:GROUP] [FILE] 
Example: chown :developer project.py
Useful flags: -R (recursive, applies changes to directories and their contents), -v (shows a message for every file processed), -c (reports changes only when changes are actually made), -h (modifies the symbolic link itself)

## Command: sudo
What it does: Allows a permitted user to execute a command with root user previleges / privileges of other user 
Syntax: sudo [command]  
Example: sudo nano /etc/hosts
Useful flags: -u (run the command as a user other than root), -i (interative login shell as the root user), -s (run a shell with root privileges and preserve current environment), -l (lsit the commands the current user is allowed to run with sudo)

## Command: whoami
What it does: Displays the username associated with the current effective user ID
Syntax: whoami
Example: whoami 
Useful flags: --help ,--version

## Command: ping
What it does: Test reachability of a host on a network and to measure the round trip time
Syntax: ping [option] [destination]  
Example: ping www.google.com
Useful flags: -c (sending a specific number of packets), -i (wait a specified amount of time before sending each packet), -s (specify the size of the packet in byte), -a (play an audible beep sound when reply is received), -4 (force the use of IPv4), -6 (force the use of IPv6)




