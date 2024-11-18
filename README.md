# Da Cool Media Downloader

Da Cool Media Downloader (or DCMD) is a helpful script that guides you through the downloading process without having to remember commands to download your content.

There are better options out there with full-on GUI's but I made this for personal needs and thought I might just share it to the world. ( ͡° ͜ʖ ͡°)

> **DO NOT FORK THIS AND CHANGE THE NAME**  
> this will cause the script to mess up in some parts. Just fork it and that's it. Don't change ***A THING*** >:(

## Setup

To setup your codespace or to run on a computer without yt-dlp and gallery-dl, I provide helpful installers.  

### TUI

If you want a clean TUI (Text User Interface) on Linux, check if you either have whiptail or dialog installed. Use this script to check if you have these programs:

``` bash
which whiptail
which dialog
```

If you get:

``` bash
/usr/bin/whiptail
/usr/bin/dialog
```

You have both installed. No need to uninstall anything, it will automatically resort to dialog.  

If you have one missing, don’t panic. DCMD will automatically choose the one avaliable.  

If you get nothing, DCMD will automatically resort to a text based option.

### Codespaces

You need to run `setupCodespaces` to install all necessary stuff. You may need to `chmod +x setupCodespaces`

### Linux

Run command `setupLinux` to install. You may need to `chmod +x setupLinux`

### Windows

Run `setupWin.bat`. EZ :)

## Usage

The usage process is pretty straight forward. Execute `./dcmd` to guide you through the downloading process.

## License

This is Licensed under GNU GPL v3
