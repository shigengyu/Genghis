import cgi

def html_escape(s):
    result = ''
    while len(s) > 0:
        index = s.find('<pre')
        if index >= 0:
            result += cgi.escape(s[0:index])
            s = s[index:]
            index = s.find('</pre>')
            result += s[0:index+6]
            s = s[index+6:]
        else:
            result += cgi.escape(s)
            s = ''
    return result