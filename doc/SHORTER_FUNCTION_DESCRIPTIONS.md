Commands
--------
**mk, md, mkdir1** | `mkdir --parents`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L390-L393) | Create directory and descend into.
**rb, runInBackground** | `nohup "$@" &>/d`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L451-L453) | Run command in background.
**cpdir** | `cp --interactiv`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L371-L373) | Copy directories safely.
**te, terminal** | `x-terminal-emul`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L554-L556) | Open new terminal with same working directory.

####  Misc 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------

####  Tree 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**gs** | `git -c color.st`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1574-L1577) | Print short repository status.
**q** | `exit` | Exit bash shell.
**clone** | `git clone git@g`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1632-L1634) | Clone github project.
**blue** | `echo -en "\e]PC`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1228-L1230) | Change hue of color blue in linux terminal.
**gd** | `git diff "$@"` | Display changes between commits.

####  Archives 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------

####  Files 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**?** | `echo $?` | Print exit code of last command.

####  Ls 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**wr** | `woff`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1799-L1802) | Reset wireless device.
**ip1** | `/sbin/ifconfig `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1665-L1671) | Print internal ip.

####  Less 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**gl** | `git log --decor`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1581-L1583) | Display log of commits.
**mvdir** | `mv --interactiv`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L377-L379) | Move directories safely.

####  Text Editors 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------

####  Basics 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**t, tree1** | `tree -C -I .git`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L286-L288) | Print directory structure.
**lo, locate1** | `locate  "$1" \`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1043-L1047) | Locate files on filesystem containing pattern in their names.
**gr** | `__printLinesCon`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1025-L1028) | Print or display with pager lines containing pattern.

####  Echo 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**v** | `vim -p "$@"` | Edit file with vim.

####  Run In Background 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------

####  Package Information 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------

####  Git 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**sv** | `sudo vim -p "$@`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L767-L769) | Edit file with vim as super user.
**du1** | `du --summarize `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1135-L1137) | Print disk space occupied by file or folder.
**e** | `echo "$@"` | Print text.

####  System Information 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**ne, network** | `localIp=$(ip1)`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1744-L1775) | Print ssh port status of local devices and ping google.
**bk, backup** | `sudo cp --prese`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L397-L399) | Backup file.
**vv** | `view -p "$@"` | View file in vim.

####  Network 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------

####  Package Search 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**i, www, internet** | `__runCommandInB`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1833-L1835) | Start default browser in background.
**l** | `___displayOutpu`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L184-L187) | List or display directory contents in pager using short listing format.

####  Github 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**extract** | `if [ -z "$1" ];`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1067-L1100) | Extract archive of any type.
**ch, canhaz** | `sudo apt-get in`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1279-L1281) | Install package.
**o, openFile** | `__runCommandInB`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L549-L551) | Open file with default app.
**df1** | `df -h | grep "s`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1129-L1131) | Print available disk space in simplified form.
**rmdir** | `rm --interactiv`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L384-L386) | Delete directories safely.

####  Internet 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------

####  Search 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------

####  Package Management 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------

####  Sudo 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**ga** | `git add "$@"` | Add files to repository.

####  Wireless 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**pa, pingAll** | `ping -c 1 -q $(`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1692-L1696) | Ping gateway and google.
**me, makeExecutable** | `if [[ ! -f "$1"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L596-L625) | Make file executable or create new bash or python script.
**f, fuck** | `sudo $(history `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L713-L715) | Execute last command as super user.
**c** | `cat "$@"` | Print file contents.

