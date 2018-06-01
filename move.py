import os

filenames = os.listdir('dirs')

for filename in filenames:
	if filename.endswith('.rar') or filename.endswith('.zip'):
		os.system('mkdir dirs/%s'%filename[:-4])
		os.system('mv dirs/%s dirs/%s/'%(filename, filename[:-4]))

