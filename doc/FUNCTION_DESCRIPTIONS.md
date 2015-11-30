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
**ll** | `___displayOutpu`[**`...`**](../standard_functions#L199-L202) | List or display directory contents in pager using medium listing format.
**lll** | `___displayOutpu`[**`...`**](../standard_functions#L204-L207) | List or display directory contents in pager using long listing format.
**la** | `__listOrDisplay`[**`...`**](../standard_functions#L209-L212) | List or display all directory contents in pager using short listing format.
**lla** | `__listOrDisplay`[**`...`**](../standard_functions#L214-L217) | List or display all directory contents in pager using medium listing format.
**llla** | `__listOrDisplay`[**`...`**](../standard_functions#L219-L222) | List or display all directory contents in pager using long listing format.
**lt** | `__listOrDisplay`[**`...`**](../standard_functions#L224-L227) | List or display directory contents in pager ordered by date using short listing format.
**llt** | `__listOrDisplay`[**`...`**](../standard_functions#L229-L232) | List or display directory contents in pager ordered by date using medium listing format.
**lllt** | `__listOrDisplay`[**`...`**](../standard_functions#L234-L237) | List or display directory contents in pager ordered by date using long listing format.
**dl** | `__listOrDisplay`[**`...`**](../standard_functions#L239-L242) | List or display matching directories in pager using short listing format.
**dll** | `__listOrDisplay`[**`...`**](../standard_functions#L244-L247) | List or display matching directories in pager using medium listing format.
**dlll** | `__listOrDisplay`[**`...`**](../standard_functions#L249-L252) | List or display matching directories in pager using long listing format.
**l1** | `__listOrDisplay`[**`...`**](../standard_functions#L254-L257) | List or display in pager one directory item per line using short listing format.
**la1** | `__listOrDisplay`[**`...`**](../standard_functions#L259-L262) | List or display in pager one directory item per line including hidden files using short listing format.
**first** | `ls "$@" | head `[**`...`**](../standard_functions#L265-L267) | List first file in directory.
**nf, newest** | `ls -pt | grep -`[**`...`**](../standard_functions#L270-L272) | Print name of newest file in directory.
**rf, randomFile** | `ls -pt | grep -`[**`...`**](../standard_functions#L275-L277) | Print name of random file in directory.
**findd, directories** | `find . -name .g`[**`...`**](../standard_functions#L282-L284) | Print all subdirectories.

###  Tree 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**t, tree1** | `tree -C -I .git`[**`...`**](../standard_functions#L296-L298) | Print directory structure.
**tt** | `clear`[**`...`**](../standard_functions#L300-L303) | Clear screen andprint directory structure.

###  Cd 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**.., cd..** | `___goUpNumberOf`[**`...`**](../standard_functions#L329-L331) | Go up one directory.
**...** | `___goUpNumberOf`[**`...`**](../standard_functions#L333-L335) | Go up two directories.
**....** | `___goUpNumberOf`[**`...`**](../standard_functions#L337-L339) | Go up three directories.
**.....** | `___goUpNumberOf`[**`...`**](../standard_functions#L341-L343) | Go up four directories.
**......** | `___goUpNumberOf`[**`...`**](../standard_functions#L345-L347) | Go up five directories.
**.......** | `___goUpNumberOf`[**`...`**](../standard_functions#L349-L351) | Go up six directories.
**cdiso** | `sudo mkdir /med`[**`...`**](../standard_functions#L354-L358) | Mount iso and cd into.

###  Files 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**cp** | `cp --interactiv`[**`...`**](../standard_functions#L367-L369) | Copy files safely.
**mv** | `mv --interactiv`[**`...`**](../standard_functions#L373-L375) | Move files safely.
**rm** | `rm --interactiv`[**`...`**](../standard_functions#L380-L382) | Delete files safely.
**cpdir** | `cp --interactiv`[**`...`**](../standard_functions#L386-L388) | Copy directories safely.
**mvdir** | `mv --interactiv`[**`...`**](../standard_functions#L392-L394) | Move directories safely.
**rmdir** | `rm --interactiv`[**`...`**](../standard_functions#L399-L401) | Delete directories safely.
**mk, md, mkdir1** | `mkdir --parents`[**`...`**](../standard_functions#L405-L408) | Create directory and descend into.
**bk, backup** | `sudo cp --prese`[**`...`**](../standard_functions#L412-L414) | Backup file.
**switch** | `tempFile=$(mkte`[**`...`**](../standard_functions#L417-L422) | Switch contents of files.

###  Pwd 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**p** | `if [[ $# -eq 0 `[**`...`**](../standard_functions#L431-L437) | Print working directory or path to file.

###  Echo 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**e** | `echo "$@"` | Print text.
**ee** | `echo -e "$@"` | Print text interpreting backslashed characters.
**en** | `echo -n "$@"` | Print text without trailing newline.

###  Run In Background 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**rb, runInBackground** | `nohup "$@" &>/d`[**`...`**](../standard_functions#L466-L468) | Run command in background.

###  Basics 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**ef, editFunctions** | `"$EDITOR" ~/.st`[**`...`**](../standard_functions#L477-L479) | Edit standard aliases.
**er, editUsersRc** | `"$EDITOR" ~/.st`[**`...`**](../standard_functions#L481-L483) | Edit users standard rc.
**er1, editProjectsRc** | `projectLocation`[**`...`**](../standard_functions#L485-L488) | Edit projects standard rc.
**ba** | `bash "$@"` | Start new bash shell.
**ty, type1** | `# Checks if com`[**`...`**](../standard_functions#L527-L547) | Print command type or definition.
**c** | `cat "$@"` | Print file contents.
**?** | `echo $?` | Print exit code of last command.
**cl, clr** | `clear` | Clear the screen.
**re** | `reset "$@"` | Reset the screen.
**q** | `exit` | Exit bash shell.
**o, openFile** | `__runCommandInB`[**`...`**](../standard_functions#L577-L579) | Open file with default app.
**te, terminal** | `x-terminal-emul`[**`...`**](../standard_functions#L582-L584) | Open new terminal with same working directory.
**to** | `touch  "$@"` | Update files timestamp or create new one.
**da** | `date  "$@"` | Print date and time.
**ma, make1** | `make  "$@" 2>&1`[**`...`**](../standard_functions#L602-L606) | Run make with pager.
**na, explorer** | `__runCommandInB`[**`...`**](../standard_functions#L614-L616) | Start file explorer in background in working directory.
**diff1** | `colordiff  "$@"`[**`...`**](../standard_functions#L620-L622) | Compare files line by line in color.
**me, makeExecutable** | `if [[ ! -f "$1"`[**`...`**](../standard_functions#L626-L659) | Make file executable or create new bash or python script.

###  History 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**h, history1** | `if [ "$#" -eq 0`[**`...`**](../standard_functions#L668-L679) | Search command history for pattern.

###  Text Editors 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**v** | `vim -p "$@"` | Edit file with vim.
**vv** | `view -p "$@"` | View file in vim.
**n, nano1** | `nano --undo --a`[**`...`**](../standard_functions#L708-L710) | Edit file with nano.
**nv** | `nano --view --u`[**`...`**](../standard_functions#L722-L724) | View file in nano.
**g, gedit1** | `__runCommandInB`[**`...`**](../standard_functions#L728-L730) | Edit file with gedit.
**sub** | `__runCommandInB`[**`...`**](../standard_functions#L733-L735) | Edit file with sublime text.

###  Sudo 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**s** | `sudo "$@"` | Execute command as super user.
**f, please** | `sudo $(history `[**`...`**](../standard_functions#L749-L751) | Execute last command as super user.
**sudoCp** | `sudo cp --inter`[**`...`**](../standard_functions#L755-L757) | Copy files safely as super user.
**smv** | `sudo mv --inter`[**`...`**](../standard_functions#L761-L763) | Move files safely as super user.
**srm** | `sudo rm --inter`[**`...`**](../standard_functions#L768-L770) | Delete files safely as super user.
**scpdir** | `sudo cp --inter`[**`...`**](../standard_functions#L774-L776) | Copy directories safely as super user.
**smvdir** | `sudo mv --inter`[**`...`**](../standard_functions#L780-L782) | Move directories safely as super user.
**srmdir** | `sudo rm --inter`[**`...`**](../standard_functions#L787-L789) | Delete directories safely as super user.
**sm, sle** | `sudo less --RAW`[**`...`**](../standard_functions#L797-L799) | Display text or file in pager as super user.
**sv** | `sudo vim -p "$@`[**`...`**](../standard_functions#L803-L805) | Edit file with vim as super user.
**svv** | `sudo view -p "$`[**`...`**](../standard_functions#L809-L811) | View file in vim as super user.
**sn** | `sudo nano --und`[**`...`**](../standard_functions#L823-L825) | Edit file with nano as super user.
**sg** | `sudo gedit  "$@`[**`...`**](../standard_functions#L829-L831) | Edit file with gedit as super user.

###  Procesess 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**taskManager, ht** | `htop  "$@"` | Run terminal task manager.
**ps1** | `ps  "$@" | __pr`[**`...`**](../standard_functions#L918-L920) | Print users processes.
**psa, pse, processes** | `ps -e  "$@" | _`[**`...`**](../standard_functions#L924-L926) | Print all processes.
**pgrep1** | `pgrep --list-na`[**`...`**](../standard_functions#L931-L933) | Find processes with part of name.
**kill1** | `kill -9 "$@"` | Kill process with kill signal.
**st, strace1, trace** | `strace -s\ 2000`[**`...`**](../standard_functions#L950-L953) | Trace system calls.

###  Text 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**he** | `head "$@"` | Print first ten lines.
**he1, firstLine** | `head -n1 "$@"` | Print first line.
**ta** | `tail "$@"` | Print last ten lines.
**ta1, lastLine** | `tail -n1 "$@"` | Print last line.
**wcl, countLines** | `wc -l "$@"` | Count lines.
**wcw, countWords** | `wc -w "$@"` | Count words.
**trd** | `tr --delete "$@`[**`...`**](../standard_functions#L992-L994) | Delete characters.
**loc, linesOfCode** | `rootDir="$PWD"`[**`...`**](../standard_functions#L999-L1015) | Count lines in files with extension in working and subdirectories.

###  Tables 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**table** | `column -t -s "$`[**`...`**](../standard_functions#L1024-L1026) | Line up columns.
**cut1, keepColumns** | `cut --delimiter`[**`...`**](../standard_functions#L1032-L1034) | Keep columns.
**sort1** | `sort --field-se`[**`...`**](../standard_functions#L1040-L1042) | Sort lines by column.

###  Search 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**grep1** | `grep --color=au`[**`...`**](../standard_functions#L1055-L1057) | Print lines containing pattern.
**gr** | `__printLinesCon`[**`...`**](../standard_functions#L1061-L1064) | Print or display with pager lines containing pattern.
**grr** | `__printLinesCon`[**`...`**](../standard_functions#L1068-L1074) | Print or display with pager numbered lines containing pattern in working and subdirectories.
**lo, locate1** | `locate  "$1" \`[**`...`**](../standard_functions#L1079-L1083) | Locate files on filesystem containing pattern in their names.
**find1** | `find . -not -iw`[**`...`**](../standard_functions#L1090-L1094) | Locate files containing pattern in their names in working and sub directories.

###  Archives 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**extract** | `if [ -z "$1" ];`[**`...`**](../standard_functions#L1103-L1136) | Extract archive of any type.

###  Terminal Multiplexer 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**tm, mu** | `tmux  "$@"` | Run terminal multiplexer.
**mua** | `tmux attach "$@`[**`...`**](../standard_functions#L1150-L1152) | Run terminal multiplexer and attach to last session.
**mul** | `tmux ls` | List terminal multiplexers sessions.

###  System Information 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**df1** | `df -h | grep "s`[**`...`**](../standard_functions#L1165-L1167) | Print available disk space in simplified form.
**du1** | `du --summarize `[**`...`**](../standard_functions#L1171-L1173) | Print disk space occupied by file or folder.
**fr, free1** | `echo "all:  "$(`[**`...`**](../standard_functions#L1176-L1183) | Print all and free memory space in megabytes.
**temp, temperature** | `acpi -t` | Print temperature of cpu.
**batt, battery** | `acpi` | Print battery status.
**uname1, kernelVersion** | `uname --all` | Print operating system information.
**pci, lspci1** | `lspci -v "$@" |`[**`...`**](../standard_functions#L1203-L1205) | Print info about pci devices.

###  Power 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**reboot** | `sudo reboot` | Restart computer.
**poweroff** | `sudo poweroff` | Shut down computer.
**hib** | `sudo pm-hiberna`[**`...`**](../standard_functions#L1223-L1225) | Hibernate computer.
**sus** | `sudo pm-suspend`[**`...`**](../standard_functions#L1228-L1230) | Suspend computer.

###  Keyboard 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**uskeys** | `setxkbmap -layo`[**`...`**](../standard_functions#L1238-L1240) | Switch to american keyboard layout.
**keycode** | `xev "$@"` | Monitor keycodes of pressed keys.
**norepeat** | `xset -r` | Turn off key repeat.
**repeat** | `xset r` | Turn on key repeat.

###  Misc 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**blue** | `echo -en "\e]PC`[**`...`**](../standard_functions#L1264-L1266) | Change hue of color blue in linux terminal.
**path** | `echo -e ${PATH/`[**`...`**](../standard_functions#L1269-L1271) | List directories contained in path variable.
**bc1** | `gcalccmd "$@"` | Run terminal calculator that supports decimal numbers.
**hd1** | `hd  "$@" | __pr`[**`...`**](../standard_functions#L1280-L1282) | Print hexadecimal representation of file or stream.
**profile** | `source /etc/pro`[**`...`**](../standard_functions#L1285-L1287) | Run profile script.
**vimode** | `set -o vi` | Change bash line editing to vi mode.
**emacsmode** | `set -o emacs` | Change bash line editing to emacs mode.
**ssd** | `sudo fstrim -v `[**`...`**](../standard_functions#L1300-L1302) | Trim ssd.
**typingTutor** | `gtypist "$@"` | Start typing tutor.

###  Package Management 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**ch, canhaz** | `sudo apt-get in`[**`...`**](../standard_functions#L1315-L1317) | Install package.
**update** | `sudo apt-get up`[**`...`**](../standard_functions#L1320-L1322) | Update information about available packages.
**upgrade** | `sudo apt-get up`[**`...`**](../standard_functions#L1325-L1327) | Upgrade all packages.
**dist-upgrade** | `sudo apt-get di`[**`...`**](../standard_functions#L1332-L1334) | Upgrade all packages intelligently.
**remove** | `sudo apt-get re`[**`...`**](../standard_functions#L1338-L1340) | Remove package and all unneeded packages.
**purge** | `sudo apt-get pu`[**`...`**](../standard_functions#L1345-L1347) | Remove package and all unneeded packages together with configuration files.
**autoremove** | `sudo apt-get au`[**`...`**](../standard_functions#L1351-L1353) | Remove unneeded packages.
**installed, packages** | `cat /var/log/ap`[**`...`**](../standard_functions#L1357-L1362) | Print packages that were installed by user.
**allInstalled, allPackages** | `dpkg --get-sele`[**`...`**](../standard_functions#L1365-L1369) | Print all installed packages.
**depends** | `apt-cache show `[**`...`**](../standard_functions#L1372-L1378) | Print package dependencies.

###  Package Information 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**pd, describe** | `apt-cache show `[**`...`**](../standard_functions#L1386-L1388) | Print package description.
**ve, version** | `# Check if pass`[**`...`**](../standard_functions#L1406-L1423) | Print installed and available version of package or command.
**package** | `call1=$(sudo wh`[**`...`**](../standard_functions#L1453-L1469) | Print package of installed command together with description and location.

###  Package Search 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**findPackage** | `apt-cache searc`[**`...`**](../standard_functions#L1478-L1481) | Find available packages with part of name or description.
**ap, apropos1, findCommand** | `apropos "$@" \`[**`...`**](../standard_functions#L1486-L1489) | Find installed commands with part of name or description.
**apt-file1** | `apt-file -x sea`[**`...`**](../standard_functions#L1492-L1495) | Find available packages that provide command.
**wi, whatis1** | `# Checks if it `[**`...`**](../standard_functions#L1534-L1558) | Describe package or command or find available packages with part of name or command.

###  Git 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**commit** | `git commit -am `[**`...`**](../standard_functions#L1567-L1569) | Commit changed and deleted files with message.
**commitm** | `git commit -a "`[**`...`**](../standard_functions#L1573-L1575) | Commit changed and deleted files and edit message in editor.
**init** | `git init "$@"` | Initialize repository.
**push** | `git push "$@"` | Push changes to remote repository.
**pull** | `git pull "$@"` | Pull changes from remote repository.
**merge** | `git merge "$@"` | Merge specified branch with current one.
**gc, checkout** | `git checkout "$`[**`...`**](../standard_functions#L1600-L1602) | Checkout branch or file.
**gb, branch** | `git branch "$@"`[**`...`**](../standard_functions#L1605-L1607) | List branches or create new one.
**gs** | `git -c color.st`[**`...`**](../standard_functions#L1610-L1613) | Print short repository status.
**gl** | `git log --graph`[**`...`**](../standard_functions#L1617-L1619) | Display minimal log of commits.
**gll** | `git log --graph`[**`...`**](../standard_functions#L1623-L1625) | Display medium log of commits.
**glll** | `git log --decor`[**`...`**](../standard_functions#L1629-L1631) | Display log of commits.
**gu** | `git remote upda`[**`...`**](../standard_functions#L1635-L1638) | Update information about remote repository and print status.
**gd** | `git diff "$@"` | Display changes between commits.
**ga** | `git add "$@"` | Add files to repository.
**gm** | `git mv "$@"` | Move repositories files.
**gls, lsgit** | `git ls-files "$`[**`...`**](../standard_functions#L1659-L1661) | List files that are in repository.

###  Github 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**clone** | `git clone git@g`[**`...`**](../standard_functions#L1670-L1672) | Clone github project.
**origin** | `git remote add `[**`...`**](../standard_functions#L1676-L1680) | Set github project as remote repository.
**cloneAll** | `if [[ -z "$1" ]`[**`...`**](../standard_functions#L1683-L1695) | Clone all users github projects.

###  Network 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**ip1** | `/sbin/ifconfig `[**`...`**](../standard_functions#L1703-L1710) | Print internal ip.
**ip2** | `lynx --dump htt`[**`...`**](../standard_functions#L1713-L1715) | Print external ip.
**gateway** | `route -n \`[**`...`**](../standard_functions#L1718-L1723) | Print gateways ip.
**mac** | `ifconfig | grep`[**`...`**](../standard_functions#L1726-L1728) | Print mac addresses of network devices.
**pa, pingAll** | `ping -c 1 -q $(`[**`...`**](../standard_functions#L1731-L1735) | Ping gateway and google.
**nmap1** | `if [[ $# -eq 0 `[**`...`**](../standard_functions#L1739-L1755) | Scan local network.
**ne, network** | `localIp=$(ip1)`[**`...`**](../standard_functions#L1783-L1814) | Print ssh port status of local devices and ping google.

###  Wireless 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**woff** | `sudo rfkill blo`[**`...`**](../standard_functions#L1822-L1827) | Block wireless device.
**won** | `sudo rfkill unb`[**`...`**](../standard_functions#L1830-L1835) | Unblock wireless device.
**wr** | `woff`[**`...`**](../standard_functions#L1838-L1841) | Reset wireless device.
**up** | `sudo ifconfig w`[**`...`**](../standard_functions#L1844-L1846) | Activate wireless interface.
**down** | `sudo ifconfig w`[**`...`**](../standard_functions#L1849-L1851) | Deactivate wireless interface.
**wlan** | `sudo iwlist wla`[**`...`**](../standard_functions#L1854-L1864) | Print wireless networks in range.

###  Internet 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**i, www, internet** | `__runCommandInB`[**`...`**](../standard_functions#L1872-L1874) | Start default browser in background.
**fire** | `__runCommandInB`[**`...`**](../standard_functions#L1877-L1879) | Start firefox in background.
**chrome** | `__runCommandInB`[**`...`**](../standard_functions#L1884-L1886) | Start chrome in background.
**lynx1** | `lynx -accept_al`[**`...`**](../standard_functions#L1892-L1894) | Start terminal web browser.

###  Audio 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**mixer** | `alsamixer "$@"` | Start terminal volume control.
**a** | `___setVolumeTo `[**`...`**](../standard_functions#L1912-L1914) | Increase volume by six decibels.
**z** | `___setVolumeTo `[**`...`**](../standard_functions#L1917-L1919) | Decrease volume by six decibels.
**aa** | `___setVolumeTo `[**`...`**](../standard_functions#L1922-L1924) | Increase volume by two decibels.
**zz** | `___setVolumeTo `[**`...`**](../standard_functions#L1927-L1929) | Decrease volume by two decibels.

###  Framework 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**fu** | `"${EDITOR:-nano`[**`...`**](../standard_functions#L1937-L1939) | Edit standard functions.
**rc** | `"${EDITOR:-nano`[**`...`**](../standard_functions#L1942-L1944) | Edit standard rc.

