#SingleInstance, Force
SendMode Input
SetWorkingDir, %A_ScriptDir%

loop, 100 ; 1k = 15 sec
{
    send, {WheelDown down}
    sleep, 1
}
send, {WheelDown up}