## Level 11 → 12
Command used: { ssh bandit110@bandit.labs.overthewire.org -p 2220, ls, cat}  
Password found: [7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4]  
Process: [-->the data is ROT-13 rotated copy the data and decode it using ROT-13 on any site ]
What I learned: [->letter substituation cypher ROT-13]

## Level 12 → 13
Command used: { ssh bandit12@bandit.labs.overthewire.org -p 2220}  
Password found: [FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn]  
Process: [-->NO WORDSSSS]

## Level 13 → 14
Command used: { ssh bandit13@bandit.labs.overthewire.org -p 2220, chmod, ssh}  
Password found: [MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS]  
Process: [-->ssh through private key on port 2220 on user@host where host will  be local host ]
What I learned: [->logging into ssh using a private sshkey]

## Level 14 → 15
Command used: { ssh bandit14@bandit.labs.overthewire.org -p 2220, nc, nmap}  
Password found: [8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo]  
Process: [-->nmap can be used to scan open ports on local host, nc 127.0.0.1 30000]
What I learned: [->use of nmap for port scanning and connecting to a local host using netcat]

## Level 15 → 16
Command used: { ssh bandit15@bandit.labs.overthewire.org -p 2220, ncat}  
Password found: [kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx]  
Process: [--> using ncat to connect to local host port 30001 using ssl encryption ]
What I learned: [->connection to a ip:port using encryption with the help of ncat --ssl]

## Level 16 → 17
Command used: { ssh bandit16@bandit.labs.overthewire.org -p 2220, nmap,ncat}  
Password found: [EReVavePLFHtFlFsjn3hyzMlvSuSAcRD]  
Process: [--> use nmap -sV <locahostip> <start_port>-<end_port> to scan the port in the given range--> check which ports are open and are listening to encrypted message and not sending "echo" output --> nc ]
What I learned: [->using nmap to scan a specific port range]

## Level 17 → 18
Command used: { ssh bandit17@bandit.labs.overthewire.org -p 2220, ls, diff}  
Password found: [x2gLTTjFwMOhQ8oWNbMN362QKxfRqGlO]  
Process: [-->use diff command to find what has been changed between 2 different versions of the same file ]
What I learned: [->using diff command to find the difference between 2 files]

## Level 18 → 19
Command used: { ssh bandit18@bandit.labs.overthewire.org -p 2220, ls, cat, ssh}  
Password found: [cGWpMaKXVwDUNgPAVJbWYuGHVn9zl3j8]  
Process: [-->using command on a ssh server without logging in but with command send through the ssh command itself ]
What I learned: [->using commands directly by using ssh (without being logged in)]

## Level 19 → 20
Command used: { ssh bandit19@bandit.labs.overthewire.org -p 2220, ls, cat}  
Password found: [0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO]  
Process: [-->run the file one time to check how it works then --> the executable file takes a command as input and executes it using privileges of another user]
What I learned: [->execution of files uising command line argument]

## Level 20 → 21
Command used: { ssh bandit20@bandit.labs.overthewire.org -p 2220, nmap, nc, tmux}  
Password found: [EeoULMCra2q0dSkYj561DX7s1CpBuOBt]  
Process: [-->open a listening port using nc --> connect to the port using the ./suconnect program --> send the password from the listening port ]
What I learned: [->how to run multiple instances of command line in one using tmux --> how to start a listening port]