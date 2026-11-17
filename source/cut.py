import cv2, numpy as np
from PIL import Image
src=cv2.imread('photo.jpg')
X0,Y0,X1,Y1=100,430,960,1600
img=src[Y0:Y1,X0:X1].copy(); H,W=img.shape[:2]
P=[(445,468),(520,446),(600,460),(648,515),(655,590),(645,612),(628,650),(626,740),(660,760),(715,735),(758,825),(835,835),(868,885),(890,940),(903,1010),(906,1090),(900,1230),(880,1350),(868,1450),(862,1600),
(240,1600),(240,1490),(256,1400),(235,1330),(200,1260),(175,1190),(156,1130),(143,1090),(150,1000),(190,900),(245,830),(350,800),(430,720),(437,650),(420,610),(392,590),(390,540)]
poly=np.array([(x-X0,y-Y0) for x,y in P],np.int32)
m=np.zeros((H,W),np.uint8); cv2.fillPoly(m,[poly],255)
k=lambda r:cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(2*r+1,2*r+1))
sure=cv2.erode(m,k(22)); outer=cv2.dilate(m,k(22))
gc=np.full((H,W),cv2.GC_BGD,np.uint8)
gc[outer>0]=cv2.GC_PR_BGD; gc[m>0]=cv2.GC_PR_FGD; gc[sure>0]=cv2.GC_FGD
bg=np.zeros((1,65));fg=np.zeros((1,65))
cv2.grabCut(img,gc,None,bg,fg,6,cv2.GC_INIT_WITH_MASK)
a=np.where((gc==1)|(gc==3),255,0).astype(np.uint8)
a=cv2.morphologyEx(a,cv2.MORPH_OPEN,k(2)); a=cv2.morphologyEx(a,cv2.MORPH_CLOSE,k(4))
n,lab,st,_=cv2.connectedComponentsWithStats(a); a=np.where(lab==1+np.argmax(st[1:,4]),255,0).astype(np.uint8)
d9=cv2.dilate(m,k(9));d1=cv2.erode(m,k(4));d9[1150-Y0:,:]=np.maximum(d1[1150-Y0:,:],0);a=cv2.bitwise_and(a,d9);g=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY);z=np.zeros((H,W),bool);z[1140-Y0:1460-Y0,:340-X0]=True;a[z&(g>70)]=0;a=cv2.morphologyEx(a,cv2.MORPH_OPEN,k(5));n,lab,st,_=cv2.connectedComponentsWithStats(a);a=np.where(lab==1+np.argmax(st[1:,4]),255,0).astype(np.uint8);a=cv2.erode(a,k(1));a=cv2.GaussianBlur(a,(0,0),1.2)
# inpaint the vest patch text
pm=np.zeros((H,W),np.uint8); cv2.rectangle(pm,(605-X0,1112-Y0),(698-X0,1152-Y0),255,-1)
img=cv2.inpaint(img,pm,5,cv2.INPAINT_TELEA)
# stylise: smooth + detail, blend
sm=cv2.edgePreservingFilter(img,flags=1,sigma_s=35,sigma_r=0.28)
img=cv2.addWeighted(img,0.55,sm,0.45,0)
img=cv2.detailEnhance(img,sigma_s=8,sigma_r=0.12)
# maroon coat -> black
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV).astype(np.float32)
h,s,v=hsv[...,0],hsv[...,1],hsv[...,2]
mk=(((h>=160)|(h<=4))&(s>55)&(v<170)).astype(np.float32)
mk=cv2.GaussianBlur(mk,(0,0),2)
hsv[...,1]=s*(1-0.85*mk); hsv[...,2]=v*(1-0.55*mk)
img=cv2.cvtColor(np.clip(hsv,0,255).astype(np.uint8),cv2.COLOR_HSV2BGR).astype(np.float32)
# gold rim light from upper right
af=a.astype(np.float32)/255; bl=cv2.GaussianBlur(af,(0,0),3)
gx=cv2.Sobel(bl,cv2.CV_32F,1,0); gy=cv2.Sobel(bl,cv2.CV_32F,0,1); mag=np.sqrt(gx**2+gy**2)+1e-6
nx,ny=-gx/mag,-gy/mag; w=np.clip(nx*0.75+ny*-0.66,0,1)*0.9+0.22
band=np.clip(af-cv2.GaussianBlur(cv2.erode(a,k(4)).astype(np.float32)/255,(0,0),2),0,1)
rim=np.clip(band*w*1.6,0,1)[...,None]
gold=np.array([0,199,255],np.float32)
img=img*(1-rim)+gold*rim*1.0+img*rim*0.25
# warm grade
img=np.clip(img*np.array([0.92,0.98,1.05]),0,255)
rgba=np.dstack([img.astype(np.uint8),a])
Image.fromarray(cv2.cvtColor(rgba,cv2.COLOR_BGRA2RGBA)).save('cut_full.png')
bgc=np.full((H,W,3),90,np.uint8); comp=(img*af[...,None]+bgc*(1-af[...,None])).astype(np.uint8)
cv2.imwrite('prev.jpg',cv2.resize(comp,(W//2,H//2)))
print(W,H)

from PIL import Image as I
def fade(im,px):
    arr=np.array(im); h=arr.shape[0]; ramp=np.clip((h-1-np.arange(h))/px,0,1)[:,None]
    arr[...,3]=(arr[...,3]*ramp).astype(np.uint8); return I.fromarray(arr)
full=I.open('cut_full.png')
# id.png: chest-up (orig y440-1290 -> crop 10-860)
idc=full.crop((20,10,840,870)); idc=idc.resize((idc.width*2,idc.height*2),I.LANCZOS); idc=fade(idc,260)
idc.save('../assets/id.png',optimize=True)
idc.resize((idc.width*45//100,idc.height*45//100),I.LANCZOS).save('id_embed.png',optimize=True)
# right_pointing.png: waist-up on LEFT, empty right
wc=full.crop((20,10,840,1130)); wc=fade(wc,200)
can=I.new('RGBA',(1230,1120),(0,0,0,0)); can.paste(wc,(0,0),wc)
can=can.resize((can.width*14//10,can.height*14//10),I.LANCZOS)
can.save('../assets/right_pointing.png',optimize=True)
can.resize((can.width*45//100,can.height*45//100),I.LANCZOS).save('rp_embed.png',optimize=True)
print(idc.size,can.size)
