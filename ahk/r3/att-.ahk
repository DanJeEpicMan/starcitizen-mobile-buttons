#SingleInstance, Force
SendMode Input
SetWorkingDir, %A_ScriptDir%

send, {LAlt down}
send, {4 down}
sleep, 100
send, {4 up}
send, {LAlt up}