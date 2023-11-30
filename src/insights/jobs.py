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
        job_types = list()
        for job in self.jobs_list:
            if job['job_type'] not in job_types:
                job_types.append(job['job_type'])
        return job_types

    def filter_by_multiple_criteria(self) -> List[dict]:
        pass


# test = ProcessJobs()
# test.read('data/jobs.csv')
# print(test.get_unique_job_types())
