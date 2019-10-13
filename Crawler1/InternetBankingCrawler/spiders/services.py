import json
from typing import List, Tuple

config = {}


def read_config(file_path):
    global config
    with open(file_path) as r:
        content = r.read()
        config = json.loads(content)


class ConfigService:
    def __init__(self, file: str):
        if not config:
            read_config(file)

        self.config = config

    def get_search_keywords(self) -> List[str]:
        return self.config['keywords']


class LoginRequestService:

    def __init__(self):
        self.do_login_url = 'https://www.bancsabadell.com/txbs/LoginDNISCA.doLogin.bs?language=ENG'
        self.do_login_headers = {
            'Host': 'www.bancsabadell.com',
            'Connection': 'keep-alive',
            # 'Content-Length': '4598',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'DNT': '1',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/77.0.3865.90 Chrome/77.0.3865.90 Safari/537.36',
            'Sec-Fetch-Mode': 'cors',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://www.bancsabadell.com',
            'Sec-Fetch-Site': 'same-origin',
            'Referer': 'https://www.bancsabadell.com/cs/Satellite/SabAtl/Particulares/1191332204474/en/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-MT,en;q=0.9,ro-RO;q=0.8,ro;q=0.7,es-ES;q=0.6,es;q=0.5,ar-EG;q=0.4,ar;q=0.3,en-US;q=0.2',
            'apikey': 'NzSvsHgWN80FXBUJ'
        }

        self.do_login_cookies = {
            'BSOP_FW': '',
            'TS01437867': '016e0ef7e5afea15405d9172bc00ca58ea6c684a2fe927d4baf3a7b1318129896653955d5d8492171ca0ea1a75a569b70bf031dac94e2ed157821422f2cef8096ee2661ac8cba92123861de3e0c8e1daa2865788b6a97a57983d9dac7a2dc7568235bfff7c',
            'JSESSIONID': '36ED019346EDDCA51F7C3FA8DAE5E964.FatwireServer4_CS76',
            'FTWCOOKIE': 'rd1o00000000000000000000ffffac121689o7360',
            'BigIP_LTM_CBS': '34804396.48129.0000',
            'bmuid': '1570634900815-8CAE446C-A542-4B09-9C70-E0ED06E996A8',
            'isBancaPrivada': 'false',
            'DeviceTokenCookie': '37.223.221.153.1570634906810',
            'mid': '7445460524411003168',
            'sc_fuentetrafico': 'none',
            '___r9154651': '0.0216354744487',
            'AMCV0A43C2415798EF2E7F000101AdobeOrgS': '1',
            's_campaign': 'Dominios%20de%20referencia',
            's_gts': '1',
            's_mco2': '%5B%5B%27Dominios%2520de%2520referencia%27%2C%271570634915218%27%5D%5D',
            's_cc': 'true',
            'aam_uuid': '50030376753425476083180558876167064976',
            'LOGINTYPE': '1',
            'BSOP_PP': 'RIGHTSIZING_COMPARATOR|BSO_IBIZUM|BSO_WELCOME|BSO_MOD_GESTOR|BSO_DNINEW|BSO_RENTING',
            'IberMarketOperations': 'false',
            'BSPersonalizacion': '3110_00000000_0_0__120_0_0_0_0_1222100211100_11101_7__0_____________211_____32________01__03_0011___________________________________________12__________________________________________________________',
            'INTERCOOKIE': 'rd1o00000000000000000000ffffac121674o5628',
            'FFPPSESSION': 'rd1o00000000000000000000ffffac12164bo8520',
            's_nr': '1570635233546',
            'SA_Session': '1191332204474_1178258082826',
            'SA_Session_404': '1191332204474_1178258082826',
            'JSESSIONID_JBSWL': '36ED019346EDDCA51F7C3FA81570637432375',
            '___tk915465': '0.38622413022634317',
            'TS018632ca': '016e0ef7e50a39a4eb5a9064f793a7e96977a09534a3c0875bb00b8ddf301b889c18553beca6543894990e6bb987ef29d142d0384182e222528b5b511184342817de5773fdc3f036a1a97bc0cf446d750597345867cfd96c722125da23f83037dc56dfc2e8d049177ef55e83e410d73639553183a251c90012425c1a7b6a6ed242197ee90c26f4fc5847d4cc43026ca2616c516fd6be31d77c74f0dbfed0de399efc146a12',
            '___tk9154651': '0.2623625285503668',
            'cdContextId': '14',
            'segmento': 'Particulares',
            'logout': '',
            'LSESSIONID': 'jLd1oKQU4oggdyuHKxIt3D4Iqf2So3TdVk23EXavFtPX08UvP8J158KiYnKKy4sIQkmZH6MkjBQYLFmVeac%3D',
            'cdSNum': '1570899162654-sji0000628-f7a511c7-cea9-4405-96d0-aac53126774e',
            'utag_main': 'v_id:016db122b0220014d7756af1aa9502085004f07d00bd0$_sn:3$_ss:1$_st:1570901077028$vapi_domain:bancsabadell.com',
            'aceptacionCookies_SabAtl': 'true',
            '___so9154651': 'eyJsc2giOjM2NjYxNDU5ODAsInNkIjpudWxsLCJzZGMiOm51bGwsImUiOnsibiI6MywiYSI6W3siMzAiOnRydWUsInNyIjoiaHR0cHM6Ly93d3cuYmFuY3NhYmFkZWxsLmNvbS9TdGF0aWNGaWxlcy9TYWJBdGwvaW1nL2ljb25vcy9pY192aW5GaW5QYWdlLmdpZiJ9LCIzMCJdLCJyaWQiOjAuMzE0NTM5MTAxMTg3MDQ1NzZ9LCJyIjoiL2NzL1NhdGVsbGl0ZS9TYWJBdGwvUGFydGljdWxhcmVzLzExOTEzMzIyMDQ0NzQvZW4vIiwibiI6MTAsImMiOjEwLCJtayI6W119',
            'AMCV0A43C2415798EF2E7F000101AdobeOrg': '-1712354808%7CMCIDTS%7C18182%7CMCMID%7C50282985127791910493208212113197835265%7CMCAAMLH-1571504077%7C6%7CMCAAMB-1571504077%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1570906477s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-18186%7CvVersion%7C4.3.0',
            's_vnum': '1573226915194%26vn%3D3',
            's_invisit': 'true',
            's_mco1': '%5B%5B%27TraficoDirecto%27%2C%271570637096120%27%5D%2C%5B%27TraficoDirecto%27%2C%271570637117002%27%5D%2C%5B%27TraficoDirecto%27%2C%271570637119121%27%5D%2C%5B%27TraficoDirecto%27%2C%271570899277443%27%5D%2C%5B%27TraficoDirecto%27%2C%271570899277532%27%5D%5D'
        }

        self.do_login_form_data = {
            'pin': 'xxxxxx',
            'language': 'ENG',
            'signText': '',
            'msgLogin': 'PERTaWduYXR1cmVDbGllbnQtT3BlcmF0aW9uPkdlbmVyaWNTaWduPC9EU2lnbmF0dXJlQ2xpZW50LU9wZXJhdGlvbj48RFNpZ25hdHVyZUNsaWVudC1QYXJhbWV0ZXIgbmFtZT0iRGF0YSI%2BMTE5MjYwNjc2NTY3MDwvRFNpZ25hdHVyZUNsaWVudC1QYXJhbWV0ZXI%2BPERTaWduYXR1cmVDbGllbnQtUGFyYW1ldGVyIG5hbWU9IlNpZ25hdHVyZVR5cGUiPlN0YW5kYXJkPC9EU2lnbmF0dXJlQ2xpZW50LVBhcmFtZXRlcj48RFNpZ25hdHVyZUNsaWVudC1QYXJhbWV0ZXIgbmFtZT0iUHJvdmlkZXIiPjwvRFNpZ25hdHVyZUNsaWVudC1QYXJhbWV0ZXI%2BPERTaWduYXR1cmVDbGllbnQtUGFyYW1ldGVyIG5hbWU9IkFwcGxpY2F0aW9uIj5CUzwvRFNpZ25hdHVyZUNsaWVudC1QYXJhbWV0ZXI%2BPERTaWduYXR1cmVDbGllbnQtUGFyYW1ldGVyIG5hbWU9Ik5vQ2VydGlmaWNhdGVzVVJMIj4vdHhicy9zdGFydC5pbml0LmJzPC9EU2lnbmF0dXJlQ2xpZW50LVBhcmFtZXRlcj48RFNpZ25hdHVyZUNsaWVudC1QYXJhbWV0ZXIgbmFtZT0iSWRpb21hSUQiPjE8L0RTaWduYXR1cmVDbGllbnQtUGFyYW1ldGVyPjxEU2lnbmF0dXJlQ2xpZW50LVBhcmFtZXRlciBuYW1lPSJJZ25vcmVUb2tlbiI%2BZmFsc2U8L0RTaWduYXR1cmVDbGllbnQtUGFyYW1ldGVyPjxEU2lnbmF0dXJlQ2xpZW50LVBhcmFtZXRlciBuYW1lPSJJbWFnZUdyYWRpZW50ZSI%2BL2czcmVwb3NpdG9yeS9HRU4vTE9HT19CU19MT0dPQlMuR0lGPC9EU2lnbmF0dXJlQ2xpZW50LVBhcmFtZXRlcj48RFNpZ25hdHVyZUNsaWVudC1QYXJhbWV0ZXIgbmFtZT0iTG9nb1Byb3ZpZGVyVVJMIj4vZzNyZXBvc2l0b3J5L0dFTi9MT0dPX0JTX0xPR09CUy5HSUY8L0RTaWduYXR1cmVDbGllbnQtUGFyYW1ldGVyPg%3D%3D',
            'signLogin': 'MIID%2FAYJKoZIhvcNAQcCoIID7TCCA%2BkCAQExCzAJBgUrDgMCGgUAMAsGCSqGSIb3DQEHAaCCAtIwggLOMIICN6ADAgECAhA1vxLflU%2FsDO6wvIXk%2B791MA0GCSqGSIb3DQEBBQUAMDoxEzARBgNVBAoTCmUteHRlbmRub3cxIzAhBgNVBAMTGmUteHRlbmRub3cgQ2xhc3MgMyBDQSB0ZXN0MB4XDTAzMTEyNzAwMDAwMFoXDTA0MTEyNjIzNTk1OVowfjETMBEGA1UEChQKZS14dGVuZG5vdzEfMB0GA1UECxQWRm9yIFRlc3QgUHVycG9zZXMgT25seTETMBEGA1UEAxMKZXh0ZW5kIGdmcDEPMA0GA1UEKhMGZXh0ZW5kMQwwCgYDVQQEEwNnZnAxEjAQBgNVBAUTCTExMTExMTExSDCBnzANBgkqhkiG9w0BAQEFAAOBjQAwgYkCgYEA0%2BgGQVMeNHv7u8Zz8Xly%2B5%2B80FwZhX6p9osupPKmoYCr%2BIB1U03s4LDVZznkR98zicKJqt3U8evssm6toUhpwfd1dAeOq%2BUmrKa3Mz3e5WW2FK5rw30sDMpjZSxHDK66z2czJrYVijIDPqfFYUuicUDzcUPNC%2BJLxJG7q3VUCysCAwEAAaOBkDCBjTALBgNVHQ8EBAMCBaAwCQYDVR0TBAIwADBNBgNVHR8ERjBEMEKgQKA%2BhjxodHRwOi8vcGlsb3RvbnNpdGVjcmwuYWNlLmVzL2V4dGVuZG5vd0lUQ2xhc3MzL0xhdGVzdENSTC5jcmwwEQYJYIZIAYb4QgEBBAQDAgeAMBEGCmCGSAGG%2BEUBBgkEAwEB%2FzANBgkqhkiG9w0BAQUFAAOBgQBtFWcEumky5yVG9fjrAtpwjWTLGkrOd1zTzc03SvUokJcJz9LQvH6iZ0K6Mo1AdX60hJnXskbKWEw93ItvgKsBxf6nUp2CIdj%2FXOk4KQvzZfrb%2F9JLtcA2SfcwMGeSN%2BK3DbuNy51kf%2BLSMK1AwDCEU9OfhOycRkZ0ApEDz9YGFzGB8zCB8AIBATBOMDoxEzARBgNVBAoTCmUteHRlbmRub3cxIzAhBgNVBAMTGmUteHRlbmRub3cgQ2xhc3MgMyBDQSB0ZXN0AhA1vxLflU%2FsDO6wvIXk%2B791MAkGBSsOAwIaBQAwDQYJKoZIhvcNAQEBBQAEgYBGY%2BdR0v%2BW4LVoVNqJgUgDuVoX8tNW1wOQOUXi4iVHzcZ%2BvU7kOZv4gS8W5EJuHQT3U7O%2FbnhuHL7BputnausEXfsJcqcBJEzS1RZqpdJFRGHs-wgB20lbvnfOyvb814xq6m9y8tUFwFMhm%2B%2BVRowAlfHwzxiGvKZP5XH9E6GKOnQ%3D%3D',
            'evision.userLang': '',
            'evision.RSADeviceFso': '',
            'evision.csid': '36ED019346EDDCA51F7C3FA81570637432375',
            'evision.deviceTokenCookie': '37.223.221.153.1570634906810',
            'evision.RSADevicePrint': 'version%253D3%252E5%252E1%255F4%2526pm%255Ffpua%253Dmozilla%252F5%252E0%2520%2528x11%253B%2520linux%2520x86%255F64%2529%2520applewebkit%252F537%252E36%2520%2528khtml%252C%2520like%2520gecko%2529%2520ubuntu%2520chromium%252F77%252E0%252E3865%252E90%2520chrome%252F77%252E0%252E3865%252E90%2520safari%252F537%252E36%257C5%252E0%2520%2528X11%253B%2520Linux%2520x86%255F64%2529%2520AppleWebKit%252F537%252E36%2520%2528KHTML%252C%2520like%2520Gecko%2529%2520Ubuntu%2520Chromium%252F77%252E0%252E3865%252E90%2520Chrome%252F77%252E0%252E3865%252E90%2520Safari%252F537%252E36%257CLinux%2520x86%255F64%2526pm%255Ffpsc%253D24%257C1920%257C1080%257C1053%2526pm%255Ffpsw%253D%2526pm%255Ffptz%253D1%2526pm%255Ffpln%253Dlang%253Den%252DMT%257Csyslang%253D%257Cuserlang%253D%2526pm%255Ffpjv%253D0%2526pm%255Ffpco%253D1%2526pm%255Ffpasw%253Dinternal%252Dpdf%252Dviewer%257Cmhjfbmdgcfjbbpaeojofohoefgiehjai%2526pm%255Ffpan%253DNetscape%2526pm%255Ffpacn%253DMozilla%2526pm%255Ffpol%253Dtrue%2526pm%255Ffposp%253D%2526pm%255Ffpup%253D%2526pm%255Ffpsaw%253D1853%2526pm%255Ffpspd%253D24%2526pm%255Ffpsbd%253D%2526pm%255Ffpsdx%253D%2526pm%255Ffpsdy%253D%2526pm%255Ffpslx%253D%2526pm%255Ffpsly%253D%2526pm%255Ffpsfse%253D%2526pm%255Ffpsui%253D%2526pm%255Fos%253DLinux%2526pm%255Fbrmjv%253D77%2526pm%255Fbr%253DChrome%2526pm%255Finpt%253D%2526pm%255Fexpt%253D',
            'userDNI': 'Y6957175B',
            'userCard': '',
            'pinDNI': '',
            'injvalrnd': 'false',
            'injextrnd': '',
            'inputAtributes0': '',
            'inputAtributes1': 'en-MT',
            'inputAtributes2': '24',
            'inputAtributes3': '8',
            'inputAtributes4': '4',
            'inputAtributes5': '1920%2C1080',
            'inputAtributes6': '-120',
            'inputAtributes7': 'Europe%2FMadrid',
            'inputAtributes8': 'Linux+x86_64',
            'inputAtributes9': 'Intel+Open+Source+Technology+Center~Mesa+DRI+Intel(R)+HD+Graphics+5500+(Broadwell+GT2)+',
            'inputAtributes10': 'false',
            'inputAtributes11': '15%2Cfalse%2Cfalse'
        }

        self.do_set_logged_in_url = 'https://www.bancsabadell.com/txbs/LoginDNISCA.setLogged.bs?language=ENG'
        self.do_set_logged_in_headers = {
            'Host': 'www.bancsabadell.com',
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Origin': 'https://www.bancsabadell.com',
            'Upgrade-Insecure-Requests': '1',
            'DNT': '1',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/77.0.3865.90 Chrome/77.0.3865.90 Safari/537.36',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Sec-Fetch-Site': 'same-origin',
            'Referer': 'https://www.bancsabadell.com/cs/Satellite/SabAtl/Particulares/1191332204474/en/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-MT,en;q=0.9,ro-RO;q=0.8,ro;q=0.7,es-ES;q=0.6,es;q=0.5,ar-EG;q=0.4,ar;q=0.3,en-US;q=0.2',
            'apikey': 'NzSvsHgWN80FXBUJ'
        }

        self.do_set_logged_in_form_data = {
            'pin': 'xxxxxx',
            'language': 'ENG',
            'signText': '',
            'msgLogin': 'PERTaWduYXR1cmVDbGllbnQtT3BlcmF0aW9uPkdlbmVyaWNTaWduPC9EU2lnbmF0dXJlQ2xpZW50LU9wZXJhdGlvbj48RFNpZ25hdHVyZUNsaWVudC1QYXJhbWV0ZXIgbmFtZT0iRGF0YSI%2BMTE5MjYwNjc2NTY3MDwvRFNpZ25hdHVyZUNsaWVudC1QYXJhbWV0ZXI%2BPERTaWduYXR1cmVDbGllbnQtUGFyYW1ldGVyIG5hbWU9IlNpZ25hdHVyZVR5cGUiPlN0YW5kYXJkPC9EU2lnbmF0dXJlQ2xpZW50LVBhcmFtZXRlcj48RFNpZ25hdHVyZUNsaWVudC1QYXJhbWV0ZXIgbmFtZT0iUHJvdmlkZXIiPjwvRFNpZ25hdHVyZUNsaWVudC1QYXJhbWV0ZXI%2BPERTaWduYXR1cmVDbGllbnQtUGFyYW1ldGVyIG5hbWU9IkFwcGxpY2F0aW9uIj5CUzwvRFNpZ25hdHVyZUNsaWVudC1QYXJhbWV0ZXI%2BPERTaWduYXR1cmVDbGllbnQtUGFyYW1ldGVyIG5hbWU9Ik5vQ2VydGlmaWNhdGVzVVJMIj4vdHhicy9zdGFydC5pbml0LmJzPC9EU2lnbmF0dXJlQ2xpZW50LVBhcmFtZXRlcj48RFNpZ25hdHVyZUNsaWVudC1QYXJhbWV0ZXIgbmFtZT0iSWRpb21hSUQiPjE8L0RTaWduYXR1cmVDbGllbnQtUGFyYW1ldGVyPjxEU2lnbmF0dXJlQ2xpZW50LVBhcmFtZXRlciBuYW1lPSJJZ25vcmVUb2tlbiI%2BZmFsc2U8L0RTaWduYXR1cmVDbGllbnQtUGFyYW1ldGVyPjxEU2lnbmF0dXJlQ2xpZW50LVBhcmFtZXRlciBuYW1lPSJJbWFnZUdyYWRpZW50ZSI%2BL2czcmVwb3NpdG9yeS9HRU4vTE9HT19CU19MT0dPQlMuR0lGPC9EU2lnbmF0dXJlQ2xpZW50LVBhcmFtZXRlcj48RFNpZ25hdHVyZUNsaWVudC1QYXJhbWV0ZXIgbmFtZT0iTG9nb1Byb3ZpZGVyVVJMIj4vZzNyZXBvc2l0b3J5L0dFTi9MT0dPX0JTX0xPR09CUy5HSUY8L0RTaWduYXR1cmVDbGllbnQtUGFyYW1ldGVyPg%3D%3D',
            'signLogin': 'MIID%2FAYJKoZIhvcNAQcCoIID7TCCA%2BkCAQExCzAJBgUrDgMCGgUAMAsGCSqGSIb3DQEHAaCCAtIwggLOMIICN6ADAgECAhA1vxLflU%2FsDO6wvIXk%2B791MA0GCSqGSIb3DQEBBQUAMDoxEzARBgNVBAoTCmUteHRlbmRub3cxIzAhBgNVBAMTGmUteHRlbmRub3cgQ2xhc3MgMyBDQSB0ZXN0MB4XDTAzMTEyNzAwMDAwMFoXDTA0MTEyNjIzNTk1OVowfjETMBEGA1UEChQKZS14dGVuZG5vdzEfMB0GA1UECxQWRm9yIFRlc3QgUHVycG9zZXMgT25seTETMBEGA1UEAxMKZXh0ZW5kIGdmcDEPMA0GA1UEKhMGZXh0ZW5kMQwwCgYDVQQEEwNnZnAxEjAQBgNVBAUTCTExMTExMTExSDCBnzANBgkqhkiG9w0BAQEFAAOBjQAwgYkCgYEA0%2BgGQVMeNHv7u8Zz8Xly%2B5%2B80FwZhX6p9osupPKmoYCr%2BIB1U03s4LDVZznkR98zicKJqt3U8evssm6toUhpwfd1dAeOq%2BUmrKa3Mz3e5WW2FK5rw30sDMpjZSxHDK66z2czJrYVijIDPqfFYUuicUDzcUPNC%2BJLxJG7q3VUCysCAwEAAaOBkDCBjTALBgNVHQ8EBAMCBaAwCQYDVR0TBAIwADBNBgNVHR8ERjBEMEKgQKA%2BhjxodHRwOi8vcGlsb3RvbnNpdGVjcmwuYWNlLmVzL2V4dGVuZG5vd0lUQ2xhc3MzL0xhdGVzdENSTC5jcmwwEQYJYIZIAYb4QgEBBAQDAgeAMBEGCmCGSAGG%2BEUBBgkEAwEB%2FzANBgkqhkiG9w0BAQUFAAOBgQBtFWcEumky5yVG9fjrAtpwjWTLGkrOd1zTzc03SvUokJcJz9LQvH6iZ0K6Mo1AdX60hJnXskbKWEw93ItvgKsBxf6nUp2CIdj%2FXOk4KQvzZfrb%2F9JLtcA2SfcwMGeSN%2BK3DbuNy51kf%2BLSMK1AwDCEU9OfhOycRkZ0ApEDz9YGFzGB8zCB8AIBATBOMDoxEzARBgNVBAoTCmUteHRlbmRub3cxIzAhBgNVBAMTGmUteHRlbmRub3cgQ2xhc3MgMyBDQSB0ZXN0AhA1vxLflU%2FsDO6wvIXk%2B791MAkGBSsOAwIaBQAwDQYJKoZIhvcNAQEBBQAEgYBGY%2BdR0v%2BW4LVoVNqJgUgDuVoX8tNW1wOQOUXi4iVHzcZ%2BvU7kOZv4gS8W5EJuHQT3U7O%2FbnhuHL7BputnausEXfsJcqcBJEzS1RZqpdJFRGHs-wgB20lbvnfOyvb814xq6m9y8tUFwFMhm%2B%2BVRowAlfHwzxiGvKZP5XH9E6GKOnQ%3D%3D',
            'evision.userLang': '',
            'evision.RSADeviceFso': '',
            'evision.csid': '36ED019346EDDCA51F7C3FA81570637432375',
            'evision.deviceTokenCookie': '37.223.221.153.1570634906810',
            'evision.RSADevicePrint': 'version%253D3%252E5%252E1%255F4%2526pm%255Ffpua%253Dmozilla%252F5%252E0%2520%2528x11%253B%2520linux%2520x86%255F64%2529%2520applewebkit%252F537%252E36%2520%2528khtml%252C%2520like%2520gecko%2529%2520ubuntu%2520chromium%252F77%252E0%252E3865%252E90%2520chrome%252F77%252E0%252E3865%252E90%2520safari%252F537%252E36%257C5%252E0%2520%2528X11%253B%2520Linux%2520x86%255F64%2529%2520AppleWebKit%252F537%252E36%2520%2528KHTML%252C%2520like%2520Gecko%2529%2520Ubuntu%2520Chromium%252F77%252E0%252E3865%252E90%2520Chrome%252F77%252E0%252E3865%252E90%2520Safari%252F537%252E36%257CLinux%2520x86%255F64%2526pm%255Ffpsc%253D24%257C1920%257C1080%257C1053%2526pm%255Ffpsw%253D%2526pm%255Ffptz%253D1%2526pm%255Ffpln%253Dlang%253Den%252DMT%257Csyslang%253D%257Cuserlang%253D%2526pm%255Ffpjv%253D0%2526pm%255Ffpco%253D1%2526pm%255Ffpasw%253Dinternal%252Dpdf%252Dviewer%257Cmhjfbmdgcfjbbpaeojofohoefgiehjai%2526pm%255Ffpan%253DNetscape%2526pm%255Ffpacn%253DMozilla%2526pm%255Ffpol%253Dtrue%2526pm%255Ffposp%253D%2526pm%255Ffpup%253D%2526pm%255Ffpsaw%253D1853%2526pm%255Ffpspd%253D24%2526pm%255Ffpsbd%253D%2526pm%255Ffpsdx%253D%2526pm%255Ffpsdy%253D%2526pm%255Ffpslx%253D%2526pm%255Ffpsly%253D%2526pm%255Ffpsfse%253D%2526pm%255Ffpsui%253D%2526pm%255Fos%253DLinux%2526pm%255Fbrmjv%253D77%2526pm%255Fbr%253DChrome%2526pm%255Finpt%253D%2526pm%255Fexpt%253D',
            'userDNI': 'Y6957175B',
            'userCard': '',
            'pinDNI': '',
            'injvalrnd': 'false',
            'injextrnd': '',
            'inputAtributes0': '',
            'inputAtributes1': 'en-MT',
            'inputAtributes2': '24',
            'inputAtributes3': '8',
            'inputAtributes4': '4',
            'inputAtributes5': '1920%2C1080',
            'inputAtributes6': '-120',
            'inputAtributes7': 'Europe%2FMadrid',
            'inputAtributes8': 'Linux+x86_64',
            'inputAtributes9': 'Intel+Open+Source+Technology+Center%7EMesa+DRI+Intel%28R%29+HD+Graphics+5500+%28Broadwell+GT2%29+',
            'inputAtributes10': 'false',
            'inputAtributes11': '15%2Cfalse%2Cfalse'
        }

    #  url, form_data, headers, cookies
    def get_do_login_request(self) -> Tuple[str, dict, dict, dict]:
        return self.do_login_url, self.do_login_form_data, self.do_login_headers, self.do_login_cookies

    def get_set_logged_in_request(self) -> Tuple[str, dict, dict, dict]:
        return self.do_set_logged_in_url, self.do_set_logged_in_form_data, self.do_set_logged_in_headers, self.do_login_cookies

    def set_cookies(self, new_cookies_list: list):
        for cookie_data in new_cookies_list:
            key, value = self.get_cookie_from_string(cookie_data.decode('utf-8'))
            self.do_login_cookies[key] = value

    @staticmethod
    def get_cookie_from_string(cookie_data: str) -> Tuple[str, str]:
        cookie = cookie_data.split(';')[0].split('=')

        cookie_id = cookie[0]
        cookie_value = cookie[1]
        return cookie_id, cookie_value
