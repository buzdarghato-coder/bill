# Runs after "npx cap add android": launcher icons + dark theme colors
import os
from PIL import Image, ImageDraw
R='android/app/src/main/res'
src=Image.open('logo.jpg').convert('RGB')
fg=Image.open('icon-fg.png')
for d,(s,f) in {'mdpi':(48,108),'hdpi':(72,162),'xhdpi':(96,216),'xxhdpi':(144,324),'xxxhdpi':(192,432)}.items():
    p=f'{R}/mipmap-{d}'
    sq=src.resize((s,s),Image.LANCZOS)
    m=Image.new('L',(s*4,s*4),0);ImageDraw.Draw(m).rounded_rectangle((0,0,s*4-1,s*4-1),radius=s*4//5,fill=255);m=m.resize((s,s),Image.LANCZOS)
    a=sq.convert('RGBA');a.putalpha(m);a.save(p+'/ic_launcher.png')
    m2=Image.new('L',(s*4,s*4),0);ImageDraw.Draw(m2).ellipse((0,0,s*4-1,s*4-1),fill=255);m2=m2.resize((s,s),Image.LANCZOS)
    b=sq.convert('RGBA');b.putalpha(m2);b.save(p+'/ic_launcher_round.png')
    fg.resize((f,f),Image.LANCZOS).save(p+'/ic_launcher_foreground.png')
p=R+'/values/ic_launcher_background.xml'
open(p,'w').write(open(p).read().replace('#FFFFFF','#111217'))
p=R+'/values/styles.xml'
s=open(p).read()
s=s.replace('<item name="android:background">@null</item>\n    </style>','<item name="android:background">@null</item>\n        <item name="android:statusBarColor">#05060A</item>\n        <item name="android:navigationBarColor">#05060A</item>\n        <item name="android:windowBackground">#0B0D14</item>\n    </style>',1)
open(p,'w').write(s)
print('prepare done')
