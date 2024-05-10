import subprocess

myStr="Hello brother this is me."

with open('./MyText.txt','w+') as F:
    F.write(myStr)

subprocess.Popen(["code.exe",myStr])