
![Standard Aliases](doc/sa_logo.png)

### Make Linux more user friendly with this collection of **Bash functions**!

They provide **commands that should be in Linux** by default, or just **abbreviations of commands** that are provided, but are so commonly used that they deserve a shorter name and/or a set of configurable **“sensible” options**. When abbreviated command is executed, these predefined options are combined with the actual ones. Also most of the commands send their **output to a pager** if it doesn't fit the screen.

Collection was made for **Debian** based Linux (**Ubuntu**, **Mint**, ...) with **Gnome** desktop environment, but most commands will work on any system that has _Bash_ shell and _GNU Coreutils_ installed. For **OS X** see [instructions](README.md#how-to-run-on-os-x).

There are currently **211 commands**.

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
**p** | <code>if [[ $# -eq 0 </code>[**`...`**](standard_functions#L439-L445) | Print working directory or path to file.
**l** | <code>___displayOutpu</code>[**`...`**](standard_functions#L194-L197) | List or display directory contents in pager using short listing format.
**la** | <code>__listOrDisplay</code>[**`...`**](standard_functions#L209-L212) | List or display all directory contents in pager using short listing format.
**ll** | <code>___displayOutpu</code>[**`...`**](standard_functions#L204-L207) | List or display directory contents in pager using long listing format.
**lla** | <code>__listOrDisplay</code>[**`...`**](standard_functions#L219-L222) | List or display all directory contents in pager using long listing format.
**e** | <code>echo "$@"</code> | Print text.
**c** | <code>cat "$@"</code> | Print file contents.
**m** | <code>___printOrDispl</code>[**`...`**](standard_functions#L92-L94) | Print or display text or file in pager.
**v** | <code>vim -p "$@"</code> | Edit file with vim.
**?** | <code>echo $?</code> | Print exit code of last command.

####  Directories 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**mk, md, mkdir1** | <code>mkdir --parents</code>[**`...`**](standard_functions#L413-L416) | Create directory and descend into.
**cpdir** | <code>cp --interactiv</code>[**`...`**](standard_functions#L394-L396) | Copy directories safely.
**mvdir** | <code>mv --interactiv</code>[**`...`**](standard_functions#L400-L402) | Move directories safely.
**rmdir** | <code>rm --interactiv</code>[**`...`**](standard_functions#L407-L409) | Delete directories safely.

####  Useful 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**extract** | <code>if [ -z "$1" ];</code>[**`...`**](standard_functions#L1112-L1145) | Extract archive of any type.
**o, openFile** | <code>__runCommandInB</code>[**`...`**](standard_functions#L585-L587) | Open file with default app.
**rb, runInBackground** | <code>nohup "$@" &>/d</code>[**`...`**](standard_functions#L474-L476) | Run command in background.
**me, makeExecutable** | <code>if [[ ! -f "$1"</code>[**`...`**](standard_functions#L634-L668) | Make file executable or create new bash or python script.
**lo, locate1** | <code>locate  "$1" \</code>[**`...`**](standard_functions#L1088-L1092) | Locate files on filesystem containing pattern in their names.
**grr** | <code>__printLinesCon</code>[**`...`**](standard_functions#L1077-L1083) | Print or display with pager numbered lines containing pattern in working and subdirectories.

####  Packages 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**ch, canhaz** | <code>if [[ "$__stand</code>[**`...`**](standard_functions#L1332-L1338) | Install package.
**ve, version** | <code># Check if pass</code>[**`...`**](standard_functions#L1427-L1444) | Print installed and available version of package or command.
**wi, whatis1** | <code># Checks if it </code>[**`...`**](standard_functions#L1555-L1579) | Describe package or command or find available packages with part of name or command.

####  Git 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**gs** | <code>git -c color.st</code>[**`...`**](standard_functions#L1631-L1634) | Print short repository status.
**gd** | <code>git diff "$@"</code> | Display changes between commits.
**gl** | <code>git log --graph</code>[**`...`**](standard_functions#L1638-L1640) | Display minimal log of commits.
**init** | <code>git init "$@"</code> | Initialize repository.
**commit** | <code>git commit -am </code>[**`...`**](standard_functions#L1588-L1590) | Commit changed and deleted files with message.
**push** | <code>git push "$@"</code> | Push changes to remote repository.
**pull** | <code>git pull "$@"</code> | Pull changes from remote repository.

####  Networking 

 _Name_        | _Runs_   | _Description_  
:------------- |:--------:| ----------------
**pa, pingAll** | <code>ping -c 1 -q $(</code>[**`...`**](standard_functions#L1752-L1756) | Ping gateway and google.
**ip1** | <code>/sbin/ifconfig </code>[**`...`**](standard_functions#L1724-L1731) | Print internal ip.
**ip2** | <code>lynx --dump htt</code>[**`...`**](standard_functions#L1734-L1736) | Print external ip.
**gateway** | <code>route -n \</code>[**`...`**](standard_functions#L1739-L1744) | Print gateways ip.

How To Rename Commands
----------------------
* Check if name is already taken by running: `$ type <name>`
* Open **`.standardrc`** located in your home directory and add a new name in front of function's description.
* Save and run: `$ bash`

Misc
----
* Usually if function only makes Linux command easier to use, either by using a few “sensible” options, or just by sending output to a pager (if necessary), then it has the same name as command, but with number `1` appended at the end. Some examples are: `ps1`, `mkdir1`, `pgrep1`, `tree1`. Options for this commands are defined at the bottom of [`standardrc`](standard_rc#L328-L358) and can be customized by preference.

* **`cp`**, **`mv`**, **`rm`** and **`rmdir`** are the only functions that override already existing commands. They are all run in interactive mode, meaning you get asked for conformation before any destructive operation. If you want to execute them without this prompting, use `-f` (force) option. `rmdir` also deletes the directory contents.

* Command-line completions are automatically assigned to functions, depending on what commands they use.

* Commands for accessing the “framework”:
  * **`ty COMMAND`** – prints function's body (short for `type`),
  * **`rc`** – opens configuration file (`~/.standardrc`) in default editor,
  * **`fu`** – opens `standard_functions` in default editor.

How It Works
------------
After installation the “framework” consists of three files:

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



























