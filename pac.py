import requests
import base64

url = "https://raw.githubusercontent.com/gfwlist/gfwlist/master/gfwlist.txt"
r = requests.get(url)
encrypt_str = r.text.strip()
decrypt_str = base64.b64decode(encrypt_str.encode('utf8'))
decrypt_str = decrypt_str.decode('utf8')
decrypt_strs = decrypt_str.split('\n')
js_strs = []
for each_str in decrypt_strs:
    if each_str is None:
        continue
    if each_str.startswith('|'):
        js_strs.append(each_str.replace('|', ''))
    if each_str.startswith('.'):
        js_strs.append(each_str[1:])
js_str = "var V2Ray = \"SOCKS5 127.0.0.1:1081; SOCKS 127.0.0.1:1081; HTTP 127.0.0.1:8001; HTTPS 127.0.0.1:8001; DIRECT;\";\n\n"
js_str += "var domains = [\n"
for each_str in js_strs:
    js_str += '    "' + each_str + '",\n'
js_str = js_str[:-2] + "\n];\n\n"
js_str += "function FindProxyForURL(url, host) {\n"
js_str += "    for (var i = domains.length - 1; i >= 0; i--) {\n"
js_str += "        if (dnsDomainIs(host, domains[i])) {\n"
js_str += "            return V2Ray;\n"
js_str += "        }\n"
js_str += "    }\n"
js_str += "    return \"DIRECT\";\n"
js_str += "}\n"
with open('pac.js', 'w', encoding='utf-8') as f:
    f.write(js_str)
    f.close()
