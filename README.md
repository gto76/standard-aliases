Standard Aliases
================

Make Linux more user friendly with this collection of **Bash functions**.

It provides commands that should be in Linux by default, or just an aberrations of commands that are provided, but are so commonly used that they deserve a shorter name.

Collection was made for **Debian** based Linux (**Ubuntu**, **Mint**, ...) with **Gnome** desktop environment, but most commands will work on all systems with Bash shell.

There are currently 209 commands.

How to install
--------------

```bash
$ git clone https://github.com/gto76/standard-aliases.git
$ cd standard-aliases
$ ./install
$ bash
```

Commands
--------

Below is a list of most useful commands. If you want to check out the full list see [**LIST OF ALL COMMANDS**](doc/FUNCTION_DESCRIPTIONS.md).

####  Basic 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**l** | `___displayOutpu`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L184-L187) | List or display directory contents in pager using short listing format.
**e** | `echo "$@"` | Print text.
**c** | `cat "$@"` | Print file contents.
**m** | `___printOrDispl`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L82-L84) | Print or display text or file in pager.
**v** | `vim -p "$@"` | Edit file with vim.
**q** | `exit` | Exit bash shell.
**te, terminal** | `x-terminal-emul`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L572-L574) | Open new terminal with same working directory.
**?** | `echo $?` | Print exit code of last command.

####  Files 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**t, tree1** | `tree -C -I .git`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L286-L288) | Print directory structure.
**cpdir** | `cp --interactiv`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L376-L378) | Copy directories safely.
**mvdir** | `mv --interactiv`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L382-L384) | Move directories safely
**rmdir** | `rm --interactiv`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L389-L391) | Delete directories safely.
**mk, md, mkdir1** | `mkdir --parents`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L395-L398) | Create directory and descend into.
**bk, backup** | `sudo cp --prese`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L402-L404) | Backup file.
**o, openFile** | `__runCommandInB`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L567-L569) | Open file with default app.
**me, makeExecutable** | `if [[ ! -f "$1"`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L616-L645) | Make file executable or create new bash or python script.
**extract** | `if [ -z "$1" ];`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1087-L1120) | Extract archive of any type.
**du1** | `du --summarize `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1155-L1157) | Print disk space occupied by file or folder.
**lo, locate1** | `locate  "$1" \`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1063-L1067) | Locate files on filesystem containing pattern in their names.

####  Useful  

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**f, fuck** | `sudo $(history `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L733-L735) | Execute last command as super user.
**rb, runInBackground** | `nohup "$@" &>/d`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L456-L458) | Run command in background.
**gr** | `__printLinesCon`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1045-L1048) | Print or display with pager lines containing pattern.
**grr** | `__printLinesCon`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1052-L1058) | Print or display with pager numbered lines containing pattern in working and subdirectories.
**df1** | `df -h | grep "s`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1149-L1151) | Print available disk space in simplified form.
**ip1** | `/sbin/ifconfig `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1687-L1693) | Print internal ip.
**pa, pingAll** | `ping -c 1 -q $(`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1714-L1718) | Ping gateway and google.

####  Packages 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**ch, canhaz** | `sudo apt-get in`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1299-L1301) | Install package.
**ve, version** | `# Check if pass`[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1390-L1407) | Print installed and available version of package or command.
**wi, whatis1** | `# Checks if it `[**`...`**](https://github.com/gto76/standard-aliases/blob/master/functions#L1518-L1542) | Describe package or command or find available packages with part of name or command.

How It Works
------------
After installation the "framework" consists of three files:

* [**`standard_functions`**](standard-aliases/standard_functions): It contains the Bash functions with long descriptive names. It is located in projects directory.

* Users [**`.standardrc`**](standard-aliases/standard_rc) file: Configuration file that specifies short names for functions.  Also defines [options](standard-aliases/standard_rc#L323-L346) that functions use when they call specific commands. It is located in user's home directory.

* Automatically generated `shortcuts` file: Contains functions with short names that call functions with longer names, as defined in configuration file. It also assigns appropriate comand-line completions to the short functions. It is located in `~/.standard_aliases` directory.

How To Rename Commands
----------------------
* Check if the name is already taken by running `wi <name>`.
* Open [**`.standardrc`**](standard-aliases/standard_rc) located in your home directory and add new name in front of function's description.
* Save and run `bash` for changes to take effect.

Misc
----
+ By convention a function that calls a command with some set of options that are quite sensible for that command is usually named <command-name>1, and often also with a two letter aberration. Options for this commands are defined at the bottom of `standardrc`. // Usually if alias only makes command easier to use, either by using "sensible" options, or just by sending output of a command to pager if necessary, then it has same name as command, but with number 1 appended at the end. Some examples are:
`ps1`,
`pgrep1`,
`tree1`,
`mkdir1`.

+ Only aliases that redefine already existing commands are `cp`, `mv` and `rm`. They are all run in interactive mode, meaning you get asked for conformation before any destructive operation. If you want to execute them without this prompting, use -f (force) option. 


+ completions...
automatic completions from the command that gets parameters in function.

+ Commands for accessing the framework:
	* ty
	* al 
	* sc

To Other Files
--------------
+ All functions have long and descriptive names, that start with two underscores (so they don't pollute the shells namespace). This functions are then "aliased" with shorter name (or names), that are specified in `standardrc` configuration file. This function is then aliased with a shorter and more convenient name. Do not change the names of the functions because they may be used by other functions. Utility functions, that are not meant to be aliased start with three underscores.


Todo
----
Link to the Function link
The | in what it calls
comment files (install, aliases, functions)
Commands for accessing the framework

already defined aliases

There are xxx functions

ll, h





























