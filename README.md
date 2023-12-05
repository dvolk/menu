# menu

read $HOME/commands.txt as a list of items and present a menu for running those commands; runs commands in the background without exiting the menu

## screenshot

<img src="https://i.imgur.com/QW3WACw.png">

## commands.txt example

```
xrandr --output DP-4 --mode 2560x1600 --output DP-2 --mode 3840x2160 --above DP-4
xmodmap -e "clear Lock" -e "keycode 66 = Return" -e "keycode 232 = F1" -e "keycode 233 = F2" -e "keycode 128 = F3" -e "keycode 212 = F4" -e "keycode 237 = F5" -e "keycode 238 = F6" -e "keycode 173 = F7" -e "keycode 172 = F8" -e "keycode 171 = F9" -e "keycode 121 = F10" -e "keycode 122 = F11" -e "keycode 123 = F12"
imwheel -b "4 5"
mpv $(youtube-dl -f 22 -g $(xclip -o))
chromium
thunar
pavucontrol
scrot -s
scrot -d 3
feh --bg-fill '/home/ubuntu/Pictures/Wallpapers/DALL·E 2023-11-30 15.35.23 - Imagine a wide, dark image of a grassy field under a stormy blue sky, reminiscent of the famous Windows XP wallpaper but interpreted in a classic anim.png'
ssh -f -N -D 8080 eclipse ; sshfs eclipse: /home/ubuntu/eclipse
if nmcli connection show --active | grep -q "Wired connection 1"; then nmcli connection down "Wired connection 1"; else nmcli connection up "Wired connection 1"; fi
pkill compton ; compton
nm-applet
transmission-gtk
emacs
```