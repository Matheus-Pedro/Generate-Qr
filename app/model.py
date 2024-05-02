from dataclasses import dataclass, field
import qrcode

@dataclass
class Qrcode:
    data_address: str
    qr: qrcode.QRCode
    save_address: str
    fill: str = field(default="black")
    back_color: str = field(default="white")

    def create_qr(self):
        self.qr.add_data(self.data_address)
        self.qr.make(fit=True)
        img = self.qr.make_image(fill=self.fill, back_color=self.back_color)
        img.save(self.save_address)


object_qr = Qrcode(data_address="https://github.com/Matheus-Pedro/", qr = qrcode.QRCode(version=1, box_size=10, border=4), save_address="media/qrs/credits.png")

object_qr.create_qr()
