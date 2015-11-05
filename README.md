Standard Aliases
================

Make Linux more user friendly with this collection of **Bash functions**.

It provides commands that should be in Linux by default, or just an aberrations of commands that are provided, but are so commonly used that they deserve a shorter name.

Collection was made for **Debian** based Linux (**Ubuntu**, **Mint**, ...) with **Gnome** desktop environment, but most commands will work on all systems with installed Bash shell and GNU Coreutils.

There are currently 207 commands.

How to…
-------
### Install
```bash
$ git clone https://github.com/gto76/standard-aliases.git
$ cd standard-aliases
$ ./install
```
### Uninstall
```
$ ./uninstall
```

Commands
--------

Below is a list of most useful commands. If you want to check out the full list see [**LIST OF ALL COMMANDS**](doc/FUNCTION_DESCRIPTIONS.md).

####  Basic 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**l** | `___displayOutpu`[**`...`**](standard_functions#L193-L196) | List or display directory contents in pager using short listing format.
**e** | `echo "$@"` | Print text.
**c** | `cat "$@"` | Print file contents.
**m** | `___printOrDispl`[**`...`**](standard_functions#L91-L93) | Print or display text or file in pager.
**v** | `vim -p "$@"` | Edit file with vim.
**q** | `exit` | Exit bash shell.
**te, terminal** | `x-terminal-emul`[**`...`**](standard_functions#L581-L583) | Open new terminal with same working directory.
**?** | `echo $?` | Print exit code of last command.

####  Files 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**t, tree1** | `tree -C -I .git`[**`...`**](standard_functions#L295-L297) | Print directory structure.
**cpdir** | `cp --interactiv`[**`...`**](standard_functions#L385-L387) | Copy directories safely.
**mvdir** | `mv --interactiv`[**`...`**](standard_functions#L391-L393) | Move directories safely.
**rmdir** | `rm --interactiv`[**`...`**](standard_functions#L398-L400) | Delete directories safely.
**mk, md, mkdir1** | `mkdir --parents`[**`...`**](standard_functions#L404-L407) | Create directory and descend into.
**bk, backup** | `sudo cp --prese`[**`...`**](standard_functions#L411-L413) | Backup file.
**o, openFile** | `__runCommandInB`[**`...`**](standard_functions#L576-L578) | Open file with default app.
**me, makeExecutable** | `if [[ ! -f "$1"`[**`...`**](standard_functions#L625-L654) | Make file executable or create new bash or python script.
**extract** | `if [ -z "$1" ];`[**`...`**](standard_functions#L1096-L1129) | Extract archive of any type.
**du1** | `du --summarize `[**`...`**](standard_functions#L1164-L1166) | Print disk space occupied by file or folder.
**lo, locate1** | `locate  "$1" \`[**`...`**](standard_functions#L1072-L1076) | Locate files on filesystem containing pattern in their names.

####  Useful  

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**f, fuck** | `sudo $(history `[**`...`**](standard_functions#L742-L744) | Execute last command as super user.
**rb, runInBackground** | `nohup "$@" &>/d`[**`...`**](standard_functions#L465-L467) | Run command in background.
**gr** | `__printLinesCon`[**`...`**](standard_functions#L1054-L1057) | Print or display with pager lines containing pattern.
**grr** | `__printLinesCon`[**`...`**](standard_functions#L1061-L1067) | Print or display with pager numbered lines containing pattern in working and subdirectories.
**df1** | `df -h | grep "s`[**`...`**](standard_functions#L1158-L1160) | Print available disk space in simplified form.
**ip1** | `/sbin/ifconfig `[**`...`**](standard_functions#L1696-L1702) | Print internal ip.
**pa, pingAll** | `ping -c 1 -q $(`[**`...`**](standard_functions#L1723-L1727) | Ping gateway and google.

####  Packages 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**ch, canhaz** | `sudo apt-get in`[**`...`**](standard_functions#L1308-L1310) | Install package.
**ve, version** | `# Check if pass`[**`...`**](standard_functions#L1399-L1416) | Print installed and available version of package or command.
**wi, whatis1** | `# Checks if it `[**`...`**](standard_functions#L1527-L1551) | Describe package or command or find available packages with part of name or command.

How To Rename Commands
----------------------
* Check if name is already taken by running: `$ wi <name>`
* Open **`.standard_rc`** located in your home directory and add new name in front of function's description.
* Save and run: `$ bash`

How It Works
------------
After installation the "framework" consists of three files:

* [**`standard_functions`**](standard-aliases/standard_functions): It contains Bash functions with long descriptive names. It is located in projects directory.

* Users [**`.standardrc`**](standard-aliases/standard_rc) file: Configuration file that specifies short names for functions.  Also defines [options](standard-aliases/standard_rc#L323-L346) that functions use when they call specific commands. It is located in user's home directory.

* Automatically generated **`aliases`** file: Contains functions with short names that call functions with longer names, as defined in configuration file. It also assigns appropriate comand-line completions to the short functions. It is located in `~/.standard_aliases` directory.
 
Every time new Bash shell is started, the "framework" checks if any changes were made to functions or configuration file and if so, then generates new `aliases` file.

Misc
----
* Usually if function only makes Linux command easier to use, either by using a few "sensible" options, or just by sending output of a command to a pager if necessary, then it has same name as command, but with number `1` appended at the end. Some examples are: `ps1`, `pgrep1`, `tree1`, `mkdir1`. Options for this commands are defined at the bottom of [`standardrc`](standard-aliases/standard_rc#L323-L346).

* Only functions that redefine already existing commands are `cp`, `mv` and `rm`. They are all run in interactive mode, meaning you get asked for conformation before any destructive operation. If you want to execute them without this prompting, use -f (force) option. 

* Command-line completions are automatically assigned to functions, depending on what commands they use. (Exception are `git` commands, for which completions don't work.)

* Commands for accessing the framework:
	* ty
	* al 
	* sc











































