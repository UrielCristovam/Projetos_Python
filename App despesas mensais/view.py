import os
import shutil

def count_files_and_folders(folder_path, extension):
    num_files = 0
    num_folders = 0

    for item in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, item)) and item.endswith(extension):
            num_files += 1
        elif os.path.isdir(os.path.join(folder_path,item)):
            num_folders += 1
            sub_folder_path = os.path.join(folder_path, item)
            sub_num_files, sub_num_folders = count_files_and_folders(sub_folder_path, extension)
            num_files += sub_num_files
            num_folders += sub_num_folders

    return num_files, num_folders

def copiar_arquivos(origem,destino, ext):

    diretorio_origem = origem
    diretorio_destino = destino

    extensao = ext

    for nome_arquivo in os.listdir(diretorio_origem):
        if nome_arquivo.endswith(extensao):
            caminho_origem=os.path.join(diretorio_origem, nome_arquivo)
            caminho_destino = os.path.join(diretorio_destino, nome_arquivo)
            shutil.copy(caminho_origem, caminho_destino)

