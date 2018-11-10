import hashlib

def checkio(string, algorithm):
    algo = {'md5': hashlib.md5(), 'sha1': hashlib.sha1(), 'sha224': hashlib.sha224(), 'sha256':hashlib.sha256(),
            'sha384': hashlib.sha384(), 'sha512': hashlib.sha512()}
    h = algo[algorithm]
    h.update(bytes(string, 'utf-8'))
    return h.hexdigest()
    
if __name__ == '__main__':
    assert checkio('welcome', 'md5') == '40be4e59b9a2a2b5dffb918c0e86b3d7'
    assert checkio('happy spam', 'sha224') == '6e9dc3e01d57f1598c2b40ce59fc3527e698c77b15d0840ae96a8b5e'
    assert checkio(u"welcome to pycon","sha384") == '0a67310f6eaf6adb5fb6f4c679aedce3716c6d1528a201189c55f631b9656c69f68899dca4699ef44d74a238bd7106e1'
    assert checkio(u"Пароль","sha224") == '6102a4a0a632f30c3f7d0fa2da3958da2ca4b09478bbc01a14928447'
