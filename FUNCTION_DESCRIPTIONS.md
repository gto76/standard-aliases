Commands
========

###  Less 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**le, less1** | `less --RAW-CONT`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L22-L24) | Display text in pager.
**m** | `___printOrDispl`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L64-L66) | Print or display text in pager.
**mm** | `if [[ "$#" -gt `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L77-L106) | Print and display text in pager if necessary.

###  Ls 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**l** | `___displayOutpu`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L173-L176) | List or display directory contents in pager using short listing format.
**ll** | `___displayOutpu`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L178-L181) | List or display directory contents in pager using medium listing format.
**lll** | `___displayOutpu`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L183-L186) | List or display directory contents in pager using long listing format.
**la** | `__listOrDisplay`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L188-L191) | List or display all directory contents in pager using short listing format.
**lla** | `__listOrDisplay`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L193-L196) | List or display all directory contents in pager using medium listing format.
**llla** | `__listOrDisplay`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L198-L201) | List or display all directory contents in pager using long listing format.
**lt** | `__listOrDisplay`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L203-L206) | List or display directory contents in pager ordered by date using short listing format.
**llt** | `__listOrDisplay`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L208-L211) | List or display directory contents in pager ordered by date using medium listing format.
**lllt** | `__listOrDisplay`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L213-L216) | List or display directory contents in pager ordered by date using long listing format.
**dl** | `__listOrDisplay`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L218-L221) | List or display matching directories in pager using short listing format.
**dll** | `__listOrDisplay`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L223-L226) | List or display matching directories in pager using medium listing format.
**dlll** | `__listOrDisplay`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L228-L231) | List or display matching directories in pager using long listing format.
**l1** | `__listOrDisplay`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L233-L236) | List or display in pager one directory item per line using short listing format.
**la1** | `__listOrDisplay`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L238-L241) | List or display in pager one directory item per line including hidden files using short listing format.
**first** | `ls "$@" | head `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L244-L246) | Print name of first file in directory.
**rf, randomFile** | `ls "$@" | sort `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L249-L251) | Print name of random file in directory.
**findd, directories** | `find . -name .g`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L255-L257) | Print all subdirectories.

###  Tree 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**t, tree1** | `tree -C -I .git`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L265-L267) | Print directory structure.

###  Cd 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**.., cd..** | `___goUpNumberOf`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L293-L295) | Go up one directory.
**...** | `___goUpNumberOf`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L297-L299) | Go up two directories.
**....** | `___goUpNumberOf`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L301-L303) | Go up three directories.
**.....** | `___goUpNumberOf`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L305-L307) | Go up four directories.
**......** | `___goUpNumberOf`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L309-L311) | Go up five directories.
**.......** | `___goUpNumberOf`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L313-L315) | Go up six directories.
**cdiso** | `sudo mkdir /med`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L318-L322) | Mount iso and cd into.

###  Files 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**cp** | `cp --interactiv`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L331-L333) | Copy files safely.
**mv** | `mv --interactiv`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L337-L339) | Move files safely.
**rm** | `rm --interactiv`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L344-L346) | Delete files safely.
**cpdir** | `cp --interactiv`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L350-L352) | Copy directories safely.
**mvdir** | `mv --interactiv`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L356-L358) | Move directories safely.
**rmdir** | `rm --interactiv`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L363-L365) | Delete directories safely.
**mk, md, mkdir1** | `mkdir --parents`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L369-L372) | Create directory and descend into.
**bk, backup** | `sudo cp --prese`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L376-L378) | Backup file.
**switch** | `tempFile=$(mkte`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L381-L386) | Switch contents of files.

###  Pwd 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**p** | `if [[ $# -eq 0 `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L395-L401) | Print working directory or path to file.

###  Echo 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**e** | `echo "$@"` | Print text.
**ee** | `echo -e "$@"` | Print text interpreting backslashed characters.
**en** | `echo -n "$@"` | Print text without trailing newline.

###  Run In Background 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**rb, runInBackground** | `nohup "$@" &>/d`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L430-L432) | Run command in background.

###  Basics 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**al, aliases** | `vim ~/.standard`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L442-L444) | Edit standard aliases.
**ba** | `bash "$@"` | Start new bash shell.
**ty, type1** | `type "$@" | __p`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L455-L457) | Print command type or definition.
**tyty** | `type $(type "$@`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L460-L463) | Print function that a function calls.
**c** | `cat "$@"` | Print file contents.
**?, exitCode** | `echo $?` | Print exit code of last command.
**cl** | `clear` | Clear the screen.
**re** | `reset "$@"` | Reset the screen.
**q** | `exit` | Exit bash shell.
**o, openFile** | `__runCommandInB`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L493-L495) | Open file with default app.
**te, terminal** | `gnome-terminal `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L498-L500) | Open new terminal with same working directory.
**to** | `touch  "$@"` | Update files timestamp or create new one.
**da** | `date  "$@"` | Print date and time.
**ma, make1** | `make  "$@" 2>&1`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L515-L517) | Run make with pager.
**na, explorer** | `__runCommandInB`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L525-L527) | Start file explorer in background in working directory.
**diff1** | `colordiff  "$@"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L530-L532) | Compare files line by line in color.
**me, makeExecutable** | `if [[ ! -f "$1"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L536-L565) | Make file executable or create new bash or python script.

###  History 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**h, history1** | `if [ "$#" -eq 0`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L574-L583) | Search command history for pattern.

###  Text Editors 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**v** | `vim -p "$@"` | Edit file with vim.
**vv** | `view -p "$@"` | View file in vim.
**n, nano1** | `nano --undo --a`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L611-L613) | Edit file with nano.
**nv** | `nano --view --u`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L615-L617) | View file in nano.
**g, gedit1** | `__runCommandInB`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L620-L622) | Edit file with gedit.
**sub** | `__runCommandInB`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L625-L627) | Edit file with sublime text.

###  Sudo 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**s** | `sudo "$@"` | Execute command as super user.
**f, fu, fuck** | `sudo $(history `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L641-L643) | Execute last command as super user.
**sudoCp** | `sudo cp --inter`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L647-L649) | Copy files safely as super user.
**smv** | `sudo mv --inter`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L653-L655) | Move files safely as super user.
**srm** | `sudo rm --inter`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L660-L662) | Delete files safely as super user.
**scpdir** | `sudo cp --inter`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L666-L668) | Copy directories safely as super user.
**smvdir** | `sudo mv --inter`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L672-L674) | Move directories safely as super user.
**srmdir** | `sudo rm --inter`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L679-L681) | Delete directories safely as super user.
**sm, sle** | `sudo less --RAW`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L684-L686) | Display text in pager as super user.
**svv** | `sudo view -p "$`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L689-L691) | View file in vim as super user.
**sv** | `sudo vim -p "$@`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L694-L696) | Edit file with vim as super user.
**sn** | `sudo nano --und`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L699-L701) | Edit file with nano as super user.
**sg** | `sudo gedit  "$@`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L704-L706) | Edit file with gedit as super user.

###  Procesess 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**ht, taskManager** | `htop  "$@"` | Run terminal task manager.
**ps1** | `ps  "$@" | __pr`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L792-L794) | Print users processes.
**psa, pse, processes** | `ps -e  "$@" | _`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L797-L799) | Print all processes.
**pgrep1** | `pgrep --list-na`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L803-L805) | Find processes with part of name.
**kill1** | `kill -9 "$@"` | Kill process with kill signal.
**st, strace1, trace** | `strace -s\ 2000`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L821-L824) | Trace system calls.

###  Text 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**he** | `head "$@"` | Print first ten lines.
**he1, firstLine** | `head -n1 "$@"` | Print first line.
**ta** | `tail "$@"` | Print last ten lines.
**ta1, lastLine** | `tail -n1 "$@"` | Print last line.
**wcl, countLines** | `wc -l "$@"` | Count lines.
**wcw, countWords** | `wc -w "$@"` | Count words.
**trd** | `tr --delete "$@`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L863-L865) | Delete characters.
**loc, linesOfCode** | `rootDir="$PWD"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L870-L885) | Count lines in files with extension in working and subdirectories.

###  Tables 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**table** | `column -t -s "$`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L894-L896) | Line up columns.
**cut1, keepColumns** | `cut --delimiter`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L902-L904) | Keep columns.
**sort1** | `sort --field-se`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L910-L912) | Sort lines by column.

###  Search 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**grep1** | `grep --color=au`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L923-L925) | Print lines containing pattern.
**gr** | `__printLinesCon`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L929-L932) | Print or display with pager lines containing pattern.
**grr** | `__printLinesCon`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L936-L942) | Print or display with pager lines containing pattern in working and subdirectories.
**lo, locate1** | `locate  "$1" \`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L946-L950) | Locate files on filesystem containing pattern in their names.
**find1** | `find  . -name "`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L956-L960) | Locate files containing pattern in their names in working and sub directories.

###  Archives 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**extract** | `if [ -z "$1" ];`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L969-L1002) | Extract archive of any type.

###  Terminal Multiplexer 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**tm** | `tmux  "$@"` | Run terminal multiplexer.
**tma** | `tmux attach "$@`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1015-L1017) | Run terminal multiplexer and attach to last session.
**tml** | `tmux ls` | List terminal multiplexers sessions.

###  System Information 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**df1** | `df -h | grep "s`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1030-L1032) | Print available disk space in simplified form.
**du1** | `du --summarize `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1036-L1038) | Print disk space occupied by file or folder.
**fr, free1** | `echo "all:  "$(`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1041-L1048) | Print all and free memory space in megabytes.
**temp, temperature** | `acpi -t` | Print temperature of cpu.
**batt, battery** | `acpi` | Print battery status.
**uname1, kernelVersion** | `uname --all` | Print operating system information.
**pci, lspci1** | `lspci -v "$@" |`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1066-L1068) | Print info about pci devices.

###  Power 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**restart** | `sudo shutdown -`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1077-L1079) | Restart computer.
**poweroff** | `sudo shutdown n`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1082-L1084) | Shut down computer.
**hib** | `sudo pm-hiberna`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1087-L1089) | Hibernate computer.
**sus** | `sudo pm-suspend`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1092-L1094) | Suspend computer.

###  Keyboard 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**uskeys** | `setxkbmap -layo`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1102-L1104) | Switch to american keyboard layout.
**keycode** | `xev "$@"` | Monitor keycodes of pressed keys.
**norepeat** | `xset -r` | Turn off key repeat.
**repeat** | `xset r` | Turn on key repeat.

###  Misc 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**blue** | `echo -en "\e]PC`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1128-L1130) | Change hue of color blue in linux terminal.
**path** | `echo -e ${PATH/`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1133-L1135) | List directories contained in path variable.
**bc1** | `gcalccmd "$@"` | Run terminal calculator that supports decimal numbers.
**hd1** | `hd  "$@" | __pr`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1143-L1145) | Print hexadecimal representation of file or stream.
**profile** | `source /etc/pro`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1148-L1150) | Run profile script.
**vimode** | `set -o vi` | Change bash line editing to vi mode.
**emacsmode** | `set -o emacs` | Change bash line editing to emacs mode.
**ssd** | `sudo fstrim -v `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1163-L1165) | Trim ssd.
**tt** | `gtypist "$@"` | Start typing tutor.

###  Package Management 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**ch, canhaz** | `sudo apt-get in`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1178-L1180) | Install package.
**update** | `sudo apt-get up`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1183-L1185) | Update information about available packages.
**upgrade** | `sudo apt-get up`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1188-L1190) | Upgrade all packages.
**dist-upgrade** | `sudo apt-get di`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1195-L1197) | Upgrade all packages intelligently.
**remove** | `sudo apt-get re`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1201-L1203) | Remove package and all unneeded packages.
**purge** | `sudo apt-get pu`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1208-L1210) | Remove package and all unneeded packages together with configuration files.
**autoremove** | `sudo apt-get au`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1214-L1216) | Remove unneeded packages.
**installed, packages** | `cat /var/log/ap`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1220-L1225) | Print packages that were installed by user.
**allInstalled, allPackages** | `dpkg --get-sele`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1228-L1232) | Print all installed packages.
**depends** | `apt-cache show `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1235-L1241) | Print package dependencies.

###  Package Information 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**pd, describe** | `apt-cache show `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1249-L1251) | Print package description.
**ve, version** | `# Check if pass`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1268-L1285) | Print version of package or version of installed commands package.
**package** | `call1=$(sudo wh`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1315-L1331) | Print package of installed command together with description and location.

###  Package Search 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**findPackage** | `apt-cache searc`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1340-L1343) | Find available packages with part of name or description.
**ap, apropos1, findCommand** | `apropos "$@" \`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1348-L1351) | Find installed commands with part of name or description.
**apt-file1** | `apt-file search`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1354-L1358) | Find available packages that provide command.
**wi, whatis1** | `# Checks if it `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1396-L1420) | Describe package or command or find available packages with part of name or available packages that provide command.

###  Git 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**commit** | `git commit -am `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1429-L1431) | Commit changed and deleted files with message.
**commitm** | `git commit -a "`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1435-L1437) | Commit changed and deleted files and edit message in editor.
**init** | `git init "$@"` | Initialize repository.
**push** | `git push "$@"` | Push changes to remote repository.
**pull** | `git pull "$@"` | Pull changes from remote repository.
**merge** | `git merge "$@"` | Merge specified branch with current one.
**gc, checkout** | `git checkout "$`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1462-L1464) | Checkout branch or file.
**gb, branch** | `git branch "$@"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1467-L1469) | List branches or create new one.
**gs** | `git -c color.st`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1472-L1475) | Print short repository status.
**gl** | `git log --decor`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1479-L1481) | Display log of commits.
**gl1** | `git log --graph`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1485-L1491) | Display minimal log of commits.
**gu** | `git remote upda`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1495-L1498) | Update information about remote repository and print status.
**gd** | `git diff "$@"` | Display changes between commits.
**ga** | `git add "$@"` | Add files to repository.
**gm** | `git mv "$@"` | Move repositories files.
**gls, lsgit** | `git ls-files "$`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1519-L1521) | List files that are in repository.

###  Github 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**clone** | `git clone git@g`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1530-L1532) | Clone github project.
**origin** | `git remote add `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1536-L1540) | Set github project as remote repository.
**cloneAll** | `if [[ -z "$1" ]`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1543-L1555) | Clone all users github projects.

###  Network 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**ip1** | `/sbin/ifconfig `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1563-L1569) | Print internal ip.
**ip2** | `lynx --dump htt`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1572-L1574) | Print external ip.
**gateway** | `route -n \`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1577-L1582) | Print gateways ip.
**mac** | `ifconfig | grep`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1585-L1587) | Print mac addresses of network devices.
**pa, pingAll** | `ping -c 1 -q `g`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1590-L1594) | Ping gateway and google.
**nmap1** | `if [[ $# -eq 0 `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1598-L1614) | Scan local network.
**ne, network** | `localIp=$(ip1)`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1642-L1673) | Print ssh port status of local devices and ping google.

###  Wireless 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**woff** | `sudo rfkill blo`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1681-L1686) | Block wireless device.
**won** | `sudo rfkill unb`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1689-L1694) | Unblock wireless device.
**wr** | `woff`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1697-L1700) | Reset wireless device.
**up** | `sudo ifconfig w`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1703-L1705) | Activate wireless interface.
**down** | `sudo ifconfig w`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1708-L1710) | Deactivate wireless interface.
**wlan** | `sudo iwlist wla`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1713-L1723) | Print wireless networks in range.

###  Internet 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**i, www, internet** | `__runCommandInB`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1731-L1733) | Start default browser in background.
**fire** | `__runCommandInB`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1736-L1738) | Start firefox in background.
**chrome** | `__runCommandInB`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1742-L1744) | Start chrome in background.
**lynx1** | `lynx -accept_al`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1748-L1750) | Start terminal web browser.

###  Audio 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**mixer** | `alsamixer "$@"` | Start terminal volume control.
**a** | `___setVolumeTo `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1768-L1770) | Increase volume by six decibels.
**** | `___setVolumeTo `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1774-L1776) | Increase volume by six decibels new one.
**zz** | `___setVolumeTo `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1780-L1782) | Decrease volume by six decibels.
**aa** | `___setVolumeTo `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1785-L1787) | Increase volume by two decibels.
