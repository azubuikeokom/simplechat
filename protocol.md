# SimpleChat Protocol
The simplechat protocol is meant to make chat services pretty easy unlike the well known protocols in the world. It is meant to make design and implementation easy. It is designed to be extended

## How it works
1. Chat gets authenticated. See section to understand how to integrate different authentication servers
2. After authentication, chat's presense is registered in active connections
3. Chat arrives, data is parsed, if poorly formed, return 4xx error of the right kind
4. Chat is sent to finder to check if receipient's socket is active on chats and if yes, data is sent 
5. If receipient is not active, send message to chat-log for short term storage - 7 days retention by default
6. 

### Gateway
Takes all requests, routes to connection services

### Authentication
Chats are first authenticated and a JWT key with very long expiration is generated and returned to user

### Connection
Users joining chat are registered and save to a NoSQL database as active connections

### Parser
Parses requests and discardes poorly formed requests


### Finder
Checks the connection table for active connections to identify the socket hash of the client


## Features
1. As users join, the online section gets populated with users joining

### Message Structure

    sender: simplechat:okom@simplechat.com
    receipient: simplechat:peter@simplechat.com
    content-type: application/json
    timestamp: 10:12:23 05-03-2026
    key: 8454kjfirt945dfefdfdfdf
    expire: "experimental"

    hello there i trust you are doing
    ok. I miss you

