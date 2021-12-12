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
**me, makeExecutable** | <code>if [[ ! -f "$1"</code>[**`...`**](../standard_functions#L635-L683) | Make file executable or create new bash or python script.

###  History 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**h, history1** | <code>if [ "$#" -eq 0</code>[**`...`**](../standard_functions#L692-L703) | Search command history for pattern.

###  Text Editors 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**v** | <code>vim -p "$@"</code> | Edit file with vim.
**vv** | <code>view -p "$@"</code> | View file in vim.
**n, nano1** | <code>nano --undo --a</code>[**`...`**](../standard_functions#L732-L734) | Edit file with nano.
**nv** | <code>nano --view --u</code>[**`...`**](../standard_functions#L746-L748) | View file in nano.
**g, gedit1** | <code>__runCommandInB</code>[**`...`**](../standard_functions#L752-L754) | Edit file with gedit.
**sub** | <code>__runCommandInB</code>[**`...`**](../standard_functions#L757-L759) | Edit file with sublime text.

###  Sudo 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**s** | <code>sudo "$@"</code> | Execute command as super user.
**f, please** | <code>sudo $(history </code>[**`...`**](../standard_functions#L773-L775) | Execute last command as super user.
**sudoCp** | <code>sudo cp --inter</code>[**`...`**](../standard_functions#L779-L781) | Copy files safely as super user.
**smv** | <code>sudo mv --inter</code>[**`...`**](../standard_functions#L785-L787) | Move files safely as super user.
**srm** | <code>sudo rm --inter</code>[**`...`**](../standard_functions#L792-L794) | Delete files safely as super user.
**scpdir** | <code>sudo cp --inter</code>[**`...`**](../standard_functions#L798-L800) | Copy directories safely as super user.
**smvdir** | <code>sudo mv --inter</code>[**`...`**](../standard_functions#L804-L806) | Move directories safely as super user.
**srmdir** | <code>sudo rm --inter</code>[**`...`**](../standard_functions#L811-L813) | Delete directories safely as super user.
**sm, sle** | <code>sudo less --RAW</code>[**`...`**](../standard_functions#L821-L823) | Display text or file in pager as super user.
**sv, se** | <code>sudoedit "$@"</code> | Edit file with vim as super user.
**svv** | <code>sudo view -p "$</code>[**`...`**](../standard_functions#L833-L835) | View file in vim as super user.
**sn** | <code>sudo nano --und</code>[**`...`**](../standard_functions#L847-L849) | Edit file with nano as super user.
**sg** | <code>sudo gedit  "$@</code>[**`...`**](../standard_functions#L853-L855) | Edit file with gedit as super user.

###  Procesess 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**taskManager, ht** | <code>htop  "$@"</code> | Run terminal task manager.
**ps1** | <code>ps  "$@" &#124; __pr</code>[**`...`**](../standard_functions#L942-L944) | Print users processes.
**psa, pse, processes** | <code>ps -e  "$@" &#124; _</code>[**`...`**](../standard_functions#L948-L950) | Print all processes.
**pgrep1** | <code>pgrep --list-na</code>[**`...`**](../standard_functions#L955-L957) | Find processes with part of name.
**kill1** | <code>kill -9 "$@"</code> | Kill process with kill signal.
**st, strace1, trace** | <code>strace -s\ 2000</code>[**`...`**](../standard_functions#L974-L977) | Trace system calls.

###  Text 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**he** | <code>head "$@"</code> | Print first ten lines.
**he1, firstLine** | <code>head -n1 "$@"</code> | Print first line.
**ta** | <code>tail "$@"</code> | Print last ten lines.
**ta1, lastLine** | <code>tail -n1 "$@"</code> | Print last line.
**wcl, countLines** | <code>wc -l "$@"</code> | Count lines.
**wcw, countWords** | <code>wc -w "$@"</code> | Count words.
**trd** | <code>tr --delete "$@</code>[**`...`**](../standard_functions#L1016-L1018) | Delete characters.
**loc, linesOfCode** | <code>rootDir="$PWD"</code>[**`...`**](../standard_functions#L1023-L1039) | Count lines in files with extension in working and subdirectories.

###  Tables 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**table** | <code>column -t -s "$</code>[**`...`**](../standard_functions#L1048-L1050) | Line up columns.
**cut1, keepColumns** | <code>cut --delimiter</code>[**`...`**](../standard_functions#L1056-L1058) | Keep columns.
**sort1** | <code>sort --field-se</code>[**`...`**](../standard_functions#L1064-L1066) | Sort lines by column.

###  Search 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**grep1** | <code>grep --color=au</code>[**`...`**](../standard_functions#L1079-L1081) | Print lines containing pattern.
**gr** | <code>__printLinesCon</code>[**`...`**](../standard_functions#L1085-L1088) | Print or display with pager lines containing pattern.
**grr** | <code>__printLinesCon</code>[**`...`**](../standard_functions#L1092-L1098) | Print or display with pager numbered lines containing pattern in working and subdirectories.
**lo, locate1** | <code>locate  "$1" \</code>[**`...`**](../standard_functions#L1103-L1107) | Locate files on filesystem containing pattern in their names.
**find1** | <code>find . -not -iw</code>[**`...`**](../standard_functions#L1114-L1118) | Locate files containing pattern in their names in working and sub directories.

###  Archives 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**extract** | <code>if [ -z "$1" ];</code>[**`...`**](../standard_functions#L1127-L1160) | Extract archive of any type.

###  Terminal Multiplexer 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**tm, mu** | <code>tmux  "$@"</code> | Run terminal multiplexer.
**tma, mua** | <code>tmux attach "$@</code>[**`...`**](../standard_functions#L1174-L1176) | Run terminal multiplexer and attach to last session.
**tml, mul** | <code>tmux ls</code> | List terminal multiplexers sessions.

###  System Information 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**df1** | <code>df -h &#124; grep "s</code>[**`...`**](../standard_functions#L1189-L1191) | Print available disk space in simplified form.
**du1** | <code>du --summarize </code>[**`...`**](../standard_functions#L1195-L1197) | Print disk space occupied by file or folder.
**fr, free1** | <code>echo "all:  "$(</code>[**`...`**](../standard_functions#L1200-L1207) | Print all and free memory space in megabytes.
**temp, temperature** | <code>acpi -t</code> | Print temperature of cpu.
**batt, battery** | <code>acpi</code> | Print battery status.
**uname1, kernelVersion** | <code>uname --all</code> | Print operating system information.
**pci, lspci1** | <code>lspci -v "$@" &#124;</code>[**`...`**](../standard_functions#L1227-L1229) | Print info about pci devices.

###  Power 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**reboot** | <code>sudo reboot</code> | Restart computer.
**poweroff** | <code>sudo poweroff</code> | Shut down computer.
**hib** | <code>sudo pm-hiberna</code>[**`...`**](../standard_functions#L1247-L1249) | Hibernate computer.
**sus** | <code>sudo pm-suspend</code>[**`...`**](../standard_functions#L1252-L1254) | Suspend computer.

###  Keyboard 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**uskeys** | <code>setxkbmap -layo</code>[**`...`**](../standard_functions#L1262-L1264) | Switch to american keyboard layout.
**keycode** | <code>xev "$@"</code> | Monitor keycodes of pressed keys.
**norepeat** | <code>xset -r</code> | Turn off key repeat.
**repeat** | <code>xset r</code> | Turn on key repeat.

###  Misc 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**blue** | <code>echo -en "\e]PC</code>[**`...`**](../standard_functions#L1288-L1290) | Change hue of color blue in linux terminal.
**path** | <code>echo -e ${PATH/</code>[**`...`**](../standard_functions#L1293-L1295) | List directories contained in path variable.
**bc1** | <code>gcalccmd "$@"</code> | Run terminal calculator that supports decimal numbers.
**hd1** | <code>hd  "$@" &#124; __pr</code>[**`...`**](../standard_functions#L1304-L1306) | Print hexadecimal representation of file or stream.
**profile** | <code>source /etc/pro</code>[**`...`**](../standard_functions#L1309-L1311) | Run profile script.
**vimode** | <code>set -o vi</code> | Change bash line editing to vi mode.
**emacsmode** | <code>set -o emacs</code> | Change bash line editing to emacs mode.
**ssd** | <code>sudo fstrim -v </code>[**`...`**](../standard_functions#L1324-L1326) | Trim ssd.
**typingTutor** | <code>gtypist "$@"</code> | Start typing tutor.
**extension** | <code>curl --silent f</code>[**`...`**](../standard_functions#L1334-L1339) | Describe file extension.

###  Package Management 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**ch, canhaz** | <code>if [[ "$__stand</code>[**`...`**](../standard_functions#L1347-L1353) | Install package.
**update** | <code>sudo apt-get up</code>[**`...`**](../standard_functions#L1356-L1358) | Update information about available packages.
**upgrade** | <code>sudo apt-get up</code>[**`...`**](../standard_functions#L1361-L1363) | Upgrade all packages.
**dist-upgrade** | <code>sudo apt-get di</code>[**`...`**](../standard_functions#L1368-L1370) | Upgrade all packages intelligently.
**remove** | <code>sudo apt-get re</code>[**`...`**](../standard_functions#L1374-L1376) | Remove package and all unneeded packages.
**purge** | <code>sudo apt-get pu</code>[**`...`**](../standard_functions#L1381-L1383) | Remove package and all unneeded packages together with configuration files.
**autoremove** | <code>sudo apt-get au</code>[**`...`**](../standard_functions#L1387-L1389) | Remove unneeded packages.
**installed, packages** | <code>cat /var/log/ap</code>[**`...`**](../standard_functions#L1393-L1398) | Print packages that were installed by user.
**allInstalled, allPackages** | <code>dpkg --get-sele</code>[**`...`**](../standard_functions#L1401-L1405) | Print all installed packages.
**depends** | <code>apt-cache show </code>[**`...`**](../standard_functions#L1408-L1414) | Print package dependencies.

###  Package Information 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**pd, describe** | <code>apt-cache show </code>[**`...`**](../standard_functions#L1422-L1424) | Print package description.
**ve, version** | <code># Check if pass</code>[**`...`**](../standard_functions#L1442-L1459) | Print installed and available version of package or command.
**package** | <code>call1=$(sudo wh</code>[**`...`**](../standard_functions#L1489-L1505) | Print package of installed command together with description and location.

###  Package Search 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**findPackage** | <code>apt-cache searc</code>[**`...`**](../standard_functions#L1514-L1517) | Find available packages with part of name or description.
**ap, apropos1, findCommand** | <code>apropos "$@" \</code>[**`...`**](../standard_functions#L1522-L1525) | Find installed commands with part of name or description.
**apt-file1** | <code>apt-file -x sea</code>[**`...`**](../standard_functions#L1528-L1531) | Find available packages that provide command.
**wi, whatis1** | <code># Checks if it </code>[**`...`**](../standard_functions#L1570-L1594) | Describe package or command or find available packages with part of name or command.

###  Git 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**commit** | <code>git commit -am </code>[**`...`**](../standard_functions#L1603-L1605) | Commit changed and deleted files with message.
**commitm** | <code>git commit -a "</code>[**`...`**](../standard_functions#L1609-L1611) | Commit changed and deleted files and edit message in editor.
**init** | <code>git init "$@"</code> | Initialize repository.
**push** | <code>git push "$@"</code> | Push changes to remote repository.
**pull** | <code>git pull "$@"</code> | Pull changes from remote repository.
**merge** | <code>git merge "$@"</code> | Merge specified branch with current one.
**gc, checkout** | <code>git checkout "$</code>[**`...`**](../standard_functions#L1636-L1638) | Checkout branch or file.
**gb, branch** | <code>git branch "$@"</code>[**`...`**](../standard_functions#L1641-L1643) | List branches or create new one.
**gs** | <code>git -c color.st</code>[**`...`**](../standard_functions#L1646-L1649) | Print short repository status.
**gl** | <code>git log --graph</code>[**`...`**](../standard_functions#L1653-L1655) | Display minimal log of commits.
**gll** | <code>git log --graph</code>[**`...`**](../standard_functions#L1659-L1661) | Display medium log of commits.
**glll** | <code>git log --decor</code>[**`...`**](../standard_functions#L1665-L1667) | Display log of commits.
**gu** | <code>git remote upda</code>[**`...`**](../standard_functions#L1671-L1674) | Update information about remote repository and print status.
**gd** | <code>git diff "$@"</code> | Display changes between commits.
**ga** | <code>git add "$@"</code> | Add files to repository.
**gm** | <code>git mv "$@"</code> | Move repositories files.
**gls, lsgit** | <code>git ls-files "$</code>[**`...`**](../standard_functions#L1695-L1697) | List files that are in repository.

###  Github 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**clone** | <code>git clone git@g</code>[**`...`**](../standard_functions#L1706-L1708) | Clone github project.
**origin** | <code>git remote add </code>[**`...`**](../standard_functions#L1712-L1716) | Set github project as remote repository.
**cloneAll** | <code>if [[ -z "$1" ]</code>[**`...`**](../standard_functions#L1719-L1731) | Clone all users github projects.

###  Network 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**ip1** | <code>/sbin/ifconfig </code>[**`...`**](../standard_functions#L1739-L1746) | Print internal ip.
**ip2** | <code>lynx --dump htt</code>[**`...`**](../standard_functions#L1749-L1751) | Print external ip.
**gateway** | <code>route -n \</code>[**`...`**](../standard_functions#L1754-L1759) | Print gateways ip.
**mac** | <code>ifconfig &#124; grep</code>[**`...`**](../standard_functions#L1762-L1764) | Print mac addresses of network devices.
**pa, pingAll** | <code>ping -c 1 -q $(</code>[**`...`**](../standard_functions#L1767-L1771) | Ping gateway and google.
**nmap1** | <code>if [[ $# -eq 0 </code>[**`...`**](../standard_functions#L1775-L1791) | Scan local network.
**ne, network** | <code>localIp=$(ip1)</code>[**`...`**](../standard_functions#L1819-L1850) | Print ssh port status of local devices and ping google.

###  Wireless 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**woff** | <code>sudo rfkill blo</code>[**`...`**](../standard_functions#L1858-L1863) | Block wireless device.
**won** | <code>sudo rfkill unb</code>[**`...`**](../standard_functions#L1866-L1871) | Unblock wireless device.
**wr** | <code>woff</code>[**`...`**](../standard_functions#L1874-L1877) | Reset wireless device.
**up** | <code>sudo ifconfig w</code>[**`...`**](../standard_functions#L1880-L1882) | Activate wireless interface.
**down** | <code>sudo ifconfig w</code>[**`...`**](../standard_functions#L1885-L1887) | Deactivate wireless interface.
**wlan** | <code>sudo iwlist wla</code>[**`...`**](../standard_functions#L1890-L1900) | Print wireless networks in range.

###  Internet 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**i, www, internet** | <code>__runCommandInB</code>[**`...`**](../standard_functions#L1908-L1910) | Start default browser in background.
**fire** | <code>__runCommandInB</code>[**`...`**](../standard_functions#L1913-L1915) | Start firefox in background.
**chrome** | <code>__runCommandInB</code>[**`...`**](../standard_functions#L1920-L1922) | Start chrome in background.
**lynx1** | <code>lynx -accept_al</code>[**`...`**](../standard_functions#L1928-L1930) | Start terminal web browser.

###  Audio 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**mixer** | <code>alsamixer "$@"</code> | Start terminal volume control.
**a** | <code>___setVolumeTo </code>[**`...`**](../standard_functions#L1948-L1950) | Increase volume by six decibels.
**z** | <code>___setVolumeTo </code>[**`...`**](../standard_functions#L1953-L1955) | Decrease volume by six decibels.
**aa** | <code>___setVolumeTo </code>[**`...`**](../standard_functions#L1958-L1960) | Increase volume by two decibels.
**zz** | <code>___setVolumeTo </code>[**`...`**](../standard_functions#L1963-L1965) | Decrease volume by two decibels.

###  Framework 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**fu** | <code>"${EDITOR:-nano</code>[**`...`**](../standard_functions#L1973-L1975) | Edit standard functions.
**rc, al** | <code>"${EDITOR:-nano</code>[**`...`**](../standard_functions#L1978-L1980) | Edit standard rc.

