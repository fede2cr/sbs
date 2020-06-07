#!/usr/bin/env python3

"""
# Slackware Build System
# https://github.com/fede2cr/sbs

# Usage:
# $ sbs q a/bash

# This will queue the SlackBuild script "bash" from series "a", to be executed
# Logs from this building process will be recorded


# Cuando se agrega paquete a la cola, se ejecuta build en background

# Build revisa si no hay builds en ejecución,
# y sino le hace un pop a lo que esté en la bd
# Build solo termina cuando hay a que hacerle pop

TODO: I hate locks in tools like apt. But version 0 will be uni-host
TODO: Build in background as default. The cli would just print how many are
      in queue
TODO: We are using read() for now, but we need to accept package name
      over args
TODO: Source managment! Import from -current, upload changes, etc 
TODO: Integrate distcc into buildvm, for cluster compilation
"""

import slackware_build_system as sbs

print("Digite el nombre del paquete: ", end="")
build_package = input()
print("Digite la serie: ", end="")
input_series = input()
if input_series.lower() not in sbs.series:
    print("Serie incorrecta")

sbs.build()
