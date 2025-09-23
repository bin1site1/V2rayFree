import requests  # 导入requests库，用于发送HTTP请求
from bs4 import BeautifulSoup  # 导入BeautifulSoup库，用于解析HTML
from datetime import datetime, timezone  # 导入datetime库，用于处理日期和时间
import pytz  # 导入pytz库，用于处理时区
import jdatetime  # 导入jdatetime库，用于处理Jalali日期


newaddresses = [
"https://t.me/s/configV2rayForFree",
"https://t.me/s/configV2rayNG",
"https://t.me/s/DailyV2RY",
"https://t.me/s/DirectVPN",
"https://t.me/s/EliV2ray",
"https://t.me/s/free4allVPN",
"https://t.me/s/freeland8",
"https://t.me/s/MsV2ray",
"https://t.me/s/PrivateVPNs",
"https://t.me/s/ServerNett",
"https://t.me/s/ShadowsocksM",
"https://t.me/s/V2pedia",
"https://t.me/s/v2ray_for_free",
"https://t.me/s/vmess_vless_v2rayng",
"https://t.me/s/vmessiran",
"https://t.me/s/VmessProtocol",
"https://t.me/s/VorTexIRN",
"https://t.me/s/vpn_tehran",
"https://t.me/s/vpnmasi",
"https://t.me/s/iP_CF",
"https://t.me/s/v2ray_cartel",
"https://t.me/s/ARv2ray",
"https://t.me/s/Joker_v2ray_configs",
"https://t.me/s/mrsoulb",
"https://t.me/s/Netifyvpn",
"https://t.me/s/NETMelliAnti",
"https://t.me/s/networld_vpn",
"https://t.me/s/Prime_Verse",
"https://t.me/s/Shadownet021",
"https://t.me/s/V2ray_Collector",
"https://t.me/s/v2rayconfigsNN",
"https://t.me/s/v2rayng_021",
"https://t.me/s/V2RayNG_CaFe",
"https://t.me/s/v2rayserverfreenet",
"https://t.me/s/v2xay",
"https://t.me/s/vpnaloo",
"https://t.me/s/zeshtobad",
"https://t.me/s/prrofile_purple",
"https://t.me/s/shadowproxy66",
"https://t.me/s/sinavm",
"https://t.me/s/Outline_ir",
"https://t.me/s/Pruoxyi",
"https://t.me/s/v2ray_configs_pool",
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
"https://t.me/s/Rayan_Config",
"https://t.me/s/info_2it_channel",
"https://t.me/s/lexernet",
"https://t.me/s/AblNet7",
"https://t.me/s/manzariyeh_rasht",
"https://t.me/s/Farah_VPN",
"https://t.me/s/SSRSUB",
"https://t.me/s/Parsashonam",
"https://raw.githubusercontent.com/barry-far/V2ray-config/main/Splitted-By-Protocol/vmess.txt",
"https://raw.githubusercontent.com/barry-far/V2ray-config/main/Splitted-By-Protocol/vmess.txt",
"https://raw.githubusercontent.com/barry-far/V2ray-config/main/Splitted-By-Protocol/vless.txt",
"https://raw.githubusercontent.com/barry-far/V2ray-config/main/Splitted-By-Protocol/vless.txt",
"https://raw.githubusercontent.com/barry-far/V2ray-config/main/Splitted-By-Protocol/trojan.txt",
"https://raw.githubusercontent.com/barry-far/V2ray-config/main/Splitted-By-Protocol/trojan.txt",
"https://raw.githubusercontent.com/barry-far/V2ray-config/main/Splitted-By-Protocol/ss.txt",
"https://raw.githubusercontent.com/barry-far/V2ray-config/main/Splitted-By-Protocol/ss.txt",
"https://raw.githubusercontent.com/barry-far/V2ray-config/main/Splitted-By-Protocol/ssr.txt",
"https://raw.githubusercontent.com/barry-far/V2ray-config/main/Splitted-By-Protocol/ssr.txt",
"https://raw.githubusercontent.com/barry-far/V2ray-config/main/Sub1.txt",
"https://raw.githubusercontent.com/barry-far/V2ray-config/main/Sub2.txt",
"https://raw.githubusercontent.com/barry-far/V2ray-config/main/Sub3.txt",
"https://raw.githubusercontent.com/barry-far/V2ray-config/main/Sub4.txt",
"https://raw.githubusercontent.com/barry-far/V2ray-config/main/Sub5.txt",
"https://raw.githubusercontent.com/barry-far/V2ray-config/main/Sub6.txt",
"https://raw.githubusercontent.com/barry-far/V2ray-config/main/Sub7.txt",
"https://raw.githubusercontent.com/barry-far/V2ray-config/main/Sub8.txt",
"https://github.com/Epodonios/v2ray-configs/raw/main/All_Configs_Sub.txt",
"https://github.com/Epodonios/v2ray-configs/raw/main/All_Configs_base64_Sub.txt",
"https://github.com/Epodonios/v2ray-configs/raw/main/Splitted-By-Protocol/vless.txt",
"https://github.com/Epodonios/v2ray-configs/raw/main/Splitted-By-Protocol/vmess.txt",
"https://github.com/Epodonios/v2ray-configs/raw/main/Splitted-By-Protocol/ss.txt",
"https://github.com/Epodonios/v2ray-configs/raw/main/Splitted-By-Protocol/ssr.txt",
"https://github.com/Epodonios/v2ray-configs/raw/main/Splitted-By-Protocol/trojan.txt",
"https://raw.githubusercontent.com/Epodonios/v2ray-configs/refs/heads/main/Sub1.txt",
"https://raw.githubusercontent.com/Epodonios/v2ray-configs/refs/heads/main/Sub2.txt",
"https://raw.githubusercontent.com/Epodonios/v2ray-configs/refs/heads/main/Sub3.txt",
"https://raw.githubusercontent.com/Epodonios/v2ray-configs/refs/heads/main/Sub4.txt",
"https://raw.githubusercontent.com/Epodonios/v2ray-configs/refs/heads/main/Sub5.txt",
"https://raw.githubusercontent.com/Epodonios/v2ray-configs/refs/heads/main/Sub6.txt",
"https://raw.githubusercontent.com/Epodonios/v2ray-configs/refs/heads/main/Sub7.txt",
"https://raw.githubusercontent.com/Epodonios/v2ray-configs/refs/heads/main/Sub8.txt",
"https://raw.githubusercontent.com/Epodonios/v2ray-configs/refs/heads/main/Sub9.txt",
"https://raw.githubusercontent.com/Epodonios/v2ray-configs/refs/heads/main/Sub10.txt",
"https://raw.githubusercontent.com/Epodonios/v2ray-configs/refs/heads/main/Sub11.txt",
"https://raw.githubusercontent.com/Epodonios/v2ray-configs/refs/heads/main/Sub12.txt",
"https://raw.githubusercontent.com/Epodonios/v2ray-configs/refs/heads/main/Sub13.txt",
"https://raw.githubusercontent.com/Epodonios/v2ray-configs/refs/heads/main/Sub14.txt",
"https://vpny.online/VPNy.json",
"https://github.com/Epodonios/v2ray-configs/raw/main/Splitted-By-Protocol/ss.txt",
"https://github.com/Epodonios/v2ray-configs/raw/main/Splitted-By-Protocol/vmess.txt",
"https://github.com/Epodonios/v2ray-configs/raw/main/Splitted-By-Protocol/trojan.txt",
"https://raw.githubusercontent.com/MatinGhanbari/v2ray-configs/main/subscriptions/v2ray/super-sub.txt",
"https://raw.githubusercontent.com/MatinGhanbari/v2ray-configs/main/subscriptions/v2ray/subs/sub1.txt",
"https://raw.githubusercontent.com/MatinGhanbari/v2ray-configs/main/subscriptions/filtered/subs/ss.txt",
"https://raw.githubusercontent.com/MatinGhanbari/v2ray-configs/main/subscriptions/filtered/subs/vless.txt",
"https://raw.githubusercontent.com/MatinGhanbari/v2ray-configs/main/subscriptions/filtered/subs/vmess.txt",
"https://robin.victoriacross.ir",
"https://raw.githubusercontent.com/STR97/STRUGOV/refs/heads/main/Vless",
"https://raw.githubusercontent.com/NiREvil/vless/refs/heads/main/sub/SSTime",
"https://raw.githubusercontent.com/darkvpnapp/CloudflarePlus/refs/heads/main/index.html",
"https://raw.githubusercontent.com/barry-far/V2ray-config/main/Splitted-By-Protocol/ss.txt",
"https://raw.githubusercontent.com/barry-far/V2ray-config/main/Splitted-By-Protocol/vmess.txt",
"https://raw.githubusercontent.com/barry-far/V2ray-config/main/Splitted-By-Protocol/vless.txt",
"https://dev1.irdevs.sbs",
"https://v2.alicivil.workers.dev",
"https://v2.alicivil.workers.dev/?list=us&count=300&shuffle=true&unique=false",
"https://raw.githubusercontent.com/mahdibland/ShadowsocksAggregator/master/Eternity",
"https://raw.githubusercontent.com/mahdibland/ShadowsocksAggregator/master/EternityAir",
"https://raw.githubusercontent.com/mahdibland/ShadowsocksAggregator/master/sub/splitted/trojan.txt",
"https://raw.githubusercontent.com/Surfboardv2ray/TGParse/main/splitted/mixed",
"https://raw.githubusercontent.com/Surfboardv2ray/TGParse/main/python/hysteria2",
"https://shadowmere.xyz/api/b64sub",
"https://openproxylist.com/v2ray/",
"https://openproxylist.com/v2ray/",
"https://raw.githubusercontent.com/NiREvil/vless/refs/heads/main/sub/fragment",
"https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Protocols/ss.txt",
"https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Protocols/vmess.txt",
"https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Protocols/vless.txt",
"https://raw.githubusercontent.com/Mahdi0024/ProxyCollector/master/sub/proxies.txt",
"https://raw.githubusercontent.com/arshiacomplus/v2rayExtractor/refs/heads/main/mix/sub.html",
"https://raw.githubusercontent.com/arshiacomplus/v2rayExtractor/refs/heads/main/vless.html",
"https://raw.githubusercontent.com/10ium/free-config/refs/heads/main/HighSpeed.txt",
"https://raw.githubusercontent.com/DarknessShade/Sub/main/V2mix",
"https://raw.githubusercontent.com/DarknessShade/Sub/main/Ss",
"https://raw.githubusercontent.com/nscl5/5/refs/heads/main/configs/all.txt",
"https://raw.githubusercontent.com/nscl5/5/refs/heads/main/configs/vmess.txt",
"https://raw.githubusercontent.com/youfoundamin/V2rayCollector/main/mixed_iran.txt",
"https://raw.githubusercontent.com/youfoundamin/V2rayCollector/main/ss_iran.txt",
"https://raw.githubusercontent.com/youfoundamin/V2rayCollector/main/vless_iran.txt",
"https://raw.githubusercontent.com/itsyebekhe/PSG/main/lite/subscriptions/xray/normal/mix",
"https://raw.githubusercontent.com/itsyebekhe/PSG/main/lite/subscriptions/xray/normal/hy2",
"https://raw.githubusercontent.com/itsyebekhe/PSG/main/subscriptions/xray/normal/vmess",
"https://raw.githubusercontent.com/lagzian/IranConfigCollector/main/Base64.txt",
"https://raw.githubusercontent.com/lagzian/SS-Collector/refs/heads/main/SS/TrinityBase",
"https://raw.githubusercontent.com/MahsaNetConfigTopic/config/refs/heads/main/xray_final.txt",
"https://raw.githubusercontent.com/hamedcode/port-based-v2ray-configs/main/sub/vless.txt",
"https://raw.githubusercontent.com/hamedcode/port-based-v2ray-configs/main/sub/vmess.txt",
"https://raw.githubusercontent.com/hamedcode/port-based-v2ray-configs/main/sub/ss.txt",
"https://raw.githubusercontent.com/AzadNetCH/Clash/main/AzadNet.txt",
"https://raw.githubusercontent.com/Leon406/SubCrawler/refs/heads/main/sub/share/a11",
"https://raw.githubusercontent.com/imalrzai/ExclaveVirtual/refs/heads/main/ExclaveVirtual",
"https://raw.githubusercontent.com/Pawdroid/Free-servers/refs/heads/main/sub",
"https://raw.githubusercontent.com/Surfboardv2ray/TGParse/main/splitted/ss",
"https://raw.githubusercontent.com/Surfboardv2ray/TGParse/main/splitted/trojan",
"https://raw.githubusercontent.com/Surfboardv2ray/TGParse/main/splitted/vless",
"https://raw.githubusercontent.com/roosterkid/openproxylist/main/V2RAY_BASE64.txt",
"https://raw.githubusercontent.com/HosseinKoofi/GO_V2rayCollector/main/mixed_iran.txt",
"https://raw.githubusercontent.com/HosseinKoofi/GO_V2rayCollector/main/vless_iran.txt",
"https://raw.githubusercontent.com/HosseinKoofi/GO_V2rayCollector/main/ss_iran.txt",
"https://raw.githubusercontent.com/ebrasha/free-v2ray-public-list/refs/heads/main/ss_configs.txt",
"https://raw.githubusercontent.com/ebrasha/free-v2ray-public-list/refs/heads/main/V2Ray-Config-By-EbraSha.txt",
"https://raw.githubusercontent.com/ebrasha/free-v2ray-public-list/refs/heads/main/vmess_configs.txt",
"https://raw.githubusercontent.com/Argh94/V2RayAutoConfig/refs/heads/main/configs/Vmess.txt",
"https://raw.githubusercontent.com/Argh94/V2RayAutoConfig/refs/heads/main/configs/Hysteria2.txt",
"https://raw.githubusercontent.com/Argh94/V2RayAutoConfig/refs/heads/main/configs/Germany.txt",
"https://raw.githubusercontent.com/Stinsonysm/GO_V2rayCollector/refs/heads/main/trojan_iran.txt",
"https://raw.githubusercontent.com/MhdiTaheri/V2rayCollector_Py/refs/heads/main/sub/Mix/mix.txt",
"https://raw.githubusercontent.com/MhdiTaheri/V2rayCollector_Py/refs/heads/main/sub/United%20States/config.txt",
"https://raw.githubusercontent.com/liketolivefree/kobabi/main/sub.txt",
"https://raw.githubusercontent.com/liketolivefree/kobabi/main/sub_all.txt",
"https://raw.githubusercontent.com/10ium/ScrapeAndCategorize/refs/heads/main/output_configs/Hysteria2.txt",
"https://raw.githubusercontent.com/10ium/V2ray-Config/main/Splitted-By-Protocol/hysteria2.txt",
"https://raw.githubusercontent.com/10ium/V2Hub3/main/merged_base64",
"https://raw.githubusercontent.com/10ium/base64-encoder/main/encoded/10ium_mixed_iran.txt",
"https://raw.githubusercontent.com/10ium/ScrapeAndCategorize/refs/heads/main/output_configs/Vless.txt",
"https://raw.githubusercontent.com/10ium/ScrapeAndCategorize/refs/heads/main/output_configs/ShadowSocks.txt",
"https://raw.githubusercontent.com/10ium/ScrapeAndCategorize/refs/heads/main/output_configs/Trojan.txt",
"https://raw.githubusercontent.com/Epodonios/v2ray-configs/refs/heads/main/Sub1.txt",
"https://raw.githubusercontent.com/Epodonios/v2ray-configs/refs/heads/main/Sub2.txt",
"https://raw.githubusercontent.com/Epodonios/v2ray-configs/refs/heads/main/Sub3.txt",
"https://github.com/Epodonios/v2ray-configs/raw/main/All_Configs_base64_Sub.txt",
"https://raw.githubusercontent.com/barry-far/V2ray-config/main/Sub1.txt",
"https://raw.githubusercontent.com/barry-far/V2ray-config/main/Sub2.txt",
"https://raw.githubusercontent.com/barry-far/V2ray-config/main/Sub3.txt",
"https://raw.githubusercontent.com/barry-far/V2ray-config/main/Sub4.txt",
"https://raw.githubusercontent.com/aqayerez/MatnOfficial-VPN/refs/heads/main/MatnOfficial#MatnOfficial",
"https://raw.githubusercontent.com/V2RAYCONFIGSPOOL/V2RAY_SUB/refs/heads/main/v2ray_configs.txt",
"https://raw.githubusercontent.com/bamdad23/JavidnamanIran/refs/heads/main/WS%2BHysteria2",
"https://raw.githubusercontent.com/mshojaei77/v2rayAuto/refs/heads/main/telegram/popular_channels_1",
"https://raw.githubusercontent.com/mshojaei77/v2rayAuto/refs/heads/main/telegram/popular_channels_2",
"https://raw.githubusercontent.com/mshojaei77/v2rayAuto/refs/heads/main/subs/hysteria",
"https://raw.githubusercontent.com/mshojaei77/v2rayAuto/refs/heads/main/subs/hy2",
"https://raw.githubusercontent.com/ndsphonemy/proxy-sub/refs/heads/main/speed.txt",
"https://raw.githubusercontent.com/ndsphonemy/proxy-sub/refs/heads/main/hys-tuic.txt",
"https://trojanvmess.pages.dev/cmcm?b64#cmcm?b64",
"https://raw.githubusercontent.com/Mosifree/-FREE2CONFIG/refs/heads/main/Reality",
"https://raw.githubusercontent.com/Mosifree/-FREE2CONFIG/refs/heads/main/Vless",
"https://raw.githubusercontent.com/AzadNetCH/Clash/refs/heads/main/AzadNet_iOS.txt",
"https://raw.githubusercontent.com/Proxydaemitelegram/Proxydaemi44/refs/heads/main/Proxydaemi44",
"https://raw.githubusercontent.com/MrMohebi/xray-proxy-grabber-telegram/refs/heads/master/collected-proxies/xray-json-full/actives_all.json",
"https://raw.githubusercontent.com/barry-far/V2ray-config/main/Sub6.txt",
"https://raw.githubusercontent.com/barry-far/V2ray-config/main/Sub7.txt",
"https://raw.githubusercontent.com/barry-far/V2ray-config/main/Sub8.txt",
"https://raw.githubusercontent.com/barry-far/V2ray-Configs/main/Sub9.txt",
"https://azadnet05.pages.dev/sub/4d794980-54c0-4fcb-8def-c2beaecadbad#EN-Normal",
"https://raw.githubusercontent.com/amirparsaxs/Vip-s/refs/heads/main/Sub.vip",
"https://raw.githubusercontent.com/rango-cfs/NewCollector/refs/heads/main/v2ray_links.txt",

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
current_month = current_date_time.strftime("%m")  # 月份（数字）
current_day = current_date_time.strftime("%d")    # 日期
updated_hour = current_date_time.strftime("%H")   # 小时
updated_minute = current_date_time.strftime("%M") # 分钟
final_string = f"{current_month}月{current_day}日 | {updated_hour}:{updated_minute}"  # 中文格式时间字符串
final_others_string = f"{current_month}月{current_day}日"  # 仅日期字符串
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
            config_string = "#🌐已更新于" + config_string + " | 每15分钟更新一次"  # 第一行写更新时间
        else:
            config_string = "#🌐服务器" + str(i) + " | " + str(final_others_string) + " |bin1site1.github.io "  # 其他行写服务器编号和日期
        config_final = code + config_string  # 拼接配置和注释
        file.write(config_final + "\n")  # 写入文件并换行
        i += 1  # 服务器计数器加一
