
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
