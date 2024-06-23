import argparse
import csv

def parse_arguments():
    parser = argparse.ArgumentParser(description='Calculate unemployment statistics for a specific country.')
    parser.add_argument('input_file', type=str, help='Input CSV file containing unemployment data.')
    parser.add_argument('--country', required=True, type=str)
    parser.add_argument('-o', '--operation', choices=['avg', 'min', 'max'], default='avg')
    parser.add_argument('--from', dest='from_year', type=int)
    parser.add_argument('--to', dest='to_year', type=int)
    return parser.parse_args()

def read_data(input_file, country, from_year, to_year):
    with open(input_file, mode='r', newline='') as file:
        reader = csv.reader(file)
        data = []
        for row in reader:
            if row[0] == country:
                year = int(row[2])
                if (from_year is None or year >= from_year) and (to_year is None or year <= to_year):
                    data.append(float(row[3]))
        return data

def calculate_statistics(data, operation):
    if not data:
        raise ValueError('No data available for the given parameters.')
    if operation == 'avg':
        return sum(data) / len(data)
    elif operation == 'min':
        return min(data)
    elif operation == 'max':
        return max(data)

def main():
    args = parse_arguments()
    data = read_data(args.input_file, args.country, args.from_year, args.to_year)
    result = calculate_statistics(data, args.operation)
    print(result)

if __name__ == '__main__':
    main()
