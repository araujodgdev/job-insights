from src.insights.jobs import ProcessJobs
from typing import List


class ProcessIndustries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_unique_industries(self) -> List[str]:
        unique_industries = list()
        for job in self.jobs_list:
            if job["industry"] not in unique_industries and job["industry"]:
                unique_industries.append(job["industry"])

        return unique_industries
