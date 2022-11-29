import imp
import re
import json
import time
import names
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from twocaptcha import TwoCaptcha
from selenium.webdriver.common.by import By

with open('config.json') as config:
    script_config = json.load(config)

captcha_config = {
            'server': '2captcha.com',
            'apiKey': '8fd1a9973973bf0093d3d1540f3ff0f3',
            'softId':  123,
            'callback': 'https://your.site/result-receiver',
            'defaultTimeout':    120,
            'recaptchaTimeout':  600,
            'pollingInterval':   10,
        }

class Generator:
    def __init__(self):
        print("--------")
        print("CONFIG")
        print(script_config)
        print('----------')
        print('1. Create Accounts <> 2. Get Presale Codes')
        print('----------')
        opt = input('Enter Input --> ')
        if opt == '1':
            opt2 = input('How many accounts ? --> ? ')
            for i in range(int(opt2)):
                self.get_page()
        if opt == '2':
            print('Wait! Currently in development...')

    def __get_captcha(self):
        api_key = '8fd1a9973973bf0093d3d1540f3ff0f3'
        solver = TwoCaptcha(api_key)
        solver = TwoCaptcha(**captcha_config)
        result = solver.recaptcha(
                sitekey='6LfiUs8ZAAAAABb8MIdgSOktw4LFBV5YX471E58i',
                url='https://www.metallica.com/register/',
                version='v2'
        )

        response = result['captchaId']
        time.sleep(5)
        captcha_result = self.s.get(f'http://2captcha.com/res.php?key={api_key}&action=get&id={response}&json=1')
        request = captcha_result.json()['request']
        max_retry = 0
        while request == 'CAPTCHA_NOT_READY':
            print('retrying...')
            if max_retry < 5:
                time.sleep(3)
                captcha_result = self.s.get(f'http://2captcha.com/res.php?key={api_key}&action=get&id={response}&json=1')
                request = captcha_result.json()['request']
                max_retry += 1
            else:
                break

        print(f'captcha response... {captcha_result.status_code}')
        return request

    def get_cookie(self):
        driver = webdriver.Firefox(executable_path='//Users//ty//Downloads//geckodriver\ 2 ')
        driver.implicitly_wait(30)
        driver.get('https://www.metallica.com/register/')

        time.sleep(5)
        
        cookies_list = driver.get_cookies();
        cookies_dict = {}
        for cookie in cookies_list:
            cookies_dict[cookie['name']] = cookie['value']
        
        __cq_dnt = cookies_dict['__cq_dnt']
        dw_dnt = cookies_dict['dw_dnt']
        _gcl_au = cookies_dict['_gcl_au']
        _fbp = cookies_dict['_fbp']
        _gid = cookies_dict['_gid']
        _tt_enable_cookie = cookies_dict['_tt_enable_cookie']
        _ttp = cookies_dict['_ttp']
        _li_dcdm_c = cookies_dict['_li_dcdm_c']
        _lc2_fpi = cookies_dict['_lc2_fpi']
        __cq_uuid = cookies_dict['__cq_uuid']
        __cq_seg = cookies_dict['__cq_seg']
        dw = 1
        dw_cookies_accepted = 1
        _sp_ses = cookies_dict['_sp_ses.12ed']
        cquid = cookies_dict['cquid']
        _gat_UA = 1
        sid = cookies_dict['sid']
        dwsid = cookies_dict['dwsid']
        dwanonymous_14a9e20de599203e490e731dc5bac197 = cookies_dict['dwanonymous_14a9e20de599203e490e731dc5bac197']
        dwac_c26e5001b1c5ffde452d7bcd56 = cookies_dict['dwac_c26e5001b1c5ffde452d7bcd56']
        cqcid = cookies_dict['cqcid']
        _dc_gtm_UA = cookies_dict['_dc_gtm_UA-11214620-1']
        _ga = cookies_dict['_ga']
        _sp_id = cookies_dict['_sp_id.12ed']
        _ga_A = cookies_dict['_ga_8MT9WZCNB1']
        _ga_B = cookies_dict['_ga_QKEQR920KZ']

        # registration_form = driver.find_element(By.NAME, 'csrf_token')
        # print(registration_form.text)

        return f"""__cq_dnt={__cq_dnt}; dw_dnt={dw_dnt}; _gcl_au={_gcl_au}; _fbp={_fbp}; _gid={_gid}; _tt_enable_cookie={_tt_enable_cookie}; _ttp={_ttp}; _li_dcdm_c={_li_dcdm_c}; _lc2_fpi={_lc2_fpi}; __cq_uuid={__cq_uuid}; __cq_seg={__cq_seg}; dw={dw}; dw_cookies_accepted={dw_cookies_accepted}; _sp_ses.12ed={_sp_ses}; cquid={cquid}; _gat_UA-11214620-1={_gat_UA}; sid={sid}; dwsid={dwsid}; dwanonymous_14a9e20de599203e490e731dc5bac197={dwanonymous_14a9e20de599203e490e731dc5bac197}; dwac_c26e5001b1c5ffde452d7bcd56={dwac_c26e5001b1c5ffde452d7bcd56}; cqcid={cqcid}; _dc_gtm_UA-11214620-1={_dc_gtm_UA}; _ga={_ga}; _sp_id.12ed={_sp_id}; _ga_8MT9WZCNB1={_ga_A}; _ga_QKEQR920KZ={_ga_B};"""


    def get_page(self):
        self.s = requests.session()
        page = self.s.get('https://metallica.com/register', headers={
            'authority': 'metallica.com',
            'path': f'/register',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
        })
   

        # print(page.cookies.get_dict())
        print(f'get page response... {page.status_code}')
        if page.status_code == 200:
            soup = BeautifulSoup(page.text,"html.parser")
            self.registration_csrf = soup.find("input", {"name":"csrf_token"})['value']
            self.password_html = soup.find_all('input', {'type': 'password'})
            self.password_field = self.password_html[0]['id']
            self.confirm_password_field = self.password_html[1]['id']
            self.captcha_token = self.__get_captcha()
            self.cookie = self.get_cookie()
            self.create_account()

    def create_account(self):
        self.first = names.get_first_name()
        self.last = names.get_last_name()
        data = {
            'dwfrm_profile_register_firstname': self.first,
            'dwfrm_profile_register_lastname': self.last,
            'dwfrm_profile_customer_username': f'{self.first}{self.last}123',
            'dwfrm_profile_register_email': f'{self.first}{self.last}123{script_config["catchall"]}',
            'dwfrm_profile_register_emailconfirm': f'{self.first}{self.last}123{script_config["catchall"]}',
            self.password_field: script_config["password"],
            self.confirm_password_field: script_config["password"],
            'dwfrm_profile_register_birthday': '05/06/2001',
            'dwfrm_profile_customer_gender': '1',
            'dwfrm_profile_customer_country': 'us',
            'dwfrm_profile_customer_postal': '18704',
            'g-recaptcha-response': self.captcha_token,
            'dwfrm_profile_confirm': 'Apply',
            'csrf_token': self.registration_csrf
        }
        
        createAcc = self.s.post(f'https://metallica.com/on/demandware.store/Sites-Metallica-Site/default/Account-RegistrationForm?&format=ajax',data=data,headers={
            'authority':'www.metallica.com',
            'path': '/on/demandware.store/Sites-Metallica-Site/Account-RegistrationForm',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language':'en-US,en;q=0.9',
            'content-length': '1296',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': self.cookie,
            'origin': 'https://www.metallica.com',
            'referer': f'https://www.metallica.com/register',
            'sec-ch-ua': """sec-ch-ua: "Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24" """,
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': 'macOS',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest'
        })
    
        print(f'create response... {createAcc.json()}')
        self.email = f'{self.first}{self.last}123{script_config["catchall"]}:{script_config["password"]}'
        print(f'{self.first}{self.last}123{script_config["catchall"]}:{script_config["password"]}')
        with open('accounts.txt','a') as accountFile:
            accountFile.write(f'{self.first}{self.last}123{script_config["catchall"]}:{script_config["password"]}\n')
        with open('accountsWithNames.txt','a') as accountFile:
            accountFile.write(f'{self.first}{self.last}123{script_config["catchall"]}:{script_config["password"]}:{self.first}:{self.last}\n')

Generator()