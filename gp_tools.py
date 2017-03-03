#!/usr/bin/env python
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
        gogro_sd_dir = diretoro do sdcard onde estao os videos
        detino_dir = diretorio onde os videos vao ser arquivados

"""

import os, sys

try:
  gopro_sdcard_dir = sys.argv[1]
  destino_dir = sys.argv[2]
  lista_arquivos = [f for f in os.listdir(gopro_sdcard_dir) if f[-3:] == 'MP4']
  print lista_arquivos
except IndexError:
  print (__doc__)
except:
  #print "Erro inesperado: "
  raise
