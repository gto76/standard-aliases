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
**me, makeExecutable** | `if [[ ! -f "$1"`[**`...`**](../standard_functions#L626-L655) | Make file executable or create new bash or python script.

###  History 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**h, history1** | `if [ "$#" -eq 0`[**`...`**](../standard_functions#L664-L675) | Search command history for pattern.

###  Text Editors 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**v** | `vim -p "$@"` | Edit file with vim.
**vv** | `view -p "$@"` | View file in vim.
**n, nano1** | `nano --undo --a`[**`...`**](../standard_functions#L704-L706) | Edit file with nano.
**nv** | `nano --view --u`[**`...`**](../standard_functions#L718-L720) | View file in nano.
**g, gedit1** | `__runCommandInB`[**`...`**](../standard_functions#L724-L726) | Edit file with gedit.
**sub** | `__runCommandInB`[**`...`**](../standard_functions#L729-L731) | Edit file with sublime text.

###  Sudo 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**s** | `sudo "$@"` | Execute command as super user.
**f, fuck** | `sudo $(history `[**`...`**](../standard_functions#L745-L747) | Execute last command as super user.
**sudoCp** | `sudo cp --inter`[**`...`**](../standard_functions#L751-L753) | Copy files safely as super user.
**smv** | `sudo mv --inter`[**`...`**](../standard_functions#L757-L759) | Move files safely as super user.
**srm** | `sudo rm --inter`[**`...`**](../standard_functions#L764-L766) | Delete files safely as super user.
**scpdir** | `sudo cp --inter`[**`...`**](../standard_functions#L770-L772) | Copy directories safely as super user.
**smvdir** | `sudo mv --inter`[**`...`**](../standard_functions#L776-L778) | Move directories safely as super user.
**srmdir** | `sudo rm --inter`[**`...`**](../standard_functions#L783-L785) | Delete directories safely as super user.
**sm, sle** | `sudo less --RAW`[**`...`**](../standard_functions#L793-L795) | Display text or file in pager as super user.
**sv** | `sudo vim -p "$@`[**`...`**](../standard_functions#L799-L801) | Edit file with vim as super user.
**svv** | `sudo view -p "$`[**`...`**](../standard_functions#L805-L807) | View file in vim as super user.
**sn** | `sudo nano --und`[**`...`**](../standard_functions#L819-L821) | Edit file with nano as super user.
**sg** | `sudo gedit  "$@`[**`...`**](../standard_functions#L825-L827) | Edit file with gedit as super user.

###  Procesess 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**taskManager, ht** | `htop  "$@"` | Run terminal task manager.
**ps1** | `ps  "$@" | __pr`[**`...`**](../standard_functions#L914-L916) | Print users processes.
**psa, pse, processes** | `ps -e  "$@" | _`[**`...`**](../standard_functions#L920-L922) | Print all processes.
**pgrep1** | `pgrep --list-na`[**`...`**](../standard_functions#L927-L929) | Find processes with part of name.
**kill1** | `kill -9 "$@"` | Kill process with kill signal.
**st, strace1, trace** | `strace -s\ 2000`[**`...`**](../standard_functions#L946-L949) | Trace system calls.

###  Text 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**he** | `head "$@"` | Print first ten lines.
**he1, firstLine** | `head -n1 "$@"` | Print first line.
**ta** | `tail "$@"` | Print last ten lines.
**ta1, lastLine** | `tail -n1 "$@"` | Print last line.
**wcl, countLines** | `wc -l "$@"` | Count lines.
**wcw, countWords** | `wc -w "$@"` | Count words.
**trd** | `tr --delete "$@`[**`...`**](../standard_functions#L988-L990) | Delete characters.
**loc, linesOfCode** | `rootDir="$PWD"`[**`...`**](../standard_functions#L995-L1011) | Count lines in files with extension in working and subdirectories.

###  Tables 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**table** | `column -t -s "$`[**`...`**](../standard_functions#L1020-L1022) | Line up columns.
**cut1, keepColumns** | `cut --delimiter`[**`...`**](../standard_functions#L1028-L1030) | Keep columns.
**sort1** | `sort --field-se`[**`...`**](../standard_functions#L1036-L1038) | Sort lines by column.

###  Search 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**grep1** | `grep --color=au`[**`...`**](../standard_functions#L1051-L1053) | Print lines containing pattern.
**gr** | `__printLinesCon`[**`...`**](../standard_functions#L1057-L1060) | Print or display with pager lines containing pattern.
**grr** | `__printLinesCon`[**`...`**](../standard_functions#L1064-L1070) | Print or display with pager numbered lines containing pattern in working and subdirectories.
**lo, locate1** | `locate  "$1" \`[**`...`**](../standard_functions#L1075-L1079) | Locate files on filesystem containing pattern in their names.
**find1** | `find -not -iwho`[**`...`**](../standard_functions#L1086-L1090) | Locate files containing pattern in their names in working and sub directories.

###  Archives 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**extract** | `if [ -z "$1" ];`[**`...`**](../standard_functions#L1099-L1132) | Extract archive of any type.

###  Terminal Multiplexer 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**tm, mu** | `tmux  "$@"` | Run terminal multiplexer.
**mua** | `tmux attach "$@`[**`...`**](../standard_functions#L1146-L1148) | Run terminal multiplexer and attach to last session.
**mul** | `tmux ls` | List terminal multiplexers sessions.

###  System Information 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**df1** | `df -h | grep "s`[**`...`**](../standard_functions#L1161-L1163) | Print available disk space in simplified form.
**du1** | `du --summarize `[**`...`**](../standard_functions#L1167-L1169) | Print disk space occupied by file or folder.
**fr, free1** | `echo "all:  "$(`[**`...`**](../standard_functions#L1172-L1179) | Print all and free memory space in megabytes.
**temp, temperature** | `acpi -t` | Print temperature of cpu.
**batt, battery** | `acpi` | Print battery status.
**uname1, kernelVersion** | `uname --all` | Print operating system information.
**pci, lspci1** | `lspci -v "$@" |`[**`...`**](../standard_functions#L1199-L1201) | Print info about pci devices.

###  Power 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**reboot** | `sudo reboot` | Restart computer.
**poweroff** | `sudo poweroff` | Shut down computer.
**hib** | `sudo pm-hiberna`[**`...`**](../standard_functions#L1219-L1221) | Hibernate computer.
**sus** | `sudo pm-suspend`[**`...`**](../standard_functions#L1224-L1226) | Suspend computer.

###  Keyboard 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**uskeys** | `setxkbmap -layo`[**`...`**](../standard_functions#L1234-L1236) | Switch to american keyboard layout.
**keycode** | `xev "$@"` | Monitor keycodes of pressed keys.
**norepeat** | `xset -r` | Turn off key repeat.
**repeat** | `xset r` | Turn on key repeat.

###  Misc 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**blue** | `echo -en "\e]PC`[**`...`**](../standard_functions#L1260-L1262) | Change hue of color blue in linux terminal.
**path** | `echo -e ${PATH/`[**`...`**](../standard_functions#L1265-L1267) | List directories contained in path variable.
**bc1** | `gcalccmd "$@"` | Run terminal calculator that supports decimal numbers.
**hd1** | `hd  "$@" | __pr`[**`...`**](../standard_functions#L1276-L1278) | Print hexadecimal representation of file or stream.
**profile** | `source /etc/pro`[**`...`**](../standard_functions#L1281-L1283) | Run profile script.
**vimode** | `set -o vi` | Change bash line editing to vi mode.
**emacsmode** | `set -o emacs` | Change bash line editing to emacs mode.
**ssd** | `sudo fstrim -v `[**`...`**](../standard_functions#L1296-L1298) | Trim ssd.
**typingTutor** | `gtypist "$@"` | Start typing tutor.

###  Package Management 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**ch, canhaz** | `sudo apt-get in`[**`...`**](../standard_functions#L1311-L1313) | Install package.
**update** | `sudo apt-get up`[**`...`**](../standard_functions#L1316-L1318) | Update information about available packages.
**upgrade** | `sudo apt-get up`[**`...`**](../standard_functions#L1321-L1323) | Upgrade all packages.
**dist-upgrade** | `sudo apt-get di`[**`...`**](../standard_functions#L1328-L1330) | Upgrade all packages intelligently.
**remove** | `sudo apt-get re`[**`...`**](../standard_functions#L1334-L1336) | Remove package and all unneeded packages.
**purge** | `sudo apt-get pu`[**`...`**](../standard_functions#L1341-L1343) | Remove package and all unneeded packages together with configuration files.
**autoremove** | `sudo apt-get au`[**`...`**](../standard_functions#L1347-L1349) | Remove unneeded packages.
**installed, packages** | `cat /var/log/ap`[**`...`**](../standard_functions#L1353-L1358) | Print packages that were installed by user.
**allInstalled, allPackages** | `dpkg --get-sele`[**`...`**](../standard_functions#L1361-L1365) | Print all installed packages.
**depends** | `apt-cache show `[**`...`**](../standard_functions#L1368-L1374) | Print package dependencies.

###  Package Information 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**pd, describe** | `apt-cache show `[**`...`**](../standard_functions#L1382-L1384) | Print package description.
**ve, version** | `# Check if pass`[**`...`**](../standard_functions#L1402-L1419) | Print installed and available version of package or command.
**package** | `call1=$(sudo wh`[**`...`**](../standard_functions#L1449-L1465) | Print package of installed command together with description and location.

###  Package Search 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**findPackage** | `apt-cache searc`[**`...`**](../standard_functions#L1474-L1477) | Find available packages with part of name or description.
**ap, apropos1, findCommand** | `apropos "$@" \`[**`...`**](../standard_functions#L1482-L1485) | Find installed commands with part of name or description.
**apt-file1** | `apt-file -x sea`[**`...`**](../standard_functions#L1488-L1491) | Find available packages that provide command.
**wi, whatis1** | `# Checks if it `[**`...`**](../standard_functions#L1530-L1554) | Describe package or command or find available packages with part of name or command.

###  Git 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**commit** | `git commit -am `[**`...`**](../standard_functions#L1563-L1565) | Commit changed and deleted files with message.
**commitm** | `git commit -a "`[**`...`**](../standard_functions#L1569-L1571) | Commit changed and deleted files and edit message in editor.
**init** | `git init "$@"` | Initialize repository.
**push** | `git push "$@"` | Push changes to remote repository.
**pull** | `git pull "$@"` | Pull changes from remote repository.
**merge** | `git merge "$@"` | Merge specified branch with current one.
**gc, checkout** | `git checkout "$`[**`...`**](../standard_functions#L1596-L1598) | Checkout branch or file.
**gb, branch** | `git branch "$@"`[**`...`**](../standard_functions#L1601-L1603) | List branches or create new one.
**gs** | `git -c color.st`[**`...`**](../standard_functions#L1606-L1609) | Print short repository status.
**gl** | `git log --graph`[**`...`**](../standard_functions#L1613-L1615) | Display minimal log of commits.
**gll** | `git log --graph`[**`...`**](../standard_functions#L1619-L1621) | Display medium log of commits.
**glll** | `git log --decor`[**`...`**](../standard_functions#L1625-L1627) | Display log of commits.
**gu** | `git remote upda`[**`...`**](../standard_functions#L1631-L1634) | Update information about remote repository and print status.
**gd** | `git diff "$@"` | Display changes between commits.
**ga** | `git add "$@"` | Add files to repository.
**gm** | `git mv "$@"` | Move repositories files.
**gls, lsgit** | `git ls-files "$`[**`...`**](../standard_functions#L1655-L1657) | List files that are in repository.

###  Github 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**clone** | `git clone git@g`[**`...`**](../standard_functions#L1666-L1668) | Clone github project.
**origin** | `git remote add `[**`...`**](../standard_functions#L1672-L1676) | Set github project as remote repository.
**cloneAll** | `if [[ -z "$1" ]`[**`...`**](../standard_functions#L1679-L1691) | Clone all users github projects.

###  Network 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**ip1** | `/sbin/ifconfig `[**`...`**](../standard_functions#L1699-L1705) | Print internal ip.
**ip2** | `lynx --dump htt`[**`...`**](../standard_functions#L1708-L1710) | Print external ip.
**gateway** | `route -n \`[**`...`**](../standard_functions#L1713-L1718) | Print gateways ip.
**mac** | `ifconfig | grep`[**`...`**](../standard_functions#L1721-L1723) | Print mac addresses of network devices.
**pa, pingAll** | `ping -c 1 -q $(`[**`...`**](../standard_functions#L1726-L1730) | Ping gateway and google.
**nmap1** | `if [[ $# -eq 0 `[**`...`**](../standard_functions#L1734-L1750) | Scan local network.
**ne, network** | `localIp=$(ip1)`[**`...`**](../standard_functions#L1778-L1809) | Print ssh port status of local devices and ping google.

###  Wireless 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**woff** | `sudo rfkill blo`[**`...`**](../standard_functions#L1817-L1822) | Block wireless device.
**won** | `sudo rfkill unb`[**`...`**](../standard_functions#L1825-L1830) | Unblock wireless device.
**wr** | `woff`[**`...`**](../standard_functions#L1833-L1836) | Reset wireless device.
**up** | `sudo ifconfig w`[**`...`**](../standard_functions#L1839-L1841) | Activate wireless interface.
**down** | `sudo ifconfig w`[**`...`**](../standard_functions#L1844-L1846) | Deactivate wireless interface.
**wlan** | `sudo iwlist wla`[**`...`**](../standard_functions#L1849-L1859) | Print wireless networks in range.

###  Internet 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**i, www, internet** | `__runCommandInB`[**`...`**](../standard_functions#L1867-L1869) | Start default browser in background.
**fire** | `__runCommandInB`[**`...`**](../standard_functions#L1872-L1874) | Start firefox in background.
**chrome** | `__runCommandInB`[**`...`**](../standard_functions#L1879-L1881) | Start chrome in background.
**lynx1** | `lynx -accept_al`[**`...`**](../standard_functions#L1887-L1889) | Start terminal web browser.

###  Audio 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**mixer** | `alsamixer "$@"` | Start terminal volume control.
**a** | `___setVolumeTo `[**`...`**](../standard_functions#L1907-L1909) | Increase volume by six decibels.
**z** | `___setVolumeTo `[**`...`**](../standard_functions#L1912-L1914) | Decrease volume by six decibels.
**aa** | `___setVolumeTo `[**`...`**](../standard_functions#L1917-L1919) | Increase volume by two decibels.
**zz** | `___setVolumeTo `[**`...`**](../standard_functions#L1922-L1924) | Decrease volume by two decibels.

###  Framework 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**fu** | `"${EDITOR:-vi}"`[**`...`**](../standard_functions#L1932-L1934) | Edit standard functions.
**rc** | `"${EDITOR:-vi}"`[**`...`**](../standard_functions#L1937-L1939) | Edit standard rc.

