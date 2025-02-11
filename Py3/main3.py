#p3
import pprint as p
import os

class Process_files:

    def __init__(self):
        self.files = []

    # Получить список файлов
    def get_list_files(self, folder_path, type_files):
        try:
            all_files = os.listdir(folder_path)
            self.files = [el for el in all_files if el.endswith("."+type_files)].copy()
        except FileNotFoundError:
            print(f"Ошибка: Папка '{folder_path}' не найдена.")
        except Exception as e:
            print(f"Общая ошибка: {e}")

    # Слияние файлов папки в merge_filename
    def merge_txt_files(self, folder_path, merge_filename):
            self.get_list_files(folder_path,'txt')
            count_lines = {}
            for filename in self.files:
                filepath = os.path.join(folder_path, filename)  # Полный путь к файлу
                try:
                    with open(filepath, 'r', encoding='utf-8') as file:
                        lines = file.readlines()
                        count_lines[filename]= len(lines)

                except Exception as e:
                    print(f"1 Ошибка при обработке файла {filename}: {e}")
            print('----2')
            p.pprint(count_lines)
            sorted_data = dict(sorted(count_lines.items(), key=lambda item: item[1]))
            print(sorted_data)
            try:
                file_res = open(merge_filename, 'w', encoding='utf-8')
            except Exception as e:
                print(f"2 Ошибка при открытии файла результата: {e}")

            for filename in sorted_data:
                filepath = os.path.join(folder_path, filename)
                try:
                    with open(filepath, 'r', encoding='utf-8') as file:
                        lines = file.readlines()
                        file_res.writelines(filename+'\n')
                        file_res.writelines(str(sorted_data[filename])+'\n')
                        file_res.writelines(lines)
                        file_res.writelines('\n')
                except Exception as e:
                    print(f"3 Ошибка при обработке файла : {e}")
            file_res.close()


def print_hi(name):
    print(f'Hello, {name}')


if __name__ == '__main__':
    print_hi('world')
    print('----')
    pf=Process_files()
    pf.get_list_files("./" ,"txt")
    p.pprint(pf.files)
    print('----')
    pf.merge_txt_files("./", "./res.md")
    print('----')
    try:
        with open('res.md', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                print(line.strip())
    except Exception as e:
        print(f"4 Ошибка при обработке файла: {e}")






