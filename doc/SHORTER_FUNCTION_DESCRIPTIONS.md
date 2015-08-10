Commands
--------

####  Less 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------

####  Ls 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**l** | `___displayOutpu`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L173-L176) | List or display directory contents in pager using short listing format.

####  Tree 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**t, tree1** | `tree -C -I .git`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L271-L273) | Print directory structure.

####  Files 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**cpdir** | `cp --interactiv`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L356-L358) | Copy directories safely.
**mvdir** | `mv --interactiv`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L362-L364) | Move directories safely.
**rmdir** | `rm --interactiv`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L369-L371) | Delete directories safely.
**mk, md, mkdir1** | `mkdir --parents`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L375-L378) | Create directory and descend into.
**bk, backup** | `sudo cp --prese`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L382-L384) | Backup file.

####  Echo 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**e** | `echo "$@"` | Print text.

####  Run In Background 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**rb, runInBackground** | `nohup "$@" &>/d`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L436-L438) | Run command in background.

####  Basics 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**c** | `cat "$@"` | Print file contents.
**?** | `echo $?` | Print exit code of last command.
**q** | `exit` | Exit bash shell.
**o, openFile** | `__runCommandInB`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L531-L533) | Open file with default app.
**te, terminal** | `x-terminal-emul`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L536-L538) | Open new terminal with same working directory.
**me, makeExecutable** | `if [[ ! -f "$1"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L574-L603) | Make file executable or create new bash or python script.

####  Text Editors 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**v** | `vim -p "$@"` | Edit file with vim.
**vv** | `view -p "$@"` | View file in vim.

####  Sudo 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**f, fuck** | `sudo $(history `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L679-L681) | Execute last command as super user.
**sv** | `sudo vim -p "$@`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L727-L729) | Edit file with vim as super user.

####  Search 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**gr** | `__printLinesCon`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L967-L970) | Print or display with pager lines containing pattern.
**lo, locate1** | `locate  "$1" \`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L984-L988) | Locate files on filesystem containing pattern in their names.

####  Archives 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**extract** | `if [ -z "$1" ];`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1007-L1040) | Extract archive of any type.

####  System Information 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**df1** | `df -h | grep "s`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1068-L1070) | Print available disk space in simplified form.
**du1** | `du --summarize `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1074-L1076) | Print disk space occupied by file or folder.

####  Misc 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**blue** | `echo -en "\e]PC`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1166-L1168) | Change hue of color blue in linux terminal.

####  Package Management 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**ch, canhaz** | `sudo apt-get in`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1216-L1218) | Install package.

####  Package Information 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------

####  Package Search 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------

####  Git 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**gs** | `git -c color.st`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1510-L1513) | Print short repository status.
**gl** | `git log --decor`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1517-L1519) | Display log of commits.
**gd** | `git diff "$@"` | Display changes between commits.
**ga** | `git add "$@"` | Add files to repository.

####  Github 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**clone** | `git clone git@g`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1568-L1570) | Clone github project.

####  Network 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**ip1** | `/sbin/ifconfig `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1601-L1607) | Print internal ip.
**pa, pingAll** | `ping -c 1 -q $(`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1628-L1632) | Ping gateway and google.
**ne, network** | `localIp=$(ip1)`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1680-L1711) | Print ssh port status of local devices and ping google.

####  Wireless 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**wr** | `woff`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1735-L1738) | Reset wireless device.

####  Internet 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**i, www, internet** | `__runCommandInB`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1769-L1771) | Start default browser in background.

