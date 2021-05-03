@REM Converter for windows bulk 

cd .\Input\


 for /R %%f in (*.vsv) do (
 "python.exe ..\converter.py" "%%f" "%%f.kml"
 )