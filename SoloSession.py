import psutil
import sys
import time

def ac():
    if len(sys.argv) == 2 and sys.argv[1] == "-ac":
        return
    else:
        return input("Press enter to exit...")

def main():
    gta = None

    for id in psutil.pids():
        p = psutil.Process(id)

        if p.name() == "GTA5.exe":
            gta = p
            break
    
    if gta == None:
        print("Could not find GTA.EXE process, Please have GTA open and be in a public online session.")
        print("Otherwise open an issue at github.com/oliverjrose99/GTASoloSession")
        
        return ac()

    print("Found GTA.EXE process, starting suspend...")
    gta.suspend()
    
    for i in reversed(range(10)):
        print((i+1), end=" ", flush=True)
        time.sleep(1)

    gta.resume()
    print("\n\nYou should now be in a GTA Online public solo session.")
    print("If not please open an issue at github.com/oliverjrose99/SoloSessionExe")
    
    return ac()


if __name__ == "__main__":
    main()
