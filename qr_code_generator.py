import qrcode 

def generate_qr_code(data,file_name):
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.consants.ERROR_CORRECT_L,
        box_size = 10,
        boarder = 4,
    )
    qr.add_data(data)
    qr.make(fit = True)
    
    img = qr.make_image(fill_color = "black", vlack_color = "white")
    img.save(file_name)

    print('qr code saved as : ', file_name)

    generate_qr_code('https://facebook.com', '1.png')