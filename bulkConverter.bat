@REM Converter for windows bulk 

cd .\Input\


 for /R %%f in (*.vsv) do (
 "python.exe ..\converter.py" -compress LZW 
    -colorspace Gray -colors 32 "%%f" "%%f"
 )