import requests  # 导入requests库，用于发送HTTP请求
from bs4 import BeautifulSoup  # 导入BeautifulSoup库，用于解析HTML
from datetime import datetime, timezone  # 导入datetime库，用于处理日期和时间
import pytz  # 导入pytz库，用于处理时区
import jdatetime  # 导入jdatetime库，用于处理Jalali日期


newaddresses = [
   "https://t.me/s/Awlix_ir",
"https://t.me/s/beiten",
"https://t.me/s/beta_v2ray",
"https://t.me/s/CloudCityy",
"https://t.me/s/config_v2ray",
"https://t.me/s/Configforvpn01",
"https://t.me/s/ConfigsHubPlus",
"https://t.me/s/configV2rayForFree",
"https://t.me/s/configV2rayNG",
"https://t.me/s/custom_14",
"https://t.me/s/DailyV2RY",
"https://t.me/s/DigiV2ray",
"https://t.me/s/DirectVPN",
"https://t.me/s/Easy_Free_VPN",
"https://t.me/s/EliV2ray",
"https://t.me/s/FalconPolV2rayNG",
"https://t.me/s/forwardv2ray",
"https://t.me/s/FOX_VPN66",
"https://t.me/s/foxrayiran",
"https://t.me/s/free4allVPN",
"https://t.me/s/freeland8",
"https://t.me/s/FreeNet1500",
"https://t.me/s/FreeV2rays",
"https://t.me/s/freev2rayssr",
"https://t.me/s/FreeVlessVpn",
"https://t.me/s/frev2ray"
"https://t.me/s/frev2rayng",
"https://t.me/s/God_CONFIG",
"https://t.me/s/HTTPCustomLand",
"https://t.me/s/inikotesla",
"https://t.me/s/iranvpnet",
"https://t.me/s/iSeqaro",
"https://t.me/s/mahsaamoon1",
"https://t.me/s/MsV2ray",
"https://t.me/s/napsternetv_config",
"https://t.me/s/Network_442",
"https://t.me/s/OutlineVpnOfficial",
"https://t.me/s/ParsRoute",
"https://t.me/s/PrivateVPNs",
"https://t.me/s/proxystore11",
"https://t.me/s/ServerNett",
"https://t.me/s/Shadowlinkserverr",
"https://t.me/s/ShadowSocks_s",
"https://t.me/s/ShadowsocksM",
"https://t.me/s/shadowsocksshop",
"https://t.me/s/TUICity",
"https://t.me/s/v2_team",
"https://t.me/s/v2_vmess",
"https://t.me/s/v2line",
"https://t.me/s/V2pedia",
"https://t.me/s/v2ray_ar",
"https://t.me/s/v2ray_custom",
"https://t.me/s/v2ray_for_free",
"https://t.me/s/V2Ray_FreedomIran",
"https://t.me/s/V2RAY_NEW",
"https://t.me/s/v2ray_outlineir",
"https://t.me/s/v2rayan",
"https://t.me/s/v2RayChannel",
"https://t.me/s/V2rayN_Free",
"https://t.me/s/v2rayn_server",
"https://t.me/s/v2rayng_org",
"https://t.me/s/v2rayng_v",
"https://t.me/s/v2rayNG_VPN",
"https://t.me/s/V2RayOxygen",
"https://t.me/s/ViPVpn_v2ray",
"https://t.me/s/vmess_iran",
"https://t.me/s/vmess_vless_v2rayng",
"https://t.me/s/vmessiran",
"https://t.me/s/VmessProtocol",
"https://t.me/s/vmessq",
"https://t.me/s/VorTexIRN",
"https://t.me/s/VPN_443",
"https://t.me/s/vpn_ocean",
"https://t.me/s/vpn_proxy_custom",
"https://t.me/s/vpn_tehran",
"https://t.me/s/vpnmasi",
"https://t.me/s/WeePeeN",
"https://t.me/s/yaney_01",
"https://t.me/s/YtTe3la",
"https://t.me/s/vpn_xw",
"https://t.me/s/azadi_az_inja_migzare",
"https://t.me/s/reality_daily",
"https://t.me/s/zen_cloud",
"https://t.me/s/V2rayCollectorDonate",
"https://t.me/s/iP_CF",
"https://t.me/s/TLS_v2ray",
"https://t.me/s/v2raycollector",
"https://t.me/s/Cov2ray",
"https://t.me/s/v2ray_cartel",
"https://t.me/s/speedconfig00",
"https://t.me/s/FOXNT",
"https://t.me/s/EspinasVPN",
"https://t.me/s/vpnsshocean",
"https://t.me/s/filterkoshi",
"https://t.me/s/ARv2ray",
"https://t.me/s/Eleven_vpn",
"https://t.me/s/freeownvpn",
"https://t.me/s/msv2raynp",
"https://t.me/s/Injastvpn",
"https://t.me/s/Joker_v2ray_configs",
"https://t.me/s/JOKERRVPN",
"https://t.me/s/kvetch_matin",
"https://t.me/s/mrsoulb",
"https://t.me/s/Netifyvpn",
"https://t.me/s/NETMelliAnti",
"https://t.me/s/networld_vpn",
"https://t.me/s/Prime_Verse",
"https://t.me/s/SAVTEAM",
"https://t.me/s/Shadownet021",
"https://t.me/s/V2ray_Collector",
"https://t.me/s/v2ray_hubb",
"https://t.me/s/v2rayconfigsNN",
"https://t.me/s/v2rayng_021",
"https://t.me/s/V2RayNG_CaFe",
"https://t.me/s/V2rayNG3",
"https://t.me/s/v2rayserverfreenet",
"https://t.me/s/v2xay",
"https://t.me/s/vemssprotocol",
"https://t.me/s/vpnaloo",
"https://t.me/s/zeshtobad",
"https://t.me/s/ProxyFn",
"https://t.me/s/prrofile_purple",
"https://t.me/s/shadowproxy66",
"https://t.me/s/sinavm",
"https://t.me/s/VPNCUSTOMIZE",
"https://t.me/s/Outline_ir",
"https://t.me/s/Pruoxyi",
"https://t.me/s/v2ray_configs_pool",
"https://t.me/s/v2ray_configs_pools",
"https://t.me/s/ultrasurf_12",
"https://t.me/s/V2RAY_VMESS_free",
"https://t.me/s/FreakConfig",
"https://t.me/s/v2rayNG_Matsuri",
"https://t.me/s/meli_proxyy",
"https://t.me/s/oneclickvpnkeys",
"https://t.me/s/Outline_Vpn",
"https://t.me/s/proxy_kafee",
"https://t.me/s/v2ray_sub",
"https://t.me/s/SaghiVpnX",
"https://t.me/s/Daily_Configs",
"https://t.me/s/customv2ray",
"https://t.me/s/Fr33C0nfig ",
"https://t.me/s/UnlimitedDev",
"https://t.me/s/vmessorg",
"https://t.me/s/v2rayngvpn",
"https://t.me/s/SafeNet_Server",
"https://t.me/s/vmessprotocol ",
"https://t.me/s/vmesskhodam",
"https://t.me/s/singbox1",
"https://t.me/s/i10VPN ",
"https://t.me/s/Viturey",
"https://t.me/s/pPal03",
"https://t.me/s/Rayan_Config",
"https://t.me/s/info_2it_channel",
"https://t.me/s/lexernet",
"https://t.me/s/AblNet7",
"https://t.me/s/manzariyeh_rasht",
"https://t.me/s/Farah_VPN",
"https://t.me/s/SSRSUB",
"https://t.me/s/Parsashonam",


]
# 定义去重函数，输入列表，返回去重后的列表
def remove_duplicates(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

html_pages = []  # 用于存储每个网页的HTML内容

# 遍历所有地址，获取网页内容
for url in newaddresses:
    response = requests.get(url)  # 发送GET请求
    html_pages.append(response.text)  # 保存网页内容

codes = []  # 用于存储所有抓取到的配置代码

# 遍历所有HTML页面，解析并提取code标签内容
for page in html_pages:
    soup = BeautifulSoup(page, 'html.parser')  # 解析HTML
    code_tags = soup.find_all('code')  # 查找所有code标签

    for code_tag in code_tags:
        code_content = code_tag.text.strip()  # 获取并去除首尾空格
        # 判断是否为目标协议的配置
        if (
            "vless://" in code_content
            or "ss://" in code_content
            or "vmess://" in code_content
            or "trojan://" in code_content
            or "ssr://" in code_content  # 添加ssr协议
        ):
            codes.append(code_content)  # 添加到codes列表

codes = list(set(codes))  # 去重

processed_codes = []  # 用于存储处理后的配置

# 获取当前时间（上海时区）
current_date_time = datetime.now(pytz.timezone('Asia/Shanghai'))
current_month = current_date_time.strftime("%b")  # 月份
current_day = current_date_time.strftime("%d")    # 日期
updated_hour = current_date_time.strftime("%H")   # 小时
updated_minute = current_date_time.strftime("%M") # 分钟
final_string = f"{current_month}-{current_day} | {updated_hour}:{updated_minute}"  # 格式化时间字符串
final_others_string = f"{current_month}-{current_day}"  # 仅日期字符串
config_string = "#✅ " + str(final_string) + "-"  # 配置头部字符串

# 处理每个配置，去除#后面的内容
for code in codes:
    vmess_parts = code.split("vmess://")  # 分割vmess协议
    vless_parts = code.split("vless://")  # 分割vless协议

    for part in vmess_parts + vless_parts:
        # 判断是否为目标协议
        if (
            "ss://" in part
            or "vmess://" in part
            or "vless://" in part
            or "trojan://" in part
            or "ssr://" in part  # 添加SSR协议支持
        ):
            service_name = part.split("serviceName=")[-1].split("&")[0]  # 提取serviceName参数
            processed_part = part.split("#")[0]  # 去除#后面的内容
            processed_codes.append(processed_part)  # 添加到处理后的列表

processed_codes = remove_duplicates(processed_codes)  # 再次去重

new_processed_codes = []  # 用于存储最终处理后的配置

# 再次处理配置，去除#后面的内容
for code in processed_codes:
    vmess_parts = code.split("vmess://")  # 分割vmess协议
    vless_parts = code.split("vless://")  # 分割vless协议

    for part in vmess_parts + vless_parts:
        # 判断是否为目标协议
        if "ss://" in part or "vmess://" in part or "vless://" in part or "trojan://" in part or "ssr://" in part:
            service_name = part.split("serviceName=")[-1].split("&")[0]  # 提取serviceName参数
            processed_part = part.split("#")[0]  # 去除#后面的内容
            new_processed_codes.append(processed_part)  # 添加到最终处理后的列表

i = 0  # 初始化服务器计数器
with open("config.txt", "w", encoding="utf-8") as file:  # 以写入模式打开文件
    for code in new_processed_codes:
        if i == 0:
            config_string = "#🌐已更新于" + config_string + " | 每15分钟更新配置"  # 第一行写更新时间
        else:
            config_string = "#🌐服务器" + str(i) + " | " + str(final_others_string) + " |bin1site1.github.io "  # 其他行写服务器编号和日期
        config_final = code + config_string  # 拼接配置和注释
        file.write(config_final + "\n")  # 写入文件并换行
        i += 1  # 服务器计数器加一
