import usbtmc

print("Imports completed. Connecting to scope...")
oscope = usbtmc.usb_instrument()
print("Scope Connected")
    if(googleAudio == 'run'): oscope.write("RUN")
    if(googleAudio == 'stop'): oscope.write("STOP")

