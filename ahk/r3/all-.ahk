#SingleInstance, Force
SendMode Input
SetWorkingDir, %A_ScriptDir%

send, {LAlt down}
send, {7 down}
sleep, 100
send, {7 up}
send, {LAlt up}