fa= open("BENİ OKU.txt", "w")
fa.write("""Aradığınız INFOlar 'info.txt' dosyasına kaydedilecektir

Bu Uygulama Emir Ali ATEŞ tarafından yazılmıştır.

""")







print("""       
      :::::::::::       ::::    :::       ::::::::::       :::::::: 
         :+:           :+:+:   :+:       :+:             :+:    :+: 
        +:+           :+:+:+  +:+       +:+             +:+    +:+  
       +#+           +#+ +:+ +#+       :#::+::#        +#+    +:+   
      +#+           +#+  +#+#+#       +#+             +#+    +#+    
     #+#           #+#   #+#+#       #+#             #+#    #+#     
###########       ###    ####       ###              ########            . e x e

                                                powered by emyounoone        
""")

print("LOADING..")
import time
time.sleep(1)
print("-------")
import time
time.sleep(1)
print("--------------")
import time
time.sleep(1)
print("---------------------")
import time
time.sleep(1)
print("----------------------------")
import time
time.sleep(1)
language=int(input("--Please Select A Language--\n1)Turkish\n2)English \n :"))
while True:
    f = open("INFOlar.txt", "a")
    
    if language == (1):
        print("Program Türkçe Başlıyor..")
        import time

        time.sleep(2)
        import time
        time.sleep(2)
        problem = input("Almak İstediğin Bilgiyi Yazar Mısın?\n ")
        import wikipediaapi
        wiki_wiki = wikipediaapi.Wikipedia(language='tr', extract_format=wikipediaapi.ExtractFormat.WIKI)
        p_wiki = wiki_wiki.page(problem)
        page_py = wiki_wiki.page(problem)
        print("Page - Exists: %s" % page_py.exists())
        print(p_wiki.text + "\n \n \n" + "1'e Basarak Yeniden INFO alabilirsin 2'ye Basarak Çıkabilirsin")
        f.write("INFO:     "+p_wiki.text)
        tr_=int(input(""))
        if tr_==(1):
            print("Yükleniyor..")
            import time
            time.sleep(2)
            continue
        elif tr_==(2):
            break
            quit()
        else:
            print("Geçerli Bir Kod Gir..")






    while True:
        
        c = open("INFOs.txt", "a")
        
        if language == (2):
            print("Program Is Starting English..")
            import time

            time.sleep(2)
            import time
            time.sleep(2)
            problemeng=input("Can you write the information you want to get?  :")
            import wikipediaapi
            wiki_wiki = wikipediaapi.Wikipedia(language='en', extract_format=wikipediaapi.ExtractFormat.WIKI)
            p_wiki = wiki_wiki.page(problemeng)
            print(p_wiki.text)
            page_py = wiki_wiki.page(problemeng)
            print("Page - Exists: %s" % page_py.exists())
            print(p_wiki.text + "\n \n \n" + "Press 1 to Give INFO again Press 2 to Quit")
            c.write("INFO:     "+p_wiki.text)
            eng_=int(input(""))
            if eng_ == (1):
                print("Loading..")
                import time

                time.sleep(2)
                continue
            elif eng_ == (2):
                break
                quit()
            else:
                print("Enter A Valid Code..")









