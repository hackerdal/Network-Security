@hackerdal
#a simple ping scan script

import subprocess

pclist = ["pc1","pc2","pc3",...]#type your pc list here

for i in pclist:
  print("--------------------------------------------------------------------------")
  print(i)
  subprocess.run(["ping",i])
  #ping the computers in your list automatically and show the result
