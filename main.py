import pyqrcode
import png
import tkinter

from pyqrcode import QRCode

apple_store = "https://apps.apple.com/us/app/dcnr1-99-5/id1525937514"
play_store = "https://play.google.com/store/apps/details?id=com.dcnr1.player&hl=en_GB"

apple_url = pyqrcode.create(apple_store)
play_url = pyqrcode.create(play_store)

apple_url.svg("apple_dcnr.svg", scale=8)
play_url.svg("play_dcnr.svg", scale=8)

apple_url.png("apple_dcnr.png", scale=6)
play_url.png("play_dcnr.png", scale=6)

