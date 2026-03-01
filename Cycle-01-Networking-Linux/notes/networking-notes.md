# Networking Notes

---

# 📚 OSI Model

The OSI model has **7 layers**

| Layer No | Layer Name | Function |
|----------|------------|----------|
| 7 | Application | Provides network services to end user applications (HTTP,FTP). |
| 6 | Presentation | Responsible for data translation, encryption and compression. |
| 5 | Session | Provides services to presentation layer to organize dialogue and manage data exchange (establish, manage and terminate sessions). |
| 4 | Transport | Defines services to segment, transfer and reassemble data for individual communication (end to end communication, segmentation and reliability (UDP/TCP)). |
| 3 | Network | Responsible for logical addressing (IP addressing) and routing of packets between networks. |
| 2 | Data Link | Describes methods for data frame exchange, MAC addressing and error detection on local network. |
| 1 | Physical | Describes means of transmission of raw bits over the physical medium. |

---

# 🔹 TCP vs UDP
-TCP :- Transmission Control Protocol
-UDP :- User Datagram Protocol

| S.No.| Attribute | TCP | UDP |
|------|-----------|-----|-----|
| 1 | Connection Type | Connection oriented uses three way handshake (syn -> syn/ack -> ack) | Connectionless no handshake  |
| 2 | Reliability | Sends ACK for received packets and provides retransmission for dropped/lost packets | No ACK for received packets and no retransmission of dropped/lost packets |
| 3 | Ordering | Ensures Data arrives in Order and is reassembled with the help of Sequence number | No guarantee of packet being received in order |
| 4 | Error Handling | Error Detection and recovery  | Basic error detection only (checksum) |
| 5 | Speed | Slower due to reliability and error checks | Faster due to less overhead and error checks |
| 6 | Header Size | Larger (20-60 bytes) | Smaller (8 bytes)  |
| 7 | Broadcast and Multicast | Does not support | Does support |
| 8 | Concern | Focuses on Data reliability | Focuses on real-time data Transmission |
| 9 | Use Case | HTTP, HTTPS, FTP, SSH, Email | DNS, Streaming, Gaming, VoIP |

---

# 🔹 Common protocols 

| Protocol | Port Number | Transport Protocol | Purpose |
|----------|-------------|--------------------|---------|
| HTTP | 80 | TCP | Web Browsing |
| HTTPS | 443 | TCP | Secure Web Browsing |
| FTP | 21 | TCP | File Transfer |
| SFTP | 22 | TCP | Secure File Transfer |
| SSH | 22 | TCP | Secure Remote Access |
| Telnet | 23 | TCP | Remote Access |
| SMTP | 25 | TCP | Sending Email |
| DNS | 53 | UDP/TCP | Domain Name Resolution |
| DHCP | 67/68 | UDP | Automatic IP assignment |
| POP3 | 110 | TCP | Receiving Email |
| RDP | 3389 | TCP | Remote Desktop |

---

# 🔹 Working Of DNS

1. User requests a website on the browser application.
1. Browser checks local cache (browser cache, OS cache and Local Host file) for the IP related to the website , if found then returns the IP to load the website, else goes to the next step.
1. Request is send to the Recursive Resolver (ISP or Public DNS (8.8.8.8:google,1.1.1.1:cloudflare)) for address resolution, if found then returns the IP to the client to load the website, else goes to the next step.
1. Request is sent to the Root DNS server, which responds with the address of the appropriate TLD server.
1. Recursive Resolver receives the Authoritative name server's address from the TLD server (.com, .gov, .net, .edu, .org etc) and searches for the IP address for the requested domain. 
1. Resolver sends IP back to the browser, browser now connects to the IP using HTTP/HTTPS.

---