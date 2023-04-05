#SingleInstance, Force
SendMode Input
SetWorkingDir, %A_ScriptDir%

send, {LAlt down}
send, {6 down} 
sleep, 100
send, {6 up}
send, {LAlt up}