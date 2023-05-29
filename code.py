import asyncio
import board
import busio
import time

from ezo_sensors import Ezo

# instantiate the objects
humidity = Ezo(0x6F, "hum", False)
res = Ezo(0x66, "tmp", False)
ph = Ezo(0x63, "ph", False)

async def monitor_uart():
    while True:
        data = uart.read(32)  # read up to 32 bytes

        if data is not None:
            # convert bytearray to string
            data_string = ''.join([chr(b) for b in data])
            print(data_string, end="")

        # allow other tasks to do work
        await asyncio.sleep(0)

# main coroutine
async def main():  # Don't forget the async!
    # create sensor tasks
    res_temp_task = asyncio.create_task(
        res.cmd_r()
    )
    hum_task = asyncio.create_task(
        humidity.cmd_r()
    )
    ph_task = asyncio.create_task(
        ph.cmd_r()
    )
    
    # start all of the tasks
    await asyncio.gather(
        res_temp_task, hum_task, ph_task
    )  # Don't forget the await!

# start the main coroutine
asyncio.run(main())
