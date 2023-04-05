#SingleInstance, Force
SendMode Input
SetWorkingDir, %A_ScriptDir%

send, {LAlt down}
send, {5 down}
sleep, 100
send, {5 up}
send, {LAlt up}