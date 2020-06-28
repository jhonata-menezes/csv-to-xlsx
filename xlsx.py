import sys
import xlsxwriter
import csv
import logging
import argparse

logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s', level=logging.INFO)

def getOptions(args=sys.argv[1:]):
    parser = argparse.ArgumentParser(description="Parses command")
    parser.add_argument("-i", "--input", required=True, help="input csv")
    parser.add_argument("-o", "--output", default='output.xlsx', help="output xlsx")
    parser.add_argument("-s", "--delimiter", default=';', help="csv delimiter")
    parser.add_argument("-q", "--quotechar", default='"', help="csv quotechar")
    options = parser.parse_args(args)
    return options

def read_csv(input, delimiter=';', quotechar='"'):
    with open(input) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=delimiter, quotechar=quotechar)
        for row in spamreader:
            yield row

def main():
    options = getOptions()
    logging.info('started')

    workbook = xlsxwriter.Workbook(options.output, {'constant_memory': True})
    worksheet = workbook.add_worksheet()

    i = 0
    for row in read_csv(options.input, options.delimiter, options.quotechar):
        for col, data in enumerate(row):
            if data.isdigit():
                worksheet.write_number(i, col, int(data))
            else:
                worksheet.write_string(i, col, data)
        i+=1
        if i % 10000 == 0:
            logging.info(f'processed {i} rows')

    logging.info(f'finished with {i} rows')
    workbook.close()

if __name__ == '__main__':
    main()
