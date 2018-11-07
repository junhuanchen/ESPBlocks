# -*- mode: python -*-

block_cipher = None


data_files = [("img", "img")]

a = Analysis(['editor.py'],
             pathex=['C:\\Users\\pi\\Documents\\GitHub\\ESPBlocks'],
             binaries=[],
             datas=data_files,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='editor',
          debug=False,
          strip=False,
          upx=True,
          console=False,
          icon="win_icon.ico" )
