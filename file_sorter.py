import os

for file in os.listdir():
    if not '.' in file or '.py' in file:
        continue

    extension = file[file.find('.'):]
    print(extension)
    extension = extension.upper()
    os.makedirs(extension, exist_ok=True)
    os.replace(file, f'{extension}\\{file}')


print('Files sorted into respective folders')
