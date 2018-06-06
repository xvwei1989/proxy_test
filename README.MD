terminal shadowsocks
在 .bash_profile里添加
alias proxy='export all_proxy=socks5://127.0.0.1:1080'
alias unproxy='unset all_proxy'


1.使用ssl创建未经验证的上下文，在urlopen中传入上下文参数


import ssl
ssl._create_default_https_context = ssl._create_unverified_context
