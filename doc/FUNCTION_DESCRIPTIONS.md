Commands
========

###  Less 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**le, less1** | `less --RAW-CONT`[**`...`**](../standard_functions#L36-L38) | Display text or file in pager.
**m** | `___printOrDispl`[**`...`**](../standard_functions#L91-L93) | Print or display text or file in pager.

###  Ls 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**l** | `___displayOutpu`[**`...`**](../standard_functions#L193-L196) | List or display directory contents in pager using short listing format.
**ll** | `___displayOutpu`[**`...`**](../standard_functions#L198-L201) | List or display directory contents in pager using medium listing format.
**lll** | `___displayOutpu`[**`...`**](../standard_functions#L203-L206) | List or display directory contents in pager using long listing format.
**la** | `__listOrDisplay`[**`...`**](../standard_functions#L208-L211) | List or display all directory contents in pager using short listing format.
**lla** | `__listOrDisplay`[**`...`**](../standard_functions#L213-L216) | List or display all directory contents in pager using medium listing format.
**llla** | `__listOrDisplay`[**`...`**](../standard_functions#L218-L221) | List or display all directory contents in pager using long listing format.
**lt** | `__listOrDisplay`[**`...`**](../standard_functions#L223-L226) | List or display directory contents in pager ordered by date using short listing format.
**llt** | `__listOrDisplay`[**`...`**](../standard_functions#L228-L231) | List or display directory contents in pager ordered by date using medium listing format.
**lllt** | `__listOrDisplay`[**`...`**](../standard_functions#L233-L236) | List or display directory contents in pager ordered by date using long listing format.
**dl** | `__listOrDisplay`[**`...`**](../standard_functions#L238-L241) | List or display matching directories in pager using short listing format.
**dll** | `__listOrDisplay`[**`...`**](../standard_functions#L243-L246) | List or display matching directories in pager using medium listing format.
**dlll** | `__listOrDisplay`[**`...`**](../standard_functions#L248-L251) | List or display matching directories in pager using long listing format.
**l1** | `__listOrDisplay`[**`...`**](../standard_functions#L253-L256) | List or display in pager one directory item per line using short listing format.
**la1** | `__listOrDisplay`[**`...`**](../standard_functions#L258-L261) | List or display in pager one directory item per line including hidden files using short listing format.
**first** | `ls "$@" | head `[**`...`**](../standard_functions#L264-L266) | List first file in directory.
**nf, newest** | `ls -pt | grep -`[**`...`**](../standard_functions#L269-L271) | Print name of newest file in directory.
**rf, randomFile** | `ls -pt | grep -`[**`...`**](../standard_functions#L274-L276) | Print name of random file in directory.
**findd, directories** | `find . -name .g`[**`...`**](../standard_functions#L281-L283) | Print all subdirectories.

###  Tree 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**t, tree1** | `tree -C -I .git`[**`...`**](../standard_functions#L295-L297) | Print directory structure.
**tt** | `clear`[**`...`**](../standard_functions#L299-L302) | Clear screen andprint directory structure.

###  Cd 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**.., cd..** | `___goUpNumberOf`[**`...`**](../standard_functions#L328-L330) | Go up one directory.
**...** | `___goUpNumberOf`[**`...`**](../standard_functions#L332-L334) | Go up two directories.
**....** | `___goUpNumberOf`[**`...`**](../standard_functions#L336-L338) | Go up three directories.
**.....** | `___goUpNumberOf`[**`...`**](../standard_functions#L340-L342) | Go up four directories.
**......** | `___goUpNumberOf`[**`...`**](../standard_functions#L344-L346) | Go up five directories.
**.......** | `___goUpNumberOf`[**`...`**](../standard_functions#L348-L350) | Go up six directories.
**cdiso** | `sudo mkdir /med`[**`...`**](../standard_functions#L353-L357) | Mount iso and cd into.

###  Files 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**cp** | `cp --interactiv`[**`...`**](../standard_functions#L366-L368) | Copy files safely.
**mv** | `mv --interactiv`[**`...`**](../standard_functions#L372-L374) | Move files safely.
**rm** | `rm --interactiv`[**`...`**](../standard_functions#L379-L381) | Delete files safely.
**cpdir** | `cp --interactiv`[**`...`**](../standard_functions#L385-L387) | Copy directories safely.
**mvdir** | `mv --interactiv`[**`...`**](../standard_functions#L391-L393) | Move directories safely.
**rmdir** | `rm --interactiv`[**`...`**](../standard_functions#L398-L400) | Delete directories safely.
**mk, md, mkdir1** | `mkdir --parents`[**`...`**](../standard_functions#L404-L407) | Create directory and descend into.
**bk, backup** | `sudo cp --prese`[**`...`**](../standard_functions#L411-L413) | Backup file.
**switch** | `tempFile=$(mkte`[**`...`**](../standard_functions#L416-L421) | Switch contents of files.

###  Pwd 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**p** | `if [[ $# -eq 0 `[**`...`**](../standard_functions#L430-L436) | Print working directory or path to file.

###  Echo 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**e** | `echo "$@"` | Print text.
**ee** | `echo -e "$@"` | Print text interpreting backslashed characters.
**en** | `echo -n "$@"` | Print text without trailing newline.

###  Run In Background 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**rb, runInBackground** | `nohup "$@" &>/d`[**`...`**](../standard_functions#L465-L467) | Run command in background.

###  Basics 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**ef, editFunctions** | `"$EDITOR" ~/.st`[**`...`**](../standard_functions#L476-L478) | Edit standard aliases.
**er, editUsersRc** | `"$EDITOR" ~/.st`[**`...`**](../standard_functions#L480-L482) | Edit users standard rc.
**er1, editProjectsRc** | `projectLocation`[**`...`**](../standard_functions#L484-L487) | Edit projects standard rc.
**ba** | `bash "$@"` | Start new bash shell.
**ty, type1** | `# Checks if com`[**`...`**](../standard_functions#L526-L546) | Print command type or definition.
**c** | `cat "$@"` | Print file contents.
**?** | `echo $?` | Print exit code of last command.
**cl, clr** | `clear` | Clear the screen.
**re** | `reset "$@"` | Reset the screen.
**q** | `exit` | Exit bash shell.
**o, openFile** | `__runCommandInB`[**`...`**](../standard_functions#L576-L578) | Open file with default app.
**te, terminal** | `x-terminal-emul`[**`...`**](../standard_functions#L581-L583) | Open new terminal with same working directory.
**to** | `touch  "$@"` | Update files timestamp or create new one.
**da** | `date  "$@"` | Print date and time.
**ma, make1** | `make  "$@" 2>&1`[**`...`**](../standard_functions#L601-L605) | Run make with pager.
**na, explorer** | `__runCommandInB`[**`...`**](../standard_functions#L613-L615) | Start file explorer in background in working directory.
**diff1** | `colordiff  "$@"`[**`...`**](../standard_functions#L619-L621) | Compare files line by line in color.
**me, makeExecutable** | `if [[ ! -f "$1"`[**`...`**](../standard_functions#L625-L654) | Make file executable or create new bash or python script.

###  History 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**h, history1** | `if [ "$#" -eq 0`[**`...`**](../standard_functions#L663-L672) | Search command history for pattern.

###  Text Editors 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**v** | `vim -p "$@"` | Edit file with vim.
**vv** | `view -p "$@"` | View file in vim.
**n, nano1** | `nano --undo --a`[**`...`**](../standard_functions#L701-L703) | Edit file with nano.
**nv** | `nano --view --u`[**`...`**](../standard_functions#L715-L717) | View file in nano.
**g, gedit1** | `__runCommandInB`[**`...`**](../standard_functions#L721-L723) | Edit file with gedit.
**sub** | `__runCommandInB`[**`...`**](../standard_functions#L726-L728) | Edit file with sublime text.

###  Sudo 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**s** | `sudo "$@"` | Execute command as super user.
**f, fuck** | `sudo $(history `[**`...`**](../standard_functions#L742-L744) | Execute last command as super user.
**sudoCp** | `sudo cp --inter`[**`...`**](../standard_functions#L748-L750) | Copy files safely as super user.
**smv** | `sudo mv --inter`[**`...`**](../standard_functions#L754-L756) | Move files safely as super user.
**srm** | `sudo rm --inter`[**`...`**](../standard_functions#L761-L763) | Delete files safely as super user.
**scpdir** | `sudo cp --inter`[**`...`**](../standard_functions#L767-L769) | Copy directories safely as super user.
**smvdir** | `sudo mv --inter`[**`...`**](../standard_functions#L773-L775) | Move directories safely as super user.
**srmdir** | `sudo rm --inter`[**`...`**](../standard_functions#L780-L782) | Delete directories safely as super user.
**sm, sle** | `sudo less --RAW`[**`...`**](../standard_functions#L790-L792) | Display text or file in pager as super user.
**sv** | `sudo vim -p "$@`[**`...`**](../standard_functions#L796-L798) | Edit file with vim as super user.
**svv** | `sudo view -p "$`[**`...`**](../standard_functions#L802-L804) | View file in vim as super user.
**sn** | `sudo nano --und`[**`...`**](../standard_functions#L816-L818) | Edit file with nano as super user.
**sg** | `sudo gedit  "$@`[**`...`**](../standard_functions#L822-L824) | Edit file with gedit as super user.

###  Procesess 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**taskManager, ht** | `htop  "$@"` | Run terminal task manager.
**ps1** | `ps  "$@" | __pr`[**`...`**](../standard_functions#L911-L913) | Print users processes.
**psa, pse, processes** | `ps -e  "$@" | _`[**`...`**](../standard_functions#L917-L919) | Print all processes.
**pgrep1** | `pgrep --list-na`[**`...`**](../standard_functions#L924-L926) | Find processes with part of name.
**kill1** | `kill -9 "$@"` | Kill process with kill signal.
**st, strace1, trace** | `strace -s\ 2000`[**`...`**](../standard_functions#L943-L946) | Trace system calls.

###  Text 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**he** | `head "$@"` | Print first ten lines.
**he1, firstLine** | `head -n1 "$@"` | Print first line.
**ta** | `tail "$@"` | Print last ten lines.
**ta1, lastLine** | `tail -n1 "$@"` | Print last line.
**wcl, countLines** | `wc -l "$@"` | Count lines.
**wcw, countWords** | `wc -w "$@"` | Count words.
**trd** | `tr --delete "$@`[**`...`**](../standard_functions#L985-L987) | Delete characters.
**loc, linesOfCode** | `rootDir="$PWD"`[**`...`**](../standard_functions#L992-L1008) | Count lines in files with extension in working and subdirectories.

###  Tables 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**table** | `column -t -s "$`[**`...`**](../standard_functions#L1017-L1019) | Line up columns.
**cut1, keepColumns** | `cut --delimiter`[**`...`**](../standard_functions#L1025-L1027) | Keep columns.
**sort1** | `sort --field-se`[**`...`**](../standard_functions#L1033-L1035) | Sort lines by column.

###  Search 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**grep1** | `grep --color=au`[**`...`**](../standard_functions#L1048-L1050) | Print lines containing pattern.
**gr** | `__printLinesCon`[**`...`**](../standard_functions#L1054-L1057) | Print or display with pager lines containing pattern.
**grr** | `__printLinesCon`[**`...`**](../standard_functions#L1061-L1067) | Print or display with pager numbered lines containing pattern in working and subdirectories.
**lo, locate1** | `locate  "$1" \`[**`...`**](../standard_functions#L1072-L1076) | Locate files on filesystem containing pattern in their names.
**find1** | `find -not -iwho`[**`...`**](../standard_functions#L1083-L1087) | Locate files containing pattern in their names in working and sub directories.

###  Archives 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**extract** | `if [ -z "$1" ];`[**`...`**](../standard_functions#L1096-L1129) | Extract archive of any type.

###  Terminal Multiplexer 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**tm, mu** | `tmux  "$@"` | Run terminal multiplexer.
**mua** | `tmux attach "$@`[**`...`**](../standard_functions#L1143-L1145) | Run terminal multiplexer and attach to last session.
**mul** | `tmux ls` | List terminal multiplexers sessions.

###  System Information 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**df1** | `df -h | grep "s`[**`...`**](../standard_functions#L1158-L1160) | Print available disk space in simplified form.
**du1** | `du --summarize `[**`...`**](../standard_functions#L1164-L1166) | Print disk space occupied by file or folder.
**fr, free1** | `echo "all:  "$(`[**`...`**](../standard_functions#L1169-L1176) | Print all and free memory space in megabytes.
**temp, temperature** | `acpi -t` | Print temperature of cpu.
**batt, battery** | `acpi` | Print battery status.
**uname1, kernelVersion** | `uname --all` | Print operating system information.
**pci, lspci1** | `lspci -v "$@" |`[**`...`**](../standard_functions#L1196-L1198) | Print info about pci devices.

###  Power 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**reboot** | `sudo reboot` | Restart computer.
**poweroff** | `sudo poweroff` | Shut down computer.
**hib** | `sudo pm-hiberna`[**`...`**](../standard_functions#L1216-L1218) | Hibernate computer.
**sus** | `sudo pm-suspend`[**`...`**](../standard_functions#L1221-L1223) | Suspend computer.

###  Keyboard 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**uskeys** | `setxkbmap -layo`[**`...`**](../standard_functions#L1231-L1233) | Switch to american keyboard layout.
**keycode** | `xev "$@"` | Monitor keycodes of pressed keys.
**norepeat** | `xset -r` | Turn off key repeat.
**repeat** | `xset r` | Turn on key repeat.

###  Misc 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**blue** | `echo -en "\e]PC`[**`...`**](../standard_functions#L1257-L1259) | Change hue of color blue in linux terminal.
**path** | `echo -e ${PATH/`[**`...`**](../standard_functions#L1262-L1264) | List directories contained in path variable.
**bc1** | `gcalccmd "$@"` | Run terminal calculator that supports decimal numbers.
**hd1** | `hd  "$@" | __pr`[**`...`**](../standard_functions#L1273-L1275) | Print hexadecimal representation of file or stream.
**profile** | `source /etc/pro`[**`...`**](../standard_functions#L1278-L1280) | Run profile script.
**vimode** | `set -o vi` | Change bash line editing to vi mode.
**emacsmode** | `set -o emacs` | Change bash line editing to emacs mode.
**ssd** | `sudo fstrim -v `[**`...`**](../standard_functions#L1293-L1295) | Trim ssd.
**typingTutor** | `gtypist "$@"` | Start typing tutor.

###  Package Management 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**ch, canhaz** | `sudo apt-get in`[**`...`**](../standard_functions#L1308-L1310) | Install package.
**update** | `sudo apt-get up`[**`...`**](../standard_functions#L1313-L1315) | Update information about available packages.
**upgrade** | `sudo apt-get up`[**`...`**](../standard_functions#L1318-L1320) | Upgrade all packages.
**dist-upgrade** | `sudo apt-get di`[**`...`**](../standard_functions#L1325-L1327) | Upgrade all packages intelligently.
**remove** | `sudo apt-get re`[**`...`**](../standard_functions#L1331-L1333) | Remove package and all unneeded packages.
**purge** | `sudo apt-get pu`[**`...`**](../standard_functions#L1338-L1340) | Remove package and all unneeded packages together with configuration files.
**autoremove** | `sudo apt-get au`[**`...`**](../standard_functions#L1344-L1346) | Remove unneeded packages.
**installed, packages** | `cat /var/log/ap`[**`...`**](../standard_functions#L1350-L1355) | Print packages that were installed by user.
**allInstalled, allPackages** | `dpkg --get-sele`[**`...`**](../standard_functions#L1358-L1362) | Print all installed packages.
**depends** | `apt-cache show `[**`...`**](../standard_functions#L1365-L1371) | Print package dependencies.

###  Package Information 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**pd, describe** | `apt-cache show `[**`...`**](../standard_functions#L1379-L1381) | Print package description.
**ve, version** | `# Check if pass`[**`...`**](../standard_functions#L1399-L1416) | Print installed and available version of package or command.
**package** | `call1=$(sudo wh`[**`...`**](../standard_functions#L1446-L1462) | Print package of installed command together with description and location.

###  Package Search 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**findPackage** | `apt-cache searc`[**`...`**](../standard_functions#L1471-L1474) | Find available packages with part of name or description.
**ap, apropos1, findCommand** | `apropos "$@" \`[**`...`**](../standard_functions#L1479-L1482) | Find installed commands with part of name or description.
**apt-file1** | `apt-file -x sea`[**`...`**](../standard_functions#L1485-L1488) | Find available packages that provide command.
**wi, whatis1** | `# Checks if it `[**`...`**](../standard_functions#L1527-L1551) | Describe package or command or find available packages with part of name or command.

###  Git 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**commit** | `git commit -am `[**`...`**](../standard_functions#L1560-L1562) | Commit changed and deleted files with message.
**commitm** | `git commit -a "`[**`...`**](../standard_functions#L1566-L1568) | Commit changed and deleted files and edit message in editor.
**init** | `git init "$@"` | Initialize repository.
**push** | `git push "$@"` | Push changes to remote repository.
**pull** | `git pull "$@"` | Pull changes from remote repository.
**merge** | `git merge "$@"` | Merge specified branch with current one.
**gc, checkout** | `git checkout "$`[**`...`**](../standard_functions#L1593-L1595) | Checkout branch or file.
**gb, branch** | `git branch "$@"`[**`...`**](../standard_functions#L1598-L1600) | List branches or create new one.
**gs** | `git -c color.st`[**`...`**](../standard_functions#L1603-L1606) | Print short repository status.
**gl** | `git log --graph`[**`...`**](../standard_functions#L1610-L1612) | Display minimal log of commits.
**gll** | `git log --graph`[**`...`**](../standard_functions#L1616-L1618) | Display medium log of commits.
**glll** | `git log --decor`[**`...`**](../standard_functions#L1622-L1624) | Display log of commits.
**gu** | `git remote upda`[**`...`**](../standard_functions#L1628-L1631) | Update information about remote repository and print status.
**gd** | `git diff "$@"` | Display changes between commits.
**ga** | `git add "$@"` | Add files to repository.
**gm** | `git mv "$@"` | Move repositories files.
**gls, lsgit** | `git ls-files "$`[**`...`**](../standard_functions#L1652-L1654) | List files that are in repository.

###  Github 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**clone** | `git clone git@g`[**`...`**](../standard_functions#L1663-L1665) | Clone github project.
**origin** | `git remote add `[**`...`**](../standard_functions#L1669-L1673) | Set github project as remote repository.
**cloneAll** | `if [[ -z "$1" ]`[**`...`**](../standard_functions#L1676-L1688) | Clone all users github projects.

###  Network 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**ip1** | `/sbin/ifconfig `[**`...`**](../standard_functions#L1696-L1702) | Print internal ip.
**ip2** | `lynx --dump htt`[**`...`**](../standard_functions#L1705-L1707) | Print external ip.
**gateway** | `route -n \`[**`...`**](../standard_functions#L1710-L1715) | Print gateways ip.
**mac** | `ifconfig | grep`[**`...`**](../standard_functions#L1718-L1720) | Print mac addresses of network devices.
**pa, pingAll** | `ping -c 1 -q $(`[**`...`**](../standard_functions#L1723-L1727) | Ping gateway and google.
**nmap1** | `if [[ $# -eq 0 `[**`...`**](../standard_functions#L1731-L1747) | Scan local network.
**ne, network** | `localIp=$(ip1)`[**`...`**](../standard_functions#L1775-L1806) | Print ssh port status of local devices and ping google.

###  Wireless 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**woff** | `sudo rfkill blo`[**`...`**](../standard_functions#L1814-L1819) | Block wireless device.
**won** | `sudo rfkill unb`[**`...`**](../standard_functions#L1822-L1827) | Unblock wireless device.
**wr** | `woff`[**`...`**](../standard_functions#L1830-L1833) | Reset wireless device.
**up** | `sudo ifconfig w`[**`...`**](../standard_functions#L1836-L1838) | Activate wireless interface.
**down** | `sudo ifconfig w`[**`...`**](../standard_functions#L1841-L1843) | Deactivate wireless interface.
**wlan** | `sudo iwlist wla`[**`...`**](../standard_functions#L1846-L1856) | Print wireless networks in range.

###  Internet 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**i, www, internet** | `__runCommandInB`[**`...`**](../standard_functions#L1864-L1866) | Start default browser in background.
**fire** | `__runCommandInB`[**`...`**](../standard_functions#L1869-L1871) | Start firefox in background.
**chrome** | `__runCommandInB`[**`...`**](../standard_functions#L1876-L1878) | Start chrome in background.
**lynx1** | `lynx -accept_al`[**`...`**](../standard_functions#L1884-L1886) | Start terminal web browser.

###  Audio 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**mixer** | `alsamixer "$@"` | Start terminal volume control.
**a** | `___setVolumeTo `[**`...`**](../standard_functions#L1904-L1906) | Increase volume by six decibels.
**z** | `___setVolumeTo `[**`...`**](../standard_functions#L1909-L1911) | Decrease volume by six decibels.
**aa** | `___setVolumeTo `[**`...`**](../standard_functions#L1914-L1916) | Increase volume by two decibels.
**zz** | `___setVolumeTo `[**`...`**](../standard_functions#L1919-L1921) | Decrease volume by two decibels.

