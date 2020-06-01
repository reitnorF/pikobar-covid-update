import json
with open('data.json') as f:
	data = json.load(f)

count = 0
odp = 0
pdp = 0
positif = 0
kelurahan = ""
anak= 0
remaja=0
dtp=0
elp=0
tua=0

for k in data['data']['content']:
	if k['nama_kel'] == 'Tridaya Sakti':
		kelurahan = k['nama_kel']
		print str(k['status']) +" "+ str(k['gender'])+ " " + str(k['umur']) 
		count = count + 1
		if k['status'] == 'ODP':
			odp = odp + 1
		elif k['status'] == 'PDP':
			pdp = pdp + 1
		elif k['status'] == 'Positif':
			positif = positif + 1
		if (k['umur'] <= 10) and (k['umur'] >=1):
			anak = anak+1
		elif k['umur'] <= 18:
			remaja = remaja+1
		elif k['umur'] <= 39:
			dtp = dtp+1
		elif k['umur'] <= 59:
			elp = elp+1
		else:
			tua = tua+1


print kelurahan
print "Suspect " + str(count)
print "ODP " + str(odp)
print "PDP " + str(pdp)
print "Positif" + str(positif)
print ""
print "Anak-Anak " + str(anak)
print "Remaja " + str(remaja)
print "Dewasa Muda (19-39) " + str(dtp)
print "Dewasa (40-59) " + str(elp)
print "Tua (60++)" + str(tua) 