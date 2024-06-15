meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "ROFL": "bir şakaya karşılık cevap",
            "SHEESH": "onaylamak",
            "CREEPY": "korkunç",
            "AGGRO": "agresifleşmek/sinirlenmek",
            }
            
 
print("Meme Sözlüğüne Hoşgeldiniz!")            
for i in range(5):
    print(str(5 - i) + " kadar kelime arama hakkınız var")
    word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")   
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("dats too new-gen for us")
        
print("Hakkınız kalmadı, lütfen programı yeniden başlatın.")
