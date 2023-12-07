# Menu

Present menu for common commands

- Reads a file as a list of items and presents a menu for running those commands
- Runs commands in the background without exiting the menu
- Uses only python standard library
- Uses curses so can be used on servers
- Commands prefixed with '$' launch in the foreground

## Screenshot

<img src="https://i.imgur.com/0KDwJKv.png">

## Installation

```
wget https://raw.githubusercontent.com/dvolk/menu/master/main.py
sudo mv main.py /usr/local/bin/mymenu
sudo chmod a+x /usr/local/bin/mymenu
```

## Running

```
mymenu
```

## example: i3 window manager keybind: mod+q pop up menu

add to `.config/i3/config`

```
bindsym $mod+q exec xfce4-terminal --geometry "80x$(($(wc -l < /home/ubuntu/commands.txt) + 7))" --title "mymenu" --command "mymenu /home/ubuntu/commands.txt"
bindsym $mod+b exec xfce4-terminal --geometry "80x$(($(wc -l < /home/ubuntu/root_commands.txt) + 7))" --title "mymenu" --command "sudo mymenu /home/ubuntu/root_commands.txt"
for_window [title="mymenu"] floating enable
```
