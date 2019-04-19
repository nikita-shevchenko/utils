#!/usr/bin/env python
# coding: utf-8

import os
import json


language_folders = [x for x in os.listdir('.') if '-' in x]


def clean_json(language_folders):
    for language in language_folders:
        print('-' * 24)
        print('Start {} translations'.format(language))
        print('-' * 24)
        with open('{}/translation.json'.format(language)) as f:
            data = json.load(f)
        clear_data = {'common': {}};
        for key in data:
            intersections = set(clear_data['common'].keys()).intersection(set(data[key].keys()))
            if intersections:
                for intersection in intersections:
                    if (clear_data['common'][intersection] == data[key][intersection]):
                        continue
                    print('We can translate {} like \n{} \n{}'.format(intersection, clear_data['common'][intersection], data[key][intersection]))
                    translation = input('Enter correct:')
                    clear_data['common'][intersection] = translation
                    del data[key][intersection]
            clear_data['common'] = {**clear_data['common'], **data[key]}
        with open('{}/translation-fixed.json'.format(language), 'w', encoding='utf8') as f:
            json.dump(clear_data, f, ensure_ascii=False)
        print('-' * 24)
        print('End {} translations'.format(language))
        print('-' * 24)
        print('\n' * 2)


if __name__ == '__main__':
    clean_json(language_folders)




