import asyncio

async def brew_coffee():
    print("brew coffee")
    await asyncio.sleep(2)
    print("Coffee is ready")

asyncio.run(brew_coffee())