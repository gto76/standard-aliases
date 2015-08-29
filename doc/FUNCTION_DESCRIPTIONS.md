Commands
========

###  Less 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**le, less1** | `less --RAW-CONT`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L27-L29) | Display text or file in pager.
**m** | `___printOrDispl`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L82-L84) | Print or display text or file in pager.

###  Ls 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**l** | `___displayOutpu`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L184-L187) | List or display directory contents in pager using short listing format.
**ll** | `___displayOutpu`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L189-L192) | List or display directory contents in pager using medium listing format.
**lll** | `___displayOutpu`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L194-L197) | List or display directory contents in pager using long listing format.
**la** | `__listOrDisplay`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L199-L202) | List or display all directory contents in pager using short listing format.
**lla** | `__listOrDisplay`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L204-L207) | List or display all directory contents in pager using medium listing format.
**llla** | `__listOrDisplay`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L209-L212) | List or display all directory contents in pager using long listing format.
**lt** | `__listOrDisplay`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L214-L217) | List or display directory contents in pager ordered by date using short listing format.
**llt** | `__listOrDisplay`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L219-L222) | List or display directory contents in pager ordered by date using medium listing format.
**lllt** | `__listOrDisplay`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L224-L227) | List or display directory contents in pager ordered by date using long listing format.
**dl** | `__listOrDisplay`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L229-L232) | List or display matching directories in pager using short listing format.
**dll** | `__listOrDisplay`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L234-L237) | List or display matching directories in pager using medium listing format.
**dlll** | `__listOrDisplay`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L239-L242) | List or display matching directories in pager using long listing format.
**l1** | `__listOrDisplay`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L244-L247) | List or display in pager one directory item per line using short listing format.
**la1** | `__listOrDisplay`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L249-L252) | List or display in pager one directory item per line including hidden files using short listing format.
**first** | `ls "$@" | head `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L255-L257) | List first file in directory.
**nf, newest** | `ls -pt | grep -`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L260-L262) | Print name of newest file in directory.
**rf, randomFile** | `ls -pt | grep -`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L265-L267) | Print name of random file in directory.
**findd, directories** | `find . -name .g`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L272-L274) | Print all subdirectories.

###  Tree 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**t, tree1** | `tree -C -I .git`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L286-L288) | Print directory structure.
**tt** | `clear`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L290-L293) | Clear screen andprint directory structure.

###  Cd 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**.., cd..** | `___goUpNumberOf`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L319-L321) | Go up one directory.
**...** | `___goUpNumberOf`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L323-L325) | Go up two directories.
**....** | `___goUpNumberOf`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L327-L329) | Go up three directories.
**.....** | `___goUpNumberOf`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L331-L333) | Go up four directories.
**......** | `___goUpNumberOf`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L335-L337) | Go up five directories.
**.......** | `___goUpNumberOf`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L339-L341) | Go up six directories.
**cdiso** | `sudo mkdir /med`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L344-L348) | Mount iso and cd into.

###  Files 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**cp** | `cp --interactiv`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L357-L359) | Copy files safely.
**mv** | `mv --interactiv`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L363-L365) | Move files safely.
**rm** | `rm --interactiv`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L370-L372) | Delete files safely.
**cpdir** | `cp --interactiv`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L376-L378) | Copy directories safely.
**mvdir** | `mv --interactiv`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L382-L384) | Move directories safely.
**rmdir** | `rm --interactiv`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L389-L391) | Delete directories safely.
**mk, md, mkdir1** | `mkdir --parents`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L395-L398) | Create directory and descend into.
**bk, backup** | `sudo cp --prese`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L402-L404) | Backup file.
**switch** | `tempFile=$(mkte`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L407-L412) | Switch contents of files.

###  Pwd 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**p** | `if [[ $# -eq 0 `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L421-L427) | Print working directory or path to file.

###  Echo 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**e** | `echo "$@"` | Print text.
**ee** | `echo -e "$@"` | Print text interpreting backslashed characters.
**en** | `echo -n "$@"` | Print text without trailing newline.

###  Run In Background 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**rb, runInBackground** | `nohup "$@" &>/d`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L456-L458) | Run command in background.

###  Basics 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**ef, editFunctions** | `"$EDITOR" ~/.st`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L467-L469) | Edit standard aliases.
**er, editUsersRc** | `"$EDITOR" ~/.st`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L471-L473) | Edit users standard rc.
**er1, editProjectsRc** | `projectLocation`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L475-L478) | Edit projects standard rc.
**ba** | `bash "$@"` | Start new bash shell.
**ty, type1** | `# Checks if com`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L517-L537) | Print command type or definition.
**c** | `cat "$@"` | Print file contents.
**?** | `echo $?` | Print exit code of last command.
**cl, clr** | `clear` | Clear the screen.
**re** | `reset "$@"` | Reset the screen.
**q** | `exit` | Exit bash shell.
**o, openFile** | `__runCommandInB`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L567-L569) | Open file with default app.
**te, terminal** | `x-terminal-emul`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L572-L574) | Open new terminal with same working directory.
**to** | `touch  "$@"` | Update files timestamp or create new one.
**da** | `date  "$@"` | Print date and time.
**ma, make1** | `make  "$@" 2>&1`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L592-L594) | Run make with pager.
**na, explorer** | `__runCommandInB`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L602-L604) | Start file explorer in background in working directory.
**diff1** | `colordiff  "$@"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L608-L610) | Compare files line by line in color.
**me, makeExecutable** | `if [[ ! -f "$1"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L614-L643) | Make file executable or create new bash or python script.

###  History 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**h, history1** | `if [ "$#" -eq 0`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L652-L661) | Search command history for pattern.

###  Text Editors 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**v** | `vim -p "$@"` | Edit file with vim.
**vv** | `view -p "$@"` | View file in vim.
**n, nano1** | `nano --undo --a`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L690-L692) | Edit file with nano.
**nv** | `nano --view --u`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L704-L706) | View file in nano.
**g, gedit1** | `__runCommandInB`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L710-L712) | Edit file with gedit.
**sub** | `__runCommandInB`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L715-L717) | Edit file with sublime text.

###  Sudo 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**s** | `sudo "$@"` | Execute command as super user.
**f, fuck** | `sudo $(history `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L731-L733) | Execute last command as super user.
**sudoCp** | `sudo cp --inter`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L737-L739) | Copy files safely as super user.
**smv** | `sudo mv --inter`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L743-L745) | Move files safely as super user.
**srm** | `sudo rm --inter`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L750-L752) | Delete files safely as super user.
**scpdir** | `sudo cp --inter`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L756-L758) | Copy directories safely as super user.
**smvdir** | `sudo mv --inter`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L762-L764) | Move directories safely as super user.
**srmdir** | `sudo rm --inter`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L769-L771) | Delete directories safely as super user.
**sm, sle** | `sudo less --RAW`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L779-L781) | Display text or file in pager as super user.
**sv** | `sudo vim -p "$@`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L785-L787) | Edit file with vim as super user.
**svv** | `sudo view -p "$`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L791-L793) | View file in vim as super user.
**sn** | `sudo nano --und`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L805-L807) | Edit file with nano as super user.
**sg** | `sudo gedit  "$@`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L811-L813) | Edit file with gedit as super user.
NoneNoneNoneNoneNoneNoneNoneNoneNoneNoneNoneNoneNoneNoneNoneNoneNone
###  Procesess 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**taskManager, ht** | `htop  "$@"` | Run terminal task manager.
**ps1** | `ps  "$@" | __pr`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L900-L902) | Print users processes.
**psa, pse, processes** | `ps -e  "$@" | _`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L906-L908) | Print all processes.
**pgrep1** | `pgrep --list-na`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L913-L915) | Find processes with part of name.
**kill1** | `kill -9 "$@"` | Kill process with kill signal.
**st, strace1, trace** | `strace -s\ 2000`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L932-L935) | Trace system calls.

###  Text 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**he** | `head "$@"` | Print first ten lines.
**he1, firstLine** | `head -n1 "$@"` | Print first line.
**ta** | `tail "$@"` | Print last ten lines.
**ta1, lastLine** | `tail -n1 "$@"` | Print last line.
**wcl, countLines** | `wc -l "$@"` | Count lines.
**wcw, countWords** | `wc -w "$@"` | Count words.
**trd** | `tr --delete "$@`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L974-L976) | Delete characters.
**loc, linesOfCode** | `rootDir="$PWD"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L981-L997) | Count lines in files with extension in working and subdirectories.

###  Tables 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**table** | `column -t -s "$`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1006-L1008) | Line up columns.
**cut1, keepColumns** | `cut --delimiter`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1014-L1016) | Keep columns.
**sort1** | `sort --field-se`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1022-L1024) | Sort lines by column.

###  Search 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**grep1** | `grep --color=au`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1037-L1039) | Print lines containing pattern.
**gr** | `__printLinesCon`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1043-L1046) | Print or display with pager lines containing pattern.
**grr** | `__printLinesCon`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1050-L1056) | Print or display with pager numbered lines containing pattern in working and subdirectories.
**lo, locate1** | `locate  "$1" \`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1061-L1065) | Locate files on filesystem containing pattern in their names.
**find1** | `find  . -name "`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1072-L1076) | Locate files containing pattern in their names in working and sub directories.

###  Archives 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**extract** | `if [ -z "$1" ];`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1085-L1118) | Extract archive of any type.

###  Terminal Multiplexer 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**tm, mu** | `tmux  "$@"` | Run terminal multiplexer.
**mua** | `tmux attach "$@`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1132-L1134) | Run terminal multiplexer and attach to last session.
**mul** | `tmux ls` | List terminal multiplexers sessions.

###  System Information 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**df1** | `df -h | grep "s`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1147-L1149) | Print available disk space in simplified form.
**du1** | `du --summarize `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1153-L1155) | Print disk space occupied by file or folder.
**fr, free1** | `echo "all:  "$(`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1158-L1165) | Print all and free memory space in megabytes.
**temp, temperature** | `acpi -t` | Print temperature of cpu.
**batt, battery** | `acpi` | Print battery status.
**uname1, kernelVersion** | `uname --all` | Print operating system information.
**pci, lspci1** | `lspci -v "$@" |`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1185-L1187) | Print info about pci devices.

###  Power 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**reboot** | `sudo reboot` | Restart computer.
**poweroff** | `sudo poweroff` | Shut down computer.
**hib** | `sudo pm-hiberna`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1205-L1207) | Hibernate computer.
**sus** | `sudo pm-suspend`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1210-L1212) | Suspend computer.

###  Keyboard 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**uskeys** | `setxkbmap -layo`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1220-L1222) | Switch to american keyboard layout.
**keycode** | `xev "$@"` | Monitor keycodes of pressed keys.
**norepeat** | `xset -r` | Turn off key repeat.
**repeat** | `xset r` | Turn on key repeat.

###  Misc 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**blue** | `echo -en "\e]PC`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1246-L1248) | Change hue of color blue in linux terminal.
**path** | `echo -e ${PATH/`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1251-L1253) | List directories contained in path variable.
**bc1** | `gcalccmd "$@"` | Run terminal calculator that supports decimal numbers.
**hd1** | `hd  "$@" | __pr`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1262-L1264) | Print hexadecimal representation of file or stream.
**profile** | `source /etc/pro`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1267-L1269) | Run profile script.
**vimode** | `set -o vi` | Change bash line editing to vi mode.
**emacsmode** | `set -o emacs` | Change bash line editing to emacs mode.
**ssd** | `sudo fstrim -v `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1282-L1284) | Trim ssd.
**typingTutor** | `gtypist "$@"` | Start typing tutor.

###  Package Management 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**ch, canhaz** | `sudo apt-get in`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1297-L1299) | Install package.
**update** | `sudo apt-get up`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1302-L1304) | Update information about available packages.
**upgrade** | `sudo apt-get up`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1307-L1309) | Upgrade all packages.
**dist-upgrade** | `sudo apt-get di`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1314-L1316) | Upgrade all packages intelligently.
**remove** | `sudo apt-get re`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1320-L1322) | Remove package and all unneeded packages.
**purge** | `sudo apt-get pu`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1327-L1329) | Remove package and all unneeded packages together with configuration files.
**autoremove** | `sudo apt-get au`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1333-L1335) | Remove unneeded packages.
**installed, packages** | `cat /var/log/ap`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1339-L1344) | Print packages that were installed by user.
**allInstalled, allPackages** | `dpkg --get-sele`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1347-L1351) | Print all installed packages.
**depends** | `apt-cache show `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1354-L1360) | Print package dependencies.

###  Package Information 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**pd, describe** | `apt-cache show `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1368-L1370) | Print package description.
**ve, version** | `# Check if pass`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1388-L1405) | Print installed and available version of package or command.
**package** | `call1=$(sudo wh`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1435-L1451) | Print package of installed command together with description and location.

###  Package Search 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**findPackage** | `apt-cache searc`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1460-L1463) | Find available packages with part of name or description.
**ap, apropos1, findCommand** | `apropos "$@" \`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1468-L1471) | Find installed commands with part of name or description.
**apt-file1** | `apt-file -x sea`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1474-L1477) | Find available packages that provide command.
**wi, whatis1** | `# Checks if it `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1516-L1540) | Describe package or command or find available packages with part of name or command.

###  Git 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**commit** | `git commit -am `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1549-L1551) | Commit changed and deleted files with message.
**commitm** | `git commit -a "`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1555-L1557) | Commit changed and deleted files and edit message in editor.
**init** | `git init "$@"` | Initialize repository.
**push** | `git push "$@"` | Push changes to remote repository.
**pull** | `git pull "$@"` | Pull changes from remote repository.
**merge** | `git merge "$@"` | Merge specified branch with current one.
**gc, checkout** | `git checkout "$`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1582-L1584) | Checkout branch or file.
**gb, branch** | `git branch "$@"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1587-L1589) | List branches or create new one.
**gs** | `git -c color.st`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1592-L1595) | Print short repository status.
**gl** | `git log --graph`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1599-L1601) | Display minimal log of commits.
**gll** | `git log --graph`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1605-L1607) | Display medium log of commits.
**glll** | `git log --decor`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1611-L1613) | Display log of commits.
**gu** | `git remote upda`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1617-L1620) | Update information about remote repository and print status.
**gd** | `git diff "$@"` | Display changes between commits.
**ga** | `git add "$@"` | Add files to repository.
**gm** | `git mv "$@"` | Move repositories files.
**gls, lsgit** | `git ls-files "$`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1641-L1643) | List files that are in repository.

###  Github 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**clone** | `git clone git@g`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1652-L1654) | Clone github project.
**origin** | `git remote add `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1658-L1662) | Set github project as remote repository.
**cloneAll** | `if [[ -z "$1" ]`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1665-L1677) | Clone all users github projects.

###  Network 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**ip1** | `/sbin/ifconfig `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1685-L1691) | Print internal ip.
**ip2** | `lynx --dump htt`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1694-L1696) | Print external ip.
**gateway** | `route -n \`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1699-L1704) | Print gateways ip.
**mac** | `ifconfig | grep`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1707-L1709) | Print mac addresses of network devices.
**pa, pingAll** | `ping -c 1 -q $(`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1712-L1716) | Ping gateway and google.
**nmap1** | `if [[ $# -eq 0 `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1720-L1736) | Scan local network.
**ne, network** | `localIp=$(ip1)`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1764-L1795) | Print ssh port status of local devices and ping google.

###  Wireless 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**woff** | `sudo rfkill blo`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1803-L1808) | Block wireless device.
**won** | `sudo rfkill unb`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1811-L1816) | Unblock wireless device.
**wr** | `woff`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1819-L1822) | Reset wireless device.
**up** | `sudo ifconfig w`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1825-L1827) | Activate wireless interface.
**down** | `sudo ifconfig w`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1830-L1832) | Deactivate wireless interface.
**wlan** | `sudo iwlist wla`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1835-L1845) | Print wireless networks in range.

###  Internet 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**i, www, internet** | `__runCommandInB`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1853-L1855) | Start default browser in background.
**fire** | `__runCommandInB`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1858-L1860) | Start firefox in background.
**chrome** | `__runCommandInB`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1865-L1867) | Start chrome in background.
**lynx1** | `lynx -accept_al`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1873-L1875) | Start terminal web browser.

###  Audio 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**mixer** | `alsamixer "$@"` | Start terminal volume control.
**a** | `___setVolumeTo `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1893-L1895) | Increase volume by six decibels.
**z** | `___setVolumeTo `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1898-L1900) | Decrease volume by six decibels.
**aa** | `___setVolumeTo `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1903-L1905) | Increase volume by two decibels.
**zz** | `___setVolumeTo `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1908-L1910) | Decrease volume by two decibels.
**** | `ls` | Test function.

