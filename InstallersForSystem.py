import requests

def download(file_url, destination_path):
    try:
        # Отправка GET-запроса для загрузки файла
        response = requests.get(file_url, stream=True)
        # Запись содержимого файла в локальный файл
        with open(destination_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=128):
                f.write(chunk)
        print("d:/" + "Файл успешно загружен в", destination_path)
        return True
    except Exception as e:
        print("d:/" + "Ошибка при загрузке файла:", e)
        return False

def opis():
    return "d:/ Драйвер InstallersForSystem может скачивать файлы из интернета изпользуя функции которые в нём находятся"

def name():
    return "d:/ InstallersForSystem"

def help():
    print("d:/ help - помощь\ndow (файл)- скачать файл")
