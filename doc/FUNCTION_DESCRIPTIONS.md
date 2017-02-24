Commands
========

###  Less 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**le, less1** | `less --RAW-CONT`[**`...`**](../standard_functions#L37-L39) | Display text or file in pager.
**m** | `___printOrDispl`[**`...`**](../standard_functions#L92-L94) | Print or display text or file in pager.

###  Ls 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**l** | `___displayOutpu`[**`...`**](../standard_functions#L194-L197) | List or display directory contents in pager using short listing format.
**ll** | `___displayOutpu`[**`...`**](../standard_functions#L204-L207) | List or display directory contents in pager using long listing format.
**la** | `__listOrDisplay`[**`...`**](../standard_functions#L209-L212) | List or display all directory contents in pager using short listing format.
**lla** | `__listOrDisplay`[**`...`**](../standard_functions#L219-L222) | List or display all directory contents in pager using long listing format.
**lt** | `__listOrDisplay`[**`...`**](../standard_functions#L224-L227) | List or display directory contents in pager ordered by date using short listing format.
**llt** | `__listOrDisplay`[**`...`**](../standard_functions#L234-L237) | List or display directory contents in pager ordered by date using long listing format.
**dl** | `__listOrDisplay`[**`...`**](../standard_functions#L239-L242) | List or display matching directories in pager using short listing format.
**dll** | `__listOrDisplay`[**`...`**](../standard_functions#L249-L252) | List or display matching directories in pager using long listing format.
**l1** | `__listOrDisplay`[**`...`**](../standard_functions#L254-L257) | List or display in pager one directory item per line using short listing format.
**la1** | `__listOrDisplay`[**`...`**](../standard_functions#L259-L262) | List or display in pager one directory item per line including hidden files using short listing format.
**first** | `ls "$@" | head `[**`...`**](../standard_functions#L265-L267) | List first file in directory.
**nf, newest** | `ls -pt "$@" | g`[**`...`**](../standard_functions#L270-L272) | Print name of newest file in directory.
**rf, randomFile** | `ls -pt | grep -`[**`...`**](../standard_functions#L275-L277) | Print name of random file in directory.
**findd, directories** | `find . -name .g`[**`...`**](../standard_functions#L282-L284) | Print all subdirectories.
**extensions** | `find . -type f `[**`...`**](../standard_functions#L287-L292) | Print all file extensions.

###  Tree 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**t, tree1** | `tree -C -I .git`[**`...`**](../standard_functions#L304-L306) | Print directory structure.
**tt** | `clear`[**`...`**](../standard_functions#L308-L311) | Clear screen andprint directory structure.

###  Cd 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**.., cd..** | `___goUpNumberOf`[**`...`**](../standard_functions#L337-L339) | Go up one directory.
**...** | `___goUpNumberOf`[**`...`**](../standard_functions#L341-L343) | Go up two directories.
**....** | `___goUpNumberOf`[**`...`**](../standard_functions#L345-L347) | Go up three directories.
**.....** | `___goUpNumberOf`[**`...`**](../standard_functions#L349-L351) | Go up four directories.
**......** | `___goUpNumberOf`[**`...`**](../standard_functions#L353-L355) | Go up five directories.
**.......** | `___goUpNumberOf`[**`...`**](../standard_functions#L357-L359) | Go up six directories.
**cdiso** | `sudo mkdir /med`[**`...`**](../standard_functions#L362-L366) | Mount iso and cd into.

###  Files 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**cp** | `cp --interactiv`[**`...`**](../standard_functions#L375-L377) | Copy files safely.
**mv** | `mv --interactiv`[**`...`**](../standard_functions#L381-L383) | Move files safely.
**rm** | `rm --interactiv`[**`...`**](../standard_functions#L388-L390) | Delete files safely.
**cpdir** | `cp --interactiv`[**`...`**](../standard_functions#L394-L396) | Copy directories safely.
**mvdir** | `mv --interactiv`[**`...`**](../standard_functions#L400-L402) | Move directories safely.
**rmdir** | `rm --interactiv`[**`...`**](../standard_functions#L407-L409) | Delete directories safely.
**mk, md, mkdir1** | `mkdir --parents`[**`...`**](../standard_functions#L413-L416) | Create directory and descend into.
**bk, backup** | `sudo cp --prese`[**`...`**](../standard_functions#L420-L422) | Backup file.
**switch** | `tempFile=$(mkte`[**`...`**](../standard_functions#L425-L430) | Switch contents of files.

###  Pwd 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**p** | `if [[ $# -eq 0 `[**`...`**](../standard_functions#L439-L445) | Print working directory or path to file.

###  Echo 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**e** | `echo "$@"` | Print text.
**ee** | `echo -e "$@"` | Print text interpreting backslashed characters.
**en** | `echo -n "$@"` | Print text without trailing newline.

###  Run In Background 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**rb, runInBackground** | `nohup "$@" &>/d`[**`...`**](../standard_functions#L474-L476) | Run command in background.

###  Basics 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**ef, editFunctions** | `"$EDITOR" ~/.st`[**`...`**](../standard_functions#L485-L487) | Edit standard aliases.
**er, editUsersRc** | `"$EDITOR" ~/.st`[**`...`**](../standard_functions#L489-L491) | Edit users standard rc.
**er1, editProjectsRc** | `projectLocation`[**`...`**](../standard_functions#L493-L496) | Edit projects standard rc.
**ba** | `bash "$@"` | Start new bash shell.
**ty, type1** | `# Checks if com`[**`...`**](../standard_functions#L535-L555) | Print command type or definition.
**c** | `cat "$@"` | Print file contents.
**?** | `echo $?` | Print exit code of last command.
**cl, clr** | `clear` | Clear the screen.
**re** | `reset "$@"` | Reset the screen.
**q** | `exit` | Exit bash shell.
**o, openFile** | `__runCommandInB`[**`...`**](../standard_functions#L585-L587) | Open file with default app.
**te, terminal** | `x-terminal-emul`[**`...`**](../standard_functions#L590-L592) | Open new terminal with same working directory.
**to** | `touch  "$@"` | Update files timestamp or create new one.
**da** | `date  "$@"` | Print date and time.
**ma, make1** | `make  "$@" 2>&1`[**`...`**](../standard_functions#L610-L614) | Run make with pager.
**na, explorer** | `__runCommandInB`[**`...`**](../standard_functions#L622-L624) | Start file explorer in background in working directory.
**diff1** | `colordiff  "$@"`[**`...`**](../standard_functions#L628-L630) | Compare files line by line in color.
**me, makeExecutable** | `if [[ ! -f "$1"`[**`...`**](../standard_functions#L634-L667) | Make file executable or create new bash or python script.

###  History 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**h, history1** | `if [ "$#" -eq 0`[**`...`**](../standard_functions#L676-L687) | Search command history for pattern.

###  Text Editors 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**v** | `vim -p "$@"` | Edit file with vim.
**vv** | `view -p "$@"` | View file in vim.
**n, nano1** | `nano --undo --a`[**`...`**](../standard_functions#L716-L718) | Edit file with nano.
**nv** | `nano --view --u`[**`...`**](../standard_functions#L730-L732) | View file in nano.
**g, gedit1** | `__runCommandInB`[**`...`**](../standard_functions#L736-L738) | Edit file with gedit.
**sub** | `__runCommandInB`[**`...`**](../standard_functions#L741-L743) | Edit file with sublime text.

###  Sudo 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**s** | `sudo "$@"` | Execute command as super user.
**f, please** | `sudo $(history `[**`...`**](../standard_functions#L757-L759) | Execute last command as super user.
**sudoCp** | `sudo cp --inter`[**`...`**](../standard_functions#L763-L765) | Copy files safely as super user.
**smv** | `sudo mv --inter`[**`...`**](../standard_functions#L769-L771) | Move files safely as super user.
**srm** | `sudo rm --inter`[**`...`**](../standard_functions#L776-L778) | Delete files safely as super user.
**scpdir** | `sudo cp --inter`[**`...`**](../standard_functions#L782-L784) | Copy directories safely as super user.
**smvdir** | `sudo mv --inter`[**`...`**](../standard_functions#L788-L790) | Move directories safely as super user.
**srmdir** | `sudo rm --inter`[**`...`**](../standard_functions#L795-L797) | Delete directories safely as super user.
**sm, sle** | `sudo less --RAW`[**`...`**](../standard_functions#L805-L807) | Display text or file in pager as super user.
**sv, se** | `sudoedit "$@"` | Edit file with vim as super user.
**svv** | `sudo view -p "$`[**`...`**](../standard_functions#L817-L819) | View file in vim as super user.
**sn** | `sudo nano --und`[**`...`**](../standard_functions#L831-L833) | Edit file with nano as super user.
**sg** | `sudo gedit  "$@`[**`...`**](../standard_functions#L837-L839) | Edit file with gedit as super user.

###  Procesess 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**taskManager, ht** | `htop  "$@"` | Run terminal task manager.
**ps1** | `ps  "$@" | __pr`[**`...`**](../standard_functions#L926-L928) | Print users processes.
**psa, pse, processes** | `ps -e  "$@" | _`[**`...`**](../standard_functions#L932-L934) | Print all processes.
**pgrep1** | `pgrep --list-na`[**`...`**](../standard_functions#L939-L941) | Find processes with part of name.
**kill1** | `kill -9 "$@"` | Kill process with kill signal.
**st, strace1, trace** | `strace -s\ 2000`[**`...`**](../standard_functions#L958-L961) | Trace system calls.

###  Text 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**he** | `head "$@"` | Print first ten lines.
**he1, firstLine** | `head -n1 "$@"` | Print first line.
**ta** | `tail "$@"` | Print last ten lines.
**ta1, lastLine** | `tail -n1 "$@"` | Print last line.
**wcl, countLines** | `wc -l "$@"` | Count lines.
**wcw, countWords** | `wc -w "$@"` | Count words.
**trd** | `tr --delete "$@`[**`...`**](../standard_functions#L1000-L1002) | Delete characters.
**loc, linesOfCode** | `rootDir="$PWD"`[**`...`**](../standard_functions#L1007-L1023) | Count lines in files with extension in working and subdirectories.

###  Tables 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**table** | `column -t -s "$`[**`...`**](../standard_functions#L1032-L1034) | Line up columns.
**cut1, keepColumns** | `cut --delimiter`[**`...`**](../standard_functions#L1040-L1042) | Keep columns.
**sort1** | `sort --field-se`[**`...`**](../standard_functions#L1048-L1050) | Sort lines by column.

###  Search 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**grep1** | `grep --color=au`[**`...`**](../standard_functions#L1063-L1065) | Print lines containing pattern.
**gr** | `__printLinesCon`[**`...`**](../standard_functions#L1069-L1072) | Print or display with pager lines containing pattern.
**grr** | `__printLinesCon`[**`...`**](../standard_functions#L1076-L1082) | Print or display with pager numbered lines containing pattern in working and subdirectories.
**lo, locate1** | `locate  "$1" \`[**`...`**](../standard_functions#L1087-L1091) | Locate files on filesystem containing pattern in their names.
**find1** | `find . -not -iw`[**`...`**](../standard_functions#L1098-L1102) | Locate files containing pattern in their names in working and sub directories.

###  Archives 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**extract** | `if [ -z "$1" ];`[**`...`**](../standard_functions#L1111-L1144) | Extract archive of any type.

###  Terminal Multiplexer 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**tm, mu** | `tmux  "$@"` | Run terminal multiplexer.
**tma, mua** | `tmux attach "$@`[**`...`**](../standard_functions#L1158-L1160) | Run terminal multiplexer and attach to last session.
**tml, mul** | `tmux ls` | List terminal multiplexers sessions.

###  System Information 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**df1** | `df -h | grep "s`[**`...`**](../standard_functions#L1173-L1175) | Print available disk space in simplified form.
**du1** | `du --summarize `[**`...`**](../standard_functions#L1179-L1181) | Print disk space occupied by file or folder.
**fr, free1** | `echo "all:  "$(`[**`...`**](../standard_functions#L1184-L1191) | Print all and free memory space in megabytes.
**temp, temperature** | `acpi -t` | Print temperature of cpu.
**batt, battery** | `acpi` | Print battery status.
**uname1, kernelVersion** | `uname --all` | Print operating system information.
**pci, lspci1** | `lspci -v "$@" |`[**`...`**](../standard_functions#L1211-L1213) | Print info about pci devices.

###  Power 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**reboot** | `sudo reboot` | Restart computer.
**poweroff** | `sudo poweroff` | Shut down computer.
**hib** | `sudo pm-hiberna`[**`...`**](../standard_functions#L1231-L1233) | Hibernate computer.
**sus** | `sudo pm-suspend`[**`...`**](../standard_functions#L1236-L1238) | Suspend computer.

###  Keyboard 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**uskeys** | `setxkbmap -layo`[**`...`**](../standard_functions#L1246-L1248) | Switch to american keyboard layout.
**keycode** | `xev "$@"` | Monitor keycodes of pressed keys.
**norepeat** | `xset -r` | Turn off key repeat.
**repeat** | `xset r` | Turn on key repeat.

###  Misc 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**blue** | `echo -en "\e]PC`[**`...`**](../standard_functions#L1272-L1274) | Change hue of color blue in linux terminal.
**path** | `echo -e ${PATH/`[**`...`**](../standard_functions#L1277-L1279) | List directories contained in path variable.
**bc1** | `gcalccmd "$@"` | Run terminal calculator that supports decimal numbers.
**hd1** | `hd  "$@" | __pr`[**`...`**](../standard_functions#L1288-L1290) | Print hexadecimal representation of file or stream.
**profile** | `source /etc/pro`[**`...`**](../standard_functions#L1293-L1295) | Run profile script.
**vimode** | `set -o vi` | Change bash line editing to vi mode.
**emacsmode** | `set -o emacs` | Change bash line editing to emacs mode.
**ssd** | `sudo fstrim -v `[**`...`**](../standard_functions#L1308-L1310) | Trim ssd.
**typingTutor** | `gtypist "$@"` | Start typing tutor.
**extension** | `curl --silent f`[**`...`**](../standard_functions#L1318-L1323) | Describe file extension.

###  Package Management 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**ch, canhaz** | `if [[ "$__stand`[**`...`**](../standard_functions#L1331-L1337) | Install package.
**update** | `sudo apt-get up`[**`...`**](../standard_functions#L1340-L1342) | Update information about available packages.
**upgrade** | `sudo apt-get up`[**`...`**](../standard_functions#L1345-L1347) | Upgrade all packages.
**dist-upgrade** | `sudo apt-get di`[**`...`**](../standard_functions#L1352-L1354) | Upgrade all packages intelligently.
**remove** | `sudo apt-get re`[**`...`**](../standard_functions#L1358-L1360) | Remove package and all unneeded packages.
**purge** | `sudo apt-get pu`[**`...`**](../standard_functions#L1365-L1367) | Remove package and all unneeded packages together with configuration files.
**autoremove** | `sudo apt-get au`[**`...`**](../standard_functions#L1371-L1373) | Remove unneeded packages.
**installed, packages** | `cat /var/log/ap`[**`...`**](../standard_functions#L1377-L1382) | Print packages that were installed by user.
**allInstalled, allPackages** | `dpkg --get-sele`[**`...`**](../standard_functions#L1385-L1389) | Print all installed packages.
**depends** | `apt-cache show `[**`...`**](../standard_functions#L1392-L1398) | Print package dependencies.

###  Package Information 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**pd, describe** | `apt-cache show `[**`...`**](../standard_functions#L1406-L1408) | Print package description.
**ve, version** | `# Check if pass`[**`...`**](../standard_functions#L1426-L1443) | Print installed and available version of package or command.
**package** | `call1=$(sudo wh`[**`...`**](../standard_functions#L1473-L1489) | Print package of installed command together with description and location.

###  Package Search 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**findPackage** | `apt-cache searc`[**`...`**](../standard_functions#L1498-L1501) | Find available packages with part of name or description.
**ap, apropos1, findCommand** | `apropos "$@" \`[**`...`**](../standard_functions#L1506-L1509) | Find installed commands with part of name or description.
**apt-file1** | `apt-file -x sea`[**`...`**](../standard_functions#L1512-L1515) | Find available packages that provide command.
**wi, whatis1** | `# Checks if it `[**`...`**](../standard_functions#L1554-L1578) | Describe package or command or find available packages with part of name or command.

###  Git 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**commit** | `git commit -am `[**`...`**](../standard_functions#L1587-L1589) | Commit changed and deleted files with message.
**commitm** | `git commit -a "`[**`...`**](../standard_functions#L1593-L1595) | Commit changed and deleted files and edit message in editor.
**init** | `git init "$@"` | Initialize repository.
**push** | `git push "$@"` | Push changes to remote repository.
**pull** | `git pull "$@"` | Pull changes from remote repository.
**merge** | `git merge "$@"` | Merge specified branch with current one.
**gc, checkout** | `git checkout "$`[**`...`**](../standard_functions#L1620-L1622) | Checkout branch or file.
**gb, branch** | `git branch "$@"`[**`...`**](../standard_functions#L1625-L1627) | List branches or create new one.
**gs** | `git -c color.st`[**`...`**](../standard_functions#L1630-L1633) | Print short repository status.
**gl** | `git log --graph`[**`...`**](../standard_functions#L1637-L1639) | Display minimal log of commits.
**gll** | `git log --graph`[**`...`**](../standard_functions#L1643-L1645) | Display medium log of commits.
**glll** | `git log --decor`[**`...`**](../standard_functions#L1649-L1651) | Display log of commits.
**gu** | `git remote upda`[**`...`**](../standard_functions#L1655-L1658) | Update information about remote repository and print status.
**gd** | `git diff "$@"` | Display changes between commits.
**ga** | `git add "$@"` | Add files to repository.
**gm** | `git mv "$@"` | Move repositories files.
**gls, lsgit** | `git ls-files "$`[**`...`**](../standard_functions#L1679-L1681) | List files that are in repository.

###  Github 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**clone** | `git clone git@g`[**`...`**](../standard_functions#L1690-L1692) | Clone github project.
**origin** | `git remote add `[**`...`**](../standard_functions#L1696-L1700) | Set github project as remote repository.
**cloneAll** | `if [[ -z "$1" ]`[**`...`**](../standard_functions#L1703-L1715) | Clone all users github projects.

###  Network 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**ip1** | `/sbin/ifconfig `[**`...`**](../standard_functions#L1723-L1730) | Print internal ip.
**ip2** | `lynx --dump htt`[**`...`**](../standard_functions#L1733-L1735) | Print external ip.
**gateway** | `route -n \`[**`...`**](../standard_functions#L1738-L1743) | Print gateways ip.
**mac** | `ifconfig | grep`[**`...`**](../standard_functions#L1746-L1748) | Print mac addresses of network devices.
**pa, pingAll** | `ping -c 1 -q $(`[**`...`**](../standard_functions#L1751-L1755) | Ping gateway and google.
**nmap1** | `if [[ $# -eq 0 `[**`...`**](../standard_functions#L1759-L1775) | Scan local network.
**ne, network** | `localIp=$(ip1)`[**`...`**](../standard_functions#L1803-L1834) | Print ssh port status of local devices and ping google.

###  Wireless 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**woff** | `sudo rfkill blo`[**`...`**](../standard_functions#L1842-L1847) | Block wireless device.
**won** | `sudo rfkill unb`[**`...`**](../standard_functions#L1850-L1855) | Unblock wireless device.
**wr** | `woff`[**`...`**](../standard_functions#L1858-L1861) | Reset wireless device.
**up** | `sudo ifconfig w`[**`...`**](../standard_functions#L1864-L1866) | Activate wireless interface.
**down** | `sudo ifconfig w`[**`...`**](../standard_functions#L1869-L1871) | Deactivate wireless interface.
**wlan** | `sudo iwlist wla`[**`...`**](../standard_functions#L1874-L1884) | Print wireless networks in range.

###  Internet 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**i, www, internet** | `__runCommandInB`[**`...`**](../standard_functions#L1892-L1894) | Start default browser in background.
**fire** | `__runCommandInB`[**`...`**](../standard_functions#L1897-L1899) | Start firefox in background.
**chrome** | `__runCommandInB`[**`...`**](../standard_functions#L1904-L1906) | Start chrome in background.
**lynx1** | `lynx -accept_al`[**`...`**](../standard_functions#L1912-L1914) | Start terminal web browser.

###  Audio 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**mixer** | `alsamixer "$@"` | Start terminal volume control.
**a** | `___setVolumeTo `[**`...`**](../standard_functions#L1932-L1934) | Increase volume by six decibels.
**z** | `___setVolumeTo `[**`...`**](../standard_functions#L1937-L1939) | Decrease volume by six decibels.
**aa** | `___setVolumeTo `[**`...`**](../standard_functions#L1942-L1944) | Increase volume by two decibels.
**zz** | `___setVolumeTo `[**`...`**](../standard_functions#L1947-L1949) | Decrease volume by two decibels.

###  Framework 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**fu** | `"${EDITOR:-nano`[**`...`**](../standard_functions#L1957-L1959) | Edit standard functions.
**rc, al** | `"${EDITOR:-nano`[**`...`**](../standard_functions#L1962-L1964) | Edit standard rc.

