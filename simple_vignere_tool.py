#!/usr/bin/python

import math
import re
import sys

spaces = re.compile("\s+")
kamus = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
class gcolor:
    OKGREEN = '\033[92m'
def encrypt ():
	a,b = 0,0
	cip = []
	pln = raw_input("Masukan plain text	: ")
	key = raw_input("Masukan key		: ")
	a_pln = list(pln)
	a_key = list(key)
	for i in range (len(a_pln)):
	
		if (a>=len(a_pln)):
			a=0
		if (b>=len(a_key)):
			b=0
		if (a_pln[a] != ' '):
			pln_n = kamus.index(a_pln[a].upper())
			key_n = kamus.index(a_key[b].upper())
			cip_n = pln_n+key_n
			if cip_n<=len(kamus):
				cip_n = cip_n
				cip.append(kamus[cip_n])
			else :
				cip_n = cip_n - len(kamus)
				cip.append(kamus[cip_n])
		else:
			cip.append(' ')
			b=b-1
		a+=1
		b+=1
	cip_j = ''.join(cip)
	print "============================================="
	print "Cipher Text nya adalah : "+cip_j

def decrypt ():
	pln = []
	cip = raw_input("Masukan cipher text	: ")
	key = raw_input("Masukan key		: ")
	a_cip = list(cip)
	a_key = list(key)
	a,b = 0,0	
	for i in range (len(a_cip)):
		if (a>=len(a_cip)):
			a=0
		if (b>=len(a_key)):
			b=0
		if (a_cip[a] != ' '):
			cip_n = kamus.index(a_cip[a].upper())
			key_n = kamus.index(a_key[b].upper())
			
			if key_n<=cip_n:
				pln_n = cip_n-key_n
				pln.append(kamus[pln_n])
			else :
				pln_n = (cip_n+len(kamus))-key_n
				pln.append(kamus[pln_n])
		else :
			pln.append(' ')
			b=b-1
		a+=1
		b+=1
	pln_j = ''.join(pln)
	print "============================================="
	print "Plain Text nya adalah : "+pln_j
		
def findkey ():
	cip = raw_input("Masukan cipher text	: ")
	pln = raw_input("Masukan plain text	: ")
	key = []
	cip = spaces.sub('',cip)
	pln = spaces.sub('',pln)
	a_cip = list(cip)
	a_pln = list(pln)
	
	for i in range (len(a_cip)):
		a=i
		b=i
		if(a>=len(a_cip)):
			a=0
		if(b>=len(a_pln)):
			b=0
		cip_n = kamus.index(a_cip[a].upper())
		pln_n = kamus.index(a_pln[b].upper())
		if (cip_n<pln_n) :
			kn = ((26-pln_n)+(cip_n))%26
		else :
			kn = abs(cip_n-pln_n)%26
		kamus[kn]
		key.append(kamus[kn])
	key_j = ''.join(key)
	print "============================================="
	print "KEY nya adalah : "+key_j
print gcolor.OKGREEN+"============================================="
print "= 	    Created by Tony Hendra	    ="
print "============================================="		
print "= 1. Encrypt Vignere Cipher		    ="
print "= 2. Decrypt Vignere Cipher		    ="
print "= 3. Find Key Vignere Cipher		    ="
print "============================================="
try:
	option = raw_input("Masukan pilihan : ")
	print "============================================="
	if option == '1':
		encrypt()
	elif option == '2':
		decrypt()
	elif option == '3':
		findkey()
	else:
		print "Pilih 1 atau 2"
except KeyboardInterrupt:
	print "\n"	
	sys.exit(0)
	
