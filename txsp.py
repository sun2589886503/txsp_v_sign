import requests
import json
import re
import os

#成长明细
#/fcgi-bin/comm_cgi?name=get_score_flow&score_type=1

# 钉钉机器人的 webhook
webhook = os.environ["https://oapi.dingtalk.com/robot/send?access_token=6bc822ec4fb64e0a680f2b05e2f6bcfa9dc01dbbea41e02c83816194f024ca49"] # 钉钉机器人的 webhook
cookie= os.environ["pgv_pvi=9532715008; pgv_si=s6097810432; pgv_pvid=4728985042; RK=jHQZOoi/cy; ptcz=c878ef3196193867079105954a7aa7da301a56cc96c5749f205f2a90a40b592e; tvfe_boss_uuid=5cb4c653f2d41c26; o_cookie=289804037; sd_userid=22151616114020884; sd_cookie_crttime=1616114020884; wsreq_logseq=323089004; lolqqcomrouteLine=a20210402groovepass; tokenParams=%3Fe_code%3D505452; eas_sid=S1V6X1n7m8R0G1T2y7y1r39917; pgv_info=ssid=s2587555769&pgvReferrer=; _qpsvr_localtk=0.03191865403077143; pac_uid=1_289804037; IED_LOG_INFO=uin*289804037|nick*%u25A1%u25A1%u25A1%20|time*1620562463; dnfqqcomrouteLine=a20190228dpl_a20210506sign_a20210506sign_a20210506sign_a20210506sign_a20210506sign_a20210506sign; login_type=1; wxrefresh_token=; psrf_qqopenid=2B21BBCB9044E5736D2F70591D598DB8; psrf_qqunionid=; euin=owcqNenPoeol; wxopenid=; psrf_qqrefresh_token=AE8F43413B603989A67FC854DA8EDF36; wxunionid=; tmeLoginType=2; psrf_access_token_expiresAt=1628754856; psrf_qqaccess_token=10F2559214A39C6E260C39309A952811; idt=1623833092; iip=0; ptui_loginuin=643056365; midas_openkey=@Fl2Orregc; midas_openid=289804037; video_guid=1e60df7a58d14662; video_platform=2; uin=o0289804037; verifysession=h016e198c269f1e584b8fdde90d2adf7616c7c063d9bec77bfb43ee1b46e6816da5c7786ac039af817c; IED_LOG_INFO2=userUin%3D289804037%26nickName%3D%2525E2%252596%2525A1%2525E2%252596%2525A1%2525E2%252596%2525A1%26nickname%3D%25E2%2596%25A1%25E2%2596%25A1%25E2%2596%25A1%26userLoginTime%3D1625793090%26logtype%3Dqq%26loginType%3Dqq%26uin%3D289804037; _video_qq_login_time_init=1625796121; main_login=qq; vqq_access_token=6D59A62A6928CAB591F0C4CA47DDC98B; vqq_appid=101483052; vqq_openid=3CC82F4EC2BF9ABB6F13F59E5FE45C1C; vqq_vuserid=361142255; vqq_vusession=a-WzjUDMuZjxCh0dRnTwbg..; vqq_refresh_token=BA487CE5A5227D0C8A0474E35DABCA9F; login_time_init=2021-7-11 17:33:41; uid=85500769; "] #腾讯spcookie
headers = {
    'Referer': 'https://film.qq.com/x/autovue/grade/?ptag=Vgrade.rule',
    'Content-Type': 'text/plain;charset=UTF-8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.54',
    'Referer':'https://v.qq.com',
    'Cookie':cookie
}
global content
contents=''
def output(content):
    global contents
    contents += '\n' + content
    print(content)
    return contents
def sign_1():
    # 观看60分钟签到请求
    url_1 ='https://vip.video.qq.com/fcgi-bin/comm_cgi?name=spp_MissionFaHuo&cmd=4&task_id=1&_=1582997048625&callback=Zepto1582997031843'
    sign_1 = requests.get(url=url_1,headers=headers)
    content = re.findall('\{[^\}]+\}', sign_1.text)[0]
    contents=json.loads(content)['msg']
    output(f'[+] 观看60分钟签到状态： {contents}')
def sign_3():
    # 弹幕签到请求
    url_3 =  'https://vip.video.qq.com/fcgi-bin/comm_cgi?name=spp_MissionFaHuo&cmd=4&task_id=3&_=1582368319252&callback=Zepto1582368297765'
    sign_3 = requests.get(url=url_3,headers=headers)
    content = re.findall('\{[^\}]+\}', sign_3.text)[0]
    contents=json.loads(content)['msg']
    output(f'[+] 弹幕签到状态： {contents}')
    
def sign_6():
    # 赠送签到请求
    url_6 =  'https://vip.video.qq.com/fcgi-bin/comm_cgi?name=spp_MissionFaHuo&cmd=4&task_id=6&_=1582366326994&callback=Zepto1582366310545'
    sign_6 = requests.get(url=url_6,headers=headers)
    content = re.findall('\{[^\}]+\}', sign_6.text)[0]
    contents=json.loads(content)['msg']
    output(f'[+] 赠送签到状态： {contents}')
    
def sign_7():
    # 下载签到请求
    url_7 = 'https://vip.video.qq.com/fcgi-bin/comm_cgi?name=spp_MissionFaHuo&cmd=4&task_id=7&_=1582364733058&callback=Zepto1582364712694'  
    sign_7 = requests.get(url=url_7,headers=headers)
    content = re.findall('\{[^\}]+\}', sign_7.text)[0]
    contents=json.loads(content)['msg']
    output(f'[+] 下载签到状态： {contents}')
    
# 签到请求 20v力   
def sign_10():
    url_10 = 'https://vip.video.qq.com/fcgi-bin/comm_cgi?name=hierarchical_task_system&cmd=2&_=1555060502385&callback=Zepto1555060502385'
    sign_10 = requests.get(url=url_10,headers=headers)
    content = re.findall('\{[^\}]+\}', sign_10.text)[0]
    contents=json.loads(content)['msg']
    output(f'[+] 签到请求1状态： {contents}')
   
# 签到请求,随机
def sign_11():
    url_11 = 'https://v.qq.com/x/bu/mobile_checkin'
    sign_11 = requests.get(url=url_11,headers=headers)
    #content = re.findall('\{[^\}]+\}', sign_11.text)[0]
    #contents=json.loads(content)['msg']
    #print(f'[+] 签到请求2状态： {contents}')
    if 'Unauthorized' in sign_11:
        output ('[+] 签到请求2状态：  错误,Cookie 失效')
       
    else:
        output ('[+] 签到请求2状态：  成功')
        

def userinfo():
    header = {
    'Host': 'vip.video.qq.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.54',
    'Cookie':'tvfe_boss_uuid=fff6e261fdba336a; pgv_pvid=6821202755; video_platform=2; video_guid=2d0a084412b55178; uin=o0753476038; skey=@NQgPsvEUE; RK=4YyJuUobT8; luin=o0753476038; lskey=00010000ce7372c16fe52c61283aa90966dbc5c8bead2fe8372f220a2461bdb560951ec12179fa0bb377fa88; ptcz=9b5d1500609128b17f085cb97b737bf47f005d34215333107cb262ec7d473d4f; qq_nick=%25E6%25A1%259C; qq_head=http%3A%2F%2Fthirdqq.qlogo.cn%2Fg%3Fb%3Dsdk%26k%3DsslUu06z79AOu48ZNd7PNg%26s%3D140%26t%3D1621760613; main_login=qq; vuserid=155043867; vusession=SWZlb4ckl3FjTLg9okMkoA..; last_refresh_time=1624196483264; last_refresh_vuserid=155043867;',
    'Referer': 'https://film.qq.com/x/autovue/grade/?ptag=Vgrade.rule',
    }
    #获取用户信息
    url= 'https://vip.video.qq.com/rpc/trpc.query_vipinfo.vipinfo.QueryVipInfo/GetVipUserInfoH5'
    data={
        "geticon":1,
        "viptype":"svip",
        "platform":100
        }
    userinfo = requests.post(url=url,json=data,headers=header)
    #当前V力值
    level_score=json.loads(userinfo.text)['score']
    output(f'[+] 当前V力值： {level_score}')
   
def dingtalk(contents):
    webhook_url = webhook
    dd_header = {"Content-Type": "application/json", "Charset": "UTF-8"}
    dd_message = {
        "msgtype": "text",
        "text": {
            "content": f'腾讯视频签到提醒！\n{contents}'
        }
    }
    r = requests.post(url=webhook_url,headers=dd_header,data=json.dumps(dd_message))
    if r.status_code == 200:
        print('[+] 钉钉消息已推送，请查收  ')
def main():
    title='开始签到'
    content_1=sign_1()
    content_3=sign_3()
    content_6=sign_6()
    content_7=sign_7()
    content_10=sign_10()
    content_11=sign_11()
    content_userinfo=userinfo()
    global contents
    #dingtalk(contents)

if __name__ == '__main__':
    main()   
