import os
import pdb

yearnames = os.listdir('dirs')

for yearname in yearnames:
	os.chdir('/home/zeng/Desktop/site_code/dirs/%s'%yearname)
	os.system('git init')
	os.system('git add *')
	os.system('git commit -m \'first\'')
	os.system('git remote add origin https://github.com/huchuanlu/%s.git'%yearname)
	os.system('git remote set-url origin git@github.com:huchuanlu/%s.git'%yearname)
	os.system('git push -u origin master')

