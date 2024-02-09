# # Bu kod parçacığı bir metin dosyasının tamamını okumamızı sağlar
# f = open('text.txt', 'w', encoding='utf-8')
# text = f.read()
# print(text)
# f.close()
# Ve işte bir metin dosyasının tamamını nasıl yeniden yazabileceğimiz:
# f = open('metinbelgesi.txt', 'w', encoding='utf-8')
# text = 'Yeni Yazı'
# f.write(text)
# f.close()

# Daha kısa bir versiyonu:
with open('text.txt', 'r', encoding='utf-8') as f:
    print(f.read())