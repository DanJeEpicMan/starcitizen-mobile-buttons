#SingleInstance, Force
SendMode Input
SetWorkingDir, %A_ScriptDir%

send, i
sleep 2000
send, {space down} 
sleep, 3000
send, {space up}
send, {NumPad8 down}
sleep, 2000
send, {NumPad8 up}
send, c