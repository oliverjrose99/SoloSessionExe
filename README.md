# SoloSessionExe
A small tool to help put you in a GTA Online solo public session.

## Usage
1. [Download](https://github.com/oliverjrose99/SoloSessionExe/releases) the tool
2. Start GTA and join an online public session
3. Run the tool and wait about 10 seconds
4. Profit? You will be in a solo public session

When using a shortcut to the exe, you can append `-ac` to the target (in the properties) which will cause the window to auto close once completed.

If you close the tool while GTA's suspended, it will remain suspended until you resume it in Resource Monitor or you close and reopen GTA. This may be fixed in a future version.

## FAQ

### How does it work?
This tool uses a common public method which is to suspend the GTA process for a few seconds and then resume it. This method is also known as the "Task Manager" or "Resource Monitor" method.

### Will this work for XBox/PlayStation?
No, this is a PC only tool and method. See the [GTA Online Mega Guide](https://www.reddit.com/r/gtaonline/comments/agu9aj/the_gta_online_mega_guide/) made by the r/gtaonline subreddit for other methods and general tips and tricks.

### Will I get banned for using this?
The tool doesn't modify any memory or files, and the method used (as of 01/07/19) wont get you banned. R* still allows solo public sessions and doesn't kick you out of them, so use them to your advantage.

### How long does it last for?
How long you will stay solo for varies quite a lot as it is still a public session and others can get put in by the R* servers. There is no limit as to how many times you can use the method/tool. Personally I've had sessions last between 20 minutes and 3 hours.

### The tool doesn't work?
* Try running the tool in admin mode (right click, "Run As Administrator")
* Make sure you are in a public online session before using the tool
* Open a Github issue and make sure to add any odd details about your system/setup

## Licences / Libraries
This project is under the MIT license which can be found in the licence file. The project also uses [psutil](https://github.com/giampaolo/psutil) whos license can be found in the same file. 