## Level 0 → 1
Command used: { ssh bandit0@bandit.labs.overthewire.org -p 2220, ls, cat}  
Password found: [ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If]  
Process: [--> ls used to list the files in the directory --> cat used to display the content of the readme file]
What I learned: [-> how to list the files in the given directory and how to display the contents of the file ]

## Level 1 → 2
Command used: { ssh bandit1@bandit.labs.overthewire.org -p 2220, ls, cat}  
Password found: [263JGJPfgU6LtdEvgfWU1XP5yac29mFx]  
Process: [--> ls used to list the files in the directory --> cat ./- used to display the contents of the file with a dashed filename ]
What I learned: [-> how to open a file with a dash in its name while using a terminal ]

## Level 2 → 3
Command used: { ssh bandit2@bandit.labs.overthewire.org -p 2220, ls, cat}  
Password found: [MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx]  
Process: [--> ls used to list the files in the directory -->backslash "\" just before the spaces can be used to escape the space (cat ./--spaces\ in....) ]
What I learned: [-> opening a file with space and dash in its name]

## Level 3 → 4
Command used: { ssh bandit3@bandit.labs.overthewire.org -p 2220, ls, cat}  
Password found: [2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ]  
Process: [--> ls -al used to list all the files in the directory(even the hidden files) -->cd inhere to enter the hidden folder then used cat ./<filename> see the contents of the file]
What I learned: [-> listing a hidden directory using ls]

## Level 4 → 5
Command used: { ssh bandit4@bandit.labs.overthewire.org -p 2220, ls, cat, file}  
Password found: [4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw]  
Process: [-->cd inhere to enter the folder --> ls to check the contents of the folder -> check individual files file type using (file ./<file_name>) or use (file ./*) to see the file type of all the files in the directory --> use cat to see the contents of the file which is ASCII text type]
What I learned: [-> how to check the type of file using the file command (individually and all at once)]

## Level 5 → 6
Command used: { ssh bandit5@bandit.labs.overthewire.org -p 2220, ls, cat, du, grep}  
Password found: [HWasnPhtq9AVKe0dmk45nxy20cvUa6EG]  
Process: [-->cd inhere to enter the folder --> ls to check the contents of the folder ->du -a -b to list all the files and their size recursively from all the folders
--> du -a -b | grep 1033 to pick the output of du -a -b where the size is 1033 bytes -> cd to enter the directory and cat used to check the contents of the file]
What I learned: [-> how to list files recursively in a folder (du) --> how to list files along with their size (recursively) --> using | (pipe) to pipe down the output of one command as the input of another --> using grep to find a text (word or line) in a a stream of output (prints the whole line)