import os
import pdb

yearnames = os.listdir('dirs')

for yearname in yearnames:
	extnames = os.listdir('dirs/%s'%yearname)
	for extname in extnames:
		if extname.endswith('.zip'):
			os.system('unzip -d dirs/%s dirs/%s/%s'%(yearname, yearname, extname))
			os.system('rm dirs/%s/%s'%(yearname, extname))
			hhnames = os.listdir('dirs/%s'%yearname)
			os.system('mv dirs/%s/%s/* dirs/%s/'%(yearname, hhnames[0], yearname))
			os.system('rm -rf dirs/%s/%s'%(yearname, hhnames[0]))
		if extname.endswith('.rar'):
			os.system('unrar x dirs/%s/%s dirs/%s/'%(yearname, extname, yearname))
			os.system('rm dirs/%s/%s'%(yearname, extname))
			hhnames = os.listdir('dirs/%s'%yearname)
			os.system('mv dirs/%s/%s/* dirs/%s/'%(yearname, hhnames[0], yearname))
			os.system('rm -rf dirs/%s/%s'%(yearname, hhnames[0]))
