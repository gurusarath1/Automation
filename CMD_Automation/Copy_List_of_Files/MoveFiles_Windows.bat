echo [CopyOperationInitiated] >> CopyFiles_log.txt
set arg1=%1
mkdir Copied

for /F "tokens=*" %%A in (FileList.txt) do (
echo %%A>> CopyFiles_log.txt
copy %%A Copied>> CopyFiles_log.txt
echo ==========>> CopyFiles_log.txt
)