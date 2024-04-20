from services.csv_loader import CSVLoaderService
from services.mapper import Mapper
from services.reducer import Reducer


if __name__ == "__main__":
    # Wiring Depedencies
    csv_loader_service = CSVLoaderService()
    mapper = Mapper()
    reducer = Reducer()

    # Load the csv file
    data = csv_loader_service.open()

    map_result = mapper.run(data)
    mapreduce_result = reducer.run(map_result)

    print(mapreduce_result)
