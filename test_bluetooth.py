import asyncio
from services.bluetooth_service import BluetoothService

async def main():
    bt = BluetoothService()

    devices = await bt.scan_devices()

    print("\nNearby Bluetooth Devices:\n")

    for device in devices:
        print(f"{device.name} - {device.address}")

asyncio.run(main())