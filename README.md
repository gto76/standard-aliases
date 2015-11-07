Standard Aliases
================

Make Linux more user friendly with this collection of **Bash functions**.

It provides commands that should be in Linux by default, or just an aberrations of commands that are provided, but are so commonly used that they deserve a shorter name.

Collection was made for **Debian** based Linux (**Ubuntu**, **Mint**, ...) with **Gnome** desktop environment, but most commands will work on all systems with installed Bash shell and GNU Coreutils.

There are currently 209 commands.

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
**l** | `___displayOutpu`[**`...`**](standard_functions#L194-L197) | List or display directory contents in pager using short listing format.
**e** | `echo "$@"` | Print text.
**c** | `cat "$@"` | Print file contents.
**m** | `___printOrDispl`[**`...`**](standard_functions#L92-L94) | Print or display text or file in pager.
**v** | `vim -p "$@"` | Edit file with vim.
**q** | `exit` | Exit bash shell.
**te, terminal** | `x-terminal-emul`[**`...`**](standard_functions#L582-L584) | Open new terminal with same working directory.
**?** | `echo $?` | Print exit code of last command.

####  Files 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**t, tree1** | `tree -C -I .git`[**`...`**](standard_functions#L296-L298) | Print directory structure.
**cpdir** | `cp --interactiv`[**`...`**](standard_functions#L386-L388) | Copy directories safely.
**mvdir** | `mv --interactiv`[**`...`**](standard_functions#L392-L394) | Move directories safely.
**rmdir** | `rm --interactiv`[**`...`**](standard_functions#L399-L401) | Delete directories safely.
**mk, md, mkdir1** | `mkdir --parents`[**`...`**](standard_functions#L405-L408) | Create directory and descend into.
**bk, backup** | `sudo cp --prese`[**`...`**](standard_functions#L412-L414) | Backup file.
**o, openFile** | `__runCommandInB`[**`...`**](standard_functions#L577-L579) | Open file with default app.
**me, makeExecutable** | `if [[ ! -f "$1"`[**`...`**](standard_functions#L626-L655) | Make file executable or create new bash or python script.
**extract** | `if [ -z "$1" ];`[**`...`**](standard_functions#L1099-L1132) | Extract archive of any type.
**du1** | `du --summarize `[**`...`**](standard_functions#L1167-L1169) | Print disk space occupied by file or folder.
**lo, locate1** | `locate  "$1" \`[**`...`**](standard_functions#L1075-L1079) | Locate files on filesystem containing pattern in their names.

####  Useful  

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**f, fuck** | `sudo $(history `[**`...`**](standard_functions#L745-L747) | Execute last command as super user.
**rb, runInBackground** | `nohup "$@" &>/d`[**`...`**](standard_functions#L466-L468) | Run command in background.
**gr** | `__printLinesCon`[**`...`**](standard_functions#L1057-L1060) | Print or display with pager lines containing pattern.
**grr** | `__printLinesCon`[**`...`**](standard_functions#L1064-L1070) | Print or display with pager numbered lines containing pattern in working and subdirectories.
**df1** | `df -h | grep "s`[**`...`**](standard_functions#L1161-L1163) | Print available disk space in simplified form.
**ip1** | `/sbin/ifconfig `[**`...`**](standard_functions#L1699-L1705) | Print internal ip.
**pa, pingAll** | `ping -c 1 -q $(`[**`...`**](standard_functions#L1726-L1730) | Ping gateway and google.

####  Packages 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**ch, canhaz** | `sudo apt-get in`[**`...`**](standard_functions#L1311-L1313) | Install package.
**ve, version** | `# Check if pass`[**`...`**](standard_functions#L1402-L1419) | Print installed and available version of package or command.
**wi, whatis1** | `# Checks if it `[**`...`**](standard_functions#L1530-L1554) | Describe package or command or find available packages with part of name or command.

How To Rename Commands
----------------------
* Check if name is already taken by running: `$ wi <name>`
* Open **`.standard_rc`** located in your home directory and add new name in front of function's description.
* Save and run: `$ bash`

Misc
----
* Usually if function only makes Linux command easier to use, either by using a few "sensible" options, or just by sending output of a command to a pager (if necessary), then it has same name as command, but with number `1` appended at the end. Some examples are: `ps1`, `pgrep1`, `tree1`, `mkdir1`. Options for this commands are defined at the bottom of [`standardrc`](standard_rc#L324-L348).

* `cp`, `mv` and `rm` are the only functions that override already existing commands. They are all run in interactive mode, meaning you get asked for conformation before any destructive operation. If you want to execute them without this prompting, use -f (force) option. 

* Command-line completions are automatically assigned to functions, depending on what commands they use. (Exception are `git` commands, for which completions don't work.)

* Commands for accessing the framework:
  * **`ty COMMAND`** – prints the function body (short for `type`),
  * **`rc`** – opens users conf file in default editor,
  * **`fu`** – opens standard_functions in default editor,
  * **`ba`** – starts new Bash shell (short for `bash`).

How It Works
------------
After installation the "framework" consists of three files:

* [**`standard_functions`**](standard-aliases/standard_functions): It contains Bash functions with long descriptive names. It is located in projects directory.

* Users [**`.standardrc`**](standard-aliases/standard_rc) file: Configuration file that specifies short names for functions.  Also defines [options](standard_rc#L324-L348) that this functions use when they call specific commands. It is located in user's home directory.

* Automatically generated **`aliases`** file: Contains functions with short names that call functions with longer names, as defined in configuration file. It also assigns appropriate comand-line completions to the short functions. It is located in `~/.standard_aliases` directory.
 
Every time new Bash shell is started, the "framework" checks if any changes were made to functions or configuration file and if so, then generates new `aliases` file.
