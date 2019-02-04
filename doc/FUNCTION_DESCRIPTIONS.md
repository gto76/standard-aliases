Commands
========

###  Less 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**le, less1** | <code>less --RAW-CONT</code>[**`...`**](../standard_functions#L37-L39) | Display text or file in pager.
**m** | <code>___printOrDispl</code>[**`...`**](../standard_functions#L92-L94) | Print or display text or file in pager.

###  Ls 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**l** | <code>___displayOutpu</code>[**`...`**](../standard_functions#L194-L197) | List or display directory contents in pager using short listing format.
**ll** | <code>___displayOutpu</code>[**`...`**](../standard_functions#L204-L207) | List or display directory contents in pager using long listing format.
**la** | <code>__listOrDisplay</code>[**`...`**](../standard_functions#L209-L212) | List or display all directory contents in pager using short listing format.
**lla** | <code>__listOrDisplay</code>[**`...`**](../standard_functions#L219-L222) | List or display all directory contents in pager using long listing format.
**lt** | <code>__listOrDisplay</code>[**`...`**](../standard_functions#L224-L227) | List or display directory contents in pager ordered by date using short listing format.
**llt** | <code>__listOrDisplay</code>[**`...`**](../standard_functions#L234-L237) | List or display directory contents in pager ordered by date using long listing format.
**dl** | <code>__listOrDisplay</code>[**`...`**](../standard_functions#L239-L242) | List or display matching directories in pager using short listing format.
**dll** | <code>__listOrDisplay</code>[**`...`**](../standard_functions#L249-L252) | List or display matching directories in pager using long listing format.
**l1** | <code>__listOrDisplay</code>[**`...`**](../standard_functions#L254-L257) | List or display in pager one directory item per line using short listing format.
**la1** | <code>__listOrDisplay</code>[**`...`**](../standard_functions#L259-L262) | List or display in pager one directory item per line including hidden files using short listing format.
**first** | <code>ls "$@" &#124; head </code>[**`...`**](../standard_functions#L265-L267) | List first file in directory.
**nf, newest** | <code>ls -pt "$@" &#124; g</code>[**`...`**](../standard_functions#L270-L272) | Print name of newest file in directory.
**rf, randomFile** | <code>ls -pt &#124; grep -</code>[**`...`**](../standard_functions#L275-L277) | Print name of random file in directory.
**findd, directories** | <code>find . -name .g</code>[**`...`**](../standard_functions#L282-L284) | Print all subdirectories.
**extensions** | <code>find . -type f </code>[**`...`**](../standard_functions#L287-L292) | Print all file extensions.

###  Tree 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**t, tree1** | <code>tree -C -I .git</code>[**`...`**](../standard_functions#L304-L306) | Print directory structure.
**tt** | <code>clear</code>[**`...`**](../standard_functions#L308-L311) | Clear screen andprint directory structure.

###  Cd 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**.., cd..** | <code>___goUpNumberOf</code>[**`...`**](../standard_functions#L337-L339) | Go up one directory.
**...** | <code>___goUpNumberOf</code>[**`...`**](../standard_functions#L341-L343) | Go up two directories.
**....** | <code>___goUpNumberOf</code>[**`...`**](../standard_functions#L345-L347) | Go up three directories.
**.....** | <code>___goUpNumberOf</code>[**`...`**](../standard_functions#L349-L351) | Go up four directories.
**......** | <code>___goUpNumberOf</code>[**`...`**](../standard_functions#L353-L355) | Go up five directories.
**.......** | <code>___goUpNumberOf</code>[**`...`**](../standard_functions#L357-L359) | Go up six directories.
**cdiso** | <code>sudo mkdir /med</code>[**`...`**](../standard_functions#L362-L366) | Mount iso and cd into.

###  Files 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**cp** | <code>cp --interactiv</code>[**`...`**](../standard_functions#L375-L377) | Copy files safely.
**mv** | <code>mv --interactiv</code>[**`...`**](../standard_functions#L381-L383) | Move files safely.
**rm** | <code>rm --interactiv</code>[**`...`**](../standard_functions#L388-L390) | Delete files safely.
**cpdir** | <code>cp --interactiv</code>[**`...`**](../standard_functions#L394-L396) | Copy directories safely.
**mvdir** | <code>mv --interactiv</code>[**`...`**](../standard_functions#L400-L402) | Move directories safely.
**rmdir** | <code>rm --interactiv</code>[**`...`**](../standard_functions#L407-L409) | Delete directories safely.
**mk, md, mkdir1** | <code>mkdir --parents</code>[**`...`**](../standard_functions#L413-L416) | Create directory and descend into.
**bk, backup** | <code>sudo cp --prese</code>[**`...`**](../standard_functions#L420-L422) | Backup file.
**switch** | <code>tempFile=$(mkte</code>[**`...`**](../standard_functions#L425-L430) | Switch contents of files.

###  Pwd 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**p** | <code>if [[ $# -eq 0 </code>[**`...`**](../standard_functions#L439-L445) | Print working directory or path to file.

###  Echo 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**e** | <code>echo "$@"</code> | Print text.
**ee** | <code>echo -e "$@"</code> | Print text interpreting backslashed characters.
**en** | <code>echo -n "$@"</code> | Print text without trailing newline.

###  Run In Background 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**rb, runInBackground** | <code>nohup "$@" &>/d</code>[**`...`**](../standard_functions#L474-L476) | Run command in background.

###  Basics 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**ef, editFunctions** | <code>"$EDITOR" ~/.st</code>[**`...`**](../standard_functions#L485-L487) | Edit standard aliases.
**er, editUsersRc** | <code>"$EDITOR" ~/.st</code>[**`...`**](../standard_functions#L489-L491) | Edit users standard rc.
**er1, editProjectsRc** | <code>projectLocation</code>[**`...`**](../standard_functions#L493-L496) | Edit projects standard rc.
**ba** | <code>bash "$@"</code> | Start new bash shell.
**ty, type1** | <code># Checks if com</code>[**`...`**](../standard_functions#L535-L555) | Print command type or definition.
**c** | <code>cat "$@"</code> | Print file contents.
**?** | <code>echo $?</code> | Print exit code of last command.
**cl, clr** | <code>clear</code> | Clear the screen.
**re** | <code>reset "$@"</code> | Reset the screen.
**q** | <code>exit</code> | Exit bash shell.
**o, openFile** | <code>__runCommandInB</code>[**`...`**](../standard_functions#L585-L587) | Open file with default app.
**te, terminal** | <code>x-terminal-emul</code>[**`...`**](../standard_functions#L590-L592) | Open new terminal with same working directory.
**to** | <code>touch  "$@"</code> | Update files timestamp or create new one.
**da** | <code>date  "$@"</code> | Print date and time.
**ma, make1** | <code>make  "$@" 2>&1</code>[**`...`**](../standard_functions#L610-L614) | Run make with pager.
**na, explorer** | <code>__runCommandInB</code>[**`...`**](../standard_functions#L622-L624) | Start file explorer in background in working directory.
**diff1** | <code>colordiff  "$@"</code>[**`...`**](../standard_functions#L628-L630) | Compare files line by line in color.
**me, makeExecutable** | <code>if [[ ! -f "$1"</code>[**`...`**](../standard_functions#L634-L668) | Make file executable or create new bash or python script.

###  History 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**h, history1** | <code>if [ "$#" -eq 0</code>[**`...`**](../standard_functions#L677-L688) | Search command history for pattern.

###  Text Editors 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**v** | <code>vim -p "$@"</code> | Edit file with vim.
**vv** | <code>view -p "$@"</code> | View file in vim.
**n, nano1** | <code>nano --undo --a</code>[**`...`**](../standard_functions#L717-L719) | Edit file with nano.
**nv** | <code>nano --view --u</code>[**`...`**](../standard_functions#L731-L733) | View file in nano.
**g, gedit1** | <code>__runCommandInB</code>[**`...`**](../standard_functions#L737-L739) | Edit file with gedit.
**sub** | <code>__runCommandInB</code>[**`...`**](../standard_functions#L742-L744) | Edit file with sublime text.

###  Sudo 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**s** | <code>sudo "$@"</code> | Execute command as super user.
**f, please** | <code>sudo $(history </code>[**`...`**](../standard_functions#L758-L760) | Execute last command as super user.
**sudoCp** | <code>sudo cp --inter</code>[**`...`**](../standard_functions#L764-L766) | Copy files safely as super user.
**smv** | <code>sudo mv --inter</code>[**`...`**](../standard_functions#L770-L772) | Move files safely as super user.
**srm** | <code>sudo rm --inter</code>[**`...`**](../standard_functions#L777-L779) | Delete files safely as super user.
**scpdir** | <code>sudo cp --inter</code>[**`...`**](../standard_functions#L783-L785) | Copy directories safely as super user.
**smvdir** | <code>sudo mv --inter</code>[**`...`**](../standard_functions#L789-L791) | Move directories safely as super user.
**srmdir** | <code>sudo rm --inter</code>[**`...`**](../standard_functions#L796-L798) | Delete directories safely as super user.
**sm, sle** | <code>sudo less --RAW</code>[**`...`**](../standard_functions#L806-L808) | Display text or file in pager as super user.
**sv, se** | <code>sudoedit "$@"</code> | Edit file with vim as super user.
**svv** | <code>sudo view -p "$</code>[**`...`**](../standard_functions#L818-L820) | View file in vim as super user.
**sn** | <code>sudo nano --und</code>[**`...`**](../standard_functions#L832-L834) | Edit file with nano as super user.
**sg** | <code>sudo gedit  "$@</code>[**`...`**](../standard_functions#L838-L840) | Edit file with gedit as super user.

###  Procesess 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**taskManager, ht** | <code>htop  "$@"</code> | Run terminal task manager.
**ps1** | <code>ps  "$@" &#124; __pr</code>[**`...`**](../standard_functions#L927-L929) | Print users processes.
**psa, pse, processes** | <code>ps -e  "$@" &#124; _</code>[**`...`**](../standard_functions#L933-L935) | Print all processes.
**pgrep1** | <code>pgrep --list-na</code>[**`...`**](../standard_functions#L940-L942) | Find processes with part of name.
**kill1** | <code>kill -9 "$@"</code> | Kill process with kill signal.
**st, strace1, trace** | <code>strace -s\ 2000</code>[**`...`**](../standard_functions#L959-L962) | Trace system calls.

###  Text 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**he** | <code>head "$@"</code> | Print first ten lines.
**he1, firstLine** | <code>head -n1 "$@"</code> | Print first line.
**ta** | <code>tail "$@"</code> | Print last ten lines.
**ta1, lastLine** | <code>tail -n1 "$@"</code> | Print last line.
**wcl, countLines** | <code>wc -l "$@"</code> | Count lines.
**wcw, countWords** | <code>wc -w "$@"</code> | Count words.
**trd** | <code>tr --delete "$@</code>[**`...`**](../standard_functions#L1001-L1003) | Delete characters.
**loc, linesOfCode** | <code>rootDir="$PWD"</code>[**`...`**](../standard_functions#L1008-L1024) | Count lines in files with extension in working and subdirectories.

###  Tables 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**table** | <code>column -t -s "$</code>[**`...`**](../standard_functions#L1033-L1035) | Line up columns.
**cut1, keepColumns** | <code>cut --delimiter</code>[**`...`**](../standard_functions#L1041-L1043) | Keep columns.
**sort1** | <code>sort --field-se</code>[**`...`**](../standard_functions#L1049-L1051) | Sort lines by column.

###  Search 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**grep1** | <code>grep --color=au</code>[**`...`**](../standard_functions#L1064-L1066) | Print lines containing pattern.
**gr** | <code>__printLinesCon</code>[**`...`**](../standard_functions#L1070-L1073) | Print or display with pager lines containing pattern.
**grr** | <code>__printLinesCon</code>[**`...`**](../standard_functions#L1077-L1083) | Print or display with pager numbered lines containing pattern in working and subdirectories.
**lo, locate1** | <code>locate  "$1" \</code>[**`...`**](../standard_functions#L1088-L1092) | Locate files on filesystem containing pattern in their names.
**find1** | <code>find . -not -iw</code>[**`...`**](../standard_functions#L1099-L1103) | Locate files containing pattern in their names in working and sub directories.

###  Archives 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**extract** | <code>if [ -z "$1" ];</code>[**`...`**](../standard_functions#L1112-L1145) | Extract archive of any type.

###  Terminal Multiplexer 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**tm, mu** | <code>tmux  "$@"</code> | Run terminal multiplexer.
**tma, mua** | <code>tmux attach "$@</code>[**`...`**](../standard_functions#L1159-L1161) | Run terminal multiplexer and attach to last session.
**tml, mul** | <code>tmux ls</code> | List terminal multiplexers sessions.

###  System Information 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**df1** | <code>df -h &#124; grep "s</code>[**`...`**](../standard_functions#L1174-L1176) | Print available disk space in simplified form.
**du1** | <code>du --summarize </code>[**`...`**](../standard_functions#L1180-L1182) | Print disk space occupied by file or folder.
**fr, free1** | <code>echo "all:  "$(</code>[**`...`**](../standard_functions#L1185-L1192) | Print all and free memory space in megabytes.
**temp, temperature** | <code>acpi -t</code> | Print temperature of cpu.
**batt, battery** | <code>acpi</code> | Print battery status.
**uname1, kernelVersion** | <code>uname --all</code> | Print operating system information.
**pci, lspci1** | <code>lspci -v "$@" &#124;</code>[**`...`**](../standard_functions#L1212-L1214) | Print info about pci devices.

###  Power 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**reboot** | <code>sudo reboot</code> | Restart computer.
**poweroff** | <code>sudo poweroff</code> | Shut down computer.
**hib** | <code>sudo pm-hiberna</code>[**`...`**](../standard_functions#L1232-L1234) | Hibernate computer.
**sus** | <code>sudo pm-suspend</code>[**`...`**](../standard_functions#L1237-L1239) | Suspend computer.

###  Keyboard 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**uskeys** | <code>setxkbmap -layo</code>[**`...`**](../standard_functions#L1247-L1249) | Switch to american keyboard layout.
**keycode** | <code>xev "$@"</code> | Monitor keycodes of pressed keys.
**norepeat** | <code>xset -r</code> | Turn off key repeat.
**repeat** | <code>xset r</code> | Turn on key repeat.

###  Misc 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**blue** | <code>echo -en "\e]PC</code>[**`...`**](../standard_functions#L1273-L1275) | Change hue of color blue in linux terminal.
**path** | <code>echo -e ${PATH/</code>[**`...`**](../standard_functions#L1278-L1280) | List directories contained in path variable.
**bc1** | <code>gcalccmd "$@"</code> | Run terminal calculator that supports decimal numbers.
**hd1** | <code>hd  "$@" &#124; __pr</code>[**`...`**](../standard_functions#L1289-L1291) | Print hexadecimal representation of file or stream.
**profile** | <code>source /etc/pro</code>[**`...`**](../standard_functions#L1294-L1296) | Run profile script.
**vimode** | <code>set -o vi</code> | Change bash line editing to vi mode.
**emacsmode** | <code>set -o emacs</code> | Change bash line editing to emacs mode.
**ssd** | <code>sudo fstrim -v </code>[**`...`**](../standard_functions#L1309-L1311) | Trim ssd.
**typingTutor** | <code>gtypist "$@"</code> | Start typing tutor.
**extension** | <code>curl --silent f</code>[**`...`**](../standard_functions#L1319-L1324) | Describe file extension.

###  Package Management 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**ch, canhaz** | <code>if [[ "$__stand</code>[**`...`**](../standard_functions#L1332-L1338) | Install package.
**update** | <code>sudo apt-get up</code>[**`...`**](../standard_functions#L1341-L1343) | Update information about available packages.
**upgrade** | <code>sudo apt-get up</code>[**`...`**](../standard_functions#L1346-L1348) | Upgrade all packages.
**dist-upgrade** | <code>sudo apt-get di</code>[**`...`**](../standard_functions#L1353-L1355) | Upgrade all packages intelligently.
**remove** | <code>sudo apt-get re</code>[**`...`**](../standard_functions#L1359-L1361) | Remove package and all unneeded packages.
**purge** | <code>sudo apt-get pu</code>[**`...`**](../standard_functions#L1366-L1368) | Remove package and all unneeded packages together with configuration files.
**autoremove** | <code>sudo apt-get au</code>[**`...`**](../standard_functions#L1372-L1374) | Remove unneeded packages.
**installed, packages** | <code>cat /var/log/ap</code>[**`...`**](../standard_functions#L1378-L1383) | Print packages that were installed by user.
**allInstalled, allPackages** | <code>dpkg --get-sele</code>[**`...`**](../standard_functions#L1386-L1390) | Print all installed packages.
**depends** | <code>apt-cache show </code>[**`...`**](../standard_functions#L1393-L1399) | Print package dependencies.

###  Package Information 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**pd, describe** | <code>apt-cache show </code>[**`...`**](../standard_functions#L1407-L1409) | Print package description.
**ve, version** | <code># Check if pass</code>[**`...`**](../standard_functions#L1427-L1444) | Print installed and available version of package or command.
**package** | <code>call1=$(sudo wh</code>[**`...`**](../standard_functions#L1474-L1490) | Print package of installed command together with description and location.

###  Package Search 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**findPackage** | <code>apt-cache searc</code>[**`...`**](../standard_functions#L1499-L1502) | Find available packages with part of name or description.
**ap, apropos1, findCommand** | <code>apropos "$@" \</code>[**`...`**](../standard_functions#L1507-L1510) | Find installed commands with part of name or description.
**apt-file1** | <code>apt-file -x sea</code>[**`...`**](../standard_functions#L1513-L1516) | Find available packages that provide command.
**wi, whatis1** | <code># Checks if it </code>[**`...`**](../standard_functions#L1555-L1579) | Describe package or command or find available packages with part of name or command.

###  Git 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**commit** | <code>git commit -am </code>[**`...`**](../standard_functions#L1588-L1590) | Commit changed and deleted files with message.
**commitm** | <code>git commit -a "</code>[**`...`**](../standard_functions#L1594-L1596) | Commit changed and deleted files and edit message in editor.
**init** | <code>git init "$@"</code> | Initialize repository.
**push** | <code>git push "$@"</code> | Push changes to remote repository.
**pull** | <code>git pull "$@"</code> | Pull changes from remote repository.
**merge** | <code>git merge "$@"</code> | Merge specified branch with current one.
**gc, checkout** | <code>git checkout "$</code>[**`...`**](../standard_functions#L1621-L1623) | Checkout branch or file.
**gb, branch** | <code>git branch "$@"</code>[**`...`**](../standard_functions#L1626-L1628) | List branches or create new one.
**gs** | <code>git -c color.st</code>[**`...`**](../standard_functions#L1631-L1634) | Print short repository status.
**gl** | <code>git log --graph</code>[**`...`**](../standard_functions#L1638-L1640) | Display minimal log of commits.
**gll** | <code>git log --graph</code>[**`...`**](../standard_functions#L1644-L1646) | Display medium log of commits.
**glll** | <code>git log --decor</code>[**`...`**](../standard_functions#L1650-L1652) | Display log of commits.
**gu** | <code>git remote upda</code>[**`...`**](../standard_functions#L1656-L1659) | Update information about remote repository and print status.
**gd** | <code>git diff "$@"</code> | Display changes between commits.
**ga** | <code>git add "$@"</code> | Add files to repository.
**gm** | <code>git mv "$@"</code> | Move repositories files.
**gls, lsgit** | <code>git ls-files "$</code>[**`...`**](../standard_functions#L1680-L1682) | List files that are in repository.

###  Github 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**clone** | <code>git clone git@g</code>[**`...`**](../standard_functions#L1691-L1693) | Clone github project.
**origin** | <code>git remote add </code>[**`...`**](../standard_functions#L1697-L1701) | Set github project as remote repository.
**cloneAll** | <code>if [[ -z "$1" ]</code>[**`...`**](../standard_functions#L1704-L1716) | Clone all users github projects.

###  Network 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**ip1** | <code>/sbin/ifconfig </code>[**`...`**](../standard_functions#L1724-L1731) | Print internal ip.
**ip2** | <code>lynx --dump htt</code>[**`...`**](../standard_functions#L1734-L1736) | Print external ip.
**gateway** | <code>route -n \</code>[**`...`**](../standard_functions#L1739-L1744) | Print gateways ip.
**mac** | <code>ifconfig &#124; grep</code>[**`...`**](../standard_functions#L1747-L1749) | Print mac addresses of network devices.
**pa, pingAll** | <code>ping -c 1 -q $(</code>[**`...`**](../standard_functions#L1752-L1756) | Ping gateway and google.
**nmap1** | <code>if [[ $# -eq 0 </code>[**`...`**](../standard_functions#L1760-L1776) | Scan local network.
**ne, network** | <code>localIp=$(ip1)</code>[**`...`**](../standard_functions#L1804-L1835) | Print ssh port status of local devices and ping google.

###  Wireless 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**woff** | <code>sudo rfkill blo</code>[**`...`**](../standard_functions#L1843-L1848) | Block wireless device.
**won** | <code>sudo rfkill unb</code>[**`...`**](../standard_functions#L1851-L1856) | Unblock wireless device.
**wr** | <code>woff</code>[**`...`**](../standard_functions#L1859-L1862) | Reset wireless device.
**up** | <code>sudo ifconfig w</code>[**`...`**](../standard_functions#L1865-L1867) | Activate wireless interface.
**down** | <code>sudo ifconfig w</code>[**`...`**](../standard_functions#L1870-L1872) | Deactivate wireless interface.
**wlan** | <code>sudo iwlist wla</code>[**`...`**](../standard_functions#L1875-L1885) | Print wireless networks in range.

###  Internet 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**i, www, internet** | <code>__runCommandInB</code>[**`...`**](../standard_functions#L1893-L1895) | Start default browser in background.
**fire** | <code>__runCommandInB</code>[**`...`**](../standard_functions#L1898-L1900) | Start firefox in background.
**chrome** | <code>__runCommandInB</code>[**`...`**](../standard_functions#L1905-L1907) | Start chrome in background.
**lynx1** | <code>lynx -accept_al</code>[**`...`**](../standard_functions#L1913-L1915) | Start terminal web browser.

###  Audio 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**mixer** | <code>alsamixer "$@"</code> | Start terminal volume control.
**a** | <code>___setVolumeTo </code>[**`...`**](../standard_functions#L1933-L1935) | Increase volume by six decibels.
**z** | <code>___setVolumeTo </code>[**`...`**](../standard_functions#L1938-L1940) | Decrease volume by six decibels.
**aa** | <code>___setVolumeTo </code>[**`...`**](../standard_functions#L1943-L1945) | Increase volume by two decibels.
**zz** | <code>___setVolumeTo </code>[**`...`**](../standard_functions#L1948-L1950) | Decrease volume by two decibels.

###  Framework 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**fu** | <code>"${EDITOR:-nano</code>[**`...`**](../standard_functions#L1958-L1960) | Edit standard functions.
**rc, al** | <code>"${EDITOR:-nano</code>[**`...`**](../standard_functions#L1963-L1965) | Edit standard rc.

