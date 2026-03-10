Option Explicit

Dim oShell, oFSO, sBase, oExec, sResult
Dim sCmd, i

Set oShell = CreateObject("WScript.Shell")
Set oFSO = CreateObject("Scripting.FileSystemObject")

sBase = "C:\Users\DELL\Documents\projet\immo"
oShell.CurrentDirectory = sBase

' Try Node.js first, then Python
Dim attempts(1)
attempts(0) = "node.exe """ & sBase & "\master_setup.js"""
attempts(1) = "python.exe """ & sBase & "\setup_backend.py"""

Dim succeeded : succeeded = False

For i = 0 To 1
    sCmd = attempts(i)
    On Error Resume Next
    Set oExec = oShell.Exec("cmd.exe /c " & sCmd & " 2>&1")
    If Err.Number = 0 Then
        Dim lines : lines = ""
        Do While Not oExec.StdOut.AtEndOfStream
            lines = lines & oExec.StdOut.ReadLine() & vbCrLf
        Loop
        If oExec.ExitCode = 0 Then
            succeeded = True
            MsgBox "Setup completed successfully!" & vbCrLf & vbCrLf & Left(lines, 2000), 64, "ImmoExpert Setup"
            Exit For
        End If
    End If
    On Error GoTo 0
Next

If Not succeeded Then
    ' Fallback: run python create_dirs.py for frontend
    oShell.Exec "cmd.exe /c python.exe """ & sBase & "\create_dirs.py"""
    
    If Not oFSO.FolderExists(sBase & "\backend") Then
        MsgBox "Automatic setup could not run." & vbCrLf & vbCrLf & _
               "Please open a Command Prompt and run:" & vbCrLf & vbCrLf & _
               "  cd /d " & sBase & vbCrLf & _
               "  node master_setup.js" & vbCrLf & vbCrLf & _
               "  or: python setup_backend.py && python create_dirs.py", _
               16, "ImmoExpert Setup"
    End If
End If

Set oExec = Nothing
Set oFSO = Nothing
Set oShell = Nothing
