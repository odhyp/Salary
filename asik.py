import os
from datetime import date
from dateutil.relativedelta import relativedelta


class FileManager:
    def __init__(self, tipe_pegawai):
        self.tipe_pegawai = tipe_pegawai
        self.folder_download = os.path.expanduser("~\\Downloads\\")
        self.folder_raw = os.path.join(os.path.dirname(__file__), "raw\\")
        self.file_date = (date.today() + relativedelta(months=1)).strftime('%Y_%m')
        self.file_name = "CRViewer1.xls"
