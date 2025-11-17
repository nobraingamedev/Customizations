Compress-Archive -Path "C:\Users\shiva\OneDrive\Documents\Obsidian-Notes\*" -DestinationPath "C:\Users\shiva\Desktop\Obsidian-Notes.zip" -Force

rclone copy "C:\Users\shiva\Desktop\Obsidian-Notes.zip" "gdrive:ObsidianBackupRAR" --progress --delete-excluded --drive-chunk-size=64M

cd "C:\Users\shiva\Desktop\"

Remove-Item .\Obsidian-Notes.zip

Write-Host "Press Enter to exit..."
$Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyUp") | Out-Null
Exit