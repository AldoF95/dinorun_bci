import asyncio
from lib.cortex import Cortex, logger
import json


class met:
    pass


class pow:
    pass


class dev:
    pass


async def do_stuff(cortex):
    # await cortex.inspectApi()
    print("** USER LOGIN **")
    await cortex.get_user_login()
    print("** GET CORTEX INFO **")
    await cortex.get_cortex_info()
    print("** HAS ACCESS RIGHT **")
    await cortex.has_access_right()
    print("** REQUEST ACCESS **")
    await cortex.request_access()
    print("** AUTHORIZE **")
    await cortex.authorize(debit=100)
    print("** GET LICENSE INFO **")
    await cortex.get_license_info()
    print("** QUERY HEADSETS **")
    await cortex.query_headsets()
    logger.setLevel(20)
    if len(cortex.headsets) > 0:
        print("** CREATE SESSION **")
        await cortex.create_session(activate=True,
                                    headset_id=cortex.headsets[0])
        print("** CREATE RECORD **")
        await cortex.create_record(title="test record 1")
        print("** SUBSCRIBE POW & MET **")
        # await cortex.subscribe(['pow', 'met'])
        await cortex.subscribe(['met', 'fac'])
        while cortex.packet_count < True:
            data = await cortex.get_data()
            jj = json.loads(data)
            if 'pow' in jj:
                print(jj['pow'])
            elif 'fac' in jj:
                if 'blink' in jj['fac']:
                    print(jj['fac'])
        await cortex.close_session()


def serialize(dat):
    pass


def test():
    cortex = Cortex('cortex_creds')
    asyncio.run(do_stuff(cortex))
    cortex.close()


if __name__ == '__main__':
    test()
