Standard Aliases
================

#### Make Linux more user friendly with this collection of **Bash functions**

They provide commands that should be in Linux by default, or just an abbreviations of commands that are provided, but are so commonly used that they deserve a shorter name.

Collection was made for **Debian** based Linux (**Ubuntu**, **Mint**, ...) with **Gnome** desktop environment, but most commands will work on all systems with installed _Bash_ shell and _GNU Coreutils_. For **OS X** see [instructions](README.md#how-to-run-on-os-x).

There are currently 210 commands.

How to…
-------
### Install
```
$ git clone https://github.com/gto76/standard-aliases
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
**te, terminal** | `x-terminal-emul`[**`...`**](standard_functions#L586-L588) | Open new terminal with same working directory.
**?** | `echo $?` | Print exit code of last command.

####  Files 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**t, tree1** | `tree -C -I .git`[**`...`**](standard_functions#L300-L302) | Print directory structure.
**cpdir** | `cp --interactiv`[**`...`**](standard_functions#L390-L392) | Copy directories safely.
**mvdir** | `mv --interactiv`[**`...`**](standard_functions#L396-L398) | Move directories safely.
**rmdir** | `rm --interactiv`[**`...`**](standard_functions#L403-L405) | Delete directories safely.
**mk, md, mkdir1** | `mkdir --parents`[**`...`**](standard_functions#L409-L412) | Create directory and descend into.
**bk, backup** | `sudo cp --prese`[**`...`**](standard_functions#L416-L418) | Backup file.
**o, openFile** | `__runCommandInB`[**`...`**](standard_functions#L581-L583) | Open file with default app.
**me, makeExecutable** | `if [[ ! -f "$1"`[**`...`**](standard_functions#L630-L663) | Make file executable or create new bash or python script.
**extract** | `if [ -z "$1" ];`[**`...`**](standard_functions#L1107-L1140) | Extract archive of any type.
**du1** | `du --summarize `[**`...`**](standard_functions#L1175-L1177) | Print disk space occupied by file or folder.
**lo, locate1** | `locate  "$1" \`[**`...`**](standard_functions#L1083-L1087) | Locate files on filesystem containing pattern in their names.

####  Useful  

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**f, please** | `sudo $(history `[**`...`**](standard_functions#L753-L755) | Execute last command as super user.
**rb, runInBackground** | `nohup "$@" &>/d`[**`...`**](standard_functions#L470-L472) | Run command in background.
**gr** | `__printLinesCon`[**`...`**](standard_functions#L1065-L1068) | Print or display with pager lines containing pattern.
**grr** | `__printLinesCon`[**`...`**](standard_functions#L1072-L1078) | Print or display with pager numbered lines containing pattern in working and subdirectories.
**df1** | `df -h | grep "s`[**`...`**](standard_functions#L1169-L1171) | Print available disk space in simplified form.
**ip1** | `/sbin/ifconfig `[**`...`**](standard_functions#L1707-L1714) | Print internal ip.
**ip2** | `lynx --dump htt`[**`...`**](standard_functions#L1717-L1719) | Print external ip.
**pa, pingAll** | `ping -c 1 -q $(`[**`...`**](standard_functions#L1735-L1739) | Ping gateway and google.

####  Packages 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**ch, canhaz** | `sudo apt-get in`[**`...`**](standard_functions#L1319-L1321) | Install package.
**ve, version** | `# Check if pass`[**`...`**](standard_functions#L1410-L1427) | Print installed and available version of package or command.
**wi, whatis1** | `# Checks if it `[**`...`**](standard_functions#L1538-L1562) | Describe package or command or find available packages with part of name or command.

How To Rename Commands
----------------------
* Check if name is already taken by running: `$ type <name>`
* Open **`.standardrc`** located in your home directory and add new name in front of function's description: `$ rc`
* Save and run: `$ bash`

Misc
----
* Usually if function only makes Linux command easier to use, either by using a few "sensible" options, or just by sending output to a pager (if necessary), then it has the same name as command, but with number `1` appended at the end. Some examples are: `ps1`, `mkdir1`, `pgrep1`, `tree1`. Options for this commands are defined at the bottom of [`standardrc`](standard_rc#L328-L358).

* **`cp`**, **`mv`**, **`rm`** and **`rmdir`** are the only functions that override already existing commands. They are all run in interactive mode, meaning you get asked for conformation before any destructive operation. If you want to execute them without this prompting, use `-f` (force) option. `rmdir` also deletes the directory contents.

* Command-line completions are automatically assigned to functions, depending on what commands they use.

* Commands for accessing the framework:
  * **`ty COMMAND`** – prints function's body (short for `type`),
  * **`rc`** – opens configuration file (`~/.standardrc`) in default editor,
  * **`fu`** – opens `standard_functions` in default editor,
  * **`ba`** – starts new _Bash_ shell (short for `bash`).

How It Works
------------
After installation the "framework" consists of three files:

* [**`standard_functions`**](standard_functions): It contains _Bash_ functions with long descriptive names. It is located in projects directory.

* Users [**`.standardrc`**](standard_rc) file: Configuration file that specifies short names for functions.  Also defines [options](standard_rc#L328-L358) that this functions use when they call specific commands. It is located in user's home directory.

* Automatically generated **`aliases`** file: Contains functions with short names that call functions with longer names (as defined in configuration file). It also assigns appropriate command-line completions to the short functions. It is located in `~/.standard_aliases` directory.

Every time new _Bash_ shell is started, "framework" checks if any changes were made to the functions or configuration file and if so, it generates new `aliases` file.

How to run on OS X
------------------
* Install _Developer Tools_ by running:
```
make
```

* Install _Homebrew_:
```
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

* Install _GNU Coreutils_:
```
brew install coreutils
echo '. .bashrc' >> .profile
echo 'PATH="/usr/local/opt/coreutils/libexec/gnubin:$PATH"' >> ~/.bashrc
bash
```

* Install other _GNU_ programs (optional):
```
brew tap homebrew/dupes
brew install grep --with-default-names
brew install findutils --with-default-names
brew install tree
...
```

















