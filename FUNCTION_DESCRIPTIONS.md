Commands
========

###  Less 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**le, less1** | `less --RAW-CONTROL-C`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L22-L23) | Display text in pager.
**m** | `___printOrDisplayTex`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L64-L66) | Print or display text in pager.
**mm** | `if [[ "$#" -gt 0 ]];`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L77-L95) | Print and display text in pager if necessary.

###  Ls 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**l** | `___displayOutputOfLi`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L173-L176) | List or display directory contents in pager using short listing format.
**ll** | `___displayOutputOfLi`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L178-L181) | List or display directory contents in pager using medium listing format.
**lll** | `___displayOutputOfLi`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L183-L186) | List or display directory contents in pager using long listing format.
**la** | `__listOrDisplayDirec`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L188-L191) | List or display all directory contents in pager using short listing format.
**lla** | `__listOrDisplayDirec`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L193-L196) | List or display all directory contents in pager using medium listing format.
**llla** | `__listOrDisplayDirec`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L198-L201) | List or display all directory contents in pager using long listing format.
**lt** | `__listOrDisplayDirec`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L203-L206) | List or display directory contents in pager ordered by date using short listing format.
**llt** | `__listOrDisplayDirec`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L208-L211) | List or display directory contents in pager ordered by date using medium listing format.
**lllt** | `__listOrDisplayDirec`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L213-L216) | List or display directory contents in pager ordered by date using long listing format.
**dl** | `__listOrDisplayDirec`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L218-L221) | List or display matching directories in pager using short listing format.
**dll** | `__listOrDisplayDirec`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L223-L226) | List or display matching directories in pager using medium listing format.
**dlll** | `__listOrDisplayDirec`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L228-L231) | List or display matching directories in pager using long listing format.
**l1** | `__listOrDisplayDirec`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L233-L236) | List or display in pager one directory item per line using short listing format.
**la1** | `__listOrDisplayAllDi`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L238-L241) | List or display in pager one directory item per line including hidden files using short listing format.
**first** | `ls "$@" | head -1`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L244-L246) | Print name of first file in directory.
**rf, randomFile** | `ls "$@" | sort -R | `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L249-L251) | Print name of random file in directory.
**findd, directories** | `find . -name .git -p`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L255-L257) | Print all subdirectories.

###  Tree 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**t, tree1** | `tree -C -I .git --di`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L265-L266) | Print directory structure.

###  Cd 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**.., cd..** | `___goUpNumberOfDirec`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L293-L295) | Go up one directory.
**...** | `___goUpNumberOfDirec`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L297-L299) | Go up two directories.
**....** | `___goUpNumberOfDirec`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L301-L303) | Go up three directories.
**.....** | `___goUpNumberOfDirec`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L305-L307) | Go up four directories.
**......** | `___goUpNumberOfDirec`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L309-L311) | Go up five directories.
**.......** | `___goUpNumberOfDirec`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L313-L315) | Go up six directories.
**cdiso** | `sudo mkdir /media/"$`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L318-L322) | Mount iso and cd into.

###  Files 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**cp** | `cp --interactive --v`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L331-L333) | Copy files safely.
**mv** | `mv --interactive --v`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L337-L339) | Move files safely.
**rm** | `rm --interactive "$@`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L344-L346) | Delete files safely.
**cpdir** | `cp --interactive --v`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L350-L352) | Copy directories safely.
**mvdir** | `mv --interactive --v`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L356-L358) | Move directories safely.
**rmdir** | `rm --interactive --r`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L363-L365) | Delete directories safely.
**mk, md, mkdir1** | `mkdir --parents "$1"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L369-L372) | Create directory and descend into.
**bk, backup** | `sudo cp --preserve "`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L376-L377) | Backup file.
**switch** | `tempFile=$(mktemp)`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L381-L386) | Switch contents of files.

###  Pwd 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**p** | `if [[ $# -eq 0 ]]; t`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L395-L401) | Print working directory or path to file.

###  Echo 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**e** | `echo "$@"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L409-L411) | Print text.
**ee** | `echo -e "$@"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L414-L416) | Print text interpreting backslashed characters.
**en** | `echo -n "$@"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L419-L421) | Print text without trailing newline.

###  Run In Background 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**rb, runInBackground** | `nohup "$@" &>/dev/nu`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L430-L432) | Run command in background.

###  Basics 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**al, aliases** | `vim ~/.standard_alia`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L442-L444) | Edit standard aliases.
**ba** | `bash "$@"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L448-L450) | Start new bash shell.
**ty, type1** | `type "$@" | __printO`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L455-L457) | Print command type or definition.
**tyty** | `type $(type "$@" | g`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L460-L463) | Print function that a function calls.
**c** | `cat "$@"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L467-L469) | Print contents of file.
**?, exitCode** | `echo $?`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L472-L474) | Print exit code of last command.
**cl** | `clear`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L477-L479) | Clear the screen.
**re** | `reset "$@"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L482-L484) | Reset the screen.
**q** | `exit`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L487-L489) | Exit bash shell.
**o, openFile** | `__runCommandInBackgr`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L493-L495) | Open file with default app.
**te, terminal** | `gnome-terminal "$@"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L498-L500) | Open new terminal with same working directory.
**to** | `touch  "$@"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L504-L505) | Update files timestamp or create new one.
**da** | `date  "$@"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L509-L510) | Print date and time.
**ma, make1** | `make  "$@" 2>&1 | __`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L515-L516) | Run make with pager.
**na, explorer** | `__runCommandInBackgr`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L525-L527) | Start file explorer in background in working directory.
**diff1** | `colordiff  "$@" | __`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L530-L531) | Compare files line by line in color.
**me, makeExecutable** | `if [[ ! -f "$1" ]]; `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L536-L539) | Make file executable or create new script.

###  History 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**h, history1** | `if [ "$#" -eq 0 ]; t`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L574-L583) | Search command history for pattern.

###  Text Editors 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**v, vim1** | `vim -p "$@"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L591-L592) | Edit file with vim.
**vv** | `view -p "$@"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L597-L598) | View file in vim.
**n, nano1** | `nano --undo --autoin`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L611-L612) | Edit file with nano.
**g** | `__runCommandInBackgr`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L616-L617) | Edit file with gedit.
**sub** | `__runCommandInBackgr`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L621-L623) | Edit file with sublime text.

###  Sudo 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**s** | `sudo "$@"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L631-L633) | Execute command as super user.
**f, fu, fuck** | `sudo $(history -p \!`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L637-L639) | Execute last command as super user.
**sudoCp** | `sudo cp --interactiv`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L643-L645) | Copy files safely as super user.
**smv** | `sudo mv --interactiv`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L649-L651) | Move files safely as super user.
**srm** | `sudo rm --interactiv`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L656-L658) | Delete files safely as super user.
**scpdir** | `sudo cp --interactiv`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L662-L664) | Copy directories safely as super user.
**smvdir** | `sudo mv --interactiv`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L668-L670) | Move directories safely as super user.
**srmdir** | `sudo rm --interactiv`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L675-L677) | Delete directories safely as super user.
**sm, sle** | `sudo less --RAW-CONT`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L680-L681) | Display text in pager as super user.
**svv** | `sudo view -p "$@"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L685-L686) | View file in vim as super user.
**sv** | `sudo vim -p "$@"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L690-L691) | Edit file with vim as super user.
**sn** | `sudo nano --undo --a`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L695-L696) | Edit file with nano as super user.
**sg** | `sudo gedit  "$@"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L700-L701) | Edit file with gedit as super user.

###  Procesess 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**ht, taskManager** | `htop  "$@"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L782-L783) | Run terminal task manager.
**ps1** | `ps  "$@" | __printOr`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L788-L789) | Print users processes.
**psa, pse, processes** | `ps -e  "$@" | __prin`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L793-L794) | Print all processes.
**pgrep1** | `pgrep --list-name "$`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L799-L800) | Find processes with part of name.
**kill1** | `kill -9 "$@"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L810-L812) | Kill process with kill signal.
**st, strace1, trace** | `strace -s\ 2000 -f "`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L817-L818) | Trace system calls.

###  Text 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**he** | `head "$@"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L829-L831) | Print first ten lines.
**he1, firstLine** | `head -n1 "$@"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L834-L836) | Print first line.
**ta** | `tail "$@"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L839-L841) | Print last ten lines.
**ta1, lastLine** | `tail -n1 "$@"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L844-L846) | Print last line.
**wcl, countLines** | `wc -l "$@"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L849-L851) | Count lines.
**wcw, countWords** | `wc -w "$@"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L854-L856) | Count words.
**trd** | `tr --delete "$@"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L859-L861) | Delete characters.
**loc, linesOfCode** | `rootDir="$PWD"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L866-L881) | Count lines in files with extension in working and subdirectories.

###  Tables 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**table** | `column -t -s "$@"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L890-L892) | Line up columns.
**cut1, keepColumns** | `cut --delimiter="$1"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L898-L900) | Keep columns.
**sort1** | `sort --field-separat`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L906-L908) | Sort lines by column.

###  Search 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**grep1** | `grep --color=auto --`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L919-L920) | Print lines containing pattern.
**gr** | `__printLinesContaini`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L925-L928) | Print or display with pager lines containing pattern.
**lo, locate1** | `locate  "$1" \`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L932-L933) | Locate files on filesystem containing pattern in their names.
**find1** | `find  . -name "$1" \`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L942-L943) | Locate files containing pattern in their names in working and sub directories.

###  Archives 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**extract** | `if [ -z "$1" ]; then`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L955-L963) | Extract archive of any type.

###  Tmux 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**tm** | `tmux  "$@"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L996-L997) | Run terminal multiplexer.
**tma** | `tmux attach "$@"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1001-L1003) | Run terminal multiplexer and attach to session.
**tml** | `tmux ls`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1006-L1008) | List terminal multiplexers sessions.

###  System Information 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**df1** | `df -h | grep "sd\|Si`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1016-L1018) | Print available disk space in simplified form.
**du1** | `du --summarize --hum`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1022-L1024) | Print disk space occupied by file or folder.
**fr, free1** | `echo "all:  "$(free `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1027-L1034) | Print all and ocupied memory space in megabytes.
**temp, temperature** | `acpi -t`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1037-L1039) | Print temperature of cpu.
**batt, battery** | `acpi`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1042-L1044) | Print battery status.
**uname1, kernelVersion** | `uname --all`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1047-L1049) | Print operating system information.
**pci, lspci1** | `lspci -v "$@" | __pr`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1052-L1053) | Print info about pci devices.

###  Power 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**restart** | `sudo shutdown -r now`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1063-L1065) | Restart computer.
**poweroff** | `sudo shutdown now`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1068-L1070) | Shut down computer.
**hib** | `sudo pm-hibernate`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1073-L1075) | Hibernate computer.
**sus** | `sudo pm-suspend`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1078-L1080) | Suspend computer.

###  Keyboard 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**uskeys** | `setxkbmap -layout us`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1088-L1090) | Change keyboard layout to american.
**keycode** | `xev "$@"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1093-L1095) | Monitor keycodes of pressed keys.
**norepeat** | `xset -r`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1098-L1100) | Turn off key repeat.
**repeat** | `xset r`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1103-L1105) | Turn on key repeat.

###  Misc 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**blue** | `echo -en "\e]PC7373C`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1114-L1116) | Change hue of color blue in linux terminal.
**path** | `echo -e ${PATH//:/\\`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1119-L1120) | List directories contained in path variable.
**bc1** | `gcalccmd "$@"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1124-L1126) | Run terminal calculator that supports decimal numbers.
**hd1** | `hd  "$@" | __printOr`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1129-L1130) | Print hexadecimal representation of file or stream.
**profile** | `source /etc/profile`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1134-L1136) | Run profile script.
**vimode** | `set -o vi`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1139-L1141) | Change bash line editing to vi mode.
**emacsmode** | `set -o emacs`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1144-L1146) | Change bash line editing to emacs mode.
**ssd** | `sudo fstrim -v /`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1149-L1151) | Trim ssd.
**tt** | `gtypist "$@"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1154-L1156) | Start typing tutor.

###  Package Management 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**ch, canhaz** | `sudo apt-get install`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1164-L1166) | Install package.
**update** | `sudo apt-get update`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1169-L1171) | Update information about available packages.
**upgrade** | `sudo apt-get upgrade`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1174-L1176) | Upgrade all packages.
**dist-upgrade** | `sudo apt-get dist-up`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1181-L1183) | Upgrade all packages intelligently.
**remove** | `sudo apt-get remove `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1187-L1189) | Remove package and all unneeded packages.
**purge** | `sudo apt-get purge "`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1194-L1196) | Remove package and all unneeded packages together with configuration files.
**autoremove** | `sudo apt-get autorem`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1200-L1202) | Remove unneeded packages.
**installed, packages** | `cat /var/log/apt/his`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1206-L1211) | Print packages that were installed by user.
**allInstalled, allPackages** | `dpkg --get-selection`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1214-L1218) | Print all installed packages.
**depends** | `apt-cache show "$@" `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1221-L1227) | Print package dependencies.

###  Package Information 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**pd, describe** | `apt-cache show "$@" `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1235-L1237) | Print package description.
**ve, version** | `# Check if passed na`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1254-L1271) | Print version of package or version of installed commands package.
**package** | `call1=$(sudo whatis `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1301-L1317) | Print package of installed command together with description and location.

###  Package Search 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**findPackage** | `apt-cache search "$@`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1326-L1329) | Find available packages with part of name or description.
**ap, apropos1, findCommand** | `apropos "$@" \`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1334-L1337) | Find installed commands with part of name or description.
**apt-file1** | `apt-file search "$1"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1340-L1344) | Find available packages that provide command.
**wi, whatis1** | `# Checks if it is an`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1382-L1406) | Describe package or command or find available packages with part of name or available packages that provide command.

###  Git 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**commit** | `git commit -am "$@"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1415-L1417) | Commit changed and deleted files with message.
**commitm** | `git commit -a "$@"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1421-L1423) | Commit changed and deleted files and edit message in editor.
**init** | `git init "$@"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1427-L1429) | Initialize repository.
**push** | `git push "$@"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1432-L1434) | Push changes to remote repository.
**pull** | `git pull "$@"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1437-L1439) | Pull changes from remote repository.
**merge** | `git merge "$@"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1442-L1444) | Merge specified branch with current one.
**gc, checkout** | `git checkout "$@"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1448-L1450) | Checkout branch or file.
**gb, branch** | `git branch "$@"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1453-L1455) | List branches or create new one.
**gs** | `git -c color.status=`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1458-L1461) | Print short repository status.
**gl** | `git log --decorate -`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1465-L1467) | Display log of commits.
**gl1** | `git log --graph --ab`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1471-L1477) | Display minimal log of commits.
**gu** | `git remote update "$`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1481-L1484) | Update information about remote repository and print status.
**gd** | `git diff "$@"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1488-L1490) | Display changes between commits.
**ga** | `git add "$@"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1493-L1495) | Add files to repository.
**gm** | `git mv "$@"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1500-L1502) | Move repositories files.
**gls, lsgit** | `git ls-files "$@"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1505-L1507) | List files that are in repository.

###  Github 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**clone** | `git clone git@github`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1516-L1518) | Clone github project.
**origin** | `git remote add origi`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1522-L1526) | Set github project as remote repository.
**cloneAll** | `if [[ -z "$1" ]]; th`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1529-L1541) | Clone all users github projects.

###  Network 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**ip1** | `/sbin/ifconfig \`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1549-L1555) | Print internal ip.
**ip2** | `lynx --dump http://i`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1558-L1560) | Print external ip.
**gateway** | `route -n \`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1563-L1568) | Print gateways ip.
**mac** | `ifconfig | grep HWad`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1571-L1573) | Print mac addresses of network devices.
**pa, pingAll** | `ping -c 1 -q `gatewa`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1576-L1580) | Ping gateway and google.
**nmap1** | `if [[ $# -eq 0 ]]; t`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1584-L1600) | Scan local network.
**ne, network** | `localIp=$(ip1)`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1628-L1642) | Print ssh port status of local devices and ping google.

###  Wireless 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**woff** | `sudo rfkill block $(`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1667-L1672) | Block wireless device.
**won** | `sudo rfkill unblock `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1675-L1680) | Unblock wireless device.
**wr** | `woff`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1683-L1686) | Reset wireless device.
**up** | `sudo ifconfig wlan0 `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1689-L1691) | Activate wireless interface.
**down** | `sudo ifconfig wlan0 `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1694-L1696) | Deactivate wireless interface.
**wlan** | `sudo iwlist wlan0 sc`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1699-L1709) | Print wireless networks in range.

###  Internet 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**i, www, internet** | `__runCommandInBackgr`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1717-L1719) | Start default browser in background.
**fire** | `__runCommandInBackgr`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1722-L1724) | Start firefox in background.
**chrome** | `__runCommandInBackgr`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1728-L1729) | Start chrome in background.
**lynx1** | `lynx -accept_all_coo`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1734-L1735) | Start terminal web browser.

###  Audio 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**mixer** | `alsamixer "$@"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1744-L1746) | Start terminal volume control.
**a** | `___setVolumeTo "6%+"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1754-L1756) | Increase volume by six decibels.
**z** | `___setVolumeTo "6%-"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1759-L1761) | Decrease volume by six decibels.
**aa** | `___setVolumeTo "2%+"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1764-L1766) | Increase volume by two decibels.
**zz** | `___setVolumeTo "2%-"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1769-L1771) | Decrease volume by two decibels.
