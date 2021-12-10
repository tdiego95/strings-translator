__copyright__ = "Copyright (C) 2021 Diego Turchi"
__license__ = "Public Domain"
__author__ = "Diego Turchi"
__version__ = "1.0"

import sys
from googletrans import Translator

# Consts #

supported_langs = ['ar', 'de', 'es', 'fr', 'id', 'it', 'ja', 'ko', 'nl', 'pt', 'ru', 'tr', 'vi', 'zh-cn', 'zh-tw'] 
android_string_format = '<string name="{0}">{1}</string>'
ios_string_format = '"{0}"="{1}";'
file_path = 'strings.xml'

# Vars #

en_strings = ''
target = ''

# Functions #

def translate():
	print('### Translating, take a break ☕ ###')
	file.write('\n')

	for lan in supported_langs:
		file.write('\n<!-- {0} -->\n'.format(lan.upper()))
		for text in en_strings:
			if (text == ''): continue

			if (target == 'android'):
				androidTranslate(text, lan)
			elif (target == 'ios'):
				iosTranslate(text, lan)

def androidTranslate(text, lan):
	translator = Translator()
	key = text[text.find('="') + 2 : text.find('">')]
	value = text[text.find('>') + 1 : text.find('</')]
	translated = translator.translate(value, src='en', dest=lan)
	file.write(android_string_format.format(key, translated.text) + '\n')

def iosTranslate(text, lan):
	translator = Translator()
	key = text[text.find('"') + 1 : text.find('"=')] 
	value = text[text.find('="') + 2 : text.find('";')]
	translated = translator.translate(value, src='en', dest=lan)
	file.write(ios_string_format.format(key, translated.text) + '\n')


###################
### ENTER POINT ###
###################

# Validate input data #

if len(sys.argv) > 1:
	arg = sys.argv[1]
else:
	print('Invalid arg. Use -h for help.')
	sys.exit()

if arg == '-android':
	target = arg[1:]
elif arg == '-ios':
	target = arg[1:]
elif arg == '-h':
	print('''
-h              -help
-android        -android target
-ios		-ios target
		''')
	sys.exit()
else:
	print('Invalid arg. Use -h for help.')
	sys.exit()

print('### Start script 🏃 ###')

try:
	# Read strings file #
	file = open(file_path, 'r+', encoding='utf-8')
	en_strings = file.read().split('\n')

	# Translation #
	translate()

except Exception as ex:
	print('An error occured 🛑 : {0}'.format(ex))
	print('Please clean the file and try again')
finally:
	file.close()
	print('### End script ✅ ###')
