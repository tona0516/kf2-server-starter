# encoding: UTF-8

import configparser

def get_map(config_path):
    config = configparser.ConfigParser()
    config.read_file(open(config_path))
    print(config.sections)

def input_options():
    options = []
    print("Length? (0 -> {short, 4 rounds}  1 -> {normal, 7 rounds}  2 -> {long, 10 rounds}) > ", end="")
    length = int(input())
    options.append({ "GameLength" : length })

    print("Difficulty? (0 -> Normal  1 -> Hard  2 -> Suicidal  3 -> Hell on Earth) > ", end="")
    difficulty = int(input())
    options.append({ "Difficulty" : difficulty })

    print("Mode? (0 -> Versus Survival  1 -> Weekly Outbreaks  2 -> Endless  3 -> None) > ", end="")
    mode = int(input())
    mode_str = ""
    if mode == 0:
        mode_str = "KFGameContent.KFGameInfo_VersusSurvival"
    if mode == 1:
        mode_str = "KFGameContent.KFGameInfo_WeeklySurvival"
    if mode == 2:
        mode_str = "KFGameContent.KFGameInfo_Endless"

    if mode_str != "":
        options.append({ "Game" : mode_str })
    
    return options

def main():
    # options = input_options()
    # print(options)
    get_map("./KFGame/Config/PCServer-KFGame.ini")
    pass

if __name__ == "__main__":
    main()