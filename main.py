meme_dict = {
            "CRINGE" : "Garip ya da utandırıcı bir şey",
            "LOL" : "Komik bir şeye verilen cevap",
            "LMFAO" : "Çok komik bir şeye verilen cevap",
            "NGL" : "Biri doğruyu söylerken yazılan şey"
            "SUS" : "Biri şüpheli bir şey yaptığında söylenen şey"
            }
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Böyle bir kısaltma kütüphanede yok hadi naş naş!")
