# import requests
#
# for i in range(50):
#     response1 = requests.get('http://192.168.0.115:8000/project/profile/01')
#     response2 = requests.get('http://192.168.0.115:8000/project/profile/211fa04563')
#     if response1.text==response2.text:
#         print('same')
#     else:
#         print('different')
# # print(response1.text, response2.text)
# html="<!DOCTYPE><html><body><h1>hello world</h1></body></html>"
# regno="211FA04563"
# path = r"C:\Users\saiki\PycharmProjects\WebProject\myworld\pdfs\templates\profile\%s.html" % regno
# with open(path, 'w') as f:
#     f.write(html)
#     f.close()
p='https://lh3.googleusercontent.com/pw/AM-JKLVz_lMi3wZAJry4odlCpSPD1OaOmglZbm3xp2p6pVmq0iomKScfkffanNIbTB7hpoapqSDkljqeJGXrdWxR0p6yutEUwkOceWILBGt-eY4GRcCiGmQQ0MczwZbMmCn9fQ6wxmiZePfoIZx8911ObCMO=w1863-h858-no?authuser=0'
print(p[:4]=='http')