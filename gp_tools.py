#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 ************************************************
 *  Progrma de apoio gopro                       *
 *  Autor: Marcos Oliveira                      *
 *  Versao: 0.1                                 *
 *                                              *
 *                                              *
 ************************************************

 Uso: Python gp_tools.py gopro_sd_dir destino_dir

      onde:
        gogro_sd_dir = diretório do sdcard onde estao os vídeos
        detino_dir = diretório onde os vídeos vão ser arquivados

"""

import os, sys, subprocess, datetime


def executar_comando(comando):
   proc = subprocess.Popen(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
   rel, erro = proc.communicate()
   if rel:
       print "%s executado com sucesso" % comando
   else:
       if erro:
           print erro

def listar_arquivos(gopro_sdcard_dir):
    return [f for f in os.listdir(gopro_sdcard_dir) if f[-3:] == 'MP4']

def copia_arquivo(arquivo, destino):
    comando = "cp %s %s" % (arquivo, destino)
    executar_comando(comando)

def criar_diretorio(diretorio):
    comando = "mkdir -p %s" % diretorio
    executar_comando(comando)

def calcular_md5(caminho_arquivo, nome_arquivo):
    comando = "md5sum %s/%s | cut -d" " -f1" % (caminho_arquivo, nome_arquivo)
    executar_comando(comando)

def remover(caminho_arquivo, nome_arquivo):
    comando = "rm %s/%s" % (caminho_arquivo, nome_arquivo)
    executar_comando(comando)

if __name__ == '__main__':
    try:
        lista_arquivos = listar_arquivos(sys.argv[1])
        destino = sys.argv[2] + str(datetime.datetime.now().year) + '-' + "%02d" %(datetime.datetime.now().month) + '-' + "%02d" % (datetime.datetime.now().day)
        #print destino
        criar_diretorio(destino)
        for f in lista_arquivos:
            copia_arquivo(sys.argv[1] + f, destino)
            if calcular_md5(sys.argv[1], f) == calcular_md5(destino, f):
                remover(sys.argv[1], f)
    except IndexError:
        print (__doc__)
    except:
        #print "Erro inesperado: "
        raise
