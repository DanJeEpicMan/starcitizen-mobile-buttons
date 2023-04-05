#SingleInstance, Force
SendMode Input
SetWorkingDir, %A_ScriptDir%

send, {b down} 
sleep, 5000
send, {b up}
sleep, 1000
send, {b down} 
sleep, 500
send, {b up}