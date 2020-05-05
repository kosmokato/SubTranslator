# subtranslator.py

"""
This script uses googletrans for translating subtitles files.

Was created for allow me to take an Android course in russian, translating the subtitles to english.
"""

# https://py-googletrans.readthedocs.io/en/latest/

import sys
from googletrans import Translator

if len(sys.argv)<2:
	print("[-] Not enough arguments.\n    Please, launch as " + sys.argv[0] + " <foreing_subs.srt>")
	exit()

translator = Translator()

# files
src_filename = sys.argv[1]
if src_filename.split(".")[-1] != 'srt':
	print("[-] The file is not an .srt\n    The program now will exit.")
	exit()
dst_filename = ".".join(src_filename.split(".")[:-1]) + "_translated.srt"

dst_output = []

src_file = open(src_filename, 'r').read().split("\n")
dst_file = open(dst_filename, 'w+')
# language detection
#print(translator.detect('ориентации или выход из приложения'))

# Limits:
# The maximum character limit on a single text is 15k
# If you get HTTP 5xx error or errors like #6, it’s probably because Google has banned your client IP address.
dst_file = open(dst_filename, 'w+')
for line in src_file:
	try:
		if not line: continue
		#print("[>] Translating: " + str(line))
		traduccion = translator.translate(line, src='ru', dest='en')
		print(traduccion)
		print(traduccion.origin + " --> " + traduccion.text)
		dst_file.write(traduccion.text)	
		#dst_output.append(traduccion.text)
	except Exception as e: 
		print(e)

print("[+] Translation complete and successful")
dst_file.close()


