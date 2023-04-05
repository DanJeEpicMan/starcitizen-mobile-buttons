from flask import Flask, request, render_template
import pyautogui
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        switch_name = request.form['switch']
        print(switch_name)
        if switch_name == 'Call':
            os.system('start C:/Users/danie/OneDrive/Desktop/code/flask/new_project/venvironment/ahk/r1/call.ahk')
        if switch_name == 'Plan TO':
            os.system('start C:/Users/danie/OneDrive/Desktop/code/flask/new_project/venvironment/ahk/r1/planto.ahk')
        if switch_name == 'Stat TO':
            os.system('start C:/Users/danie/OneDrive/Desktop/code/flask/new_project/venvironment/ahk/r1/statto.ahk')
        if switch_name == 'Auto LD':
            os.system('start C:/Users/danie/OneDrive/Desktop/code/flask/new_project/venvironment/ahk/r1/autold.ahk')
        if switch_name == '180 Turn':
            os.system('start C:/Users/danie/OneDrive/Desktop/code/flask/new_project/venvironment/ahk/r1/180turn.ahk')

        if switch_name == 'Max spd':
            os.system('start C:/Users/danie/OneDrive/Desktop/code/flask/new_project/venvironment/ahk/r2/maxspd.ahk')
        if switch_name == 'Scr Dwn':
            os.system('start C:/Users/danie/OneDrive/Desktop/code/flask/new_project/venvironment/ahk/r2/maxtru.ahk')
        if switch_name == 'QU Calc':
            os.system('start C:/Users/danie/OneDrive/Desktop/code/flask/new_project/venvironment/ahk/r2/qucalc.ahk')

        if switch_name == 'Att':
            os.system('start C:/Users/danie/OneDrive/Desktop/code/flask/new_project/venvironment/ahk/r3/att.ahk')
        if switch_name == 'Att-':
            os.system('start C:/Users/danie/OneDrive/Desktop/code/flask/new_project/venvironment/ahk/r3/att-.ahk')

        if switch_name == 'Host':
            os.system('start C:/Users/danie/OneDrive/Desktop/code/flask/new_project/venvironment/ahk/r3/host.ahk')
        if switch_name == 'Host-':
            os.system('start C:/Users/danie/OneDrive/Desktop/code/flask/new_project/venvironment/ahk/r3/host-.ahk')

        if switch_name == 'Frnd':
            os.system('start C:/Users/danie/OneDrive/Desktop/code/flask/new_project/venvironment/ahk/r3/frnd.ahk')
        if switch_name == 'Frnd-':
            os.system('start C:/Users/danie/OneDrive/Desktop/code/flask/new_project/venvironment/ahk/r3/frnd-.ahk')

        if switch_name == 'All':
            os.system('start C:/Users/danie/OneDrive/Desktop/code/flask/new_project/venvironment/ahk/r3/all.ahk')
        if switch_name == 'All-':
            os.system('start C:/Users/danie/OneDrive/Desktop/code/flask/new_project/venvironment/ahk/r3/all-.ahk')

        if switch_name == 'Pin':
            os.system('start C:/Users/danie/OneDrive/Desktop/code/flask/new_project/venvironment/ahk/r3.5/unpin.ahk')
        if switch_name == 'Hail':
            os.system('start C:/Users/danie/OneDrive/Desktop/code/flask/new_project/venvironment/ahk/r3.5/unpin.ahk')
        if switch_name == 'UnPin':
            os.system('start C:/Users/danie/OneDrive/Desktop/code/flask/new_project/venvironment/ahk/r3.5/unpin.ahk')

        if switch_name == 'PingL':
            os.system('start C:/Users/danie/OneDrive/Desktop/code/flask/new_project/venvironment/ahk/r4/pingl.ahk')
        if switch_name == 'Ping':
            os.system("start C:/Users/danie/OneDrive/Desktop/code/flask/new_project/venvironment/ahk/r4/ping.ahk")
        if switch_name == 'PingM':
            os.system('start C:/Users/danie/OneDrive/Desktop/code/flask/new_project/venvironment/ahk/r4/pingm.ahk')
        if switch_name == 'Noise':
            os.system("start C:/Users/danie/OneDrive/Desktop/code/flask/new_project/venvironment/ahk/r4/noise.ahk")
        if switch_name == 'Decoys':
            os.system('start C:/Users/danie/OneDrive/Desktop/code/flask/new_project/venvironment/ahk/r4/decoys.ahk')

        if switch_name == 'MisNext':
            os.system('start C:/Users/danie/OneDrive/Desktop/code/flask/new_project/venvironment/ahk/r5/misnext.ahk')
        if switch_name == 'MisBefore':
            os.system('LMB')
        if switch_name == 'Fire':
            os.system('start C:/Users/danie/OneDrive/Desktop/code/flask/new_project/venvironment/ahk/r5/fire.ahk')
        if switch_name == 'MisMore':
            os.system('start C:/Users/danie/OneDrive/Desktop/code/flask/new_project/venvironment/ahk/r5/mismore.ahk')
        if switch_name == 'MisLess':
            os.system('g')

        if switch_name == 'Hurston':
            os.system('start C:/Users/danie/OneDrive/Desktop/code/flask/new_project/venvironment/ahk/r6/hurston.ahk')
        if switch_name == 'Arial':
            os.system('start C:/Users/danie/OneDrive/Desktop/code/flask/new_project/venvironment/ahk/r6/arial.ahk')
        if switch_name == 'Aberdeen':
            os.system('start C:/Users/danie/OneDrive/Desktop/code/flask/new_project/venvironment/ahk/r6/aberdeen.ahk')
        if switch_name == 'Magda':
            os.system('start C:/Users/danie/OneDrive/Desktop/code/flask/new_project/venvironment/ahk/r6/magda.ahk')
        if switch_name == 'Ita':
            os.system('start C:/Users/danie/OneDrive/Desktop/code/flask/new_project/venvironment/ahk/r6/ita.ahk')

        if switch_name == 'ArcCorp':
            os.system('start C:/Users/danie/OneDrive/Desktop/code/flask/new_project/venvironment/ahk/r6/arccorp.ahk')
        if switch_name == 'Lyria':
            os.system('start C:/Users/danie/OneDrive/Desktop/code/flask/new_project/venvironment/ahk/r6/lyria.ahk')
        if switch_name == 'Wala':
            os.system('start C:/Users/danie/OneDrive/Desktop/code/flask/new_project/venvironment/ahk/r6/wala.ahk')

        if switch_name == 'Crusader':
            os.system('start C:/Users/danie/OneDrive/Desktop/code/flask/new_project/venvironment/ahk/r6/crusader.ahk')
        if switch_name == 'Callin':
            os.system('start C:/Users/danie/OneDrive/Desktop/code/flask/new_project/venvironment/ahk/r6/callin.ahk')
        if switch_name == 'Daymar':
            os.system('start C:/Users/danie/OneDrive/Desktop/code/flask/new_project/venvironment/ahk/r6/daymar.ahk')
        if switch_name == 'Yela':
            os.system('start C:/Users/danie/OneDrive/Desktop/code/flask/new_project/venvironment/ahk/r6/yela.ahk')

        if switch_name == 'MicroTech':
            os.system('start C:/Users/danie/OneDrive/Desktop/code/flask/new_project/venvironment/ahk/r6/microtech.ahk')
        if switch_name == 'Calliope':
            os.system('start C:/Users/danie/OneDrive/Desktop/code/flask/new_project/venvironment/ahk/r6/calliope.ahk')
        if switch_name == 'Cilo':
            os.system('start C:/Users/danie/OneDrive/Desktop/code/flask/new_project/venvironment/ahk/r6/cilo.ahk')
        if switch_name == 'Euterpe':
            os.system('start C:/Users/danie/OneDrive/Desktop/code/flask/new_project/venvironment/ahk/r6/euterpe.ahk')

    return render_template('index.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0')
