# MPV Configurations

- Go to
  - Windows ➡️ `C:\Users\<YourUserName>\AppData\Roaming\mpv`
  - Linux ➡️ `~/.config/mpv/mpv.con`
- Create two files (if not there) 👉 `mpv.conf` and `input.conf`
- Paste the content in the files as directed below

### mpv.conf

```
fs=yes
end-file=ignore
loop-file=inf
```

### input.conf

```
# Play/pause video
a cycle pause

# Decrease playback speed by 0.10
s add speed -0.10

# Increase playback speed by 0.10
d add speed 0.10

# Set playback speed to 2.20
g set speed 2.20

# Reset playback speed to 1.0
r set speed 1.0

z seek -5
x seek 5
```
