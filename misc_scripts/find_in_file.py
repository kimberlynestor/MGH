
#import sys
#sys.exit()

path = '/autofs/cluster/oribivault/raw/I53_lh_32chexvivo_20190316/'

protocol = open(path+"protocol_20190316_I53.txt", 'r')
protocol2 = protocol.readlines()
#print(protocol2)

astpath = '/space/asterion/1/users/kn751/div_discorr/'
protocol_search = open(astpath+"protocol_search.csv", "w")

for i in protocol2:
    if "\\USER\INVESTIGATORS\Fischl" in i and "field_mapping" in i:
        protocol_search.write(i+"\n")
        #print(i)
    elif "GRE_4e_150um_FA" in i:
        protocol_search.write(i+"\n")

protocol.close()
