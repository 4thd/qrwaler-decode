import time
import zlib

import base45
import cbor2
import cv2
import PIL.Image
import pyzbar.pyzbar
from pyzbar.pyzbar import decode
from tinydb import TinyDB

from messages import success, warning


class QRCodeScanner:
    def __init__(self, img: str) -> None:
        self.img = img
        self.id = 0
        self.db = TinyDB("./results/db.json")
        self.pass_db = TinyDB("./results/pass_db.json")

    def get_generic_qrcode_info(self) -> bool:
        img = cv2.imread(self.img)
        for barcode in decode(image=img):
            try:
                qr = {}
                qr["type"] = barcode.type
                qr["content"] = barcode.data
                success("Generic QR code decoded")
                self.db.insert(
                    {
                        "id": self.id,
                        "content": str(qr["content"]),
                        "type": str(qr["type"]),
                    },
                )
                success("Saved in db")
                self.id += 1
                time.sleep(1)
                return True

            except Exception as e:
                warning(f"Image not decoded => {e}")
                return False

    def get_pass_info(self) -> bool:
        try:
            image = PIL.Image.open(self.img)
            data = pyzbar.pyzbar.decode(image)
            cert = data[0].data.decode()
            b45data = cert.replace("HC1:", "")
            zlibdata = base45.b45decode(b45data)
            cbordata = zlib.decompress(zlibdata)
            decoded = cbor2.loads(cbordata)
            self.pass_db.insert(
                {
                    "id": self.id,
                    "content": cbor2.loads(decoded.value[2]),
                }
            )
            success("Saved in db")
            return True
        except Exception as e:
            print("searching...")
            return False
