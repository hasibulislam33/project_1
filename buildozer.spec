[app]
title = MyKivyApp
package.name = mykivyapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
source.exclude_dirs = bin
source.include_patterns = assets/*
source.exclude_patterns = license,images/*/*.xcf
source.main = main.py
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 1
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.arch = armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1