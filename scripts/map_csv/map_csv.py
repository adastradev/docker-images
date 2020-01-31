import argparse
import json


def generate_object(course: str):
    return json.dumps({
        "name": "Course {}".format(course),
        "exclusionType": "course",
        "description": "Course {} Exclusion".format(course),
        "fields": [
            {
                "field": "course_code",
                "simple": course
            }
        ]
    }, indent=2)


def read_data(file_path: str):
    with open(file_path, 'r', encoding='utf-8-sig') as csv_file:
        return "[{}\n]\n".format(",".join("\n{}".format(generate_object(line.strip())) for line in csv_file))


def write_result(result: str, file_path: str):
    with open(file_path, 'w', encoding='utf-8') as out_file:
        out_file.write(result)


def setup_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="CSV file to read")
    parser.add_argument("-o", "--output", help="Output file")
    return parser.parse_args()


def main():
    args = setup_arg_parser()
    result = read_data(args.input)

    if args.output:
        write_result(result, args.output)
    else:
        print(result)


if __name__ == '__main__':
    main()
