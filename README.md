# rtsp-rtp

## Description

This fork changes a few things in the library to exploit an authentication bypass in the TP-Link Tapo C200 Camera, which allows anyone with network access to stream the video feed from the camera. Only works when "Privacy Mode" is disabled.

Credits for finding this bypass go to @drmnsamoliu

https://drmnsamoliu.github.io/video.html

### What?
This is a minimal toolset needed to get an  H264/AVC stream from RTSP-enabled camera, written as a PoC in pure Python with no external dependencies.

It includes a (partial) implementation of RTSP client (supports basic and digest auth), RTP datagram (courtesy of github.com/plazmer) and NAL unit (FU-A fragmentation only) parsers.

It is **not** a fully featured, generic, production ready toolset, but rather an R&D playground.

### Limitations
- No FU-B NAL units parsing
- No QoS/RTCP
- No keepalives

### Usage
```
usage: PoC.py [-h] host file

TP-Link Tapo C200 Auth Bypass PoC

positional arguments:
  host        IP Address of the Host
  file        filename to write H264 output to

optional arguments:
  -h, --help  show this help message and exit
```

The output file can then be viewed with ffmpeg like so `ffplay -i <file>`
