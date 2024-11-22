# Da Cool Media Downloader

Da Cool Media Downloader (or DCMD) is a helpful script that guides you through the downloading process without having to remember commands to download your content. I originally made this to be used with GitHub Codespaces but later modified to make it usable for other OSes.

> However, do NOT fork this if you are changing the name. This will break some scripts and will make you to go and fix it MANUALLY

## Setup

To setup your codespace or to run on a computer without yt-dlp and gallery-dl, I provide helpful installers that install these dependencies.  

### Dependencies

You'll need

- [python](https://python.org)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [gallery-dl](https://github.com/mikf/gallery-dl)
- [whiptail](https://manpages.debian.org/bookworm/whiptail/whiptail.1.en.html) and/or [dialog](https://en.wikipedia.org/wiki/Dialog_(software))

### Codespaces

You need to run `setupCodespaces` to install all necessary stuff. You may need to `chmod +x setupCodespaces`

### Linux

Run command `setupLinux` to install. You may need to `chmod +x setupLinux`

### Windows

Run `setupWin.bat`. EZ :)

> i wish all sections were this short...

### macOS

Run `setupMacOS`. You may need to `chmod +x setupMacOS`

## Usage

The usage process is pretty straight forward. Execute `./dcmd` to guide you through the downloading process.

`dcmd --help` will output this

``` text
dcmd (c) 2024 oofybruh9. Licensed under GPLv3
Usage:
    -h --help   Print this help dialog
    -y          Use yt-dlp
    -g          Use gallery-dl
    -u          Use URL (requires -y or -g flag)
    -f          Use flags in command e.g. -f "-o ./${title}.${ext}" (requires -y or -g flag)
    -ee         ë̴̠̫́̓͠x̵̠̞̓͊͜͝e̸̻̺͕͋͐͠c̴͔͉͍̒͆̚u̵̼͖̪͆͐̿t̵̞͚̟̔͒͠e̸̡͙̘̾͝͝ i̴͓͚͑̈́͝t̵͖̝͙̔͑͝ t̸̡͓̝̾͛͋o̴̪͓̠͌̕ f̸͉̞̟͆̚͝ḯ̸̙̘̾͊n̴̢̠͖̐̈́͋d̵͓͉̀̾̈́ o̵̘͎̔͜͝͠u̸͚͉͖̓͛̔t̴̡͖͇͋́͝…̸̡̘̦̈́͊
```

## License

This is Licensed under [GNU GPL V3](LICENSE)
