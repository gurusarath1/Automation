@if (@CodeSection == @Batch) @then


@echo off

rem Use %SendKeys% to send keys to the keyboard buffer
set SendKeys=CScript //nologo //E:JScript "%~F0"

rem Start notepad program
start notepad


timeout 5
%SendKeys% "Hello, world!{ENTER}"
%SendKeys% "{UP}--->{END}<---"
%SendKeys% "{ENTER}"
timeout /T 2
%SendKeys% "exit{ENTER}"

goto :EOF


@end


// JScript section

var WshShell = WScript.CreateObject("WScript.Shell");
WshShell.SendKeys(WScript.Arguments(0));