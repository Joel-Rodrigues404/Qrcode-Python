import qrcode
import os

dado = "https://i.ibb.co/xG1q9Bg/imagem-2023-10-11-204244298.png"

img = qrcode.make(dado)

img_fold_url = 'img/'

img.save(os.path.join(img_fold_url, 'teste.png'))