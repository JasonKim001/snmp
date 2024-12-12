import asyncio
from pysnmp.entity.engine import SnmpEngine
from pysnmp.hlapi.v3arch import get_cmd, CommunityData, UdpTransportTarget, ContextData
from pysnmp.smi.rfc1902 import ObjectType, ObjectIdentity


async def run(target_ip, community_string, oid_to_get):
    errorIndication, errorStatus, errorIndex, varBinds = await get_cmd(
        # snmpwalk -v2c -c 'Jxqxsnmp!read001' 134.255.255.107 SNMPv2-MIB::sysDescr.0
        SnmpEngine(),
        CommunityData(community_string),
        await UdpTransportTarget.create((target_ip, 161)),
        ContextData(),
        ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0))
    )
    if errorIndication is not None:
        print(errorIndication)
    elif errorStatus != 0:
        print(errorStatus)
    elif errorIndex != 0:
        print(errorIndex)
    else:
        print("varBinds: ", varBinds)

def main():
    """主程序，调用 snmp_get 进行测试"""
    # 示例使用
    target_ip = "192.168.186.128"  # 替换为你的设备的IP地址
    community_string = "public"  # 替换为你的设备的社区字符串
    oid_to_get = "1.3.6.1.2.1.1.1.0"  # 替换为你想查询的OID

    # 运行 SNMP GET 操作
    asyncio.run(run(target_ip, community_string, oid_to_get))

if __name__ == '__main__':
    main()