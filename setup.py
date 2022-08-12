import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["cx_Freeze"],
                     "excludes": [],
                     "bin_path_excludes": []}
# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="mkfilename",
    version="0.1",
    description="Utility to generate filenames for archiving.",
    options={"build_exe": build_exe_options},
    executables=[Executable("mkfilename.py", base=base)],
)