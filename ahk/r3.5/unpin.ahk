#SingleInstance, Force
SendMode Input
SetWorkingDir, %A_ScriptDir%

send, {LAlt down}
send, {1 down}
sleep, 100
send, {1 up}
send, {LAlt up}