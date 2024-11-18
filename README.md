# Da Cool Media Downloader

Da Cool Media Downloader (or DCMD) is a helpful script that guides you through the downloading process without having to remember commands to download your content.

There are better options out there with full-on GUI's but I made this to download videos via codespaces.  

## Setup

To setup your codespace or to run on a computer without yt-dlp and gallery-dl, I provide helpful installers that install these dependencies.  

### Dependencies

You'll need

- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [gallery-dl](https://github.com/mikf/gallery-dl)
- [whiptail](https://manpages.debian.org/bookworm/whiptail/whiptail.1.en.html) and/or [dialog](https://en.wikipedia.org/wiki/Dialog_(software))
### Codespaces

You need to run `setupCodespaces` to install all necessary stuff. You may need to `chmod +x setupCodespaces`

### Linux

Run command `setupLinux` to install. You may need to `chmod +x setupLinux`

### Windows

Run `setupWin.bat`. EZ :)

### macOS

Run `setupMacOS`. You may need to `chmod +x setupMacOS`

## Usage

The usage process is pretty straight forward. Execute `./dcmd` to guide you through the downloading process.

## License

This is Licensed under GNU GPL v3
