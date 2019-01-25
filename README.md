# ESPBlocks

Devepoled by Marek Mansell in Python


# old install

```bash
#!/bin/bash

usermod -G dialout -a tabor
cd /usr/local/lib
apt-get install python3-tk
apt-get install python3-pil.imagetk
sudo pip3 install pyqt5
sudo apt-get install python3-pyqt5.qtwebkit
wget kempelen.ii.fmph.uniba.sk/p.zip
mv python3.5 py
unzip p.zip
rm p.zip
mv blockly-master.zip /home/tabor/Desktop
cd /home/tabor/Desktop
unzip blockly-master.zip
chown tabor:tabor blockly-master
rm blockly-master.zip
```

#now install 

```bash
git clone https://github.com/junhuanchen/ESPBlocks
cd ESPBlocks/
sudo apt-get install python3-tk
sudo apt-get install python3-pil.imagetk  
sudo apt-get install python3-pil=3.1.2-0ubuntu1.1
sudo apt-get install python3-pil python3-pil.imagetk
sudo apt-get install python-imaging python-imaging-tk
sudo apt-get install libqt5core5a=5.5.1+dfsg-16ubuntu7
sudo apt-get install python3-pyqt5=5.5.1+dfsg-3ubuntu4
sudo pip3 install pygments
sudo apt-get install python3-pyqt5.qtwebkit
python3 editor.py

```
