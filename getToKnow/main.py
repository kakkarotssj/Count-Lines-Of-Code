import os
import os.path
import sys


class Calculate(object):
    def __init__(self, path):
        self.total_lines = 0
        print self.__count_lines(path)

    def __checker(self, path):
        while not os.path.exists(path):
            print ("Path is invalid. Try again? Y/N")
            again_input = input()
            while again_input is not '':
                if again_input in ['Y', 'y']:
                    print("Enter path again...")
                    path = input()
                elif again_input in ['N', 'n']:
                    print("exiting...")
                    sys.exit(0)
                else:
                    print("Not an expected input. Try again?")
                    again_input = input()
        self.__create_structure(path)

    def __create_structure(self, path):
        everything = os.listdir(path)
        f = 0
        while f < len(everything):
            if everything[f][0] in ['.', '_'] or everything[f] == 'db.sqlite3':
                everything.remove(everything[f])
                f -= 1
            f += 1

        directory_list = []
        file_list = []
        for file_or_dir in everything:
            file_or_dir_absname = os.path.join(path, file_or_dir)
            if os.path.isdir(file_or_dir_absname):
                directory_list.append(file_or_dir_absname)
            if os.path.isfile(file_or_dir_absname):
                file_list.append(file_or_dir_absname)

        self.__process_files(file_list)
        self.__process_directory(directory_list)

    def __process_files(self, file_list):
        for file_name in file_list:
            file_descriptor = open(file_name, 'r')
            self.total_lines += self.__calculate_lines(file_descriptor)

    def __process_directory(self, directory_list):
        while True:
            try:
                directory_name = directory_list.pop(0)
                self.__create_structure(directory_name)
            except IndexError:
                break

    @staticmethod
    def __calculate_lines(file_descriptor):
        count = 0
        while file_descriptor.readline():
            count += 1

        return count

    def __count_lines(self, path):
        self.__checker(path)

        return self.total_lines
