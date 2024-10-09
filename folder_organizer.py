import os #fornece funções para interagir com o sistema operacional, nesse caso vai verificar se o diretório ja existe, se não, ele cria um 
import shutil #move os arquivos perdidos para a pasta, é um modulo de alto nivel usado para movier, copiar ou remover diretórios


downloads_folder_path = f"{__file__}".replace("desktop/folder_organizer.py", "downloads") #aponta para a pasta de download (confirmar)

for file in os.listdir(downloads_folder_path):
    filename, file_extension = os.path.splitext(file)
    file_extension = file_extension[1:]
    

    folder_to_organize_file = f"{downloads_folder_path}/{file_extension}"

    if not os.path.isdir(folder_to_organize_file):
        os.mkdir(folder_to_organize_file)

    shutil.move(f"{downloads_folder_path}/{file}", f"{folder_to_organize_file}/{file}", f"{folder_to_organize_file}/{file}")









