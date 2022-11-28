import subprocess, re
import platform
import requests, json, random, hashlib
from urllib.parse import urlencode
import os
import random
import time, uuid, binascii
from pystyle import *

class Gorgon:
	def __init__(self,params:str,data:str,cookies:str,unix:int)->None:self.unix=unix;self.params=params;self.data=data;self.cookies=cookies
	def hash(self,data:str)->str:
		try:_hash=str(hashlib.md5(data.encode()).hexdigest())
		except Exception:_hash=str(hashlib.md5(data).hexdigest())
		return _hash
	def get_base_string(self)->str:base_str=self.hash(self.params);base_str=base_str+self.hash(self.data)if self.data else base_str+str('0'*32);base_str=base_str+self.hash(self.cookies)if self.cookies else base_str+str('0'*32);return base_str
	def get_value(self)->json:base_str=self.get_base_string();return self.encrypt(base_str)
	def encrypt(self,data:str)->json:
		unix=self.unix;len=20;key=[223,119,185,64,185,155,132,131,209,185,203,209,247,194,185,133,195,208,251,195];param_list=[]
		for i in range(0,12,4):
			temp=data[8*i:8*(i+1)]
			for j in range(4):H=int(temp[j*2:(j+1)*2],16);param_list.append(H)
		param_list.extend([0,6,11,28]);H=int(hex(unix),16);param_list.append((H&4278190080)>>24);param_list.append((H&16711680)>>16);param_list.append((H&65280)>>8);param_list.append((H&255)>>0);eor_result_list=[]
		for (A,B) in zip(param_list,key):eor_result_list.append(A^B)
		for i in range(len):C=self.reverse(eor_result_list[i]);D=eor_result_list[(i+1)%len];E=C^D;F=self.rbit_algorithm(E);H=(F^4294967295^len)&255;eor_result_list[i]=H
		result=''
		for param in eor_result_list:result+=self.hex_string(param)
		return{'X-Gorgon':'0404b0d30000'+result,'X-Khronos':str(unix)}
	def rbit_algorithm(self,num):
		result='';tmp_string=bin(num)[2:]
		while len(tmp_string)<8:tmp_string='0'+tmp_string
		for i in range(0,8):result=result+tmp_string[7-i]
		return int(result,2)
	def hex_string(self,num):
		tmp_string=hex(num)[2:]
		if len(tmp_string)<2:tmp_string='0'+tmp_string
		return tmp_string
	def reverse(self,num):tmp_string=self.hex_string(num);return int(tmp_string[1:]+tmp_string[:1],16)


class TikTok_Api(object):
    def __init__(self, cookie: str) -> None:
        coo = cookie.split('sessionid=')[1].split(';')[0]
        self.cookies = 'sessionid='+coo
        
    def Get_cauhinh(self) -> bool:
        try:
            headers = {
                'authority': 'www.tiktok.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-language': 'en-US,en;q=0.9',
                'cache-control': 'max-age=0',
                'cookie': self.cookies,
                'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
            }

            response = requests.get('https://www.tiktok.com/', headers=headers).text
            tach = response.split('"uid":"')[1].split('","nickName":"')
            uid = tach[0]
            nick_name = tach[1].split('","signature"')[0]
            uniqueId = tach[1].split('"uniqueId":"')[1].split('","')[0]
            return {'uid': uid, 'nickName': nick_name, 'uniqueId': uniqueId}
        except:
            return None 
        
    def likeUser(self, aweme_id: str) -> bool:
        URL = f'https://api16-normal-c-useast2a.tiktokv.com/aweme/v1/commit/item/digg/?aweme_id={aweme_id}&type=1&os_api=25&device_type=SM-N976N&ssmix=a&manifest_version_code=270204&dpi=240&region=US&carrier_region=VN&app_name=musically_go&version_name=27.2.4&timezone_offset=-28800&ts=1668225737&ab_version=27.2.4&ac2=wifi&ac=wifi&app_type=normal&channel=googleplay&update_version_code=270204&_rticket=1668225879309&device_platform=android&iid=7164599892450969349&build_number=27.2.4&locale=en&op_region=VN&version_code=270204&timezone_name=America%2FTijuana&cdid=8d3365a0-e084-4fa2-80a0-952a6feffc09&openudid=4bfc6795c2eff49c&device_id=6854804415247074817&sys_region=US&app_language=en&resolution=720*1280&device_brand=samsung&language=en&os_version=7.1.2&aid=1340'
        params = urlencode(
                {
                    "aweme_id": aweme_id,
                    "type": "1",
                    "os_api": "25",
                    "device_type": "SM-N976N",
                    "ssmix": "a",
                    "manifest_version_code": "270204",
                    "dpi": "240",
                    "region": "VN",
                    "carrier_region": "VN",
                    "app_name": "musically_go",
                    "version_name": "27.2.4",
                    "timezone_offset": "-28800",
                    "ab_version": "27.2.4",
                    "ac2": "wifi",
                    "ac": "wifi",
                    "app_type": "normal",
                    "channel": "googleplay",
                    "update_version_code": "270204",
                    "device_platform": "android",
                    "build_number": "27.2.4",
                    "locale": "vi",
                    "op_region": "VN",
                    "version_code": "270204",
                    "timezone_name": "Asia/Ho_Chi_Minh",
                    "sys_region": "VN",
                    "app_language": "vi",
                    "resolution": "720*1280",
                    "device_brand": "samsung",
                    "language": "vi",
                    "os_version": "7.1.2",
                    "aid": "1340"
                }
                    )
        sig     = Gorgon(params=params, cookies=self.cookies, data=None, unix=int(time.time())).get_value()
        headers = {
            'cookie': self.cookies,
            'host': 'api16-normal-c-useast2a.tiktokv.com',
            'user-agent': 'com.zhiliaoapp.musically.go/270204 (Linux; U; Android 7.1.2; en_US; SM-N976N; Build/QP1A.190711.020;tt-ok/3.12.13.2-rc.5)',
            'x-gorgon':sig['X-Gorgon'],
            'x-khronos':sig['X-Khronos'],
        }
        
        try:
            rps = requests.get(
                            url=URL+params, 
                            headers=headers
                            ).json()
            if rps['is_digg'] == 0:
                return True
            else:
                return False
        except:
            return False
totalXu = 0
success = 0
error = 0
class TuongTacCheo:
    def __init__(self):
        pon=requests.get('https://tuongtaccheo.com/')
        cookie=pon.headers['Set-cookie']
        self.headers={
            'Content-type': "application/x-www-form-urlencoded",
            "x-requested-with":"XMLHttpRequest",
            "Cookie":cookie,
        }

    def loginTtcToken(self, token: str):
        pon = requests.post("https://tuongtaccheo.com/logintoken.php", headers=self.headers, data={'access_token': token})
        if 'success' in pon.text:
            return {'status': "success", 'data': {'user': pon.json()['data']['user'], 'xu': pon.json()['data']['sodu']}}
        else:
            return {'status': "error", 'msg': "Sai tài khoản hoặc mật khẩu"}
    def getXu(self):
        try:
            return requests.get("https://tuongtaccheo.com/home.php", headers = self.headers).text.split('id="soduchinh">')[1].split("</strong>")[0]
        except:
            pass
    def datNickTTC(self, user: int):
        active = requests.get(f'https://tuongtaccheo.com/cauhinh/addtiktok.php?link={user}&nickchay={user}', headers=self.headers, data={'iddat[]': id, 'loai': "tt"}).text
        if "thành công" in active:
            return True
        else:
            return False

    def getJobTym(self):
        a=requests.get(f'https://tuongtaccheo.com/tiktok/kiemtien/getpost.php', headers=self.headers).json()
        if len(a) >= 1:
            return a
        else:
            return False
    def getXuJob(self, listJob):
            id = ','.join(listJob)
            get_tt=requests.post('https://tuongtaccheo.com/tiktok/kiemtien/nhantien.php', headers=self.headers, data={"id": id})
            if 'mess' in get_tt.text and "cộng" in get_tt.text:
                return str(get_tt.json()['mess']).split('cộng ')[1].split(' xu')[0]
            else:
                return 0

class TraoDoiSub:
    def __init__(self, token: str) -> None:
        self.token = token
    def getSoDu(self: object) -> dict:
        a = requests.get(f"https://traodoisub.com/api/?fields=profile&access_token={self.token}").json()
        if 'success' in a:
            return a['data']
        else:
            return 0

    def getLikeTik(self):
        while(True):
            try:
                while(True):
                    a=requests.get(f'https://traodoisub.com/api/?fields=tiktok_like&access_token={self.token}').json()
                    if 'fail_count' in a:
                        data = a['error'], False
                        break
                    if 'countdown' not in a or "Vui lòng thao tác chậm lại" not in a:
                        data = a['data'], True
                        break
                    else:
                        pass
                return data
            except Exception as e:
                pass
            time.sleep(1)

    def postCache(self,type, id: str):
        try: 
            check=requests.get(f'https://traodoisub.com/api/coin/?type=TIKTOK_{type}_CACHE&id='+id+'&access_token='+self.token).json()
            return check['cache']
        except:
            pass
    def getXuJob(self,type):
        try:
            get_tt=requests.get(f'https://traodoisub.com/api/coin/?type=TIKTOK_{type}&id=TIKTOK_{type}_API&access_token='+self.token)
            if "success" in get_tt.text and "Xu" in get_tt.text:
                return str(get_tt.json()['data']['msg']).split('+')[1].split('Xu')[0], get_tt.json()['data']['xu'], get_tt.json()['data']['job_success']
            else:
                return 0, 0, 0
        except:
            pass

    def datNick(self, id: int):
        try:
            active = requests.post(f'https://traodoisub.com/api/?fields=tiktok_run&id={id}&access_token={self.token}').json()
            if "success" in active:
                return True
            else:
                return active['error']
        except Exception as e:
            return "Lỗi đặt nick không xác định"
def title(text):
    os.system(f'title STATUS: {text}')
def delay_job(time_delay: int):
    for x in range(time_delay, 0, -1):
        title("Delay Job {} giây      ".format(x))
        time.sleep(1)
listCookie = []
def fTDS():
    global success, error, totalXu
    while True:
        token = input(Col.purple + "{" + Col.reset + "?" + Col.purple + "}" + Col.reset + " Nhập Token TraoDoiSub " + Col.purple + "[" + Col.reset + "Nhấn " + Col.blue + "Enter" + Col.reset + " Để Chạy" + Col.purple + "]" + Col.reset + " -> ")
        tds = TraoDoiSub(token)
        info = tds.getSoDu()
        if info != 0:
            break
    if os.path.exists('./cookie.txt') == False:
        title("Tạo file chứa cookie")
        open("cookie.txt", "w+", encoding="utf-8-sig")
        
    for ck in open("cookie.txt", "r", encoding="utf-8-sig").read().split("\n"):
        if len(ck) >= 20:
            listCookie.append(ck)
    if listCookie == []:
        input(Col.red + "Vui lòng nhập cookie vào file cookie.txt")
    stt = 0
    result = 0
    title(f"( TDS ) [ User: {info['user']}] ^| Coin: {info['xu']} ]")
    os.system("cls")
    while(True):
        for cookieTik in listCookie:
            __run = time.time()
            tik = TikTok_Api(cookieTik)
            info_tik = tik.Get_cauhinh()
            if info_tik == None:
                print(Col.purple + "[" + Col.reset + '*' + Col.purple + "]" + Col.reset + f"{Col.yellow} WARNING {Col.blue}! {Col.purple}[{Col.red}COOKIE DIE{Col.purple}]{Col.reset}")
                listCookie.remove(cookieTik)
                if len(listCookie) == 0:
                    print("\033[1;37m- "*40)
                    title("Đã hết cookie để chạy")
                    input("ENTER để thoát tool")
                continue
            cauHinh = tds.datNick(info_tik['uid'])
            if cauHinh == True:
                gett = f"[ TikTok: {info_tik['nickName']} ^| UID: {info_tik['uid']} ^| Success: {success} ^| Error:  {error} ^| Total Coin Get: {totalXu} ^| Trạng thái: Cấu hình success ]"
                title(gett)
            else:
                print(Col.purple + "[" + Col.reset + '*' + Col.purple + "]" + Col.reset + f"{Col.yellow} WARNING {Col.blue}! {Col.purple}[{Col.red}ID{Col.reset}:{Col.yellow} {info_tik['uid']}{Col.red} Chưa được thêm vào cấu hình{Col.purple}]{Col.reset}")
                return
            chuyen = False
            while(True):
                try:
                    title(f"[ TikTok: {info_tik['nickName']} ^| UID: {info_tik['uid']} ^| Success: {success} ^| Error:  {error} ^| Total Coin Get: {totalXu} ^| Trạng thái: Lấy nhiệm vụ Tym ]")
                    for xne in range(3):
                        layJob = False
                        getjob = tds.getLikeTik()
                        if getjob[0] == []:
                            time.sleep(2)
                            layJob = False
                            continue
                        if getjob[1] == False:
                            print(getjob[0])
                            break
                        layJob = True
                        break
                    if layJob == False:
                        title(f"[ TikTok: {info_tik['nickName']} ^| UID: {info_tik['uid']} ^| Success: {success} ^| Error:  {error} ^| Total Coin Get: {totalXu} ^| Trạng thái: Hết nhiệm vụ Tym ]")
                        break
                    for job in getjob[0]:
                        id, user = job['id'], str(job['link']).split('video/')[1]
                        title(f"[ TikTok: {info_tik['nickName']} ^| UID: {info_tik['uid']} ^| Success: {success} ^| Error:  {error} ^| Total Coin Get: {totalXu} ^| Trạng thái: Tym ID {user}]")
                        __start = time.time()
                        follow = tik.likeUser(user)
                        stt += 1
                        if follow == True:
                            print(Col.purple + "[" + Col.reset + f'{stt}' + Col.purple + "]" + Col.reset + f"{Col.reset} Tym Video {Col.blue}! {Col.purple}[{Col.green}SUCCESS {Col.reset}|{Col.cyan} {user}{Col.purple}] {Col.purple}[{Col.blue}Execution: {Col.blue}{round(time.time() - __start, 1)}s{Col.purple}]{Col.reset}")
                            success += 1
                        else:
                            print(Col.purple + "[" + Col.reset + f'{stt}' + Col.purple + "]" + Col.reset + f"{Col.reset} Tym Video {Col.blue}! {Col.purple}[{Col.red}FAILLED {Col.reset}|{Col.cyan} {user}{Col.purple}] {Col.purple}[{Col.blue}Execution: {Col.blue}{round(time.time() - __start, 1)}s{Col.purple}]{Col.reset}")
                            error += 1
                        title(f"[ TikTok: {info_tik['nickName']} ^| UID: {info_tik['uid']} ^| Success: {success} ^| Error:  {error} ^| Total Coin Get: {totalXu} ^| Trạng thái: Tym Done")
                        cache = tds.postCache("LIKE", id)
                        if cache >= 10:
                            time.sleep(2)
                            getXu = tds.getXuJob("LIKE")
                            if getXu:
                                if int(getXu[0]) == 0:
                                    print("\033[1;37m- "*40)
                                    print(Col.purple + "[" + Col.reset + '*' + Col.purple + "]" + Col.reset + f"{Col.red} ERROR {Col.blue}! {Col.purple}[{Col.red}Acc Bị Chặn Like Vui Lòng Đổi Acc.{Col.purple}]{Col.reset}")
                                    listCookie.remove(cookieTik)
                                    if len(listCookie) == 0:
                                        print("\033[1;37m- "*40)
                                        title(f"[ TikTok: {info_tik['nickName']} ^| UID: {info_tik['uid']} ^| Success: {success} ^| Error:  {error} ^| Total Coin Get: {totalXu} ^| Trạng thái: Hết cookie]")
                                        input("ENTER để thoát tool")
                                    chuyen = True
                                    break
                                totalXu += int(getXu[0])
                                title(f"[ TikTok: {info_tik['nickName']} ^| UID: {info_tik['uid']} ^| Success: {success} ^| Error:  {error} ^| Total Coin Get: {totalXu} ^| Trạng thái: Nhận xu]")
                                chuyen = True
                                break
                    if chuyen == True:
                        break
                except Exception as e:
                    print('- Lỗi Ngoài Ý Muốn. Chạy Tiếp Đi :)))')
            
def fTTC():
    global success, error, totalXu
    while True:
        token = input(
            Col.purple + "{" + Col.reset + "?" + Col.purple + "}" + Col.reset + " Nhập Token TuongTacCheo " + Col.purple + "[" + Col.reset + "Nhấn " + Col.blue + "Enter" + Col.reset + " Để Chạy" + Col.purple + "]" + Col.reset + " -> ")
        ttc = TuongTacCheo()
        info = ttc.loginTtcToken(token)
        if info['status'] == 'success':
            info = info['data']
            break
    if os.path.exists('./cookie.txt') == False:
        title("Tạo file chứa cookie")
        open("cookie.txt", "w+", encoding="utf-8-sig")
        
    for ck in open("cookie.txt", "r", encoding="utf-8-sig").read().split("\n"):
        if len(ck) >= 20:
            listCookie.append(ck)
    if listCookie == []:
        input(Col.red + "Vui lòng nhập cookie vào file cookie.txt")
    stt = 0
    xu = info['xu']

    title(f"( TTC ) [ User: {info['user']}] ^| Coin: {info['xu']} ]")
    gom_job = []
    os.system("cls")
    while(True):
        for cookieTik in listCookie:
            __run = time.time()
            tik = TikTok_Api(cookieTik)
            info_tik = tik.Get_cauhinh()
            if info_tik == None:
                print("\033[1;37m- "*40)
                print(Col.purple + "[" + Col.reset + '*' + Col.purple + "]" + Col.reset + f"{Col.yellow} WARNING {Col.blue}! {Col.purple}[{Col.red}COOKIE DIE{Col.purple}]{Col.reset}")
                listCookie.remove(cookieTik)
                if len(listCookie) == 0:
                    print("\033[1;37m- "*40)
                    title("Đã hết cookie để chạy")
                    input("ENTER để thoát tool")
                continue
            cauHinh = ttc.datNickTTC(info_tik['uniqueId'])
            if cauHinh:
                title(f"[ TikTok: {info_tik['nickName']} ^| UID: {info_tik['uid']} ^| Success: {success} ^| Error:  {error} ^| Total Coin Get: {totalXu} ^| Trạng thái: Cấu hình success ]")
            else:
                print("\033[1;37m- "*40)
                print(Col.purple + "[" + Col.reset + '*' + Col.purple + "]" + Col.reset + f"{Col.yellow} WARNING {Col.blue}! {Col.purple}[{Col.red}ID{Col.reset}:{Col.yellow} {info_tik['uid']}{Col.red} Chưa được thêm vào cấu hình{Col.purple}]{Col.reset}")
                continue
            chuyen = False
            while True:
                getjob = ttc.getJobTym()
                title(f"[ TikTok: {info_tik['nickName']} ^| UID: {info_tik['uid']} ^| Success: {success} ^| Error:  {error} ^| Total Coin Get: {totalXu} ^| Trạng thái: Lấy nhiệm vụ Tym ]")
                if getjob == False:
                    title(f"[ TikTok: {info_tik['nickName']} ^| UID: {info_tik['uid']} ^| Success: {success} ^| Error:  {error} ^| Total Coin Get: {totalXu} ^| Trạng thái: Hết nhiệm vụ Tym ]")
                    break
                for job in getjob:
                    id, user = job['idpost'], job['link'].split('/video/')[1]
                    title(f"[ TikTok: {info_tik['nickName']} ^| UID: {info_tik['uid']} ^| Success: {success} ^| Error:  {error} ^| Total Coin Get: {totalXu} ^| Trạng thái: Tym ID {user}]")
                    __start = time.time()
                    follow = tik.likeUser(user)
                    stt += 1
                    if follow == True:
                        print(
                                Col.purple + "[" + Col.reset + f'{stt}' + Col.purple + "]" + Col.reset + f"{Col.reset} Tym Video {Col.blue}! {Col.purple}[{Col.green}SUCCESS {Col.reset}|{Col.cyan} {user}{Col.purple}] {Col.purple}[{Col.blue}Execution: {Col.blue}{round(time.time() - __start, 1)}s{Col.purple}]{Col.reset}")
                        success += 1
                    else:
                        print(
                                Col.purple + "[" + Col.reset + f'{stt}' + Col.purple + "]" + Col.reset + f"{Col.reset} Tym Video {Col.blue}! {Col.purple}[{Col.red}FAILLED {Col.reset}|{Col.cyan} {user}{Col.purple}] {Col.purple}[{Col.blue}Execution: {Col.blue}{round(time.time() - __start, 1)}s{Col.purple}]{Col.reset}")
                        error += 1
                    title(f"[ TikTok: {info_tik['nickName']} ^| UID: {info_tik['uid']} ^| Success: {success} ^| Error:  {error} ^| Total Coin Get: {totalXu} ^| Trạng thái: Tym Done")
                    gom_job.append(id)
                    so_job = len(gom_job)
                    if so_job >= 10:
                        time.sleep(2)
                        getXu = int(ttc.getXuJob(gom_job))
                        gom_job.clear()
                        if getXu == 0:
                            print("\033[1;37m- "*40)
                            print(
                                Col.purple + "[" + Col.reset + '*' + Col.purple + "]" + Col.reset + f"{Col.red} ERROR {Col.blue}! {Col.purple}[{Col.red}Acc Bị Chặn Like Vui Lòng Đổi Acc.{Col.purple}]{Col.reset}")
                            listCookie.remove(cookieTik)
                            if len(listCookie) == 0:
                                print("\033[1;37m- "*40)
                                title(f"[ TikTok: {info_tik['nickName']} ^| UID: {info_tik['uid']} ^| Success: {success} ^| Error:  {error} ^| Total Coin Get: {totalXu} ^| Trạng thái: Hết cookie]")
                                input("ENTER để thoát tool")
                            chuyen = True
                            break
                        print("\033[1;37m- "*40)
                        xu = xu + getXu
                        totalXu += int(getXu)
                        title(f"[ TikTok: {info_tik['nickName']} ^| UID: {info_tik['uid']} ^| Success: {success} ^| Error:  {error} ^| Total Coin Get: {totalXu} ^| Trạng thái: Nhận xu]")
                        chuyen = True
                        break
                if chuyen == True:
                    break
def main():
    if int(input(Col.purple + "{" + Col.reset + "1" + Col.purple + "}" + Col.reset + " Auto TikTok TraoDoiSub " + Col.purple + "[" + Col.reset + " Đa Cookie TikTok" + Col.purple + "]" + Col.reset + "\n" + Col.purple + "{" + Col.reset + "2" + Col.purple + "}" + Col.reset + " Auto TikTok TuongTacCheo " + Col.purple + "[" + Col.reset + " Đa Cookie TikTok" + Col.purple + "]" + Col.reset + Col.purple + "\n{" + Col.reset + "?" + Col.purple + "}" + Col.reset + " Nhập Lựa Chọn" + Col.reset + " ~> ")) == 1:
        os.system('title Auto TDS TikTok');fTDS()
    else:
        os.system('title Auto TTC TikTok');fTTC()
if '__main__' == __name__:
    os.system("Auto Tym TikTok")
    try:
        main()
    except KeyError:
        pass
