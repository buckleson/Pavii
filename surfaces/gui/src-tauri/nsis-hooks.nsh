!macro NSIS_HOOK_PREINSTALL
  DetailPrint "Closing running PAVii processes before installing..."
  nsExec::ExecToLog 'taskkill /IM "PAVii.exe" /T /F'
  nsExec::ExecToLog 'taskkill /IM "PAVii-desktop.exe" /T /F'
  nsExec::ExecToLog 'taskkill /IM "openworker-server.exe" /T /F'
  nsExec::ExecToLog 'taskkill /IM "OpenWorker.exe" /T /F'
  Sleep 1000
!macroend
