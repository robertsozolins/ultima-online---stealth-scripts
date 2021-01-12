import time

# Search text in gump, if text exists, press button. 
def textingump(text: str = "None", button: int = None, timeout: int = 60) -> bool:
    found = False
    gumptimer = time.time()

    while not found and gumptimer + timeout > time.time():
        for i in range(GetGumpsCount()):
            gump = GetGumpInfo(i)
            gumpnumber = i
            if len(gump['XmfHTMLGumpColor']):
                for x in gump['XmfHTMLGumpColor']:
                    if text.upper() in GetClilocByID(x['ClilocID']).upper():
                        found = True
                        break
            else:
                if len(gump['Text']):
                    for x in gump['Text']:
                        if text.upper() in x[0].upper():
                            found = True
                            break
        Wait(50)

    if found and button is not None:
        NumGumpButton(gumpnumber, button)

    return found