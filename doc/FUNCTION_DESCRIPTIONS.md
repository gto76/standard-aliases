Commands
========
**sus** | `sudo pm-suspend`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1192-L1194) | Suspend computer.
**vimode** | `set -o vi` | Change bash line editing to vi mode.
**p** | `if [[ $# -eq 0 `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L416-L422) | Print working directory or path to file.
**lla** | `__listOrDisplay`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L204-L207) | List or display all directory contents in pager using medium listing format.
**......** | `___goUpNumberOf`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L330-L332) | Go up five directories.
None**sn** | `sudo nano --und`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L787-L789) | Edit file with nano as super user.
**loc, linesOfCode** | `rootDir="$PWD"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L963-L979) | Count lines in files with extension in working and subdirectories.
**switch** | `tempFile=$(mkte`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L402-L407) | Switch contents of files.
**temp, temperature** | `acpi -t` | Print temperature of cpu.
**sm, sle** | `sudo less --RAW`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L761-L763) | Display text or file in pager as super user.
**hib** | `sudo pm-hiberna`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1187-L1189) | Hibernate computer.

###  Procesess 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**rb, runInBackground** | `nohup "$@" &>/d`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L451-L453) | Run command in background.
**wcw, countWords** | `wc -w "$@"` | Count words.
**n, nano1** | `nano --undo --a`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L672-L674) | Edit file with nano.
**bk, backup** | `sudo cp --prese`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L397-L399) | Backup file.
None**cpdir** | `cp --interactiv`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L371-L373) | Copy directories safely.
**pgrep1** | `pgrep --list-na`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L895-L897) | Find processes with part of name.
**poweroff** | `sudo poweroff` | Shut down computer.

###  History 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**wlan** | `sudo iwlist wla`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1815-L1825) | Print wireless networks in range.
**grep1** | `grep --color=au`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1019-L1021) | Print lines containing pattern.
**allInstalled, allPackages** | `dpkg --get-sele`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1329-L1333) | Print all installed packages.
**tt** | `gtypist "$@"` | Start typing tutor.
**te, terminal** | `x-terminal-emul`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L554-L556) | Open new terminal with same working directory.
**lll** | `___displayOutpu`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L194-L197) | List or display directory contents in pager using long listing format.
**mua** | `tmux attach "$@`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1114-L1116) | Run terminal multiplexer and attach to last session.
**z** | `___setVolumeTo `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1878-L1880) | Decrease volume by six decibels.

###  Misc 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**....** | `___goUpNumberOf`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L322-L324) | Go up three directories.
**cloneAll** | `if [[ -z "$1" ]`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1645-L1657) | Clone all users github projects.

###  Tree 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**gs** | `git -c color.st`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1574-L1577) | Print short repository status.
None**ta1, lastLine** | `tail -n1 "$@"` | Print last line.
**q** | `exit` | Exit bash shell.
**srmdir** | `sudo rm --inter`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L751-L753) | Delete directories safely as super user.
**er, editUsersRc** | `"$EDITOR" ~/.st`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L466-L468) | Edit users standard rc.
**clone** | `git clone git@g`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1632-L1634) | Clone github project.
**ba** | `bash "$@"` | Start new bash shell.
**wi, whatis1** | `# Checks if it `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1498-L1522) | Describe package or command or find available packages with part of name or command.
**dl** | `__listOrDisplay`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L229-L232) | List or display matching directories in pager using short listing format.
None**l1** | `__listOrDisplay`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L244-L247) | List or display in pager one directory item per line using short listing format.
**blue** | `echo -en "\e]PC`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1228-L1230) | Change hue of color blue in linux terminal.
**up** | `sudo ifconfig w`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1805-L1807) | Activate wireless interface.
**gd** | `git diff "$@"` | Display changes between commits.
**push** | `git push "$@"` | Push changes to remote repository.
**lllt** | `__listOrDisplay`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L224-L227) | List or display directory contents in pager ordered by date using long listing format.

###  Archives 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**pd, describe** | `apt-cache show `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1350-L1352) | Print package description.
**ssd** | `sudo fstrim -v `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1264-L1266) | Trim ssd.

###  Tables 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**gls, lsgit** | `git ls-files "$`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1621-L1623) | List files that are in repository.
**keycode** | `xev "$@"` | Monitor keycodes of pressed keys.

###  Files 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**cl, clr** | `clear` | Clear the screen.
**?** | `echo $?` | Print exit code of last command.
**autoremove** | `sudo apt-get au`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1315-L1317) | Remove unneeded packages.
**ta** | `tail "$@"` | Print last ten lines.
**nf, newest** | `ls -pt | grep -`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L260-L262) | Print name of newest file in directory.
**cdiso** | `sudo mkdir /med`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L339-L343) | Mount iso and cd into.

###  Power 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**batt, battery** | `acpi` | Print battery status.
**.......** | `___goUpNumberOf`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L334-L336) | Go up six directories.
**m** | `___printOrDispl`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L82-L84) | Print or display text or file in pager.
**...** | `___goUpNumberOf`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L318-L320) | Go up two directories.

###  Ls 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
None**gu** | `git remote upda`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1597-L1600) | Update information about remote repository and print status.
**hd1** | `hd  "$@" | __pr`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1244-L1246) | Print hexadecimal representation of file or stream.
**gc, checkout** | `git checkout "$`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1564-L1566) | Checkout branch or file.
**package** | `call1=$(sudo wh`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1417-L1433) | Print package of installed command together with description and location.
**wr** | `woff`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1799-L1802) | Reset wireless device.
**ip1** | `/sbin/ifconfig `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1665-L1671) | Print internal ip.
**ma, make1** | `make  "$@" 2>&1`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L574-L576) | Run make with pager.
None
###  Less 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**gl** | `git log --decor`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1581-L1583) | Display log of commits.
**findd, directories** | `find . -name .g`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L272-L274) | Print all subdirectories.
**mvdir** | `mv --interactiv`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L377-L379) | Move directories safely.
**psa, pse, processes** | `ps -e  "$@" | _`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L888-L890) | Print all processes.
**merge** | `git merge "$@"` | Merge specified branch with current one.

###  Text 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**sg** | `sudo gedit  "$@`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L793-L795) | Edit file with gedit as super user.

###  Text Editors 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**diff1** | `colordiff  "$@"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L590-L592) | Compare files line by line in color.
None
###  Basics 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**er1, editProjectsRc** | `projectLocation`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L470-L473) | Edit projects standard rc.
**purge** | `sudo apt-get pu`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1309-L1311) | Remove package and all unneeded packages together with configuration files.
**init** | `git init "$@"` | Initialize repository.
**upgrade** | `sudo apt-get up`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1289-L1291) | Upgrade all packages.
**h, history1** | `if [ "$#" -eq 0`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L634-L643) | Search command history for pattern.
**svv** | `sudo view -p "$`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L773-L775) | View file in vim as super user.
**emacsmode** | `set -o emacs` | Change bash line editing to emacs mode.
**ve, version** | `# Check if pass`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1370-L1387) | Print installed and available version of package or installed command.
**en** | `echo -n "$@"` | Print text without trailing newline.
**ps1** | `ps  "$@" | __pr`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L882-L884) | Print users processes.
**findPackage** | `apt-cache searc`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1442-L1445) | Find available packages with part of name or description.
**t, tree1** | `tree -C -I .git`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L286-L288) | Print directory structure.
**lo, locate1** | `locate  "$1" \`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1043-L1047) | Locate files on filesystem containing pattern in their names.
**he** | `head "$@"` | Print first ten lines.
**nmap1** | `if [[ $# -eq 0 `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1700-L1716) | Scan local network.
**aa** | `___setVolumeTo `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1883-L1885) | Increase volume by two decibels.
**wcl, countLines** | `wc -l "$@"` | Count lines.
**repeat** | `xset r` | Turn on key repeat.
**update** | `sudo apt-get up`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1284-L1286) | Update information about available packages.
**bc1** | `gcalccmd "$@"` | Run terminal calculator that supports decimal numbers.
**remove** | `sudo apt-get re`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1302-L1304) | Remove package and all unneeded packages.
**mac** | `ifconfig | grep`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1687-L1689) | Print mac addresses of network devices.
**gr** | `__printLinesCon`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1025-L1028) | Print or display with pager lines containing pattern.
**grr** | `__printLinesCon`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1032-L1038) | Print or display with pager numbered lines from working and subdirectories that contain pattern.

###  Echo 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**origin** | `git remote add `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1638-L1642) | Set github project as remote repository.
**smvdir** | `sudo mv --inter`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L744-L746) | Move directories safely as super user.
**smv** | `sudo mv --inter`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L725-L727) | Move files safely as super user.
**norepeat** | `xset -r` | Turn off key repeat.
**v** | `vim -p "$@"` | Edit file with vim.
None**profile** | `source /etc/pro`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1249-L1251) | Run profile script.

###  Pwd 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------

###  Terminal Multiplexer 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------

###  Run In Background 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------

###  Package Information 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**ee** | `echo -e "$@"` | Print text interpreting backslashed characters.
**path** | `echo -e ${PATH/`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1233-L1235) | List directories contained in path variable.

###  Git 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**srm** | `sudo rm --inter`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L732-L734) | Delete files safely as super user.
**sv** | `sudo vim -p "$@`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L767-L769) | Edit file with vim as super user.
**mv** | `mv --interactiv`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L358-L360) | Move files safely.
**installed, packages** | `cat /var/log/ap`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1321-L1326) | Print packages that were installed by user.
**he1, firstLine** | `head -n1 "$@"` | Print first line.
**won** | `sudo rfkill unb`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1791-L1796) | Unblock wireless device.

###  Keyboard 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**du1** | `du --summarize `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1135-L1137) | Print disk space occupied by file or folder.
**e** | `echo "$@"` | Print text.
**down** | `sudo ifconfig w`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1810-L1812) | Deactivate wireless interface.

###  System Information 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
NoneNone**cp** | `cp --interactiv`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L352-L354) | Copy files safely.
**uskeys** | `setxkbmap -layo`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1202-L1204) | Switch to american keyboard layout.
**gateway** | `route -n \`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1679-L1684) | Print gateways ip.
**g, gedit1** | `__runCommandInB`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L692-L694) | Edit file with gedit.
**rm** | `rm --interactiv`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L365-L367) | Delete files safely.
**commit** | `git commit -am `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1531-L1533) | Commit changed and deleted files with message.
**gb, branch** | `git branch "$@"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1569-L1571) | List branches or create new one.
**ne, network** | `localIp=$(ip1)`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1744-L1775) | Print ssh port status of local devices and ping google.
**trd** | `tr --delete "$@`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L956-L958) | Delete characters.
**na, explorer** | `__runCommandInB`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L584-L586) | Start file explorer in background in working directory.
**vv** | `view -p "$@"` | View file in vim.
**pci, lspci1** | `lspci -v "$@" |`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1167-L1169) | Print info about pci devices.
**fr, free1** | `echo "all:  "$(`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1140-L1147) | Print all and free memory space in megabytes.
**table** | `column -t -s "$`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L988-L990) | Line up columns.
**apt-file1** | `apt-file -x sea`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1456-L1459) | Find available packages that provide command.
**uname1, kernelVersion** | `uname --all` | Print operating system information.
**ll** | `___displayOutpu`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L189-L192) | List or display directory contents in pager using medium listing format.
**st, strace1, trace** | `strace -s\ 2000`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L914-L917) | Trace system calls.
None**sub** | `__runCommandInB`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L697-L699) | Edit file with sublime text.
**.....** | `___goUpNumberOf`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L326-L328) | Go up four directories.

###  Network 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**reboot** | `sudo reboot` | Restart computer.
**dlll** | `__listOrDisplay`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L239-L242) | List or display matching directories in pager using long listing format.
None
###  Package Search 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**mixer** | `alsamixer "$@"` | Start terminal volume control.
**i, www, internet** | `__runCommandInB`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1833-L1835) | Start default browser in background.
**woff** | `sudo rfkill blo`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1783-L1788) | Block wireless device.
None**mk, md, mkdir1** | `mkdir --parents`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L390-L393) | Create directory and descend into.
**ty, type1** | `# Check if comm`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L505-L519) | Print command type or definition.
**.., cd..** | `___goUpNumberOf`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L314-L316) | Go up one directory.

###  Github 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**la1** | `__listOrDisplay`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L249-L252) | List or display in pager one directory item per line including hidden files using short listing format.
**gl1** | `git log --graph`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1587-L1593) | Display minimal log of commits.
**gm** | `git mv "$@"` | Move repositories files.
**ap, apropos1, findCommand** | `apropos "$@" \`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1450-L1453) | Find installed commands with part of name or description.
**kill1** | `kill -9 "$@"` | Kill process with kill signal.
**dll** | `__listOrDisplay`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L234-L237) | List or display matching directories in pager using medium listing format.
**l** | `___displayOutpu`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L184-L187) | List or display directory contents in pager using short listing format.
**first** | `ls "$@" | head `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L255-L257) | List first file in directory.
**commitm** | `git commit -a "`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1537-L1539) | Commit changed and deleted files and edit message in editor.
**ef, editFunctions** | `"$EDITOR" ~/.st`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L462-L464) | Edit standard aliases.
**dist-upgrade** | `sudo apt-get di`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1296-L1298) | Upgrade all packages intelligently.
**find1** | `find  . -name "`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1054-L1058) | Locate files containing pattern in their names in working and sub directories.
**rf, randomFile** | `ls -pt | grep -`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L265-L267) | Print name of random file in directory.
**le, less1** | `less --RAW-CONT`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L27-L29) | Display text or file in pager.
**extract** | `if [ -z "$1" ];`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1067-L1100) | Extract archive of any type.
**lt** | `__listOrDisplay`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L214-L217) | List or display directory contents in pager ordered by date using short listing format.
**ch, canhaz** | `sudo apt-get in`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1279-L1281) | Install package.
**scpdir** | `sudo cp --inter`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L738-L740) | Copy directories safely as super user.
**llt** | `__listOrDisplay`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L219-L222) | List or display directory contents in pager ordered by date using medium listing format.
**da** | `date  "$@"` | Print date and time.
**o, openFile** | `__runCommandInB`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L549-L551) | Open file with default app.
**ip2** | `lynx --dump htt`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1674-L1676) | Print external ip.
**df1** | `df -h | grep "s`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1129-L1131) | Print available disk space in simplified form.
**re** | `reset "$@"` | Reset the screen.
**sudoCp** | `sudo cp --inter`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L719-L721) | Copy files safely as super user.
**fire** | `__runCommandInB`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1838-L1840) | Start firefox in background.
**sort1** | `sort --field-se`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1004-L1006) | Sort lines by column.
**rmdir** | `rm --interactiv`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L384-L386) | Delete directories safely.
**tm, taskManager, ht** | `htop  "$@"` | Run terminal task manager.
**lynx1** | `lynx -accept_al`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1853-L1855) | Start terminal web browser.
**pull** | `git pull "$@"` | Pull changes from remote repository.
**mu** | `tmux  "$@"` | Run terminal multiplexer.

###  Internet 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
None**llla** | `__listOrDisplay`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L209-L212) | List or display all directory contents in pager using long listing format.
**cut1, keepColumns** | `cut --delimiter`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L996-L998) | Keep columns.

###  Package Management 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**depends** | `apt-cache show `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1336-L1342) | Print package dependencies.
**la** | `__listOrDisplay`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L199-L202) | List or display all directory contents in pager using short listing format.
**s** | `sudo "$@"` | Execute command as super user.

###  Sudo 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**nv** | `nano --view --u`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L686-L688) | View file in nano.

###  Audio 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**to** | `touch  "$@"` | Update files timestamp or create new one.
**chrome** | `__runCommandInB`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1845-L1847) | Start chrome in background.
**ga** | `git add "$@"` | Add files to repository.
**zz** | `___setVolumeTo `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1888-L1890) | Decrease volume by two decibels.
**mul** | `tmux ls` | List terminal multiplexers sessions.
**a** | `___setVolumeTo `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1873-L1875) | Increase volume by six decibels.

###  Wireless 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------

###  Search 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**pa, pingAll** | `ping -c 1 -q $(`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1692-L1696) | Ping gateway and google.
None**me, makeExecutable** | `if [[ ! -f "$1"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L596-L625) | Make file executable or create new bash or python script.
**f, fuck** | `sudo $(history `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L713-L715) | Execute last command as super user.
None
###  Cd 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
None**c** | `cat "$@"` | Print file contents.

