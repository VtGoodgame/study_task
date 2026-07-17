from pathlib import Path

def collect_files_up_to_root(root_folder_name: str = "study_task") -> list[dict]:
    """
    Начинает с текущей рабочей директории и поднимается вверх (через parent),
    на каждом уровне собирая имена и расширения файлов.
    Останавливается, дойдя до директории с именем root_folder_name (включительно).
    """
    current = Path.cwd()
    files_list = []

    while True:
        for item in current.iterdir():
            if item.is_file():
                files_list.append({
                    "name": item.name, #полное имя файла с расширением
                    "dir": str(current), #полный путь к директории, где находится файл
                })

        if current.name == root_folder_name:
            break

        if current.parent == current:
            break

        current = current.parent

    return files_list