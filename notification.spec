# -*- mode: python -*-
a = Analysis(['notification.py'],
             pathex=['C:\\Users\\Luca\\PycharmProjects\\untitled'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
for d in a.datas:
    if 'pyconfig' in d[0]:
        a.datas.remove(d)
        break
pyz = PYZ(a.pure)
exe = EXE(pyz,
          Tree('data', prefix='data'),
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='notification.exe',
          debug=False,
          strip=None,
          upx=True,
          console=False , icon='data\\gmail_0.ico')
