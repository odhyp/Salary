from pathlib import Path


def get_root_path():
    """Get project root path
    """
    current_path = Path().absolute()
    root_path = Path(current_path)
    return root_path


def get_data_path():
    """Get data directory path
    """
    root_path = get_root_path()
    data_path = Path(root_path, 'data')
    return data_path


def get_download_path():
    """Get User/Downloads path
    """
    return Path(Path.home(), "Downloads")
