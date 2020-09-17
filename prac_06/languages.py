from prac_06 import programming_language
from prac_06.programming_language import ProgrammingLanguage


def main():

    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(ruby)
    print(python)
    print(visual_basic)

    programs = [ruby, python, visual_basic]
    for program in programs:
        print(program)

main()
