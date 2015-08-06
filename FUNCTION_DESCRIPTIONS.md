Commands
========

##  Less 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**le, less1, burek** | `less "${_L`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L22-L23) | Display text in pager.
**m** | `___printOr`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L64-L66) | Print or display text in pager.
**mm** | `if [[ "$#"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L77-L95) | Print and display text in pager if necessary.

##  Ls 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**l** | `___display`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L173-L176) | List or display directory contents in pager using short listing format.
**ll** | `___display`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L178-L181) | List or display directory contents in pager using medium listing format.
**lll** | `___display`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L183-L186) | List or display directory contents in pager using long listing format.
**la** | `__listOrDi`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L188-L191) | List or display all directory contents in pager using short listing format.
**lla** | `__listOrDi`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L193-L196) | List or display all directory contents in pager using medium listing format.
**llla** | `__listOrDi`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L198-L201) | List or display all directory contents in pager using long listing format.
**lt** | `__listOrDi`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L203-L206) | List or display directory contents in pager ordered by date using short listing format.
**llt** | `__listOrDi`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L208-L211) | List or display directory contents in pager ordered by date using medium listing format.
**lllt** | `__listOrDi`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L213-L216) | List or display directory contents in pager ordered by date using long listing format.
**dl** | `__listOrDi`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L218-L221) | List or display matching directories in pager using short listing format.
**dll** | `__listOrDi`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L223-L226) | List or display matching directories in pager using medium listing format.
**dlll** | `__listOrDi`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L228-L231) | List or display matching directories in pager using long listing format.
**l1** | `__listOrDi`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L233-L236) | List or display in pager one directory item per line using short listing format.
**la1** | `__listOrDi`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L238-L241) | List or display in pager one directory item per line including hidden files using short listing format.
**first** | `ls "$@" | `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L244-L246) | Get first file in directory.
**rf, randomFile** | `ls "$@" | `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L249-L251) | Get random file in directory.
**findd, directories** | `find . -na`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L255-L257) | Print all subdirectories.

##  Tree 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**t, tree1** | `tree "${_T`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L265-L266) | Print directory structure.

##  Cd 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**.., cd..** | `___goUpNum`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L293-L295) | Go up one directory.
**...** | `___goUpNum`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L297-L299) | Go up two directories.
**....** | `___goUpNum`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L301-L303) | Go up three directories.
**.....** | `___goUpNum`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L305-L307) | Go up four directories.
**......** | `___goUpNum`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L309-L311) | Go up five directories.
**.......** | `___goUpNum`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L313-L315) | Go up six directories.
**cdiso** | `sudo mkdir`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L318-L322) | Mount iso and cd into.

##  Files 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**cp** | `cp --inter`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L331-L333) | Copy files safely.
**mv** | `mv --inter`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L337-L339) | Move files safely.
**rm** | `rm --inter`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L344-L346) | Delete files safely.
**cpdir** | `cp --inter`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L350-L352) | Copy directories safely.
**mvdir** | `mv --inter`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L356-L358) | Move directories safely.
**rmdir** | `rm --inter`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L363-L365) | Delete directories safely.
**mk, md, mkdir1** | `mkdir --pa`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L369-L372) | Create directory and descend into.
**bk, backup** | `sudo cp --`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L376-L377) | Backup file.
**switch** | `tempFile=$`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L381-L386) | Switch contents of files.

##  Pwd 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**p** | `if [[ $# -`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L395-L401) | Print working directory or path to file.

##  Echo 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**e** | `echo "$@"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L409-L411) | Print text.
**ee** | `echo -e "$`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L414-L416) | Print text interpreting backslashed characters.
**en** | `echo -n "$`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L419-L421) | Print text without trailing newline.

##  Run In Background 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**rb, runInBackground** | `nohup "$@"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L430-L432) | Run command in background.

##  Basics 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**al, aliases** | `vim ~/.sta`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L442-L444) | Edit standard aliases.
**ba** | `bash "$@"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L448-L450) | Start new bash shell.
**ty, type1** | `type "$@" `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L455-L457) | Print command type or definition.
**tyty** | `type $(typ`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L460-L463) | Print function that a function calls.
**c** | `cat "$@"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L467-L469) | Print contents of file.
**?, exitCode** | `echo $?`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L472-L474) | Print exit code of last command.
**cl** | `clear`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L477-L479) | Clear the screen.
**re** | `reset "$@"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L482-L484) | Reset the screen.
**q** | `exit`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L487-L489) | Exit bash shell.
**o, openFile** | `__runComma`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L493-L495) | Open file with default app.
**te, terminal** | `gnome-term`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L498-L500) | Open new terminal with same working directory.
**to** | `touch "${_`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L504-L505) | Update files timestamp or create new one.
**da** | `date "${_D`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L509-L510) | Print date and time.
**ma, make1** | `make "${_M`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L515-L516) | Run make with pager.
**na, explorer** | `__runComma`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L525-L527) | Start file explorer in background in working directory.
**diff1** | `colordiff `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L530-L531) | Compare files line by line in color.
**me, makeExecutable** | `if [[ ! -f`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L536-L539) | Make file executable or create new bash script.

##  History 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**h, history1** | `if [ "$#" `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L574-L583) | Search command history for pattern.

##  Text Editors 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**v, vim1** | `vim "${_VI`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L591-L592) | Edit file with vim.
**vv** | `view "${_V`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L597-L598) | View file in vim.
**n, nano1** | `nano "${_N`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L611-L612) | Edit file with nano.
**g** | `__runComma`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L616-L617) | Edit file with gedit.
**sub** | `__runComma`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L621-L623) | Edit file with sublime text.

##  Sudo 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**s** | `sudo "$@"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L631-L633) | Run command as super user.
**f, fu, fuck** | `sudo $(his`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L637-L639) | Execute last command as super user.
**sudoCp** | `sudo cp --`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L643-L645) | Copy files safely as super user.
**smv** | `sudo mv --`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L649-L651) | Move files safely as super user.
**srm** | `sudo rm --`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L656-L658) | Delete files safely as super user.
**scpdir** | `sudo cp --`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L662-L664) | Copy directories safely as super user.
**smvdir** | `sudo mv --`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L668-L670) | Move directories safely as super user.
**srmdir** | `sudo rm --`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L675-L677) | Delete directories safely as super user.
**sm, sle** | `sudo less `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L680-L681) | Display text in pager as super user.
**svv** | `sudo view `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L685-L686) | View file in vim as super user.
**sv** | `sudo vim "`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L690-L691) | Edit file with vim as super user.
**sn** | `sudo nano `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L695-L696) | Edit file with nano as super user.
**sg** | `sudo gedit`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L700-L701) | Edit file with gedit as super user.
**fdisk** | `sudo fdisk`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L708-L710) | Run fdisk as super user.
**updatedb** | `sudo updat`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L712-L714) | Run updatedb as super user.
**ifconfig** | `sudo ifcon`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L716-L718) | Run ifconfig as super user.
**tcpdump** | `sudo tcpdu`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L720-L722) | Run tcpdump as super user.
**route** | `sudo route`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L724-L726) | Run route as super user.
**pm-hibernate** | `sudo pm-hi`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L728-L730) | Run pm-hibernate as super user.
**pm-suspend** | `sudo pm-su`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L732-L734) | Run pm-suspend as super user.
**shutdown** | `sudo shutd`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L736-L738) | Run shutdown as super user.
**fstrim** | `sudo fstri`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L740-L742) | Run fstrim as super user.
**aptget** | `sudo aptge`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L744-L746) | Run apt-get as super user.
**iw** | `sudo iw "$`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L748-L750) | Run iw as super user.
**nmap** | `sudo nmap `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L752-L754) | Run nmap as super user.
**parted** | `sudo parte`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L756-L758) | Run parted as super user.
**ntfsundelete** | `sudo ntfsu`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L760-L762) | Run ntfsundelete as super user.
**lshw** | `sudo lshw `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L764-L766) | Run lshw as super user.
**chown** | `sudo chown`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L768-L770) | Run chown as super user.
**mount** | `sudo mount`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L772-L774) | Run mount as super user.

##  Procesess 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**ht, taskManager** | `htop "${_H`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L782-L783) | Run terminal task manager.
**ps1** | `ps "${_PS_`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L788-L789) | Print users processes.
**psa, pse, processes** | `ps -e "${_`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L793-L794) | Print all processes.
**pgrep1** | `pgrep "${_`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L799-L800) | Find processes with part of name.
**kill1** | `kill -9 "$`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L810-L812) | Kill process with kill signal.
**st, strace1, trace** | `strace "${`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L817-L818) | Trace system calls.

##  Text 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**he** | `head "$@"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L829-L831) | Print first ten lines.
**he1, firstLine** | `head -n1 "`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L834-L836) | Print first line.
**ta** | `tail "$@"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L839-L841) | Print last ten lines.
**ta1, lastLine** | `tail -n1 "`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L844-L846) | Print last line.
**wcl, countLines** | `wc -l "$@"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L849-L851) | Count lines.
**wcw, countWords** | `wc -w "$@"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L854-L856) | Count words.
**trd** | `tr --delet`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L859-L861) | Delete characters.

##  Tables 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**table** | `column -t `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L870-L872) | Line up columns.
**cut1, keepColumns** | `cut --deli`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L878-L880) | Keep columns.
**sort1** | `sort --fie`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L886-L888) | Sort lines by column.

##  Search 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**grep1** | `grep --col`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L899-L900) | Print lines containing pattern.
**gr** | `__printLin`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L905-L908) | Print or display with pager lines containing pattern.
**lo, locate1** | `locate "${`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L912-L913) | Locate files on filesystem containing pattern in their names.
**find1** | `find "${_F`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L922-L923) | Locate files containing pattern in their names in working and sub directories.

##  Archives 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**extract** | `if [ -z "$`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L935-L943) | Extract archive of any type.

##  Tmux 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**tm** | `tmux "${_T`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L976-L977) | Run terminal multiplexer.
**tma** | `tmux attac`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L981-L983) | Run terminal multiplexer and attach to session.
**tml** | `tmux ls`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L986-L988) | List terminal multiplexers sessions.

##  System Information 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**df1** | `df -h | gr`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L996-L998) | Print available disk space in simplified form.
**du1** | `du --summa`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1002-L1004) | Print disk space occupied by file or folder.
**fr, free1** | `echo "all:`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1007-L1014) | Print all and ocupied memory space in megabytes.
**temp, temperature** | `acpi -t`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1017-L1019) | Print temperature of cpu.
**batt, battery** | `acpi`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1022-L1024) | Print battery status.
**uname1, kernelVersion** | `uname --al`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1027-L1029) | Print operating system information.
**pci, lspci1** | `lspci "${_`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1032-L1033) | Print info about pci devices.

##  Power 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**restart** | `sudo shutd`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1043-L1045) | Restart computer.
**poweroff** | `sudo shutd`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1048-L1050) | Shut down computer.
**hib** | `sudo pm-hi`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1053-L1055) | Hibernate computer.
**sus** | `sudo pm-su`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1058-L1060) | Suspend computer.

##  Keyboard 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**uskeys** | `setxkbmap `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1068-L1070) | Change keyboard layout to american.
**keycode** | `xev "$@"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1073-L1075) | Monitor keycodes of pressed keys.
**norepeat** | `xset -r`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1078-L1080) | Turn off key repeat.
**repeat** | `xset r`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1083-L1085) | Turn on key repeat.

##  Misc 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**blue** | `echo -en "`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1094-L1096) | Change hue of color blue in linux terminal.
**path** | `echo -e ${`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1099-L1100) | List directories contained in path variable.
**bc1** | `gcalccmd "`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1104-L1106) | Run terminal calculator that supports decimal numbers.
**hd1** | `hd "${_HD_`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1109-L1110) | Print hexadecimal representation of file or stream.
**profile** | `source /et`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1114-L1116) | Run profile script.
**vimode** | `set -o vi`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1119-L1121) | Change bash line editing to vi mode.
**emacsmode** | `set -o ema`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1124-L1126) | Change bash line editing to emacs mode.
**loc, linesOfCode** | `rootDir="$`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1131-L1148) | Count lines in files with extension in working and subdirectories.
**ssd** | `sudo fstri`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1151-L1153) | Trim ssd.
**tt** | `gtypist "$`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1156-L1158) | Start typing tutor.

##  Package Management 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**ch, canhaz** | `sudo apt-g`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1166-L1168) | Install package.
**update** | `sudo apt-g`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1171-L1173) | Update information about available packages.
**upgrade** | `sudo apt-g`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1176-L1178) | Upgrade all packages.
**dist-upgrade** | `sudo apt-g`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1183-L1185) | Upgrade all packages intelligently.
**remove** | `sudo apt-g`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1189-L1191) | Remove package and all unneeded packages.
**purge** | `sudo apt-g`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1196-L1198) | Remove package and all unneeded packages together with configuration files.
**autoremove** | `sudo apt-g`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1202-L1204) | Remove unneeded packages.
**installed, packages** | `cat /var/l`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1208-L1213) | Print packages that were installed by user.
**allInstalled, allPackages** | `dpkg --get`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1216-L1220) | Print all installed packages.
**depends** | `apt-cache `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1223-L1229) | Print package dependencies.

##  Package Information 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**pd, describe** | `apt-cache `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1237-L1239) | Print package description.
**ve, version** | `# Check if`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1256-L1273) | Print version of package or version of installed commands package.
**package** | `call1=$(su`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1303-L1319) | Print package of installed command together with description and location.

##  Package Search 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**findPackage** | `apt-cache `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1328-L1331) | Find available packages with part of name or description.
**ap, apropos1, findCommand** | `apropos "$`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1336-L1339) | Find installed commands with part of name or description.
**apt-file1** | `apt-file s`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1342-L1346) | Find available packages that provide command.
**wi, whatis1** | `# Checks i`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1384-L1408) | Describe package or command or find available packages with part of name or available packages that provide command.

##  Git 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**commit** | `git commit`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1417-L1419) | Commit changed and deleted files with message.
**commitm** | `git commit`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1423-L1425) | Commit changed and deleted files and edit message in editor.
**init** | `git init "`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1429-L1431) | Initialize repository.
**push** | `git push "`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1434-L1436) | Push changes to remote repository.
**pull** | `git pull "`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1439-L1441) | Pull changes from remote repository.
**merge** | `git merge `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1444-L1446) | Merge specified branch with current one.
**gc, checkout** | `git checko`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1450-L1452) | Checkout branch or file.
**gb, branch** | `git branch`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1455-L1457) | List branches or create new one.
**gs** | `git -c col`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1460-L1463) | Print short repository status.
**gl** | `git log --`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1467-L1469) | Display log of commits.
**gl1** | `git log --`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1473-L1479) | Display minimal log of commits.
**gu** | `git remote`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1483-L1486) | Update information about remote repository and print status.
**gd** | `git diff "`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1490-L1492) | Display changes between commits.
**ga** | `git add "$`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1495-L1497) | Add files to repository.
**gm** | `git mv "$@`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1502-L1504) | Move repositories files.
**gls, lsgit** | `git ls-fil`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1507-L1509) | List files that are in repository.

##  Github 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**clone** | `git clone `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1518-L1520) | Clone github project.
**origin** | `git remote`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1524-L1528) | Set github project as remote repository.
**cloneAll** | `if [[ -z "`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1531-L1543) | Clone all users github projects.

##  Network 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**ip1** | `/sbin/ifco`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1551-L1557) | Print internal ip.
**ip2** | `lynx --dum`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1560-L1562) | Print external ip.
**gateway** | `route -n \`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1565-L1570) | Print gateways ip.
**mac** | `ifconfig |`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1573-L1575) | Print mac addresses of network devices.
**pa, pingAll** | `ping -c 1 `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1578-L1582) | Ping gateway and google.
**nmap1** | `if [[ $# -`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1586-L1602) | Scan local network.
**ne, network** | `localIp=$(`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1630-L1644) | Print ssh port status of local devices and ping google.

##  Wireless 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**woff** | `sudo rfkil`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1669-L1674) | Block wireless device.
**won** | `sudo rfkil`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1677-L1682) | Unblock wireless device.
**wr** | `woff`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1685-L1688) | Reset wireless device.
**up** | `sudo ifcon`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1691-L1693) | Activate wireless interface.
**down** | `sudo ifcon`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1696-L1698) | Deactivate wireless interface.
**wlan** | `sudo iwlis`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1701-L1711) | Print wireless networks in range.

##  Internet 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**i, www, internet** | `__runComma`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1719-L1721) | Start default browser in background.
**fire** | `__runComma`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1724-L1726) | Start firefox in background.
**chrome** | `__runComma`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1730-L1731) | Start chrome in background.
**lynx1** | `lynx "${_L`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1736-L1737) | Start terminal web browser.

##  Audio 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**mixer** | `alsamixer `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1745-L1747) | Start terminal volume control.
**a** | `___setVolu`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1755-L1757) | Increase volume by six decibels.
**z** | `___setVolu`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1760-L1762) | Decrease volume by six decibels.
**aa** | `___setVolu`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1765-L1767) | Increase volume by two decibels.
**zz** | `___setVolu`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1770-L1772) | Decrease volume by two decibels.
