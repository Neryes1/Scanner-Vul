#from mac_vendor_lookup import MacLookup

import nmap
n = nmap.PortScanner()

def extract_names_from(tcp):
  for val in tcp.values():
    print('Serviço: ', val["name"])

n.scan('192.168.1.0/24', arguments='-n -PU', sudo=True)
for host in n.all_hosts():
  print(' ')    
  print('IP : %s (%s)' % (host, n[host].hostname()))
  if 'mac' in n[host]['addresses']:
    print('Fabricante: {}'.format(" ".join(n[host]['vendor'].values())))
  extract_names_from(n[host]["tcp"])

   
        




# inserindo MAC na mão para conferir com o resultado de cima
'''
print('================') 

  print(MacLookup().lookup("CC:06:77:F3:DD:50"))
  print(MacLookup().lookup("DC:35:F1:42:85:33"))
  print(MacLookup().lookup("30:4B:07:8F:55:F1"))
  print(MacLookup().lookup("40:B0:76:1C:DE:CD"))
'''

