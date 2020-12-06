$invocation = (Get-Variable MyInvocation).Value
$directorypath = Split-Path $invocation.MyCommand.Path
$executionpath = Split-Path $directorypath


$files = Get-ChildItem -Path $executionpath

foreach($file in $files){
    if($file.Name -like "*.py"){
        $task_string = "Running " + $file.Name + "........"
        Write-Output $task_string
        python $file
        Write-Output $file.Name + " task done."
    }
}