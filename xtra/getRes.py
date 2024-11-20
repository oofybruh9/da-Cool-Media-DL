import argparse
from pytube import YouTube

parser = argparse.ArgumentParser("python3 getRes.py")
parser.add_argument("URL", help="YouTube URL for format selection", type=str)
args = parser.parse_args()
print(args.URL)
yt = YouTube(args.URL)
