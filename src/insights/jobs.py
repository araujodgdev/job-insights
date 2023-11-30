from typing import List, Dict
import csv


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self, path: str) -> List[Dict]:
        try:
            with open(path, encoding='utf-8') as file:
                file_data = csv.DictReader(file)
                self.jobs_list = list(file_data)
                return self.jobs_list
        except FileNotFoundError:
            print('Arquivo não encontrado')
            return list()

    def get_unique_job_types(self) -> List[str]:
        pass

    def filter_by_multiple_criteria(self) -> List[dict]:
        pass
