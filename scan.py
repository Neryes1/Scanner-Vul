from mac_vendor_lookup import MacLookup

import nmap
nm = nmap.PortScanner()


nm.scan('192.168.1.0/24', arguments='-PU', sudo=True)
for h in nm.all_hosts():
    if 'mac' in nm[h]['addresses']:
      print('Fabricante: {}'.format(" ".join(nm[h]['vendor'].values())))



# inserindo MAC na mão para conferir com o resultado de cima
'''
print('================') 

  print(MacLookup().lookup("CC:06:77:F3:DD:50"))
  print(MacLookup().lookup("DC:35:F1:42:85:33"))
  print(MacLookup().lookup("30:4B:07:8F:55:F1"))
  print(MacLookup().lookup("40:B0:76:1C:DE:CD"))
'''

