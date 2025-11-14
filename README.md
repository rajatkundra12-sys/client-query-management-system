# Client Query Management System – Documentation

## Project Overview

Client Query Management System ek modular Python + Streamlit web app hai, jo support queries ko manage karne ke liye bana hai. Clients apni queries submit kar sakte hain aur support team unko dashboard par view, filter, aur resolve kar sakti hai. MySQL database ka use hota hai user aur queries data ke liye, saath hi login, registration, and security functionalities bhi hain.

## Files and Their Roles

### streamlit.py
Main entry script. User session, routing (login, registration, client/support dashboard), and authentication ko manage karta hai.

### register.py
Streamlit form se naye user ki registration ko handle karta hai (Client/Support Team role) aur backend me user create services ko call karta hai.

### login.py
Login form ko render karta hai; provided credentials validate karke user ko dashboard par le jata hai.

### logout.py
User session ko end karta hai aur logout functionality deta hai.

### Client.py
Client dashboard (add new query form, apni queries ka status dekhna) ke liye logic, UI aur data interaction implement karta hai.

### Support.py
Support side ka dashboard jahan sabhi queries aa jati hain, unko search/filter/resolve/edit kiya ja sakta hai. Status change bhi possible hai.

### Trackquery.py
Simple page/script jo client ki current queries ko list karta hai, unka status dikhata hai.

### query_services.py
Back-end CRUD operations for queries: new query ko insert karna, sabhi ya specific queries fetch karna, status update, etc.

### user_services.py
User data se judhe operations: user create, authenticate, etc.

### db.py
DB connection utilities. Har query execution ke liye DB connect/disconnect ki logic yahi hai.

### security.py
Password ko securely hash karne (bcrypt) aur verify karne ke helper functions.

### query_portal_users.sql
Users table ki SQL schema aur example users ka dump.

### query_portal_queries.sql
Queries table ki SQL schema aur example dummy data.

## Project Folder Structure
/project-root/
streamlit.py
register.py
login.py
logout.py
Client.py
Support.py
Trackquery.py
query_services.py
user_services.py
db.py
security.py
query_portal_users.sql
query_portal_queries.sql
requirements.txt


## How to Run

1. Database setup ke liye SQL files ko MySQL me import karein.
2. Python environment set up karein aur sabhi requirements install karein:
3. App start karne ke liye run karein:
4. Web browser me app open ho jayega. Register/login karein aur workflow ko explore karein.

## Workflow Summary

Client registration/login ke baad apni queries add kar sakta hai, status dekh sakta hai (Open/Closed).  
Support user login karke saari queries dekh sakta hai, unki details edit kar sakta hai, aur status (Open/Closed) update kar sakta hai.  
Passwords secure hashing ke saath store hote hain.  
Data tables ka schema SQL files me diya hai; dono ka foreign key relationship maintain hota hai.



