import subprocess

out = subprocess.check_output('wmic logicaldisk get  DriveType, caption', shell=True)

for drive in str(out).strip().split('\\r\\r\\n'):
	if '2' in drive:
		drive_litter = drive.split(':')[0]
		drive_type = drive.split(':')[1].strip()
		#print(drive_litter, drive_type)
		if drive_type == '2':
			print('Removable disk detected')
