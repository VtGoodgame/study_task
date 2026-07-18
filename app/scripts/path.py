from pathlib import Path

def collect_files_up_to_root(root_folder_name: str = "app") -> list[dict]:
    """
    Рекурсивно собирает все файлы в директории и ее поддиректориях.
    Исключает системные файлы и возвращает пути относительно корня.
    """
    # Находим корневую папку
    root_path = Path.cwd()
    while root_path.name != root_folder_name and root_path.parent != root_path:
        root_path = root_path.parent
    
    files_list = []
    
    for item in root_path.rglob('*'):
        if not item.is_file():
            continue
        
        # Пропускаем системные файлы
        if (item.name.startswith('.') or 
            item.name.startswith('__') or 
            item.suffix in ['.pyc', '.pyo', '.pyd']):
            continue
        
        files_list.append({
            "name": item.name,
            "dir": str(item.parent),
            "relative_path": str(item.relative_to(root_path)),
        })
    
    return files_list