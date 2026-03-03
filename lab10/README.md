# Lab 10: NGINX Web Server Configuration

## 1. Concepts Overview
- **Web Server**: Served static HTML content on port 8000.
- **Reverse Proxy**: NGINX acts as an intermediary for requests from clients to other servers.
- **Load Balancing**: Distributing network traffic across several servers to ensure efficiency.

## 2. Practical Implementation
1. **HTML Creation**: Developed an 'index.html' to serve as the entry point.
2. **Configuration**: Created a server block in '/etc/nginx/sites-available/'.
3. **Port Binding**: Set the server to listen on port 8000 instead of the default 80.
4. **Testing**: Verified configuration using 'sudo nginx -t'.

## 3. Results
The server successfully hosts the content at http://localhost:8000.

---
**Performed by:** Kaiyrkul
