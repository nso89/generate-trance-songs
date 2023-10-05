from random import randrange
from pathlib import Path
from typing import List
from datetime import datetime


LIMIT = 5
MAIN_TXT = Path.home().joinpath("Notes\\trance\\main.txt")


def get_line_count_from(file: Path) -> int:
    count = 0
    with open(file) as f_obj:
        for line in f_obj:
            count += 1
    return count


def get_track_list_from(file: Path, search_for: List[int]) -> List[str]:
    """
    Open a file, and using a list of line numbers, append the 
    matching line.
    """
    temp : List[str]
    with open(file) as f_obj:
       temp = [line.strip() 
               for number, line in enumerate(f_obj, start = 0) 
               if number in search_for]
    return temp


def write_a_list_to_a_file(file_name: Path, items: List[str]):
    """
    Write each element of items on a new line.
    """
    with open(file_name, "w") as stream:
        for word in items:
            stream.write(f"{word}\n")


def get_date() -> datetime:
    """   
    datetime: Formatted as YYYYMMDD-HHMMSS.  
    """
    return datetime.now().strftime("%Y%m%d-%H%M%S")


def main():

    lines : int  = get_line_count_from(file = MAIN_TXT)
    numbers : List[int] = sorted([randrange(lines) for _ in range(LIMIT)])
    today_trance = get_track_list_from(file = MAIN_TXT, search_for = numbers)

    print("\n")
    for track in today_trance:
        print(track)
    
    write_to_file = input("\nWrite to file (y/n): ").strip().lower()

    # Any string other than lowercase y is silently ignored. Not always
    # the best thing to do, but for this simple script, it works.
    if write_to_file == "y":
        file_name = Path(__file__).parent.joinpath(get_date()).with_suffix(".txt")
        write_a_list_to_a_file(file_name = file_name, items = today_trance)
        print(f"File Name: {file_name} ")

    print("\nEnjoy!")

if __name__ == "__main__":
    main()
