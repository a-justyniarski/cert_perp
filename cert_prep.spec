# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


cert_a = Analysis(
    ['main\\cert.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

core_a = Analysis(
    ['main\\core.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

excel_read_a = Analysis(
    ['main\\excel_read.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

MERGE( (cert_a, 'cert', 'cert'), (core_a, 'core', 'core'), (excel_read_a, 'excel_read', 'excel_read') )

core_pyz = PYZ(core_a.pure, core_a.zipped_data, cipher=block_cipher)
core_exe = EXE(
    core_pyz,
    core_a.scripts,
    core_a.binaries,
    core_a.zipfiles,
    core_a.datas,
    [],
    name='core',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

excel_read_pyz = PYZ(excel_read_a.pure, excel_read_a.zipped_data, cipher=block_cipher)

excel_read_exe = EXE(
    excel_read_pyz,
    excel_read_a.scripts,
    excel_read_a.binaries,
    excel_read_a.zipfiles,
    excel_read_a.datas,
    [],
    name='excel_read',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

cert_pyz = PYZ(cert_a.pure, cert_a.zipped_data, cipher=block_cipher)

cert_exe = EXE(
    cert_pyz,
    cert_a.scripts,
    [],
    exclude_binaries=True,
    name='cert',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
cert_coll = COLLECT(
    cert_exe,
    cert_a.binaries,
    cert_a.zipfiles,
    cert_a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='cert',
)
