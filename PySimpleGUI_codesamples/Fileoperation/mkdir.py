from pathlib import Path
cd = Path.cwd()
newfolderpath = cd/'新しいフォルダ'
Path(newfolderpath).mkdir()