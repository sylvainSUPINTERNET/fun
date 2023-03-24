    # app = Application(backend="uia").start("notepad.exe")
    # app.UntitledNotepad.type_keys("%FX")

    # pid = list()
    # for proc in psutil.process_iter(['pid', 'name']):

    #     if proc.info["name"] == "MinecraftLauncher.exe":
    #         pid.append(proc.info["pid"])
    
    
    
    # for i in pid:
    #     try:
    #         print(f"try for PID : {i}")
    #         app = Application(backend="win32").connect(process=i)
    #         app.top_window().set_focus()
    #         break;
    #     except RuntimeError as e:
    #         print(e)
    #     except TimeoutError as te:
    #         print(te)
    #     except ProcessLookupError as pl:
    #         print(pl)
    #     except Exception as ex:
    #         print(ex)

    # app = Application()
    # app.start(r'C:\Program Files (x86)\Minecraft\MinecraftLauncher.exe')
    
    
    # app = Application(backend="uia").connect(title_re=PROCESS_GAME_TITLE, pid=15756)
    # app.start()
