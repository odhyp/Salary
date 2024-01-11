from src.common.utils import get_download_path


class FileManager:
    def is_xls(self, file_name: str) -> bool:
        """Check if the file has a '.xls' extension.

        Args:
        - file_name (str): The name of the file.
        """
        return file_name.endswith('.xls')

    def is_xlsx(self, file_name: str) -> bool:
        """Check if the file has an '.xlsx' extension.

        Args:
        - file_name (str): The name of the file.
        """
        return file_name.endswith('.xlsx')

    def is_target_file(self, file_name: str) -> bool:
        """Check if the file is 'CRViewer1.xls'.

        Args:
        - file_name (str): The name of the file.
        """
        target_name = 'CRViewer1.xls'
        if file_name.find(target_name) == 0:
            return True
        else:
            return False

    def is_downloaded(self) -> bool:
        """Check if 'CRViewer1.xls' is downloaded.

        Args:
        - type (str): The type of the file.
        """
        for file in get_download_path().iterdir():
            is_target_file = self.is_target_file(file.name)
            is_xls = self.is_xls(file.name)
            if is_target_file and is_xls:
                return True
            else:
                continue
        return False
