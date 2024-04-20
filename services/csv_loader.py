import csv
import os


class CSVLoaderService:
    def open(self):
        project_dir = os.getcwd()
        data = []

        with open(f"{project_dir}/data/word_count.csv") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            next(csv_reader)

            for row in csv_reader:
                data.append(row)

        return data