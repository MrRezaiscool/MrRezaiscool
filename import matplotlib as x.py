import matplotlib.pyplot as x
import numpy 
img=x.imread("download_1_11zon.bmp")
a=x.imread("y1udzivcql471.png")
b=x.imread("Screenshot 2023-12-06 174842.jpg")
####c=x.imread("38811b9b-3609-4991-9823-e217d8ef5415_4_11zon.bmp")
####g=a[1:1:1]=0
#####print(g)
aks=img.copy()
aks[1,1,1]=0
print(type(aks))