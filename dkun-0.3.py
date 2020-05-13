#! /usr/bin/env python

#########################################
#	General Public License          #
#	Author:	Mostafa Vahedi          #
#	Date:	21 Apr. 2008            #
#	Version 0.3		        #
#########################################

import codecs

import sys


dk_numerical = [
chr(0x97),	# 	Arabic Thoushads Seperator
chr(0xA1)	#	ARABIC DECIMAL SEPARATOR
]


dk_vowels = [
chr(0xAB),	#	ARABIC FATHA
chr(0xAA),	#	ARABIC KASRA
chr(0xA9),	#	ARABIC DAMMA
chr(0xAC),	#	ARABIC FATHATAN
chr(0xBA),	#	ARABIC SHADDA
#chr(0x??),	#	ARABIC LETTER SUPERSCRIPT ALEF
#chr(0x??),	#	ARABIC LETTER SUBSCRIPT ALEF
chr(0xAD),	#	ARABIC HAMZA ABOVE
chr(0xAE)	#	ARABIC SUKUN
]

dk_non_joiners = [
chr(0xBC)	#	ARABIC LETTER HAMZA
]

dk_bidi_joiners_initial = [
chr(0xE1),	#	ARABIC LETTER AIN, initial form
chr(0xE5),	#	ARABIC LETTER GHAIN, initial form
chr(0xF9) 	#	ARABIC LETTER HEH, initial form
]

dk_bidi_joiners_medial = [
chr(0xE3),	#	ARABIC LETTER AIN, medial form
chr(0xE7),	#	ARABIC LETTER GHAIN, medial form
chr(0xFB) 	#	ARABIC LETTER HEH, medial form
]

dk_bidi_joiners_final = [
chr(0xE2),	#	ARABIC LETTER AIN, final form
chr(0xE6),	#	ARABIC LETTER GHAIN, final form
chr(0xFE) 	#	ARABIC LETTER FARSI YEH, final form
]

dk_bidi_joiners_isolated = [
chr(0xE0),	#	ARABIC LETTER AIN, isolated form
chr(0xE4),	#	ARABIC LETTER GHAIN, isolated form
chr(0xFC) 	#	ARABIC LETTER FARSI YEH, isolated form
]

dk_bidi_joiners_initial_medial = [
chr(0x94),	#	ARABIC TATWEEL
chr(0xFF),	#	ARABIC LETTER YEH WITH HAMZA ABOVE, initial-medial form
chr(0xC0),	#	ARABIC LETTER BEH, initial-medial form
chr(0xC2),	#	ARABIC LETTER PEH, initial-medial form
chr(0xC4),	#	ARABIC LETTER TEH, initial-medial form
chr(0xC6),	#	ARABIC LETTER THEH, initial-medial form
chr(0xC8),	#	ARABIC LETTER JEEM, initial-medial form
chr(0xCA),	#	ARABIC LETTER TCHEH, initial-medial form
chr(0xCC),	#	ARABIC LETTER HAH, initial-medial form
chr(0xCE),	#	ARABIC LETTER KHAH, initial-medial form
chr(0xD5),	#	ARABIC LETTER SEEN, initial-medial form
chr(0xD7),	#	ARABIC LETTER SHEEN, initial-medial form
chr(0xD9),	#	ARABIC LETTER SAD, initial-medial form
chr(0xDB),	#	ARABIC LETTER DAD, initial-medial form
chr(0xDD),	#	ARABIC LETTER TAH, initial-medial form
chr(0xDF),	#	ARABIC LETTER ZAH, initial-medial form
chr(0xE9),	#	ARABIC LETTER FEH, initial-medial form
chr(0xEB),	#	ARABIC LETTER QAF, initial-medial form
chr(0xED),	#	ARABIC LETTER KEHEH, initial-medial form
chr(0xEF),	#	ARABIC LETTER GAF, initial-medial form
chr(0xF2),	#	ARABIC LETTER LAM, initial-medial form
chr(0xF4),	#	ARABIC LETTER MEEM, initial-medial form
chr(0xF6),	#	ARABIC LETTER NOON, initial-medial form
chr(0xFD)	#	ARABIC LETTER FARSI YEH, initial-medial form
]

dk_bidi_joiners_final_isolated = [
chr(0xBF),	#	ARABIC LETTER BEH, final-isolated form
chr(0xC1),	#	ARABIC LETTER PEH, final-isolated form
chr(0xC3),	#	ARABIC LETTER TEH, final-isolated form
chr(0xC5),	#	ARABIC LETTER THEH, final-isolated form
chr(0xC7),	#	ARABIC LETTER JEEM, final-isolated form
chr(0xC9),	#	ARABIC LETTER TCHEH, final-isolated form
chr(0xCB),	#	ARABIC LETTER HAH, final-isolated form
chr(0xCD),	#	ARABIC LETTER KHAH, final-isolated form
chr(0xD4),	#	ARABIC LETTER SEEN, final-isolated form
chr(0xD6),	#	ARABIC LETTER SHEEN, final-isolated form
chr(0xD8),	#	ARABIC LETTER SAD, final-isolated form
chr(0xDA),	#	ARABIC LETTER DAD, final-isolated form
chr(0xDC),	#	ARABIC LETTER TAH, final-isolated form
chr(0xDE),	#	ARABIC LETTER ZAH, final-isolated form
chr(0xE8),	#	ARABIC LETTER FEH, final-isolated form
chr(0xEA),	#	ARABIC LETTER QAF, final-isolated form
chr(0xEC),	#	ARABIC LETTER KEHEH, final-isolated form
chr(0xEE),	#	ARABIC LETTER GAF, final-isolated form
chr(0xF0),	#	ARABIC LETTER LAM, final-isolated form
chr(0xF3),	#	ARABIC LETTER MEEM, final-isolated form
chr(0xF5),	#	ARABIC LETTER NOON, final-isolated form
chr(0xF8) 	#	ARABIC LETTER HEH, final-isolated form
]

dk_right_joiners_final = [
chr(0xBE)	#	ARABIC LETTER ALEF, final form
]

dk_right_joiners_isolated = [
chr(0xBD)	#	ARABIC LETTER ALEF, isolated form
]

dk_right_joiners_final_isolated = [
chr(0xBB),	#	ARABIC LETTER ALEF WITH MADDA ABOVE, isolated form
chr(0xCF),	#	ARABIC LETTER DAL
chr(0xD0),	#	ARABIC LETTER THAL
chr(0xD1),	#	ARABIC LETTER REH
chr(0xD2),	#	ARABIC LETTER ZAIN
chr(0xD3),	#	ARABIC LETTER JEH
#chr(0xBF),	#	ARABIC LETTER TEH MARBUTAH
chr(0xF1),	#	ARABIC LIGATURE LAM WITH ALEF
chr(0xF7)	#	ARABIC LETTER WAW
]


table_DK_UN = {
chr(0xB0) : [u'\u06F0'],	#	EXTENDED ARABIC-INDIC DIGIT ZERO
chr(0xB1) : [u'\u06F1'],	#	EXTENDED ARABIC-INDIC DIGIT ONE
chr(0xB2) : [u'\u06F2'],	#	EXTENDED ARABIC-INDIC DIGIT TWO
chr(0xB3) : [u'\u06F3'],	#	EXTENDED ARABIC-INDIC DIGIT THREE
chr(0xB4) : [u'\u06F4'],	#	EXTENDED ARABIC-INDIC DIGIT FOUR
chr(0xB5) : [u'\u06F5'],	#	EXTENDED ARABIC-INDIC DIGIT FIVE
chr(0xB6) : [u'\u06F6'],	#	EXTENDED ARABIC-INDIC DIGIT SIX
chr(0xB7) : [u'\u06F7'],	#	EXTENDED ARABIC-INDIC DIGIT SEVEN
chr(0xB8) : [u'\u06F8'],	#	EXTENDED ARABIC-INDIC DIGIT EIGHT
chr(0xB9) : [u'\u06F9'],	#	EXTENDED ARABIC-INDIC DIGIT NINE
chr(0xA7) : [u'\u060C'],	#	ARABIC COMMA
chr(0x94) : [u'\u0640'],	#	ARABIC TATWEEL
chr(0xA3) : [u'\u061F'],	#	ARABIC QUESTION MARK
chr(0xBB) : [u'\u0622'],	#	ARABIC LETTER ALEF WITH MADDA ABOVE, isolated form
chr(0xFF) : [u'\u0626'],	#	ARABIC LETTER YEH WITH HAMZA ABOVE, initial-medial form
chr(0xBC) : [u'\u0621'],	#	ARABIC LETTER HAMZA
chr(0xBD) : [u'\u0627'],	#	ARABIC LETTER ALEF, isolated form
chr(0xBE) : [u'\u0627'],	#	ARABIC LETTER ALEF, final form
chr(0xBF) : [u'\u0628'],	#	ARABIC LETTER BEH, final-isolated form
chr(0xC0) : [u'\u0628'],	#	ARABIC LETTER BEH, initial-medial form
chr(0xC1) : [u'\u067E'],	#	ARABIC LETTER PEH, final-isolated form
chr(0xC2) : [u'\u067E'],	#	ARABIC LETTER PEH, initial-medial form
chr(0xC3) : [u'\u062A'],	#	ARABIC LETTER TEH, final-isolated form
chr(0xC4) : [u'\u062A'],	#	ARABIC LETTER TEH, initial-medial form
chr(0xC5) : [u'\u062B'],	#	ARABIC LETTER THEH, final-isolated form
chr(0xC6) : [u'\u062B'],	#	ARABIC LETTER THEH, initial-medial form
chr(0xC7) : [u'\u062C'],	#	ARABIC LETTER JEEM, final-isolated form
chr(0xC8) : [u'\u062C'],	#	ARABIC LETTER JEEM, initial-medial form
chr(0xC9) : [u'\u0686'],	#	ARABIC LETTER TCHEH, final-isolated form
chr(0xCA) : [u'\u0686'],	#	ARABIC LETTER TCHEH, initial-medial form
chr(0xCB) : [u'\u062D'],	#	ARABIC LETTER HAH, final-isolated form
chr(0xCC) : [u'\u062D'],	#	ARABIC LETTER HAH, initial-medial form
chr(0xCD) : [u'\u062E'],	#	ARABIC LETTER KHAH, final-isolated form
chr(0xCE) : [u'\u062E'],	#	ARABIC LETTER KHAH, initial-medial form
chr(0xCF) : [u'\u062F'],	#	ARABIC LETTER DAL
chr(0xD0) : [u'\u0630'],	#	ARABIC LETTER THAL
chr(0xD1) : [u'\u0631'],	#	ARABIC LETTER REH
chr(0xD2) : [u'\u0632'],	#	ARABIC LETTER ZAIN
chr(0xD3) : [u'\u0698'],	#	ARABIC LETTER JEH
chr(0xD4) : [u'\u0633'],	#	ARABIC LETTER SEEN, final-isolated form
chr(0xD5) : [u'\u0633'],	#	ARABIC LETTER SEEN, initial-medial form
chr(0xD6) : [u'\u0634'],	#	ARABIC LETTER SHEEN, final-isolated form
chr(0xD7) : [u'\u0634'],	#	ARABIC LETTER SHEEN, initial-medial form
chr(0xD8) : [u'\u0635'],	#	ARABIC LETTER SAD, final-isolated form
chr(0xD9) : [u'\u0635'],	#	ARABIC LETTER SAD, initial-medial form
chr(0xDA) : [u'\u0636'],	#	ARABIC LETTER DAD, final-isolated form
chr(0xDB) : [u'\u0636'],	#	ARABIC LETTER DAD, initial-medial form
chr(0xDC) : [u'\u0637'],	#	ARABIC LETTER TAH, initial-medial form
chr(0xAB) : [u'\u064E'],	#	ARABIC FATHA
chr(0xAA) : [u'\u0650'],	#	ARABIC KASRA
chr(0xA9) : [u'\u064F'],	#	ARABIC DAMMA
chr(0xAC) : [u'\u064B'],	#	ARABIC FATHATAN
chr(0xBA) : [u'\u0651'],	#	ARABIC SHADDA
chr(0x95) : [u'\u0023'],	# * #
chr(0x83) : [u'\u0024'],	# * $
chr(0x96) : [u'\u066A'],	# * %
chr(0x87) : [u'\u0026'],	# * &
chr(0x9C) : [u'\u00D7'],	# * ARABIC cross (times) x
chr(0x97) : [u'\u066C'],	# 	Arabic Thoushads Seperator
#chr(0xBA) : [u'\u0670'],	#	ARABIC LETTER SUPERSCRIPT ALEF
chr(0xAD) : [u'\u0654'],	#	ARABIC HAMZA ABOVE
chr(0xA1) : [u'\u066B'],	#	ARABIC DECIMAL SEPARATOR
chr(0x91) : [u'\u0028'],	# * RIGHT PARENTHESIS
chr(0x90) : [u'\u0029'],	# * LEFT PARENTHESIS
#chr(0xBF) : [u'\u0629'],	#	ARABIC LETTER TEH MARBUTAH
chr(0x8E) : [u'\u00BB'],	#	RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK
chr(0xDD) : [u'\u0637'],	#	ARABIC LETTER TAH, final-isolated form
chr(0xDE) : [u'\u0638'],	#	ARABIC LETTER ZAH, final-isolated form
chr(0x8F) : [u'\u00AB'],	#	LEFT-POINTING DOUBLE ANGLE QUOTATION MARK
chr(0xAE) : [u'\u0652'],	#	ARABIC SUKUN
chr(0x9F) : [u'\u002D'],	# * -
chr(0xA2) : [u'\u002E'],	# * FULL STOP
#chr(0xA1) : [u'\u002F'],	# * /
chr(0x82) : [u'\u002A'],	# * *
chr(0x86) : [u'\u007E'],	# * ~
chr(0xA5) : [u'\u003A'],	# * COLON
chr(0xA6) : [u'\u061B'],	# 	ARABIC SEMICOLON
chr(0x9A) : [u'\u003E'],	# * GREATER-THAN SIGN
chr(0x9E) : [u'\u002B'],	# * +
chr(0x99) : [u'\u003D'],	# * =
chr(0x98) : [u'\u003C'],	# * LESS-THAN SIGN
chr(0x81) : [u'\u0040'],	# * @
chr(0x92) : [u'\u005D'],	# * [
chr(0x9D) : [u'\u005C'],	# * \
chr(0x93) : [u'\u005B'],	# * ]
#chr(0xAE) : [u'\u005E'],	# * ^
#chr(0xD5) : [u'\u005F'],	# * _
chr(0xA8) : [u'\u0060'],	# * `
chr(0x8B) : [u'\u007D'],	# * {
chr(0xAF) : [u'\u007C'],	# * |
chr(0xA0) : [u'\u0020'],	# * SPACE
chr(0xA4) : [u'\u0021'],	# * EXCLAMATION MARK
chr(0x8C) : [u'\u007B'],	# * }
chr(0xDF) : [u'\u0638'],	#	ARABIC LETTER ZAH, initial-medial form
chr(0xE0) : [u'\u0639'],	#	ARABIC LETTER AIN, isolated form
chr(0xE1) : [u'\u0639'],	#	ARABIC LETTER AIN, final form
chr(0xE2) : [u'\u0639'],	#	ARABIC LETTER AIN, medial form
chr(0xE3) : [u'\u0639'],	#	ARABIC LETTER AIN, initial form
chr(0xE4) : [u'\u063A'],	#	ARABIC LETTER GHAIN, isolated form
chr(0xE5) : [u'\u063A'],	#	ARABIC LETTER GHAIN, final form
chr(0xE6) : [u'\u063A'],	#	ARABIC LETTER GHAIN, medial form
chr(0xE7) : [u'\u063A'],	#	ARABIC LETTER GHAIN, initial form
chr(0xE8) : [u'\u0641'],	#	ARABIC LETTER FEH, final-isolated form
chr(0xE9) : [u'\u0641'],	#	ARABIC LETTER FEH, initial-medial form
chr(0xEA) : [u'\u0642'],	#	ARABIC LETTER QAF, final-isolated form
chr(0xEB) : [u'\u0642'],	#	ARABIC LETTER QAF, initial-medial form
chr(0xEC) : [u'\u06A9'],	#	ARABIC LETTER KEHEH, final-isolated form
chr(0xED) : [u'\u06A9'],	#	ARABIC LETTER KEHEH, initial-medial form
chr(0xEE) : [u'\u06AF'],	#	ARABIC LETTER GAF, final-isolated form
chr(0xEF) : [u'\u06AF'],	#	ARABIC LETTER GAF, initial-medial form
chr(0xF0) : [u'\u0644'],	#	ARABIC LETTER LAM, final-isolated form
chr(0xF1) : [u'\u0644\u0627'],	#	ARABIC LIGATURE LAM WITH ALEF
chr(0xF2) : [u'\u0644'],	#	ARABIC LETTER LAM, initial-medial form
chr(0xF3) : [u'\u0645'],	#	ARABIC LETTER MEEM, final-isolated form
chr(0xF4) : [u'\u0645'],	#	ARABIC LETTER MEEM, initial-medial form
chr(0xF5) : [u'\u0646'],	#	ARABIC LETTER NOON, final-isolated form
chr(0xF6) : [u'\u0646'],	#	ARABIC LETTER NOON, initial-medial form
chr(0xF7) : [u'\u0648'],	#	ARABIC LETTER WAW
chr(0xF8) : [u'\u0647'],	#	ARABIC LETTER HEH, final-isolated form
chr(0xFB) : [u'\u0647'],	#	ARABIC LETTER HEH, medial form
chr(0xF9) : [u'\u0647'],	#	ARABIC LETTER HEH, initial form
chr(0xFE) : [u'\u06CC'],	#	ARABIC LETTER FARSI YEH, final form
chr(0xFC) : [u'\u06CC'],	#	ARABIC LETTER FARSI YEH, isolated form
chr(0xFD) : [u'\u06CC']		#	ARABIC LETTER FARSI YEH, initial-medial form
}


def dk_is_numeric(ch):
	if ((ch in dk_numerical) or 
	    ((ch >= chr(0xB0)) and (ch <= chr(0xB9))) ):
		return 1
	return 0

def dk_can_join_left(ch):
	if ((ch in dk_bidi_joiners_initial) or
	    (ch in dk_bidi_joiners_medial) or
	    (ch in dk_bidi_joiners_final) or
	    (ch in dk_bidi_joiners_isolated) or
	    (ch in dk_bidi_joiners_initial_medial) or
	    (ch in dk_bidi_joiners_final_isolated)):
    		return 1
	return 0

def dk_can_join_right(ch):
	if (dk_can_join_left(ch) or 
	    (ch in dk_right_joiners_final) or
	    (ch in dk_right_joiners_isolated) or
	    (ch in dk_right_joiners_final_isolated)):
		return 1
	return 0

def dk_joining_left(ch):
	if ((ch in dk_bidi_joiners_initial) or 
	    (ch in dk_bidi_joiners_medial) or
	    (ch in dk_bidi_joiners_initial_medial)):
		return 1
	return 0


def dk_joining_right(ch):
	if ((ch in dk_right_joiners_final) or
	    (ch in dk_bidi_joiners_medial) or 
	    (ch in dk_bidi_joiners_final)):
		return 1
	return 0

def dk_not_right_joined(ch):
	if ((ch in dk_bidi_joiners_initial) or
	    (ch in dk_right_joiners_isolated) or
	    (ch in dk_bidi_joiners_isolated)):
		return 1
	return 0

def dk_adjust_shaping(text, i):
	current = text[i]
	u = u''
	try:
		u = table_DK_UN[current][0]
	except KeyError:
		print 'ERROR: unmapped character'
		return u''

	#if you don't want shaping remove the following comment
	#return u

	if ((current in dk_vowels) or (dk_is_numeric(current))):
		return u

	#find next non-vowel character on the left
	text_len = len(text)
	next_index = i+1
	while ((next_index < text_len) and (text[next_index] in dk_vowels)):
		next_index += 1

	if (next_index == text_len):
		next = ''
	else:
		next = text[next_index]

	# if current letter is joining from left but next letter is or can not joining
	if (dk_joining_left(current)):
		if (not dk_can_join_right(next)):
			u += u'\u200D' #ZWJ
		elif (dk_not_right_joined(next)):
			u += u'\u200D\u200C' #ZWJ+ZWNJ
	# if current letter can join but next letter is joining from right
	elif (dk_can_join_left(current)):
		if (dk_joining_right(next)):
			u += u'\u200C\u200D' #ZWNJ+ZWJ
		elif (dk_can_join_right(next)):
			u += u'\u200C' #ZWNJ
	return u

def dk_adjust_number(text):
	result = u''
	i = len(text)-1
	while (i >= 0):
		result += dk_adjust_shaping(text, i)
		i -= 1
	return result


def map_dk_unicode(text):
	mapped_text = u''

	i = 0
	while (i < len(text)):
		if (dk_is_numeric(text[i])):
			next_index = i
			while ((next_index+1 < len(text)) and
			       (dk_is_numeric(text[next_index+1]))):
				next_index += 1
			mapped_text += dk_adjust_number(text[i:next_index+1])
			i = next_index+1
			continue

		mapped_text += dk_adjust_shaping(text, i)
		i += 1
	return mapped_text

def dk_next_part(line, i):
	j = i
	language_flag = (line[j]<chr(0x80))
	while ((j<line_len) and ((line[j]<chr(0x80)) == language_flag) ):
		j += 1
	return j


def is_english_letter_number(c):
	if ((c >= 'a') and (c <= 'z')) or ((c >= 'A') and (c <= 'Z')):
		return 1
	if (c >= '0') and (c <= '9'):
		return 1
	return 0

def is_inbetween_chars(c):
	if ((c == '.') or (c == '-') or (c == '_') or (c == '/')):
		return 1
	return 0

def needs_english_wrapper(part):
	part_len = len(part)
	i = -1
	while (i+1 < part_len):
		i += 1
		if (is_english_letter_number(part[i]) == 1):
			continue
		if (i>0) and (is_inbetween_chars(part[i]) == 1) and \
		   (part_len > i+1) and (is_english_letter_number(part[i+1]) == 1):
			continue
		return 1
	return 0

# Main body of the program 
if len(sys.argv) <= 2:
	print 'usage: python dkun in_filename out_filename'
	exit(0)

filename = sys.argv[1]
outfile = sys.argv[2]

try:
	f = open(filename, 'r')
except IOError:
	print "Can not open the input file: " + filename
	exit(0)

try:
	of = codecs.open(outfile, encoding='utf-8', mode='w')
except IOError:
	print "Can not open the output file: " + outfile
	exit(0)

line_number = 0
for line in f:
	line_number += 1
	output_line = u''
	line_len = len(line)

	put_end_of_line = 0
	if ((line_len > 0) and (line[line_len-1] == '\n')):
		put_end_of_line = 1
		line_len = line_len - 1
	if ((line_len > 0) and (line[line_len-1] == '\r')):
		line_len = line_len - 1

	i = 0

	while (i<line_len):
		next_part_index = dk_next_part(line, i)
		next_part = line[i:next_part_index]
		next_part_latin = (line[i]<chr(0x80))

		if next_part_latin:
			if (needs_english_wrapper(next_part[::-1]) == 1):
				next_part = '\$e_'+next_part[::-1]+'\$f_'
			else:
				next_part = next_part[::-1]
			output_line += next_part.encode( 'utf-8' )
		else:
			output_line += map_dk_unicode(next_part)
		i = next_part_index
	# end of while			
	
	if (put_end_of_line == 1):
		output_line += u'\u000a'

	# write the processed line
	of.write(output_line)
	# end of line processing
# end of file processing

of.close()
f.close()
