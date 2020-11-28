import time
import sketch

last_refresh_time = 0
min_refresh_time = 10
display_loop_index = 1 #How often has been the display been updated

def refreshCheck(time_elapsed):
    return (time_elapsed > min_refresh_time)

def update_io():
    sketch.hardware_loop()

def update_display():
    global display_loop_index, last_refresh_time, display_updates_enabled
    #print("update")

    #print("updates enabled?: ", display_updates_enabled)
    if (display_updates_enabled == True):
        current_time = time.monotonic()
        if refreshCheck(delta):
            sketch.display_loop()
            print(current_time,"---- epaper refresh loop! ---- ", display_loop_index)
            display.show(group)
            # Refresh the screen
            last_refresh_time = current_time
            display_loop_index = display_loop_index + 1

            display.refresh()

sketch.setup()
while True:
    update_io()
    update_display()
