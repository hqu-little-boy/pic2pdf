# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

py_files = [
            'pic2pdf_gui.py'
            'pic2pdf_merge.py'
            'pic2pdf_merge.py'
]

a = Analysis(['pic2pdf_gui.py'],
             pathex=['/home/zengwang/作品/pic2pdf'],
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
          name='pic2pdf',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )