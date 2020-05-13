#! /usr/bin/env python
#########################################
#	General Public License          #
#	Author:	Mostafa Vahedi          #
#	Date:	22 Apr. 2007            #
#	Version 0.2		        #
#########################################

import codecs

import sys

bidi_joiners = [
u'\u0626', u'\u0628', u'\u062a', u'\u062b', u'\u062c', u'\u062d', u'\u062e',
u'\u0633', u'\u0634', u'\u0635', u'\u0636', u'\u0637', u'\u0638', u'\u0639', u'\u063a', 
u'\u0640', u'\u0641', u'\u0642', u'\u0643', u'\u0644', u'\u0645', u'\u0646', u'\u0647',
u'\u0649', u'\u064a', u'\u067e', u'\u0686', u'\u06a9', u'\u06af', u'\u200d',
u'\u06cc']

right_joiners = [
u'\u0622', u'\u0623', u'\u0624', u'\u0625', u'\u0627', u'\u0629', u'\u062f', u'\u0630', u'\u0631', 
u'\u0632', u'\u0648', u'\u0671', u'\u0600', u'\u0698']


#form_numbers, isolated, final, medial, initial
table_UN_DK = {
u'\n' : [1, '\n'],
#case u'\u0020' - 0xA0 : #space
u' ' : [1, chr(0xA0)],
#case u'\u0021' - 0xA4 : #exclamation
u'!' : [1, chr(0xA4)],
## case u'\u0022' - 0x?? : #quotation
#case u'\u0023' - 0x95 : #number sign
u'#' : [1, chr(0x95)],
#case u'\u0024' - 0x83 : #?? dollar sign
u'$' : [1, chr(0x83)],
#case u'\u0025' - 0x96 : #percent sign
u'%' : [1, chr(0x96)],
#case u'\u0026' - 0x87 : #?? ampersand
u'&' : [1, chr(0x87)],
#case u'\u0027' - 0xa9 : #apostrophe
u'\'' : [1, chr(0xa9)],
#case u'\u0028' - 0x90 : #left parenthesis
u'(' : [1, chr(0x91)],
#case u'\u0029' - 0x91 : #right parenthesis
u')' : [1, chr(0x90)],
#case u'\u002a' - 0x82 : #asterisk
u'*' : [1, chr(0x82)],
#case u'\u002b' - 0x9e : #plus sign
u'+' : [1, chr(0x9e)],
#case u'\u002c' - 0x97 : #comma
u',' : [1, chr(0x97)],
#case u'\u002d' - 0x9f : #hyphen-minus
u'-' : [1, chr(0x9f)],
#case u'\u002e' - 0xA2 : #full stop
u'.' : [1, chr(0xA2)],
#case u'\u002f' - 0xa1 : #solidus
u'/' : [1, chr(0xa1)],
#	       #-- digits 0..9 B0 - B9
#case u'\u003a' - 0xa5 : #colon
u':' : [1, chr(0xa5)],
## case u'\u003b' - 0xa6 : #handled in >128: semicolon
#case u'\u003c' - 0x98 : #less than sign
u'<' : [1, chr(0x98)],
#case u'\u003d' - 0x99 : #equal sign
u'=' : [1, chr(0x99)],
#case u'\u003e' - 0x9a : #more than sign
u'>' : [1, chr(0x9a)],
## case u'\u003f' - 0xa3 : #handled in >128: question mark
#case u'\u0040' - 0x81 : #commercialat
u'@' : [1, chr(0x81)],
##-- letters A..Z
#case u'\u005b' - 0x92 : #left square bracket
u'[' : [1, chr(0x93)],
#case u'\u005c' - 0x9d : #reverse solidus
u'\\' : [1, chr(0x9d)],
#case u'\u005d' - 0x93 : #right square bracket
u']' : [1, chr(0x92)],
#case u'\u005e' - 0xAE : #circumflex accent
u'^' : [1, chr(0xAE)],
## case u'\u005f' - 0x?? : #?? low line
#case u'\u0060' - 0xa8 : #grave accent
u'`' : [1, chr(0xa8)],
#	       #-- letters a..z
#case u'\u007b' - 0x8b : #left curly bracket
u'{' : [1, chr(0x8c)],
#case u'\u007c' - 0xaf : #vertical line
u'|' : [1, chr(0xaf)],
#case u'\u007d' - 0x8c : #right curly bracket
u'}' : [1, chr(0x8b)],
#case u'\u007e' - 0x86 : #tilde
u'~' : [1, chr(0x86)],
#case u'\u00BB' - 0x8E : #RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK
u'\u00BB' : [1, chr(0x8E)], 
#case u'\u00AB' - 0x8F : #LEFT-POINTING DOUBLE ANGLE QUOTATION MARK
u'\u00AB' : [1, chr(0x8F)], 
#case u'\u00D7' - 0x9c : #times
u'\u00D7' : [1, chr(0x9c)],
#case u'\u200C' #ZWJ
u'\u200C' : [1, ''],
#case u'\u200D' #ZWNJ
u'\u200D' : [1, ''],

#060C - 0xA7 : arabic comma
u'\u060C' : [1, chr(0xA7)],
#061B - 0xA6 : arabic semicolon
u'\u061B' : [1, chr(0xA6)],
#061F - 0XA3 : arabic question mark
u'\u061F' : [1, chr(0xA3)],
#0621 - 0xBC hamza
u'\u0621' : [1, chr(0xBC)],
#0622 - 0xBB : alef + madda, the kernel joins it if should joined!!!
u'\u0622' : [1, chr(0xBB)],
#0623 - 0xBD+0xAD - 0xBE+0xAD : alef + hamza above
u'\u0623' : [2, chr(0xBD)+chr(0xAD), chr(0xBE)+chr(0xAD)],
#0624 - 0xF7+0xAD : waw + hamza above
u'\u0624' : [1, chr(0xF7)+chr(0xAD)],
#0625 - 0xBD+\hamzabelow - 0xBE+\hamzabelow : alef + hamza below
u'\u0625' : [2, chr(0xBD)+'\\hamzabelow', chr(0xBE)+'\\hamzabelow'],
#0626 - 0xFF - 0xFC+0xAD : yeh + hamza above
u'\u0626' : [3, chr(0xFC)+chr(0xAD), chr(0xFE)+chr(0xAD), chr(0xFF)],
#0627 - 0xBD - 0xBE : alef
u'\u0627' : [2, chr(0xBD), chr(0xBE)],
#0628 - 0xBF - 0xC0 : beh
u'\u0628' : [2, chr(0xBF), chr(0xC0)],
#0629 - \0xF8 : teh marbuta
u'\u0629' : [1, '\\'+chr(0xF8)],
#062a - 0xC3 - 0xC4 : teh
u'\u062a' : [2, chr(0xC3), chr(0xC4)],
#062b - 0xC5 - 0xC6 : theh
u'\u062b' : [2, chr(0xC5), chr(0xC6)],
#062c - 0xC7 - 0xC8 : jeem
u'\u062c' : [2, chr(0xC7), chr(0xC8)],
#062d - 0xCB - 0xCC : hah
u'\u062d' : [2, chr(0xCB), chr(0xCC)],
#062e - 0xCD - 0xCE : khah
u'\u062e' : [2, chr(0xCD), chr(0xCE)],
#062f - 0xCF : dal
u'\u062f' : [1, chr(0xCF)],
#0630 - 0xD0 : thal
u'\u0630' : [1, chr(0xD0)],
#0631 - 0xD1 : reh
u'\u0631' : [1, chr(0xD1)],
#0632 - 0xD2 : zain
u'\u0632' : [1, chr(0xD2)],
#0633 - 0xD4 - 0xD5 : seen
u'\u0633' : [2, chr(0xD4), chr(0xD5)],
#0634 - 0xD6 - 0xD7 : sheen
u'\u0634' : [2, chr(0xD6), chr(0xD7)],
#0635 - 0xD8 - 0xD9 : sad
u'\u0635' : [2, chr(0xD8), chr(0xD9)],
#0636 - 0xDA - 0xDB : dad
u'\u0636' : [2, chr(0xDA), chr(0xDB)],
#0637 - 0xDC - 0xDD : tah
u'\u0637' : [2, chr(0xDC), chr(0xDD)],
#0638 - 0xDE - 0xDF : zah
u'\u0638' : [2, chr(0xDE), chr(0xDF)],
#0639 - 0xE0 - 0xE1 - 0xE2 - 0xE3 : ain
u'\u0639' : [4, chr(0xE0), chr(0xE2), chr(0xE3), chr(0xE1)],
#063a - 0xE4 - 0xE5 - 0xE6 - 0xE7 : ghain
u'\u063a' : [4, chr(0xE4), chr(0xE6), chr(0xE7), chr(0xE5)],
#0640 - 0x94 : tatweel
u'\u0640' : [1, chr(0x94)],
#0641 - 0xE8 - 0xE9 : feh
u'\u0641' : [2, chr(0xE8), chr(0xE9)],
#0642 - 0xEA - 0xEB : Qaf
u'\u0642' : [2, chr(0xEA), chr(0xEB)],
#0643 - \arabkeh - 0xED : arabic ke
u'\u0643' : [2, '\\arabkeh', chr(0xED)],
#0644 - 0xF0 - 0xF2 : lam
u'\u0644' : [2, chr(0xF0), chr(0xF2)],
#0645 - 0xF3 - 0xF4 : meem
u'\u0645' : [2, chr(0xF3), chr(0xF4)],
#0646 - 0xF5 - 0xF6 : noon
u'\u0646' : [2, chr(0xF5), chr(0xF6)],
#0647 - 0xF8 - 0xF9 - 0xFB : heh
u'\u0647' : [3, chr(0xF8), chr(0xFB), chr(0xF9)],
#0648 - 0xF7 : waw
u'\u0648' : [1, chr(0xF7)],
#0649 - \alefmaq - \alefmaqjd : alef maksura
u'\u0649' : [2, '\\alefmaq', '\\alefmaqjd'],
#064a - \arabyeh - \arabyehjd - 0xFD : arabic yeh
u'\u064a' : [3, '\\arabyeh', '\\arabyehjd', chr(0xFD)],

#064b - 0xAC : nasb
u'\u064b' : [1, chr(0xAC)],
#064c - \raf : raf
u'\u064c' : [1, '\\'+chr(0xA9)],
#064d - \jar : jar
u'\u064d' : [1, '\\'+chr(0xAA)],
#064e - 0xAB : fatha
u'\u064e' : [1, chr(0xAB)],
#064f - 0xA9 : zamma
u'\u064f' : [1, chr(0xA9)],
#0650 - 0xAA : kasra
u'\u0650' : [1, chr(0xAA)],
#0651 - 0xBA : shadda
u'\u0651' : [1, chr(0xBA)],
#0652 - 0xAE : sokun
u'\u0652' : [1, chr(0xAE)],
#0653 - \mad : madda
u'\u0653' : [1, '\\'+chr(0x86)],
#0654 - 0xAD : hamza above
u'\u0654' : [1, chr(0xAD)],
#0655 - \hamzabelow : hamza below
u'\u0655' : [1, '\\hamzabelow'],
#0656 - \alefkootahpayyn : alef subscript
u'\u0656' : [1, '\\'+chr(0xBD)+chr(0xFC)+chr(0xA0)],

#066a - 0x96 : arabic percent sign
u'\u066a' : [1, chr(0x96)],
#066b - 0xA1 : arabic decimal seperator
u'\u066b' : [1, chr(0xA1)],
#066c - 0x97 : arabic thousands seperator
u'\u066c' : [1, chr(0x97)],

#0670 - \alefkootahbala : alef superscript
u'\u0670' : [1, '\\'+chr(0xBB)],

#067e - 0xC1 - 0xC2 : peh
u'\u067e' : [2, chr(0xC1), chr(0xC2)],
#0686 - 0xC9 - 0xCA : cheh
u'\u0686' : [2, chr(0xC9), chr(0xCA)],
#0698 - 0xD3 : jeh
u'\u0698' : [1, chr(0xD3)],
#06a9 - 0xEC - 0xED : farsi keh
u'\u06a9' : [2, chr(0xEC), chr(0xED)],
#06af - 0xEE - 0xEF : gaf
u'\u06af' : [2, chr(0xEE), chr(0xEF)],
#06cc - 0xFC - 0xFD - 0xFE : farsi yeh
u'\u06cc' : [3, chr(0xFC), chr(0xFE), chr(0xFD)],

#arabic-indic digits
u'\u06F0' : [1, chr(0xB0)],
u'\u06F1' : [1, chr(0xB1)],
u'\u06F2' : [1, chr(0xB2)],
u'\u06F3' : [1, chr(0xB3)],
u'\u06F4' : [1, chr(0xB4)],
u'\u06F5' : [1, chr(0xB5)],
u'\u06F6' : [1, chr(0xB6)],
u'\u06F7' : [1, chr(0xB7)],
u'\u06F8' : [1, chr(0xB8)],
u'\u06F9' : [1, chr(0xB9)],

#arabic digits
u'\u0660' : [1, chr(0xB0)],
u'\u0661' : [1, chr(0xB1)],
u'\u0662' : [1, chr(0xB2)],
u'\u0663' : [1, chr(0xB3)],
u'\u0664' : [1, '\\arabfour'],
u'\u0665' : [1, '\\arabfive'],
u'\u0666' : [1, '\\arabsix'],
u'\u0667' : [1, chr(0xB7)],
u'\u0668' : [1, chr(0xB8)],
u'\u0669' : [1, chr(0xB9)],

#0644_#0627 - 0xF1  : lam+alef
u'\u0600' : [1, chr(0xF1)]
}

def is_right_joinable(c):
	if (c in bidi_joiners) or (c in right_joiners):
		return 1
	return 0

def is_left_joinable(c):
	if (c in bidi_joiners):
		return 1
	return 0

def is_nonend_vowel(vowel):
	if (vowel >= u'\u064e') and (vowel <= u'\u0656'):
		return 1
	if (vowel == u'\u0670'):
		return 1
	return 0	

def is_vowel(vowel):
	if (vowel >= u'\u064b') and (vowel <= u'\u0656'):
		return 1
	if (vowel == u'\u0670'):
		return 1
	return 0	

def is_six_vowel(vowel):
	if (vowel >= u'\u064b') and (vowel <= u'\u0650'):
		return 1
	return 0	


def is_right_joinable_v(line, i):
	if (i>0) and (is_right_joinable(line[i])):
		j = i-1
		if is_vowel(line[j]):
			while ((j>=0) and (is_vowel(line[j]) == 1)):
				j -= 1
		if (j == -1) or not(is_left_joinable(line[j])):
			return 0
		return 1
	return 0

def is_left_joinable_v(line, i):
	line_len = len (line)
	if (line_len>0) and (i<line_len-1) and (is_left_joinable(line[i])):
		j = i+1
		if is_vowel(line[j]):
			while ((j<line_len) and (is_vowel(line[j]) == 1)):
				j += 1
		if (j == line_len) or not(is_right_joinable(line[j])):
			return 0
		return 1
	return 0

#isolated 0, final 1, medial 2, initial 3
def find_form(line, i):	
	j_r = is_right_joinable_v(line, i)
	j_l = is_left_joinable_v(line, i)

	if (j_r == 0) and (j_l == 0):
		return 0
	if (j_r == 1) and (j_l == 0):
		return 1
	if (j_r == 1) and (j_l == 1):
		return 2
	# Therefore (j_r == 0) and (j_l == 1):
	return 3

def map_char_unicode_DK(c, form):
	try:
		n = table_UN_DK[c][0]
        except KeyError:
		return c.encode('latin-1')
	if (n == 1):
		return table_UN_DK[c][1]
	elif (n == 2):
		if (c in right_joiners):
			return table_UN_DK[c][1 + form]
		else:
			return table_UN_DK[c][1 + form/2]
	elif (n == 4):
		return table_UN_DK[c][1 + form]
	# farsi yeh (farsi or arabic or +hamza)
	if (c == u'\u06cc') or (c == u'\u0626') or (c == u'\u064a'):
		if (form >= 2):
			return table_UN_DK[c][3]
		return table_UN_DK[c][1 + form]
	elif (c == u'\u0647'): # heh
		if (form < 2):
			return table_UN_DK[c][1]
		return table_UN_DK[c][form]
	return c

def is_english_letter_number(c):
	if ((c >= u'a') and (c <= u'z')) or ((c >= u'A') and (c <= u'Z')):
		return 1
	if (c >= u'0') and (c <= u'9'):
		return 1
	return 0

def is_farsi_numerical(c):
	if ((c >= u'\u06F0') and (c <= u'\u06F9')) or (c == u'\u066b') or (c == u'\u066c'):
		return 1
	return 0

# Main body of the program 
if len(sys.argv) <= 2:
	print 'usage: python unldk in_filename out_filename'
	exit(0)

filename = sys.argv[1]
outfile = sys.argv[2]

try:
	f = codecs.open(filename, 'r', 'utf-8')
except IOError:
	print "Can not open the input file: " + filename
	exit(0)

try:
	of = open(outfile, 'w')
except IOError:
	print "Can not open the output file: " + outfile
	exit(0)

inFarsi = 0
inFarsiNumber = 0
for line in f:
	this_line = ''
	line_len = len (line)

	# to remove the Byte Order Mark = BOM
	start = 0
	if line[0] == unicode( codecs.BOM_UTF8, "utf8"):
		start = 1
	# end of BOM removal

	i = start
	farsi_part = ''
	while i < line_len:
		# find the \$f_ or \$e_
		if line[i] == u'\\':
			if line[i+1:i+4] == "$f_":
				inFarsi = 1
				i += 4
			elif line[i+1:i+4] == "$e_":
				if (inFarsiNumber == 1):
					farsi_part += number_part[::-1]
					number_part = ''
					inFarsiNubmer = 0
				this_line += farsi_part[::-1]
				fasi_part = ''
				inFarsi = 0
				i += 4
			# end of character processing
		if inFarsi == 0:
			this_line += line[i].encode('ascii')
		else:
			if (is_farsi_numerical(line[i]) == 1):
				inFarsiNumber = 1
				number_part += map_char_unicode_DK(line[i], 0)
			else:
				if (inFarsiNumber == 1):
					farsi_part += number_part[::-1]
					number_part = ''
					inFarsiNubmer = 0
				which_form = find_form(line, i)
				if (i+1 < line_len) and (line[i] == u'\u0644') and (line[i+1] == u'\u0627'):
					which_form = 1
					farsi_part += map_char_unicode_DK(u'\u0600', which_form)
					i = i + 1
				else:
					farsi_part += map_char_unicode_DK(line[i], which_form)
		i += 1
	# end of while	
	if inFarsi == 1:
		this_line += farsi_part[::-1]
		farsi_part = ''
		
	# write the processed line
	of.write(this_line)
	# end of line processing
# end of file processing

of.close()
f.close()
