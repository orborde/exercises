def plustwo(x):
    print 'START PLUSTWO', x
    for i in xrange(x):
        print 'PLUSTWO LOOP i =', i
        yield i + 2
        print 'PLUSTWO BACK FROM YIELD'
    print 'PLUSTWO END'

if __name__=='__main__':
    print 'STARTING FOR LOOP'
    print 'GENERATING THE GENERATOR'
    pt = plustwo(3)
    print 'BACK IN MAIN. THE GENERATOR IS', pt
    for output in pt:
        print 'FOR LOOP BODY output =', output
        print output
        print 'FOR LOOP BODY END'
    print 'DONE WITH FOR LOOP'
