from datetime import datetime
import os
import hashlib
import shutil

path = "D:\\learn\\skripts"     # исходная дериктория
dest_path = "D:\\learn\\dest"

for f in os.listdir(path):      # перебираю список имен файлов из исходной дериктории
    file_full_path = os.path.join(path, f)

    # проверяю, является ли имя с этим путем файлом
    if os.path.isfile(file_full_path):

      # дата создания, превращение в нормальное представление
        creation_time = os.path.getctime(file_full_path)
        dt_object = datetime.fromtimestamp(creation_time)

# содание нового имени
        formatted_date = dt_object.strftime("%Y-%m-%d_%H-%M")
        suffix = os.path.splitext(file_full_path)[1]
        file_name = os.path.splitext(f)[0]
        new_name = file_name + "_" + formatted_date + suffix

# проверяю, есть ли такой файл в конечном директории
        if os.path.exists(os.path.join(dest_path, new_name)):
            # если файл есть, считаю md5 для обоих файлов
            with open(file_full_path, 'rb') as new_file:
                source_md5 = hashlib.md5(new_file.read()).hexdigest()
            with open(os.path.join(dest_path, new_name), 'rb') as old_file:
                dest_md5 = hashlib.md5(old_file.read()).hexdigest()
    # если md5 не равны, копирую
            if source_md5 != dest_md5:
                shutil.copy(file_full_path, os.path.join(dest_path, new_name))
# если файла нет в итоговой директории, копирую
        else:
            shutil.copy(file_full_path, os.path.join(dest_path, new_name))
