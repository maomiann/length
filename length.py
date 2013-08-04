
import re

terms = {}
term = re.compile(r'([a-z]+) = (\d+\.?\d*)')
out = open('output.txt','w')
out.write("2273866930@qq.com\n\n")
with open('input.txt') as f:
    for line in f:
        if line == '\n':
            continue
        if (term.search(line)):
            v = term.findall(line)[0]
            terms[v[0]] = float(v[1])
            if v[0] == 'foot':
                terms['feet'] = terms['foot']
        else:
            for k,v in terms.iteritems():
                if line.count(k) > 0:
                    line=line.replace(k,'* %f' % v)
            line=line.replace('s','')
            line=line.replace('e','')
            out.write("%.2f m\n" % eval(line))
out.close()
