# -*- mode: python -*-

block_cipher = None


a = Analysis(['G:\\Guru_Sarath\\Study\\Python\\Automation\\MoveFiles\\MoveFiles.py'],
             pathex=['G:\\Guru_Sarath\\Study\\Python\\Automation\\MoveFiles'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='MoveFiles',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True , icon='G:\\Guru_Sarath\\Study\\Python\\Automation\\icons\\Window.ico')
