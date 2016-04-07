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
**nf, newest** | `ls -pt | grep -`[**`...`**](../standard_functions#L270-L272) | Print name of newest file in directory.
**rf, randomFile** | `ls -pt | grep -`[**`...`**](../standard_functions#L275-L277) | Print name of random file in directory.
**findd, directories** | `find . -name .g`[**`...`**](../standard_functions#L282-L284) | Print all subdirectories.
**extensions** | `find . -type f `[**`...`**](../standard_functions#L286-L288) | Print all file extensions.

###  Tree 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**t, tree1** | `tree -C -I .git`[**`...`**](../standard_functions#L300-L302) | Print directory structure.
**tt** | `clear`[**`...`**](../standard_functions#L304-L307) | Clear screen andprint directory structure.

###  Cd 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**.., cd..** | `___goUpNumberOf`[**`...`**](../standard_functions#L333-L335) | Go up one directory.
**...** | `___goUpNumberOf`[**`...`**](../standard_functions#L337-L339) | Go up two directories.
**....** | `___goUpNumberOf`[**`...`**](../standard_functions#L341-L343) | Go up three directories.
**.....** | `___goUpNumberOf`[**`...`**](../standard_functions#L345-L347) | Go up four directories.
**......** | `___goUpNumberOf`[**`...`**](../standard_functions#L349-L351) | Go up five directories.
**.......** | `___goUpNumberOf`[**`...`**](../standard_functions#L353-L355) | Go up six directories.
**cdiso** | `sudo mkdir /med`[**`...`**](../standard_functions#L358-L362) | Mount iso and cd into.

###  Files 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**cp** | `cp --interactiv`[**`...`**](../standard_functions#L371-L373) | Copy files safely.
**mv** | `mv --interactiv`[**`...`**](../standard_functions#L377-L379) | Move files safely.
**rm** | `rm --interactiv`[**`...`**](../standard_functions#L384-L386) | Delete files safely.
**cpdir** | `cp --interactiv`[**`...`**](../standard_functions#L390-L392) | Copy directories safely.
**mvdir** | `mv --interactiv`[**`...`**](../standard_functions#L396-L398) | Move directories safely.
**rmdir** | `rm --interactiv`[**`...`**](../standard_functions#L403-L405) | Delete directories safely.
**mk, md, mkdir1** | `mkdir --parents`[**`...`**](../standard_functions#L409-L412) | Create directory and descend into.
**bk, backup** | `sudo cp --prese`[**`...`**](../standard_functions#L416-L418) | Backup file.
**switch** | `tempFile=$(mkte`[**`...`**](../standard_functions#L421-L426) | Switch contents of files.

###  Pwd 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**p** | `if [[ $# -eq 0 `[**`...`**](../standard_functions#L435-L441) | Print working directory or path to file.

###  Echo 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**e** | `echo "$@"` | Print text.
**ee** | `echo -e "$@"` | Print text interpreting backslashed characters.
**en** | `echo -n "$@"` | Print text without trailing newline.

###  Run In Background 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**rb, runInBackground** | `nohup "$@" &>/d`[**`...`**](../standard_functions#L470-L472) | Run command in background.

###  Basics 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**ef, editFunctions** | `"$EDITOR" ~/.st`[**`...`**](../standard_functions#L481-L483) | Edit standard aliases.
**er, editUsersRc** | `"$EDITOR" ~/.st`[**`...`**](../standard_functions#L485-L487) | Edit users standard rc.
**er1, editProjectsRc** | `projectLocation`[**`...`**](../standard_functions#L489-L492) | Edit projects standard rc.
**ba** | `bash "$@"` | Start new bash shell.
**ty, type1** | `# Checks if com`[**`...`**](../standard_functions#L531-L551) | Print command type or definition.
**c** | `cat "$@"` | Print file contents.
**?** | `echo $?` | Print exit code of last command.
**cl, clr** | `clear` | Clear the screen.
**re** | `reset "$@"` | Reset the screen.
**q** | `exit` | Exit bash shell.
**o, openFile** | `__runCommandInB`[**`...`**](../standard_functions#L581-L583) | Open file with default app.
**te, terminal** | `x-terminal-emul`[**`...`**](../standard_functions#L586-L588) | Open new terminal with same working directory.
**to** | `touch  "$@"` | Update files timestamp or create new one.
**da** | `date  "$@"` | Print date and time.
**ma, make1** | `make  "$@" 2>&1`[**`...`**](../standard_functions#L606-L610) | Run make with pager.
**na, explorer** | `__runCommandInB`[**`...`**](../standard_functions#L618-L620) | Start file explorer in background in working directory.
**diff1** | `colordiff  "$@"`[**`...`**](../standard_functions#L624-L626) | Compare files line by line in color.
**me, makeExecutable** | `if [[ ! -f "$1"`[**`...`**](../standard_functions#L630-L663) | Make file executable or create new bash or python script.

###  History 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**h, history1** | `if [ "$#" -eq 0`[**`...`**](../standard_functions#L672-L683) | Search command history for pattern.

###  Text Editors 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**v** | `vim -p "$@"` | Edit file with vim.
**vv** | `view -p "$@"` | View file in vim.
**n, nano1** | `nano --undo --a`[**`...`**](../standard_functions#L712-L714) | Edit file with nano.
**nv** | `nano --view --u`[**`...`**](../standard_functions#L726-L728) | View file in nano.
**g, gedit1** | `__runCommandInB`[**`...`**](../standard_functions#L732-L734) | Edit file with gedit.
**sub** | `__runCommandInB`[**`...`**](../standard_functions#L737-L739) | Edit file with sublime text.

###  Sudo 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**s** | `sudo "$@"` | Execute command as super user.
**f, please** | `sudo $(history `[**`...`**](../standard_functions#L753-L755) | Execute last command as super user.
**sudoCp** | `sudo cp --inter`[**`...`**](../standard_functions#L759-L761) | Copy files safely as super user.
**smv** | `sudo mv --inter`[**`...`**](../standard_functions#L765-L767) | Move files safely as super user.
**srm** | `sudo rm --inter`[**`...`**](../standard_functions#L772-L774) | Delete files safely as super user.
**scpdir** | `sudo cp --inter`[**`...`**](../standard_functions#L778-L780) | Copy directories safely as super user.
**smvdir** | `sudo mv --inter`[**`...`**](../standard_functions#L784-L786) | Move directories safely as super user.
**srmdir** | `sudo rm --inter`[**`...`**](../standard_functions#L791-L793) | Delete directories safely as super user.
**sm, sle** | `sudo less --RAW`[**`...`**](../standard_functions#L801-L803) | Display text or file in pager as super user.
**sv, se** | `sudoedit "$@"` | Edit file with vim as super user.
**svv** | `sudo view -p "$`[**`...`**](../standard_functions#L813-L815) | View file in vim as super user.
**sn** | `sudo nano --und`[**`...`**](../standard_functions#L827-L829) | Edit file with nano as super user.
**sg** | `sudo gedit  "$@`[**`...`**](../standard_functions#L833-L835) | Edit file with gedit as super user.

###  Procesess 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**taskManager, ht** | `htop  "$@"` | Run terminal task manager.
**ps1** | `ps  "$@" | __pr`[**`...`**](../standard_functions#L922-L924) | Print users processes.
**psa, pse, processes** | `ps -e  "$@" | _`[**`...`**](../standard_functions#L928-L930) | Print all processes.
**pgrep1** | `pgrep --list-na`[**`...`**](../standard_functions#L935-L937) | Find processes with part of name.
**kill1** | `kill -9 "$@"` | Kill process with kill signal.
**st, strace1, trace** | `strace -s\ 2000`[**`...`**](../standard_functions#L954-L957) | Trace system calls.

###  Text 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**he** | `head "$@"` | Print first ten lines.
**he1, firstLine** | `head -n1 "$@"` | Print first line.
**ta** | `tail "$@"` | Print last ten lines.
**ta1, lastLine** | `tail -n1 "$@"` | Print last line.
**wcl, countLines** | `wc -l "$@"` | Count lines.
**wcw, countWords** | `wc -w "$@"` | Count words.
**trd** | `tr --delete "$@`[**`...`**](../standard_functions#L996-L998) | Delete characters.
**loc, linesOfCode** | `rootDir="$PWD"`[**`...`**](../standard_functions#L1003-L1019) | Count lines in files with extension in working and subdirectories.

###  Tables 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**table** | `column -t -s "$`[**`...`**](../standard_functions#L1028-L1030) | Line up columns.
**cut1, keepColumns** | `cut --delimiter`[**`...`**](../standard_functions#L1036-L1038) | Keep columns.
**sort1** | `sort --field-se`[**`...`**](../standard_functions#L1044-L1046) | Sort lines by column.

###  Search 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**grep1** | `grep --color=au`[**`...`**](../standard_functions#L1059-L1061) | Print lines containing pattern.
**gr** | `__printLinesCon`[**`...`**](../standard_functions#L1065-L1068) | Print or display with pager lines containing pattern.
**grr** | `__printLinesCon`[**`...`**](../standard_functions#L1072-L1078) | Print or display with pager numbered lines containing pattern in working and subdirectories.
**lo, locate1** | `locate  "$1" \`[**`...`**](../standard_functions#L1083-L1087) | Locate files on filesystem containing pattern in their names.
**find1** | `find . -not -iw`[**`...`**](../standard_functions#L1094-L1098) | Locate files containing pattern in their names in working and sub directories.

###  Archives 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**extract** | `if [ -z "$1" ];`[**`...`**](../standard_functions#L1107-L1140) | Extract archive of any type.

###  Terminal Multiplexer 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**tm, mu** | `tmux  "$@"` | Run terminal multiplexer.
**tma, mua** | `tmux attach "$@`[**`...`**](../standard_functions#L1154-L1156) | Run terminal multiplexer and attach to last session.
**tml, mul** | `tmux ls` | List terminal multiplexers sessions.

###  System Information 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**df1** | `df -h | grep "s`[**`...`**](../standard_functions#L1169-L1171) | Print available disk space in simplified form.
**du1** | `du --summarize `[**`...`**](../standard_functions#L1175-L1177) | Print disk space occupied by file or folder.
**fr, free1** | `echo "all:  "$(`[**`...`**](../standard_functions#L1180-L1187) | Print all and free memory space in megabytes.
**temp, temperature** | `acpi -t` | Print temperature of cpu.
**batt, battery** | `acpi` | Print battery status.
**uname1, kernelVersion** | `uname --all` | Print operating system information.
**pci, lspci1** | `lspci -v "$@" |`[**`...`**](../standard_functions#L1207-L1209) | Print info about pci devices.

###  Power 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**reboot** | `sudo reboot` | Restart computer.
**poweroff** | `sudo poweroff` | Shut down computer.
**hib** | `sudo pm-hiberna`[**`...`**](../standard_functions#L1227-L1229) | Hibernate computer.
**sus** | `sudo pm-suspend`[**`...`**](../standard_functions#L1232-L1234) | Suspend computer.

###  Keyboard 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**uskeys** | `setxkbmap -layo`[**`...`**](../standard_functions#L1242-L1244) | Switch to american keyboard layout.
**keycode** | `xev "$@"` | Monitor keycodes of pressed keys.
**norepeat** | `xset -r` | Turn off key repeat.
**repeat** | `xset r` | Turn on key repeat.

###  Misc 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**blue** | `echo -en "\e]PC`[**`...`**](../standard_functions#L1268-L1270) | Change hue of color blue in linux terminal.
**path** | `echo -e ${PATH/`[**`...`**](../standard_functions#L1273-L1275) | List directories contained in path variable.
**bc1** | `gcalccmd "$@"` | Run terminal calculator that supports decimal numbers.
**hd1** | `hd  "$@" | __pr`[**`...`**](../standard_functions#L1284-L1286) | Print hexadecimal representation of file or stream.
**profile** | `source /etc/pro`[**`...`**](../standard_functions#L1289-L1291) | Run profile script.
**vimode** | `set -o vi` | Change bash line editing to vi mode.
**emacsmode** | `set -o emacs` | Change bash line editing to emacs mode.
**ssd** | `sudo fstrim -v `[**`...`**](../standard_functions#L1304-L1306) | Trim ssd.
**typingTutor** | `gtypist "$@"` | Start typing tutor.

###  Package Management 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**ch, canhaz** | `sudo apt-get in`[**`...`**](../standard_functions#L1319-L1321) | Install package.
**update** | `sudo apt-get up`[**`...`**](../standard_functions#L1324-L1326) | Update information about available packages.
**upgrade** | `sudo apt-get up`[**`...`**](../standard_functions#L1329-L1331) | Upgrade all packages.
**dist-upgrade** | `sudo apt-get di`[**`...`**](../standard_functions#L1336-L1338) | Upgrade all packages intelligently.
**remove** | `sudo apt-get re`[**`...`**](../standard_functions#L1342-L1344) | Remove package and all unneeded packages.
**purge** | `sudo apt-get pu`[**`...`**](../standard_functions#L1349-L1351) | Remove package and all unneeded packages together with configuration files.
**autoremove** | `sudo apt-get au`[**`...`**](../standard_functions#L1355-L1357) | Remove unneeded packages.
**installed, packages** | `cat /var/log/ap`[**`...`**](../standard_functions#L1361-L1366) | Print packages that were installed by user.
**allInstalled, allPackages** | `dpkg --get-sele`[**`...`**](../standard_functions#L1369-L1373) | Print all installed packages.
**depends** | `apt-cache show `[**`...`**](../standard_functions#L1376-L1382) | Print package dependencies.

###  Package Information 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**pd, describe** | `apt-cache show `[**`...`**](../standard_functions#L1390-L1392) | Print package description.
**ve, version** | `# Check if pass`[**`...`**](../standard_functions#L1410-L1427) | Print installed and available version of package or command.
**package** | `call1=$(sudo wh`[**`...`**](../standard_functions#L1457-L1473) | Print package of installed command together with description and location.

###  Package Search 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**findPackage** | `apt-cache searc`[**`...`**](../standard_functions#L1482-L1485) | Find available packages with part of name or description.
**ap, apropos1, findCommand** | `apropos "$@" \`[**`...`**](../standard_functions#L1490-L1493) | Find installed commands with part of name or description.
**apt-file1** | `apt-file -x sea`[**`...`**](../standard_functions#L1496-L1499) | Find available packages that provide command.
**wi, whatis1** | `# Checks if it `[**`...`**](../standard_functions#L1538-L1562) | Describe package or command or find available packages with part of name or command.

###  Git 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**commit** | `git commit -am `[**`...`**](../standard_functions#L1571-L1573) | Commit changed and deleted files with message.
**commitm** | `git commit -a "`[**`...`**](../standard_functions#L1577-L1579) | Commit changed and deleted files and edit message in editor.
**init** | `git init "$@"` | Initialize repository.
**push** | `git push "$@"` | Push changes to remote repository.
**pull** | `git pull "$@"` | Pull changes from remote repository.
**merge** | `git merge "$@"` | Merge specified branch with current one.
**gc, checkout** | `git checkout "$`[**`...`**](../standard_functions#L1604-L1606) | Checkout branch or file.
**gb, branch** | `git branch "$@"`[**`...`**](../standard_functions#L1609-L1611) | List branches or create new one.
**gs** | `git -c color.st`[**`...`**](../standard_functions#L1614-L1617) | Print short repository status.
**gl** | `git log --graph`[**`...`**](../standard_functions#L1621-L1623) | Display minimal log of commits.
**gll** | `git log --graph`[**`...`**](../standard_functions#L1627-L1629) | Display medium log of commits.
**glll** | `git log --decor`[**`...`**](../standard_functions#L1633-L1635) | Display log of commits.
**gu** | `git remote upda`[**`...`**](../standard_functions#L1639-L1642) | Update information about remote repository and print status.
**gd** | `git diff "$@"` | Display changes between commits.
**ga** | `git add "$@"` | Add files to repository.
**gm** | `git mv "$@"` | Move repositories files.
**gls, lsgit** | `git ls-files "$`[**`...`**](../standard_functions#L1663-L1665) | List files that are in repository.

###  Github 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**clone** | `git clone git@g`[**`...`**](../standard_functions#L1674-L1676) | Clone github project.
**origin** | `git remote add `[**`...`**](../standard_functions#L1680-L1684) | Set github project as remote repository.
**cloneAll** | `if [[ -z "$1" ]`[**`...`**](../standard_functions#L1687-L1699) | Clone all users github projects.

###  Network 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**ip1** | `/sbin/ifconfig `[**`...`**](../standard_functions#L1707-L1714) | Print internal ip.
**ip2** | `lynx --dump htt`[**`...`**](../standard_functions#L1717-L1719) | Print external ip.
**gateway** | `route -n \`[**`...`**](../standard_functions#L1722-L1727) | Print gateways ip.
**mac** | `ifconfig | grep`[**`...`**](../standard_functions#L1730-L1732) | Print mac addresses of network devices.
**pa, pingAll** | `ping -c 1 -q $(`[**`...`**](../standard_functions#L1735-L1739) | Ping gateway and google.
**nmap1** | `if [[ $# -eq 0 `[**`...`**](../standard_functions#L1743-L1759) | Scan local network.
**ne, network** | `localIp=$(ip1)`[**`...`**](../standard_functions#L1787-L1818) | Print ssh port status of local devices and ping google.

###  Wireless 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**woff** | `sudo rfkill blo`[**`...`**](../standard_functions#L1826-L1831) | Block wireless device.
**won** | `sudo rfkill unb`[**`...`**](../standard_functions#L1834-L1839) | Unblock wireless device.
**wr** | `woff`[**`...`**](../standard_functions#L1842-L1845) | Reset wireless device.
**up** | `sudo ifconfig w`[**`...`**](../standard_functions#L1848-L1850) | Activate wireless interface.
**down** | `sudo ifconfig w`[**`...`**](../standard_functions#L1853-L1855) | Deactivate wireless interface.
**wlan** | `sudo iwlist wla`[**`...`**](../standard_functions#L1858-L1868) | Print wireless networks in range.

###  Internet 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**i, www, internet** | `__runCommandInB`[**`...`**](../standard_functions#L1876-L1878) | Start default browser in background.
**fire** | `__runCommandInB`[**`...`**](../standard_functions#L1881-L1883) | Start firefox in background.
**chrome** | `__runCommandInB`[**`...`**](../standard_functions#L1888-L1890) | Start chrome in background.
**lynx1** | `lynx -accept_al`[**`...`**](../standard_functions#L1896-L1898) | Start terminal web browser.

###  Audio 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**mixer** | `alsamixer "$@"` | Start terminal volume control.
**a** | `___setVolumeTo `[**`...`**](../standard_functions#L1916-L1918) | Increase volume by six decibels.
**z** | `___setVolumeTo `[**`...`**](../standard_functions#L1921-L1923) | Decrease volume by six decibels.
**aa** | `___setVolumeTo `[**`...`**](../standard_functions#L1926-L1928) | Increase volume by two decibels.
**zz** | `___setVolumeTo `[**`...`**](../standard_functions#L1931-L1933) | Decrease volume by two decibels.

###  Framework 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**fu** | `"${EDITOR:-nano`[**`...`**](../standard_functions#L1941-L1943) | Edit standard functions.
**rc, al** | `"${EDITOR:-nano`[**`...`**](../standard_functions#L1946-L1948) | Edit standard rc.

