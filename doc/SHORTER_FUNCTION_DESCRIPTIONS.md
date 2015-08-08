Commands
--------

####  Less 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**m** | `___printOrDispl`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L64-L66) | Print or display text in pager.

####  Ls 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**l** | `___displayOutpu`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L173-L176) | List or display directory contents in pager using short listing format.
**rf, randomFile** | `ls "$@" | sort `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L249-L251) | Print name of random file in directory.

####  Tree 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**t, tree1** | `tree -C -I .git`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L265-L267) | Print directory structure.

####  Cd 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**.., cd..** | `___goUpNumberOf`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L293-L295) | Go up one directory.
**cdiso** | `sudo mkdir /med`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L318-L322) | Mount iso and cd into.

####  Files 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**cpdir** | `cp --interactiv`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L350-L352) | Copy directories safely.
**mvdir** | `mv --interactiv`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L356-L358) | Move directories safely.
**rmdir** | `rm --interactiv`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L363-L365) | Delete directories safely.
**mk, md, mkdir1** | `mkdir --parents`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L369-L372) | Create directory and descend into.
**bk, backup** | `sudo cp --prese`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L376-L378) | Backup file.

####  Pwd 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**p** | `if [[ $# -eq 0 `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L395-L401) | Print working directory or path to file.

####  Echo 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**e** | `echo "$@"` | Print text.

####  Run In Background 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**rb, runInBackground** | `nohup "$@" &>/d`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L430-L432) | Run command in background.

####  Basics 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**ty, type1** | `type "$@" | __p`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L455-L457) | Print command type or definition.
**c** | `cat "$@"` | Print file contents.
**?, exitCode** | `echo $?` | Print exit code of last command.
**cl, clr** | `clear` | Clear the screen.
**re** | `reset "$@"` | Reset the screen.
**q** | `exit` | Exit bash shell.
**o, openFile** | `__runCommandInB`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L493-L495) | Open file with default app.
**te, terminal** | `gnome-terminal `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L498-L500) | Open new terminal with same working directory.
**to** | `touch  "$@"` | Update files timestamp or create new one.
**ma, make1** | `make  "$@" 2>&1`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L515-L517) | Run make with pager.
**na, explorer** | `__runCommandInB`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L525-L527) | Start file explorer in background in working directory.
**me, makeExecutable** | `if [[ ! -f "$1"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L536-L565) | Make file executable or create new bash or python script.

####  Text Editors 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**v** | `vim -p "$@"` | Edit file with vim.
**vv** | `view -p "$@"` | View file in vim.

####  Sudo 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**f, fu, fuck** | `sudo $(history `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L641-L643) | Execute last command as super user.
**sv** | `sudo vim -p "$@`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L689-L691) | Edit file with vim as super user.

####  Procesess 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**tm, taskManager, ht** | `htop  "$@"` | Run terminal task manager.
**kill1** | `kill -9 "$@"` | Kill process with kill signal.

####  Text 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**loc, linesOfCode** | `rootDir="$PWD"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L870-L885) | Count lines in files with extension in working and subdirectories.

####  Search 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**gr** | `__printLinesCon`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L929-L932) | Print or display with pager lines containing pattern.
**grr** | `__printLinesCon`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L936-L942) | Print or display with pager lines containing pattern in working and subdirectories.
**lo, locate1** | `locate  "$1" \`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L946-L950) | Locate files on filesystem containing pattern in their names.

####  Archives 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**extract** | `if [ -z "$1" ];`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L969-L1002) | Extract archive of any type.

####  System Information 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**df1** | `df -h | grep "s`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1030-L1032) | Print available disk space in simplified form.
**du1** | `du --summarize `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1036-L1038) | Print disk space occupied by file or folder.

####  Power 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**restart** | `sudo shutdown -`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1077-L1079) | Restart computer.
**poweroff** | `sudo shutdown n`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1082-L1084) | Shut down computer.
**hib** | `sudo pm-hiberna`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1087-L1089) | Hibernate computer.
**sus** | `sudo pm-suspend`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1092-L1094) | Suspend computer.

####  Misc 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**blue** | `echo -en "\e]PC`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1128-L1130) | Change hue of color blue in linux terminal.
**vimode** | `set -o vi` | Change bash line editing to vi mode.

####  Package Management 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**ch, canhaz** | `sudo apt-get in`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1178-L1180) | Install package.

####  Package Information 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------

####  Package Search 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**wi, whatis1** | `# Checks if it `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1396-L1420) | Describe package or command or find available packages with part of name or available packages that provide command.

####  Git 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**commit** | `git commit -am `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1429-L1431) | Commit changed and deleted files with message.
**push** | `git push "$@"` | Push changes to remote repository.
**pull** | `git pull "$@"` | Pull changes from remote repository.
**gs** | `git -c color.st`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1472-L1475) | Print short repository status.
**gl** | `git log --decor`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1479-L1481) | Display log of commits.
**gd** | `git diff "$@"` | Display changes between commits.
**ga** | `git add "$@"` | Add files to repository.

####  Github 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**clone** | `git clone git@g`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1530-L1532) | Clone github project.

####  Network 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**ip1** | `/sbin/ifconfig `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1563-L1569) | Print internal ip.
**pa, pingAll** | `ping -c 1 -q `g`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1590-L1594) | Ping gateway and google.
**ne, network** | `localIp=$(ip1)`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1642-L1673) | Print ssh port status of local devices and ping google.

####  Wireless 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**wr** | `woff`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1697-L1700) | Reset wireless device.

####  Internet 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**i, www, internet** | `__runCommandInB`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1731-L1733) | Start default browser in background.

