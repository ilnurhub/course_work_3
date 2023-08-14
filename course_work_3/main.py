from course_work_3.utils.utils import *

FILENAME = 'operations.json'


def main():
    operations = load_json(FILENAME)
    sorted_operations = sort_list_of_dicts(operations, 'date')
    create_several_executed_outputs(sorted_operations)


if __name__ == '__main__':
    main()
