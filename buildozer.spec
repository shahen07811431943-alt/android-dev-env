[app]
title = AndroidDevEnv
package.name = androiddevenv
package.domain = org.devenv

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,sh

version = 1.0
requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.archs = arm64-v8a
android.allow_backup = True
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE

[buildozer]
log_level = 2
warn_on_root = 1
