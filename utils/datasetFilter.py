input_file_name = '../dataset/athlete_events_original.csv'
output_file_name = '../dataset/athlete_events.csv'

output_file = open(output_file_name, 'w', newline='\n', encoding='utf-8')

with open(input_file_name) as input_file:
    line_count = 0
    for row in input_file:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
            output_file.write(row)
        else:
            if line_count < 50:
                # print(f'\tLine {line_count}\tSport is {row[12]}.')
                print(row)
            if "\"Swimming\"" in row:
                output_file.write(row)
            line_count += 1
    print(f'Processed {line_count} lines.')

output_file.close()