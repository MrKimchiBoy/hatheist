# the #atheist computer simulator
# if #atheist was a mnemonic abbreviation for a #computer instruction set. Like:
# # get char from input
# A add
# T test
# H half (/2)
# E exponent
# I invert
# S stop 
# T type char


# la = <labelOrAddress>, IE label, or address.
# # la
# add la la
# test la la
# half la
# exp la la
# inv la
# stop
# type la

class DummyInput:
    def __init__(this,s=""):
        this.s = iter([chr(c) for c in s])
    def getc(this):
        c = next(this.s,-1)
        return c

class DummyOutput:
    def __init__(this):
        this.out = ""
    def putc(this,c):
        this.out += chr(c&0xffff)


class Hatheistvm:
    def __init__(this, code,inp=None,out=None):
        if inp==None:
            inp = DummyInput("")
        if out== None:
            out = DummyOutput()
        this.inp = inp
        this.out = out
        this.code = list(code)
        this.lec = len(this.code)
        this.pc = 0
        this.running = True
    def __getitem__(this,i):
        i = i % this.lec
        return this.code[i]
    def __setitem__(this,i,v):
        i = i % this.lec
        this.code[i] = v
    def fetch(this):
        v = this[this.pc]
        this.pc = (this.pc+1) % this.lec
        return v
    def strict(this,a):
        return a % this.lec
    def repeat(this,x):
        for a in range(x):
            if not this.running:
                return
            this.step()
    def until(this,f=None):
        if f == None:
            f = lambda: this.running
        while not f():
            if not this.running:
                return
            this.step()
    def step(this):
        if not this.running:
            return
        op = this.fetch()
        if op == 0: # #
            a = this.fetch()
            this.code[a] = this.inp.getc()
        elif op == 1: # add
            a = this.fetch()
            b = this.fetch()
            this[b] = this[a] + this[b]
        elif op == 2: # test
            a = this.fetch()
            b = this.fetch()
            if this[a] < 0:
                this.pc = this.strict(b)
        elif op == 3: # half
            a = this.fetch()
            this[a] = this[a] <<1
        elif op == 4: # exp
            a = this.fetch()
            b = this.fetch()
            this[b] = int(this[a] ** this[b])
        elif op == 5: # inv
            a = this.fetch()
            this[a] = ~ this[a]
        elif op == 6: # stop
            this.running = False
        elif op == 7: # type
            a = this.fetch()
            this.out.putc(this[a])
