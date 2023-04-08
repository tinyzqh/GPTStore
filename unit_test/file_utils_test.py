from src.utils.file_utils import read_text_lines_file, write_text_lines_file


def split_words2txt(filepath, split_num=30):
    data = read_text_lines_file(filepath)
    data = [line.split(" ")[0] for line in data]
    slice_len = len(data) // split_num
    data_list = [[f"[Word List{i}]"] + data[i * slice_len : i * slice_len + slice_len] for i in range(split_num)]
    write_text_lines_file(file_path="aa.txt", text_lines=data_list)


if __name__ == "__main__":
    split_words2txt(
        filepath=r"C:\TalkBotGPT\src\utils\IELTS.txt",
    )
