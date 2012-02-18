#!/usr/bin/env python
# -*- coding: utf-8 -*- 

'''
	The Spanish Metaphone Algorithm (Algoritmo del Metáfono para el Español)

	This script implements the Metaphone algorithm (c) 1990 by Lawrence Philips.
	It was inspired by the English double metaphone algorithm implementation by
	Andrew Collins - January 12, 2007 who claims no rights to this work 
	(http://www.atomodo.com/code/double-metaphone)
	 

	The metaphone port adapted to the Spanish Language is authored 
	by Alejandro Mosquera <amosquera@dlsi.ua.es> November, 2011 
	and is covered under this copyright:

	Copyright 2011, Alejandro Mosquera <amosquera@dlsi.ua.es>.  All rights reserved.

	Redistribution and use in source and binary forms, with or without modification,
	are permitted provided that the following conditions are met:
	  
	1. Redistributions of source code must retain the above copyright notice, this 
	list of conditions and the following disclaimer.
	2. Redistributions in binary form must reproduce the above copyright notice, this
	list of conditions and the following disclaimer in the documentation and/or
	other materials provided with the distribution.
	  
	  
	THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
	ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED 
	WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
	DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR 
	ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES 
	(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; 
	LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON 
	ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT 
	(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS 
	SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
'''

class PhoneticAlgorithmsES():

    
	@staticmethod
	def string_at(string, start, string_length, lista):

   		if ((start <0) or (start >= len(string))):
      			return 0
   		for expr in lista:
       			if string.find(expr, start, start + string_length) != -1:
           			return 1
   		return 0


	@staticmethod

	def substr(string, start, string_length):
    		v = string[start:start + string_length]
    		return v
  
	@staticmethod
	def is_vowel(string, pos):
    		return string[pos] in ['A','E','I','O','U'] 

	@staticmethod
    	def strtr(st):
		if st:
			st=st.replace('á','A')
                        st=st.replace('ch','X')
                        st=st.replace('ç','S')
			st=st.replace('é','E')
		  	st=st.replace('í','I')
			st=st.replace('ó','O')
			st=st.replace('ú','U')
			st=st.replace('ñ','NY')
			st=st.replace('gü','W')
			st=st.replace('ü','U')
			st=st.replace('b','V')
			#st=st.replace('z','S')
			st=st.replace('ll','Y') 
			return st
		else:
			return ''

	def __init__(self):
        	pass
        
	def metaphone(self, string) :
        
		#initialize metaphone key string
    		meta_key   = ""
   		#set maximum metaphone key size   
    		key_length   = 6
   		#set current position to the beginning
    		current_pos   =  0
   		#get string  length
   		string_length   = len(string);
	   	#set to  the end of the string
		end_of_string_pos     = string_length - 1
		original_string = string + "    "
	   	#Let's replace some spanish characters  easily confused
		original_string = self.strtr(original_string.lower())
	   	#convert string to uppercase
		original_string = original_string.upper()

		# main loop
		while (len(meta_key) < key_length):

			#break out of the loop if greater or equal than the length
			if (current_pos >= len(original_string)):
				break;
		      	#get character from the string
			current_char = original_string[current_pos]
		      
		      	#if it is a vowel, and it is at the begining of the string,
		      	#set it as part of the meta key        
			if (self.is_vowel(original_string,current_pos)  and (current_pos == 0)):
		      
				meta_key   += current_char
				current_pos += 1            
		    
		      	#Let's check for consonants  that have a single sound 
		      	#or already have been replaced  because they share the same
		      	#sound like 'B' for 'V' and 'S' for 'Z'
		 	else:
				if (self.string_at(original_string, current_pos, 1,['D','F','J','K','M','N','P','T','V','L','Y'])) :
		      			meta_key   += current_char
			 
				    #increment by two if a repeated letter is found
				    	if (self.substr(original_string, current_pos + 1,1) == current_char):         
				       		current_pos += 2       
				    	else: # increment only by one                 
				       		current_pos += 1            
		      
				else:  #check consonants with similar confusing sounds
					if current_char == 'C':  
                                                #special case 'macho', chato,etc.      
						#if (self.substr(original_string, current_pos + 1,1)== 'H'):                     
					  	#	current_pos += 2
					     
					       #special case 'acción', 'reacción',etc.      
						if (self.substr(original_string, current_pos + 1,1)== 'C'):
							meta_key   += 'X'          
							current_pos += 2
	  
					       # special case 'cesar', 'cien', 'cid', 'conciencia'
						elif (self.string_at(original_string, current_pos, 2,['CE','CI'])) :
							meta_key   += 'Z'
						  	current_pos += 2

						else:
							meta_key   += 'K';                   
							current_pos += 1;            
				       
				       
				 	elif current_char == 'G':
				       # special case 'gente', 'ecologia',etc 
						if (self.string_at(original_string, current_pos, 2,['GE','GI'])):
					 		meta_key   += 'J'            
					 		current_pos += 2
					  	else:
					 		meta_key   += 'G';                   
					 		current_pos += 1;            
				       
				  
				    #since the letter 'h' is silent in spanish, 
				    #let's set the meta key to the vowel after the letter 'h'
				 	elif current_char =='H':                
				      		if (self.is_vowel(original_string, current_pos + 1)):
					  		meta_key += original_string[current_pos + 1]
					  		current_pos += 2

				       		else:
							meta_key   += 'H'
							current_pos += 1            
				       
				       
				    	elif current_char == 'Q':
				       		if (self.substr(original_string, current_pos + 1,1) == 'U'):
					  		current_pos += 2
				       		else: 
				       
							current_pos += 1

				       		meta_key   += 'K'          
				       
				       
				    	elif current_char == 'W':
##                                                if (current_pos == 0):
##                                                        meta_key   += 'V'
##					  		current_pos += 2 
				       		meta_key   += 'U'            
				       		current_pos += 1
					
					# perro, arrebato, cara
					elif current_char == 'R':          
						current_pos += 1
				       		meta_key   += 'R'
				       		
				       	# spain 
					elif current_char == 'S':
                                                if (not self.is_vowel(original_string, current_pos + 1)) and (current_pos == 0):
					  		meta_key += 'ES'
					  		current_pos += 1
					  	else:
                                                        current_pos += 1
                                                        meta_key   += 'S' 

					# zapato
					elif current_char == 'Z':          
						current_pos += 1
				       		meta_key   += 'Z'         
				       
				       
				    	elif current_char == 'X': 
				       	#some mexican spanish words like'Xochimilco','xochitl'         
##				       		if (current_pos == 0):
##						           
##					  		meta_key   += 'S'
##					  		current_pos += 2 
##						    
##				       		else: 
						if (not self.is_vowel(original_string, current_pos + 1)) and len(string)>1 and (current_pos == 0):
                                                        meta_key += 'EX'
					  		current_pos += 1
					  	else:  
                                                        meta_key   += 'X'
                                                        current_pos += 1 
				       
				       
				    	else:
				       		current_pos += 1
				       
			 
		 #trim any blank characters
		meta_key = meta_key.strip()
		   
		 #return the final meta key string
		return meta_key;
       

if __name__ == '__main__' :
    
    pa = PhoneticAlgorithmsES()
    words = ['X','xplosion','escalera','scalera','mi','tu','su','te','ochooomiiiillllllll','complicado','ácaro','ácido','clown','down','col','clon','waterpolo','aquino','rebosar','rebozar','grajea','gragea','encima','enzima','alhamar','abollar','aboyar','huevo','webo','macho','xocolate','chocolate','axioma','abedul','a','gengibre','yema','wHISKY','google','xilófono','web','guerra','pingüino','si','ke','que','tu','gato','gitano','queso','paquete','cuco','perro','pero','arrebato','hola', 'zapato', 'españa', 'garrulo', 'expansión', 'membrillo', 'jamón','risa','caricia', 'llaves', 'paella','cerilla']
    for s in words:
        print s, ' -> ', pa.metaphone(s)
    
    
        
