import asyncio
from bleak import BleakScanner


class BluetoothService:

    def __init__(self):
        self.phone_name = "Pratham's A16"

    async def scan_devices(self):

        devices = await BleakScanner.discover(timeout=5)

        return devices

    async def phone_nearby(self):

        devices = await self.scan_devices()

        for device in devices:

            if self.phone_name and device.name == self.phone_name:
                return True

        return False