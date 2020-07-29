import optparse
import zipfile
from threading import Thread


def extractZip(zfile, password):
	try:
		zfile.extractall(pwd=password)
		print "[+] Password Found: "+ password + '\n'
	except:
		pass


def main():
	parser = optparse.OptionParser("usage %programe " + "-f <zipfile> -d <dictionary>")
	parser.add_option('-f', dest = 'zname', type='string', help='specify zip file')
	parser.add_option('-d', dest = 'dname', type='string', help='specify dictionary file')


	(options, arg) = parser.parse_args()

	if(options.zname == None) | (options.dname == None):
		print parser.usage
		exit()
	else:
		zname = options.zname
		dname = options.dname
	zFile = zipfile.ZipFile(zname)
	passFile = open(dname)

	for line in passFile.readlines():
		password = line.strip('\n')
		t = Thread(target=extractZip, args=(zFile, password))
		t.start()

if __name__ == '__main__':
	main()

