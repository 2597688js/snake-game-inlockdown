import cx_Freeze

executables = [cx_Freeze.Executable("SnakeGame.py")]

cx_Freeze.setup(
    name="Snake game",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["gamelogo.jpg","gamebg.jpg","gameover.png","back.mp3","gameover.mp3"]}},
    executables = executables

    )