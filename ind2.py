#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import json
import os.path


if __name__ == '__main__':
    flylist = []
    list_file = 'd:\\flylist.txt'

    while True:
        command = input(">>> ").lower()
        if command == 'exit':
            break

        elif command == 'save':
            with open(list_file, "w") as f:
                json.dump(flylist, f)

        elif command == 'load':
            if os.path.exists(list_file):
                with open(list_file, "r") as f:
                    flylist = json.load(f)
            else:
                print('файла ', list_file, ' не существует!\n создайте и сохраните расписание')

        elif command == 'add':
            city = input("город назначения ")
            nfly = ''
            while not nfly.isdigit():
                nfly = input("номер рейса ")
            numfly = int(nfly)
            typea = input("тип самолета ")

            flylistdic = {
                'city': city,
                'numfly': numfly,
                'typea': typea,
            }

            flylist.append(flylistdic)
            if len(flylist) > 1:
                flylist.sort(key=lambda item: item.get('city', ''))

        elif command == 'list':
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 8
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^8} |'.format(
                    "№",
                    "Город ",
                    "Номер рейса",
                    "Тип ВС"
                )
            )
            print(line)
            for idx, flylistdic in enumerate(flylist, 1):
                print(
                    '| {:>4} | {:<30} | {:<20} | {:>8} |'.format(
                        idx,
                        flylistdic.get('city', ''),
                        flylistdic.get('numfly', '0'),
                        flylistdic.get('typea', '')
                    )
                )
            print(line)

        elif command == 'plane':
            destplane = input("тип самолёта ")

            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 8
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^8} |'.format(
                    "№",
                    "Город ",
                    "Номер рейса",
                    "Тип ВС"
                )
            )
            print(line)
            yesfly = -1
            for idx, flylistdic in enumerate(flylist, 1):
                if flylistdic.get('typea', '') == destplane:
                    yesfly = 1
                    print(
                        '| {:>4} | {:<30} | {:<20} | {:>8} |'.format(
                            idx,
                            flylistdic.get('city', ''),
                            flylistdic.get('numfly', '0'),
                            flylistdic.get('typea', '')
                        )
                    )
            print(line)
            if yesfly == -1:
                print('тип ', destplane, ' не выполняет рейсов')

        elif command == 'help' or command == '':
            print("Список команд:\n")
            print("add - добавить рейс;")
            print("list - вывести весь список рейсов;")
            print("save - сохранить список рейсов;")
            print("load - загрузить список рейсов;")
            print("plane - вывести типы самолётов;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
