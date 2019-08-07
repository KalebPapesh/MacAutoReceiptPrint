#!/bin/bash

# filter files remove
rm -v /usr/libexec/cups/filter/rastertostar
rm -v /usr/libexec/cups/filter/rastertostarlm

# PPD files remove
rm -v /usr/share/cups/model/StarMicronics/*
rmdir /usr/share/cups/model/StarMicronics
rm -v /usr/share/cups/model/C/tsp*.ppd.gz
rm -v /usr/share/cups/model/C/sp*.ppd.gz
rmdir /usr/share/cups/model/C
rm -v /Library/Printers/PPDs/Contents/Resources/fvp*.ppd.gz
rm -v /Library/Printers/PPDs/Contents/Resources/hsp*.ppd.gz
rm -v /Library/Printers/PPDs/Contents/Resources/tsp*.ppd.gz
rm -v /Library/Printers/PPDs/Contents/Resources/sp*.ppd.gz
rm -v /Library/Printers/PPDs/Contents/Resources/tup*.ppd.gz

# Delete pkg
rm -frv /Library/Receipts/starcupsdrv-*.*.*.pkg
rm -frv /var/db/receipts/com.starmicronics.starcupsdrv.bom
rm -frv /var/db/receipts/com.starmicronics.starcupsdrv.plist
