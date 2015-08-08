Standard Aliases
================

Make Linux more user friendly with this collection of [**Bash aliases**](http://tldp.org/LDP/abs/html/aliases.html).

Technically they are not aliases but Bash Functions, but *Standard Aliases* sounds less generic than *Standard Functions*...

Linux is elegant and concise, but it is also hard.
If you can't type well and/or have problem with memorizing stuff you're basically screwed.

This collection provides the commands, that should be in Linux by default,
or just an aberrations of commands that are provided, but are so commonly used that they deserve a shorter name.

Bash aliases are most useful device for customizing your Linux...
Here is a short list of ones I find most useful:


Commands
--------

Below is a short list of most useful commands. If you want to check the full list click here: [**LIST OF ALL FUNCTIONS**](FUNCTION_DESCRIPTIONS.md)


####  Basic

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ---------------
**l** | `___displayOutpu`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L172-L175) | List or display directory contents in pager using short listing format.
**e** | `echo "$@"` | Print text.
**c** | `cat "$@"` | Print file contents.
**m** | `___printOrDispl`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L63-L65) | Print or display text or file in pager.
**v** | `vim -p "$@"` | Edit file with vim.
**q** | `exit` | Exit bash shell.
**te** | `gnome-terminal `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L497-L499) | Open new terminal with same working directory.
**?** | `echo $?` | Print exit code of last command.

####  Files 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**t, tree1** | `tree -C -I .git`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L264-L266) | Print directory structure.
**cpdir** | `cp --interactiv`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L349-L351) | Copy directories safely.
**mvdir** | `mv --interactiv`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L355-L357) | Move directories safely.
**rmdir** | `rm --interactiv`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L362-L364) | Delete directories safely.
**mk, mkdir1** | `mkdir --parents`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L368-L371) | Create directory and descend into.
**bk, backup** | `sudo cp --prese`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L375-L377) | Backup file.
**o, openFile** | `__runCommandInB`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L492-L494) | Open file with default app.
**me, makeExecutable** | `if [[ ! -f "$1"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L535-L564) | Make file executable or create new bash or python script.
**extract** | `if [ -z "$1" ];`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L968-L1001) | Extract archive of any type.
**du1** | `du --summarize `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1035-L1037) | Print disk space occupied by file or folder.
**lo, locate1** | `locate  "$1" \`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L945-L949) | Locate files on filesystem containing pattern in their names.

####  Useful 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**f, fuck** | `sudo $(history `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L640-L642) | Execute last command as super user.
**rb, runInBackground** | `nohup "$@" &>/d`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L429-L431) | Run command in background.
**gr** | `__printLinesCon`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L928-L931) | Print or display with pager lines containing pattern.
**grr** | `__printLinesCon`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L935-L941) | Print or display with pager numbered lines containing pattern in working and subdirectories.
**df1** | `df -h | grep "s`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1029-L1031) | Print available disk space in simplified form.

####  Packages

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**ch, canhaz** | `sudo apt-get in`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1177-L1179) | Install package.
**ve, version** | `# Check if pass`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1267-L1284) | Print version of package or version of installed commands package.
**wi, whatis1** | `# Checks if it `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1395-L1419) | Describe package or command or find available packages with part of name or available packages that provide command.

####  Git 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**gs** | `git status -c `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1471-L1474) | Print short repository status.
**gl** | `git log --decor`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1478-L1480) | Display log of commits.
**gd** | `git diff "$@"` | Display changes between commits.
**ga** | `git add "$@"` | Add files to repository.

####  Network 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**ip1** | `/sbin/ifconfig `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1562-L1568) | Print internal ip.
**pa, pingAll** | `ping -c 1 -q $(`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1589-L1593) | Ping gateway and google.
**i, www, internet** | `__runCommandInB`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1730-L1732) | Start default browser in background.


How to install
--------------

```bash
$ git clone https://github.com/gto76/standard-aliases.git
$ cd standard-aliases
$ ./install
```

Short Description
-----------------

All functions have long and descriptive name, that starts with two underscores, so they don't polute the shells namespace. This functions are then "aliased" with shorther name, or names, that are specified in `standardrc` configuration file.

Utility functions, that are not meant to be aliased start with three underscores.

Every alias that doesen't just define a different name for a command is defined as a function with descriptive name. This function is then aliased with a shorher and more convinient name. Do not change the names of the functions because they may be used by other functions.

Also only aliases get documented by generate-readme script.

This aliases were made for debian based linux (ubuntu, mint,...) with gnome desktop environment, but most aliases will work on all systems with Bash shell.

Most aliases will send output to pager if it will be too long to fit the screen.

Some aliases require special tools that are not installed by default on most systems. You can install them all at one with command belove, but it is probably more reasonable to just install them when demand arises.

By convention a function that calls the a command with some set of options that are quiet sensible for that command is usualy aliased with <command-name>1, and often also with a two letter aberration. Options for this commands are defined in `standardrc`

Usualy if alias only makes command easier to use, either by providing the options that should have been set by default, or just by sending output of command to pager if necesary, then it has same name as command, but with number 1 apended at the end. Some examples are:
ps1
pgrep1
tree1
mkdir1

Only aliases that override the commands are cp, mv and rm. They are all run in interactive mode, meaning you get asked for conformation before any destructive operation. If you want to execute them without this promptint, then use -f (force) option. 

When adding new alias alwalys check if it is already taken by any command with `wi <alias>`.

completions...
automatioc completions from the command that gets parameters in function.

// Intentions
I know it is a bit abnockuous to think your colection of aliases is so great, that it should become adopted as standard, but what a hack, I worked on and been using them for long time, and I just feel so limited withouth them.

