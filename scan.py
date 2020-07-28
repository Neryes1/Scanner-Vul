''' 
  Projeto de TCC com o objetivo de escanear a rede interna onde contém todos 
  os dispositivos inteligentes. Essa análise vai jogar na tela os hosts, fabricantes
  do MAC e os serviços rodando.
'''

#importando a biblioteca nmap
import nmap

'''
  criando objeto n que reseberá o método PortScanner da 
  biblioteca nmap
'''
n = nmap.PortScanner()

#função para resgatar os valores dentro do tcp   
def extract_names_from(tcp):
  for val in tcp.values():
    print('Serviço: ', val["name"])

'''
  o método scan passa 3 parâmentros
  localhost = ip da rede
  arguments: -n = para não resolver DNS e -PU = descoberta de host
  sudo = pedir permissão
'''
n.scan('192.168.1.0/24', arguments='-n -PU', sudo=True)


for host in n.all_hosts():
  print(' ')    
  print('IP : %s (%s)' % (host, n[host].hostname()))
  if 'mac' in n[host]['addresses']:
    print('Fabricante: {}'.format(" ".join(n[host]['vendor'].values())))
  extract_names_from(n[host]["tcp"])

