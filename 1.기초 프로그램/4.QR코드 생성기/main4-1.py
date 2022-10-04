import qrcode   #qrcode라이브러리 불러오기

qr_data = 'www.naver.com'   #qr_data 변수에 www.naver.com 문자열을 바인딩
qr_img = qrcode.make(qr_data)   #qrcode.make로 이미지를 만들어 qr_img에 바인딩

save_path = '4.QR코드 생성기\\' + qr_data + '.png'
qr_img.save(save_path)  #이미지 저장