from cx_Freeze import setup, Executable

executables = [
    Executable(
        "main.py",
        icon="icon.ico"  # caminho do ícone
    )
]

build_options = {
    "packages": ["pygame"],
    "include_files": ["asset"]
}

setup(
    name="MountainShooter",
    version="1.0",
    description="Mountain Shooter app",
    options={"build_exe": build_options},
    executables=executables
)
