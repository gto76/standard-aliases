Standard Aliases
================

Make Linux more user friendly with this collection of bash aliases.

Bash aliases are most useful device for customizing your Linux...
Here is a short list of ones i find most useful:

** t - tree
l/ll/lll (GIF)
cpdir/mvdir/rmdir
** rb - runs command in background
** o  - open file with default app
mk - mkdir and descend into
me - make executable
gr - grep with pager
** extract - extracts archive of any type
ch - can haz
version
** wi - what is (GIF)
gs - git status
gl - git log
gd - git diff
ip1 - internal ip
ip2 - external ip
pa - ping all
** ne - network status
wr - wireless reset
i - internet: default browser in background
al - opens this file in vim

?ma - make with pager
?m  - cat or less
?te - open another terminal with same working directory
?fu - fuck: runs last command as sudo
?ty - type


Every alias that doesen't just define a different name for a command is defined as a function with descriptive name. This function is then aliased with a shorher and more convinient name. Do not change the names of the functions because they may be used by other functions.

Also only aliases get documented by generate-readme script.

By convention a function that calls the a command with some set of options that are quiet sensible for that command to be run with is named <command-name>WithSensibleOptions. This function is then usualy aliased with <command-name>1, and often also with a two letter aberration.




This aliases were made for debian based linux (ubuntu, mint,...) with gnome desktop environment, but most aliases will work on all systems with bash shell.

Most aliases will send output to pager if it will be too long to fit the screen.

Some aliases require special tools that are not installed by default on most systems. You can install them all at one with command belove, but it is probably more reasonable to just install them when demand arises.

Usualy if alias only makes command easier to use, either by providing the options that should have been set by default, or just by sending output of command to pager if necesary, then it has same name as command, but with number 1 apended at the end. Some examples are:
ps1
pgrep1
tree1
mkdir1

Only aliases that override the commands are cp, mv and rm. They are all run in interactive mode, meaning you get asked for conformation before any destructive operation. If you want to execute them without this promptint, then use -f (force) option. 

If the list belowe seems too long here is a shorthened list of aliases, that I consider almost necesary:)
m
l/ll/lll
cpdir/mvdir/rmdir
rb
o
ty
te
(ma)
mk

When adding new alias alwalys check if it is already taken by any command with `wi <alias>`.

Do not change the names of the functions, because other functions and/or aliases may be using it. You can however freely change the names of the aliases.


// Intentions
I know it is a bit abnockuous to think your colection of aliases is so great, that it should become adopted as standard, but what a hack, I worked on and been using them for long time, and I just feel so limited withouth them.


completions...
automatioc completions from the command that gets parameters in function.

Linux for the rest of us.

Linux is elegant and concise, but it is also hard.
If you can't type well and/or have problem with memorizing stuff you're basically screwed.

### Commands
 _Name_        | _Runs_  | _Description_  
:------------- |:--------:| ---------------------------------------------------
**ll**       | `__listOrDisp`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L174-L175)    | List or display directory contents in pager using medium listing format.  
**h, history1**      | `if [ "$#" ` [**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L591-L598)   | Search command history for pattern. 


###  Less 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**le, less1, burek ** | `less "${_L`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L22-L23) |  Display text in pager.
**m ** | `__printOrD`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L64-L66) |  Print or display text in pager.
**mm ** | `if [[ "$#"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L77-L95) |  Print and display text in pager if necessary.

###  Ls 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**l ** | `__displayO`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L173-L176) |  List or display directory contents in pager using short listing format.
**ll ** | `__displayO`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L178-L181) |  List or display directory contents in pager using medium listing format.
**lll ** | `__displayO`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L183-L186) |  List or display directory contents in pager using long listing format.
**la ** | `__listOrDi`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L188-L191) |  List or display all directory contents in pager using short listing format.
**lla ** | `__listOrDi`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L193-L196) |  List or display all directory contents in pager using medium listing format.
**llla ** | `__listOrDi`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L198-L201) |  List or display all directory contents in pager using long listing format.
**lt ** | `__listOrDi`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L203-L206) |  List or display directory contents in pager ordered by date using short listing format.
**llt ** | `__listOrDi`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L208-L211) |  List or display directory contents in pager ordered by date using medium listing format.
**lllt ** | `__listOrDi`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L213-L216) |  List or display directory contents in pager ordered by date using long listing format.
**dl ** | `__listOrDi`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L218-L221) |  List or display matching directories in pager using short listing format.
**dll ** | `__listOrDi`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L223-L226) |  List or display matching directories in pager using medium listing format.
**dlll ** | `__listOrDi`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L228-L231) |  List or display matching directories in pager using long listing format.
**l1 ** | `__listOrDi`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L233-L236) |  List or display in pager one directory item per line using short listing format.
**la1 ** | `__listOrDi`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L238-L241) |  List or display in pager one directory item per line including hidden files using short listing format.
**first ** | `ls "$@" | `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L244-L246) |  Get first file in directory.
**rf, randomFile ** | `ls "$@" | `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L249-L251) |  Get random file in directory.
**findd, directories ** | `find . -na`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L255-L257) |  Print all subdirectories.

###  Tree 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**t, tree1 ** | `tree "${_T`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L265-L266) |  Print directory structure.

###  Cd 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**.., cd.. ** | `__goUpNumb`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L293-L295) |  Go up one directory.
**... ** | `__goUpNumb`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L297-L299) |  Go up two directories.
**.... ** | `__goUpNumb`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L301-L303) |  Go up three directories.
**..... ** | `__goUpNumb`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L305-L307) |  Go up four directories.
**...... ** | `__goUpNumb`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L309-L311) |  Go up five directories.
**....... ** | `__goUpNumb`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L313-L315) |  Go up six directories.
**cdiso ** | `sudo mkdir`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L318-L322) |  Mount iso and cd into.

###  Files 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**cp ** | `cp --inter`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L331-L333) |  Copy files safely.
**mv ** | `mv --inter`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L337-L339) |  Move files safely.
**rm ** | `rm --inter`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L344-L346) |  Delete files safely.
**cpdir ** | `cp --inter`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L350-L352) |  Copy directories safely.
**mvdir ** | `mv --inter`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L356-L358) |  Move directories safely.
**rmdir ** | `rm --inter`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L363-L365) |  Delete directories safely.
**mk, md, mkdir1 ** | `mkdir --pa`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L369-L372) |  Create directory and descend into.
**bk, backup ** | `sudo cp --`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L376-L377) |  Backup file.
**switch ** | `tempFile=$`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L381-L386) |  Switch contents of files.

###  Pwd 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**p ** | `if [[ $# -`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L395-L401) |  Print working directory or path to file.

###  Echo 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**e ** | `echo "$@"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L409-L411) |  Print text.
**ee ** | `echo -e "$`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L414-L416) |  Print text interpreting backslashed characters.
**en ** | `echo -n "$`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L419-L421) |  Print text without trailing newline.

###  Run In Background 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**rb, runInBackground ** | `nohup "$@"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L430-L432) |  Run command in background.

###  Basics 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**al, aliases ** | `vim ~/.sta`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L442-L444) |  Edit standard aliases.
**ba ** | `bash "$@"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L448-L450) |  Start new bash shell.
**ty, type1 ** | `type "$@" `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L455-L457) |  Print command type or definition.
**tyty ** | `type $(typ`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L460-L463) |  Print function that a function calls.
**c ** | `cat "$@"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L467-L469) |  Print contents of file.
**?, exitCode ** | `echo $?`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L472-L474) |  Print exit code of last command.
**cl ** | `clear`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L477-L479) |  Clear the screen.
**re ** | `reset "$@"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L482-L484) |  Reset the screen.
**q ** | `exit`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L487-L489) |  Exit bash shell.
**o, openFile ** | `__runComma`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L493-L495) |  Open file with default app.
**te, terminal ** | `gnome-term`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L498-L500) |  Open new terminal with same working directory.
**he ** | `head "$@"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L503-L505) |  Print first ten lines.
**he1, firstLine ** | `head -n1 "`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L508-L510) |  Print first line.
**ta ** | `tail "$@"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L513-L515) |  Print last ten lines.
**ta1, lastLine ** | `tail -n1 "`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L518-L520) |  Print last line.
**wcl, countLines ** | `wc -l "$@"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L523-L525) |  Count lines.
**wcw, countWords ** | `wc -w "$@"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L528-L530) |  Count words.
**to ** | `touch "${_`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L534-L535) |  Update files timestamp or create new one.
**da ** | `date "${_D`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L539-L540) |  Print date and time.
**ma, make1 ** | `make "${_M`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L545-L546) |  Run make with pager.
**na, explorer ** | `__runComma`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L555-L557) |  Start file explorer in background in working directory.
**diff1 ** | `colordiff `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L560-L561) |  Compare files line by line in color.
**me, makeExecutable ** | `if [[ ! -f`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L566-L581) |  Make file executable or create new bash script.

###  History 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**h, history1 ** | `if [ "$#" `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L590-L599) |  Search command history for pattern.

###  Text Editors 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**v, vim1 ** | `vim "${_VI`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L607-L608) |  Edit file with vim.
**vv ** | `view "${_V`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L613-L614) |  View file in vim.
**n, nano1 ** | `nano "${_N`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L627-L628) |  Edit file with nano.
**g ** | `__runComma`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L632-L633) |  Edit file with gedit.
**sub ** | `__runComma`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L637-L639) |  Edit file with sublime text.

###  Sudo 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**s ** | `sudo "$@"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L647-L649) |  Run command as super user.
**f, fu, fuck ** | `sudo $(his`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L653-L655) |  Execute last command as super user.
**sudoCp ** | `sudo cp --`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L659-L661) |  Copy files safely as super user.
**smv ** | `sudo mv --`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L665-L667) |  Move files safely as super user.
**srm ** | `sudo rm --`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L672-L674) |  Delete files safely as super user.
**scpdir ** | `sudo cp --`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L678-L680) |  Copy directories safely as super user.
**smvdir ** | `sudo mv --`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L684-L686) |  Move directories safely as super user.
**srmdir ** | `sudo rm --`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L691-L693) |  Delete directories safely as super user.
**sm, sle ** | `sudo less `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L696-L697) |  Display text in pager as super user.
**svv ** | `sudo view `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L701-L702) |  View file in vim as super user.
**sv ** | `sudo vim "`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L706-L707) |  Edit file with vim as super user.
**sn ** | `sudo nano `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L711-L712) |  Edit file with nano as super user.
**sg ** | `sudo gedit`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L716-L717) |  Edit file with gedit as super user.
**fdisk ** | `sudo fdisk`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L724-L726) |  Run fdisk as super user.
**updatedb ** | `sudo updat`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L728-L730) |  Run updatedb as super user.
**ifconfig ** | `sudo ifcon`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L732-L734) |  Run ifconfig as super user.
**tcpdump ** | `sudo tcpdu`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L736-L738) |  Run tcpdump as super user.
**route ** | `sudo route`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L740-L742) |  Run route as super user.
**pm-hibernate ** | `sudo pm-hi`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L744-L746) |  Run pm-hibernate as super user.
**pm-suspend ** | `sudo pm-su`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L748-L750) |  Run pm-suspend as super user.
**shutdown ** | `sudo shutd`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L752-L754) |  Run shutdown as super user.
**fstrim ** | `sudo fstri`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L756-L758) |  Run fstrim as super user.
**aptget ** | `sudo aptge`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L760-L762) |  Run apt-get as super user.
**iw ** | `sudo iw "$`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L764-L766) |  Run iw as super user.
**nmap ** | `sudo nmap `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L768-L770) |  Run nmap as super user.
**parted ** | `sudo parte`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L772-L774) |  Run parted as super user.
**ntfsundelete ** | `sudo ntfsu`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L776-L778) |  Run ntfsundelete as super user.
**lshw ** | `sudo lshw `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L780-L782) |  Run lshw as super user.
**chown ** | `sudo chown`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L784-L786) |  Run chown as super user.
**mount ** | `sudo mount`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L788-L790) |  Run mount as super user.

###  Procesess 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**ht, taskManager ** | `htop "${_H`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L798-L799) |  Run terminal task manager.
**ps1 ** | `ps "${_PS_`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L804-L805) |  Print users processes.
**psa, pse, processes ** | `ps -e "${_`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L809-L810) |  Print all processes.
**pgrep1 ** | `pgrep "${_`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L815-L816) |  Find processes with part of name.
**kill1 ** | `kill -9 "$`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L826-L828) |  Kill process with kill signal.
**st, strace1, trace ** | `strace "${`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L833-L834) |  Trace system calls.

###  Text 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**trd ** | `tr --delet`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L845-L847) |  Delete characters.
**table ** | `column -t `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L851-L853) |  Line up columns.
**cut1, keepColumns ** | `cut --deli`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L859-L861) |  Keep columns.
**sort1 ** | `sort --fie`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L867-L869) |  Sort lines by column.

###  Search 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**grep1 ** | `grep --col`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L880-L881) |  Print lines containing pattern.
**gr ** | `__printLin`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L886-L889) |  Print or display with pager lines containing pattern.
**lo, locate1 ** | `locate "${`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L893-L894) |  Locate files on filesystem containing pattern in their names.
**find1 ** | `find "${_F`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L903-L904) |  Locate files containing pattern in their names in working and sub directories.

###  Archives 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**extract ** | `if [ -z "$`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L916-L924) |  Extract archive of any type.

###  Tmux 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**tm ** | `tmux "${_T`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L957-L958) |  Run terminal multiplexer.
**tma ** | `tmux attac`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L962-L964) |  Run terminal multiplexer and attach to session.
**tml ** | `tmux ls`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L967-L969) |  List terminal multiplexers sessions.

###  System Information 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**df1 ** | `df -h | gr`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L977-L979) |  Print available disk space in simplified form.
**du1 ** | `du --summa`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L983-L985) |  Print disk space occupied by file or folder.
**fr, free1 ** | `echo "all:`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L988-L995) |  Print all and ocupied memory space in megabytes.
**temp, temperature ** | `acpi -t`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L998-L1000) |  Print temperature of cpu.
**batt, battery ** | `acpi`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1003-L1005) |  Print battery status.
**uname1, kernelVersion ** | `uname --al`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1008-L1010) |  Print operating system information.
**pci, lspci1 ** | `lspci "${_`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1013-L1014) |  Print info about pci devices.

###  Power 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**restart ** | `sudo shutd`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1024-L1026) |  Restart computer.
**poweroff ** | `sudo shutd`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1029-L1031) |  Shut down computer.
**hib ** | `sudo pm-hi`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1034-L1036) |  Hibernate computer.
**sus ** | `sudo pm-su`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1039-L1041) |  Suspend computer.

###  Keyboard 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**uskeys ** | `setxkbmap `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1049-L1051) |  Change keyboard layout to american.
**keycode ** | `xev "$@"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1054-L1056) |  Monitor keycodes of pressed keys.
**norepeat ** | `xset -r`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1059-L1061) |  Turn off key repeat.
**repeat ** | `xset r`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1064-L1066) |  Turn on key repeat.

###  Misc 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**blue ** | `echo -en "`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1075-L1077) |  Change hue of color blue in linux terminal.
**path ** | `echo -e ${`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1080-L1081) |  List directories contained in path variable.
**bc1 ** | `gcalccmd "`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1085-L1087) |  Run terminal calculator that supports decimal numbers.
**hd1 ** | `hd "${_HD_`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1090-L1091) |  Print hexadecimal representation of file or stream.
**profile ** | `source /et`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1095-L1097) |  Run profile script.
**vimode ** | `set -o vi`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1100-L1102) |  Change bash line editing to vi mode.
**emacsmode ** | `set -o ema`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1105-L1107) |  Change bash line editing to emacs mode.
**loc, linesOfCode ** | `rootDir="$`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1112-L1129) |  Count lines in files with extension in working and subdirectories.
**ssd ** | `sudo fstri`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1132-L1134) |  Trim ssd.
**tt ** | `gtypist "$`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1137-L1139) |  Start typing tutor.

###  Package Management 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**ch, canhaz ** | `sudo apt-g`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1147-L1149) |  Install package.
**update ** | `sudo apt-g`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1152-L1154) |  Update information about available packages.
**upgrade ** | `sudo apt-g`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1157-L1159) |  Upgrade all packages.
**dist-upgrade ** | `sudo apt-g`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1164-L1166) |  Upgrade all packages intelligently.
**remove ** | `sudo apt-g`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1170-L1172) |  Remove package and all unneeded packages.
**purge ** | `sudo apt-g`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1177-L1179) |  Remove package and all unneeded packages together with configuration files.
**autoremove ** | `sudo apt-g`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1183-L1185) |  Remove unneeded packages.
**installed, packages ** | `cat /var/l`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1189-L1194) |  Print packages that were installed by user.
**allInstalled, allPackages ** | `dpkg --get`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1197-L1201) |  Print all installed packages.
**depends ** | `apt-cache `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1204-L1210) |  Print package dependencies.

###  Package Information 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**pd, describe ** | `apt-cache `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1218-L1220) |  Print package description.
**ve, version ** | `# Check if`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1237-L1254) |  Print version of package or version of installed commands package.
**package ** | `call1=$(su`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1284-L1300) |  Print package of installed command together with description and location.

###  Package Search 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**findPackage ** | `apt-cache `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1309-L1312) |  Find available packages with part of name or description.
**ap, apropos1, findCommand ** | `apropos "$`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1317-L1320) |  Find installed commands with part of name or description.
**apt-file1 ** | `apt-file s`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1323-L1327) |  Find available packages that provide command.
**wi, whatis1 ** | `# Checks i`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1364-L1388) |  Describe package or command or find available packages with part of name or available packages that provide command.

###  Git 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**commit ** | `git commit`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1397-L1399) |  Commit changed and deleted files with message.
**commitm ** | `git commit`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1403-L1405) |  Commit changed and deleted files and edit message in editor.
**init ** | `git init "`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1409-L1411) |  Initialize repository.
**push ** | `git push "`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1414-L1416) |  Push changes to remote repository.
**pull ** | `git pull "`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1419-L1421) |  Pull changes from remote repository.
**merge ** | `git merge `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1424-L1426) |  Merge specified branch with current one.
**gc, checkout ** | `git checko`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1430-L1432) |  Checkout branch or file.
**gb, branch ** | `git branch`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1435-L1437) |  List branches or create new one.
**gs ** | `git -c col`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1440-L1443) |  Print short repository status.
**gl ** | `git log --`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1447-L1449) |  Display log of commits.
**gl1 ** | `git log --`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1453-L1459) |  Display minimal log of commits.
**gu ** | `git remote`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1463-L1466) |  Update information about remote repository and print status.
**gd ** | `git diff "`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1470-L1472) |  Display changes between commits.
**ga ** | `git add "$`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1475-L1477) |  Add files to repository.
**gm ** | `git mv "$@`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1482-L1484) |  Move repositories files.
**gls, lsgit ** | `git ls-fil`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1487-L1489) |  List files that are in repository.

###  Github 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**clone ** | `git clone `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1498-L1500) |  Clone github project.
**origin ** | `git remote`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1504-L1508) |  Set github project as remote repository.
**cloneAll ** | `if [[ -z "`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1511-L1523) |  Clone all users github projects.

###  Network 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**ip1 ** | `/sbin/ifco`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1531-L1537) |  Print internal ip.
**ip2 ** | `lynx --dum`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1540-L1542) |  Print external ip.
**gateway ** | `route -n \`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1545-L1550) |  Print gateways ip.
**mac ** | `ifconfig |`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1553-L1555) |  Print mac addresses of network devices.
**pa, pingAll ** | `ping -c 1 `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1558-L1562) |  Ping gateway and google.
**nmap1 ** | `if [[ $# -`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1566-L1582) |  Scan local network.
**ne, network ** | `localIp=$(`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1610-L1624) |  Print ssh port status of local devices and ping google.

###  Wireless 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**woff ** | `sudo rfkil`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1649-L1654) |  Block wireless device.
**won ** | `sudo rfkil`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1657-L1662) |  Unblock wireless device.
**wr ** | `woff`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1665-L1668) |  Reset wireless device.
**up ** | `sudo ifcon`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1671-L1673) |  Activate wireless interface.
**down ** | `sudo ifcon`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1676-L1678) |  Deactivate wireless interface.
**wlan ** | `sudo iwlis`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1681-L1691) |  Print wireless networks in range.

###  Internet 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**i, www, internet ** | `__runComma`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1699-L1701) |  Start default browser in background.
**fire ** | `__runComma`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1704-L1706) |  Start firefox in background.
**chrome ** | `__runComma`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1710-L1711) |  Start chrome in background.
**lynx1 ** | `lynx "${_L`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1716-L1717) |  Start terminal web browser.

###  Audio 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**mixer ** | `alsamixer `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1725-L1727) |  Start terminal volume control.
**a ** | `__setVolum`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1735-L1737) |  Increase volume by six decibels.
**z ** | `__setVolum`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1740-L1742) |  Decrease volume by six decibels.
**aa ** | `__setVolum`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1745-L1747) |  Increase volume by two decibels.
**zz ** | `__setVolum`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L1750-L1752) |  Decrease volume by two decibels.
**ls_medium ; -l --no-group -g --human-readable --time-style=+%b\ %_d\ %Y\ %H** | `#!/bin/bas`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/standard_aliases#L0-L1) | %M
