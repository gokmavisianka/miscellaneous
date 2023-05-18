import os
import time
# Dosyaları bulmak için 'os' modülünü kullanacağız.
# İşlemin kaç saniye sürdüğünü hesaplamak için ise 'time' modülünü kullanacağız.
   
def find(starting_directory, files_to_be_found):
    def search(directory):
        # Bulmayı istediğimiz dosyaları aramak için kullanacağımız fonksiyon.
        try:
            all_files = os.listdir(directory)  # Verilen konumdaki tüm dosyaları listeler.
            folders = []  # Yalnızca uzantısız veya klasör tipindeki dosyaların yer alacağı liste.
            for i in range(len(all_files)):
                file = all_files[i]
                file_format = os.path.splitext(r"{0}/{1}".format(directory, file))[1]  # dosya formatı/tipi, Örn: .py

                if file_format == "":
                    # Özel bir formata sahip değilse 'klasör' olduğu varsayılır.
                    # Klasör değilse de 'except' bloğunda üstesinden gelinir.
                    folders.append(file)

                if file in files_to_be_found:
                    if file in files_found:
                        # Dosya daha önce bulunmuşsa, sözlükteki listeye ekleme yapılır.
                        files_found[file] += [r"{0}/{1}".format(directory, file)]
                    else:
                        # Bulunmadıysa da yenisi oluşturulur.
                        files_found.update({file: [r"{0}/{1}".format(directory, file)]})

            for file in folders:
                try:
                    # Özyineleme ile fonksiyon tekrar tekrar çağırılır.
                    # Böylece bir dizinde yer alan diğer tüm dizinler de gözden geçirilmiş olunur.
                    search(directory=r"{0}/{1}".format(directory, file))
                except PermissionError:
                    # Bazı dosyaların içine bakamıyoruz. İzin alınamadı hatası veriyor.
                    print(r"PermissionError: {0}/{1}".format(directory, file))
                except NotADirectoryError:
                    # Belirli bir dosya formatına sahip olmayan, fakat klasör de olmayan dosyalar bu hatayı verecektir.
                    pass

        except FileNotFoundError:
            print(f"FileNotFoundError: {directory}")
        except RecursionError:
            # Özyinelemi fonksiyonların 'dallanma' sınırından ötürü ortaya çıkan hata.
            print("RecursionError!")

    start_time = time.perf_counter()
    files_to_be_found = files_to_be_found  # Bulunması istenen dosyaların bulunduğu liste.
    files_found = {}  # Bulunan dosyaların yer alacağı sözlük.
    search(starting_directory)  # Aranmaya başlanacak ilk konum: starting_directory.
    end_time = time.perf_counter()
    print(f"File search completed in {round(end_time - start_time, 3)} seconds.")
    return files_found
    
# find(r"C:/PyProjects", ["A.py", "B.py"])
