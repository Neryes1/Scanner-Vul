''' 
  Projeto de TCC com o objetivo de escanear a rede interna onde contém todos 
  os dispositivos inteligentes. Essa análise vai jogar na tela os hosts, fabricantes
  do MAC e os serviços rodando.
'''

__author__ = "Bruno Nery"
__copyright__ = "Copyright 2020, by Bruno"
__credits__ = "Todos desenvolvedores de software livre"
__license__ = "GNU General Public License"
__version__ = "1.0.0"
__maintainer__ = "Bruno Nery"
__email__ = "brunery@gmail.com"
__status__ = "Prototype"

#importando a biblioteca nmap
import nmap

'''
  criando objeto n que receberá o método PortScanner da 
  biblioteca nmap
'''
n = nmap.PortScanner()

#função para resgatar os valores dentro do tcp   
#def extract_names_from(tcp):
 # for val in tcp.values():
 #   print('Serviço: ', val["name"])

'''
  o método scan passa 3 parâmentros
  localhost = ip da rede
  arguments: -n = para não resolver DNS e -PU = descoberta de host
  sudo = pedir permissão
'''
n.scan('192.168.1.0/24', arguments='-n -PU -sn', sudo=True)

def extract_names_from(tcp):
    for h in tcp.values():
        print(h['name'])
        print(h['vendor'])

for host in n.all_hosts():
    if 'host':
      print(' ')    
      print('IP : %s (%s)' % (host, n[host].hostname()))
      extract_names_from(n[host]["values"])  
