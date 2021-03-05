from PIL import Image
from PIL import ImageChops
from PIL import ImageStat
from stat import S_ISREG, ST_CTIME, ST_MODE
import os, sys, time

# precision du pourcentage
precision = 5
# dossier stockage de photos
dir_path = r'C:\\Users\\rberm\\Desktop\\detection des personnes\\photos'



print("Reading folder...")
# triage des photos par ordre chronologique listdir sort la liste et stat[ST_tIME] sort le temps
data = (os.path.join(dir_path, fn) for fn in os.listdir(dir_path))
data = ((os.stat(path), path) for path in data)
data = ((stat[ST_CTIME], path)
           for stat, path in data if S_ISREG(stat[ST_MODE]))

# init de la variable contenant la premiere pohto
im1 = ""
i = 0
print("Processing images...")
# boucle sur les photos par ordre de temps
for cdate, filename in sorted(data):
    # type MIME
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # si i=0 ou pas d'image 1 on crée l'image im1
    	if not im1 and i==0:
    		im1 = Image.open(os.path.join(dir_path, filename))
    		im1name = os.path.join(dir_path, filename)
    	else:
            # recup de la deuxieme image
    		im2 = Image.open(os.path.join(dir_path, filename))
    		im2name = os.path.join(dir_path, filename)
    		print("Analyzing ", im2name)
            # recherche des differences 
    		diff = ImageChops.difference(im2, im1)
    		stat = ImageStat.Stat(diff)
            # calcul du ratio
    		diff_ratio = sum(stat.mean) / (len(stat.mean) * 255)
    		if (diff_ratio * 100 )>precision:
    			print("Un changement a été détecté : ", diff_ratio * 100)
    			print(im1name)
    			print(im2name)
    			# definition de la difference
    			im5 = ImageChops.subtract(im1, im2, scale=1.0, offset=0)
    			os.startfile(im1name)
    			os.startfile(im2name)
    			time.sleep(1) # wait for creation
    			im5.show()
    		im1 = im2
    		im1name = im2name
    else:
        continue