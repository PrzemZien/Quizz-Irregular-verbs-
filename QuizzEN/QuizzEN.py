import tkinter as tk
import random
# function 'sprawdzanie'(This means checking) - this function chceck if your answer for is right 
# 'odpowiedz' This means answer 


dict={
'arise': 'arose/arisen',
'bet': 'bet/bet,betted/betted',
'bid!': 'bid/bid,bade/bidden,bid/bidden',
'bind': 'bound/bound',
'bleed': 'bled/bled', 'broadcast': 'broadcast/broadcast,broadcasted/broadcasted',
'deal': 'dealt/dealt', 'dig': 'dug/dug', 'fall': 'fell/fallen', 'feel': 'felt/felt', 'flee': 'fled/fled',
'flow': 'flowed/flowed', 'fly(in baseball)': 'flew/flown,flied/flied', 'forbid': 'forbad/forbidden,forbade/forbidden,forbade/forbid',
'grow': 'grew/grown', ' hit': 'hit/hit', 'hurt': 'hurt/hurt', 'lay': 'laid/laid', 'lie 1(= be down)': 'lay/lain',
'lie 2(= say sth that is not true)': 'lied/lied', 'quit': 'quit/quit,quitted/quitted', 'raise': 'raised/raised', 'rise': 'rose/risen',
'saw':'sawed/sawed,sawed/sawn', 'sew': 'sewed/sewed,sewed/sewn', 'sow': 'sowed/sowed,sowed/sown', 'seek': 'sought/sought', 'shed': 'shed/shed',
'shine(= to polish)': 'shone/shone,shined/shined', 'skid': 'skidded/skidded', 'slit': 'slit/slit', 'speed up': 'speeded up/speeded up', 'speed': 'sped/sped',
'split': 'split/split', 'spread': 'spread/spread', 'stick': 'stuck/stuck,stuck/sticked', 'strike': 'struck/struck,struck/stricken',
'stroke': 'stroked/stroked', 'sue': 'sued/sued', 'swell': 'swelled/swelled,swelled/swollen', 'tread(normalna,literary form,krotka,tread water)': 'trod/trodden,treaded/trodden,trod/trod,treaded/treaded',
'wake': 'woke/woken,waked/waked,woke/woke', 'weave': 'wove/woven,weaved/weaved', 'abide': 'abode/abode,abided/abided','awake': 'awaked/awaked,awoke/awoke,awoke/awoken',
'bear': 'bore/born,bore/borne', 'beget': 'begot/begotten,begot/begot,begot/begat','be': 'was/were/been', 'beat': 'beat/beat,beat/beaten', 'become': 'became/become',
'wear': 'wore/worn', 'wed': 'wed/wed,wedded/wedded', 'weep': 'wept/wept', 'wend': 'wended/wended', 'wet': 'wet/wet,wetted/wetted', 'will': 'would/would', 'win': 'won/won','wind': 'wound/wound,winded/winded','withdraw': 'withdrew/withdrawn',
'withhold': 'withheld/withheld','withstand': 'withstood/withstood', 'work': 'worked/worked,wrought/wrought', 'wring': 'wrung/wrung', 'write': 'wrote/written,wrote/writ', 'yield': 'yielded/yielded', 'wound': 'wounded/wounded',
'tear': 'tore/torn','tell': 'told/told','thrust': 'thrust/thrust','think': 'thought/thought','thrive': 'thrived/thrived,throve/thriven','throw': 'threw/thrown','unbend': 'unbent/unbent','unbind': 'unbound/unbound','undergo': 'underwent/underwent',
'underlie': 'underlay/underlain','understand': 'understood/understood','undertake': 'undertook/undertaken','underwrite': 'underwrote/underwritten','undersell': 'undersold/undersold','underbid': 'underbid/underbid','undo': 'undid/undone',
'unwind': 'unwound/unwound','uphold': 'upheld/upheld','upset': 'upset/upset', 'waylay': 'waylaid/waylaid','overtake': 'overtook/overtaken','overthrow': 'overthrew/overthrown','partake': 'partook/partook,partook/partaken',
'pay': 'paid/paid','pen (jako write, jako enclose)': 'penned/penned,pent/pent=','picnic': 'picnicked/picnicked','plead(krotka,najkrotsza,dluga)': 'plead/plead,pled/pled,pleaded/pleaded','preset': 'preset',
'proofread': 'proofread/proofread','prove': 'proved/proved,proved/proven','put': 'put/put','read': 'read/read','reave': 'reaved/reaved,reft/reft','rebind': 'rebound/rebound','rebuild': 'rebuilt/rebuilt',
'recast': 'recast/recast','redo': 'redid/redone','relay': 'relaid/relaid','remake': 'remade/remade','rend': 'rent/rent','repay': 'repaid/repaid','rerun': 'reran/rerun',
'resell': 'resold/resold','reset': 'reset/reset','rethink': 'rethought/rethought','rewind': 'rewound/rewound','rewrite': 'rewrote/rewritten','rid': 'rid/rid,ridded/ridded','ride': 'rode/ridden',
'ring': 'rang/rung','say': 'said/said','sell': 'sold/sold','send': 'sent/sent','set': 'set/set','shake': 'shook/shaken','shall': 'should/should', 'shave': 'shaved/shaved,shaved/shaven',
'shear': 'sheared/sheared,sheared/shorn,shore/shorn','shit': 'shit/shit,shat/shat,shitted/shitted','shite': 'shit/shit,shat/shat,shited/shited','shoe': 'shod/shod,shod/shodden','shoot': 'shot/shot','show': 'showed/showed,showed/shown',
'shrink': 'shrank/shrunk,shrunk/shrunken','shut': 'shut/shut','sing': 'sung/sung,sang/sung','sink': 'sank/sunk,sunk/sunk,sunk/sunken','sit': 'sat/sat','slay': 'slew/slain,slayed/slayed','sleep': 'slept/slept',
'slide': 'slid/slid,slid/slidden','sling': 'slung/slung','slink': 'slunk/slunk,slinked/slinked','smell': 'smelled/smelled,smelt/smelt','smite': 'smote/smote,smote/smitten,smote/smit','sneak': 'snuck/snuck,sneaked/sneaked',
'speak': 'spoke/spoken','spell': 'spelled/spelled,spelt/spelt','spend': 'spent/spent','spill': 'spilt/spilt,spilled/spilled', 'spin': 'spun/spun','spoil': 'spoilt/spoilt,spoiled/spoiled','spoonfeed': 'spoonfed/spoonfed',
'spring': 'sprung/sprung,sprang/sprung','stand': 'stood/stood','steal': 'stole/stolen','stink': 'stunk/stunk,stank/stunk','sting': 'stung/stung','strew': 'strewed/strewed,strewed/strewn','stride': 'strode/stridden',
'string': 'strung/strung','strive': 'strived/strived,strove/striven','swear': 'swore/sworn','sweat': 'sweated/sweated,sweat/sweat','sweep': 'swept/swept','swim': 'swam/swum',
'swing': 'swung/swung','spit': 'spat/spat,spit/spit,spat/spit','sunburn': 'sunburnt/sunburnt,sunburned/sunburned','shrive': 'shrove/shriven,shrived/shrived','take': 'took/taken','teach': 'taught/taught',
'eat': 'ate/eaten','fare': 'fared/fared','feed': 'fed/fed','fight': 'fought/fought','find': 'found/found','found': 'founded/founded','fill': 'filled/filled','fit': 'fit/fit,fitted/fitted','fling': 'flung/flung','fold': 'folded/folded','forecast': 'forecast/forecast,forecasted/forecasted',
'forego': 'forewent/foregone','forgo': 'forwent/forgone','forknow':'forknew/forknown','forerun': 'foreran/forerun','foresee': 'foresaw/foreseen','forespeak': 'forespoke/forespoken','foreshow': 'foreshowed/foreshowed, foreshowed/foreshown',
'foretell': 'foretold/foretold','forget': 'forgot/forgotten,forgot/forgot','forgive': 'forgave/forgiven','forsake': 'forsook/forsaken','forswear': 'forswore/foresworn','freeze': 'froze/frozen',
'forbear': 'forbore/forborne','geld': 'gelded/gelded,gelt/gelt','get': 'got/got,got/gotten','ghostwrite': 'ghostwrote/ghostwritten','gild': 'gilded/gilded,gilt/gilt','give': 'gave/given',
'go': 'went/gone','grave': 'graved/graved,graved/graven','grind': 'ground/ground','gainsay': 'gainsaid/gainsaid','handwrite': 'handwrote/handwritten','hang 1 (= to suspend)': 'hung/hung','hang 2( somebody)': 'hanged; hanged ( somebody)',
'have/has': 'had/had','hear': 'heard/heard','heave': 'heaved/heaved,heaved/hove','hew': 'hewed/hewed,hewed/hewn','hide': 'hid/hid,hid/hidden','housesit': 'housesat/housesat','hold':'held/held',
'input': 'input/input,inputted/inputted','inset': 'inset/inset','inlay': 'inlaid/inlaid','interbreed': 'interbred/interbred','interweave': 'interweaved/interweaved,interwove/interwoven', 'keep': 'kept/kept',
'kneel': 'kneeled/kneeled,knelt/knelt','knit': 'knit/knit,knitted/knitted','know': 'knew/known','lead': 'led/led','lean': 'leant/leant,leaned/leaned','leap': 'leapt/leapt,leaped/leaped','learn': 'learnt/learnt,learned/learned',
'leave': 'left/left','lese': 'lore/lorn','lend': 'lent/lent','let': 'let/let','light': 'lighted/lighted,lit/lit','lose': 'lost/lost','make': 'made/made','may': 'might/might','mean': 'meant/meant',
'meet': 'met/met','mete': 'meted/meted','mishear': 'misheard/misheard','lade': 'laded/laden,laded/laded','misdeal': 'misdealt/misdealt','misgive': 'misgave/misgiven','mislay': 'mislaid/mislaid',
'mislead': 'misled/misled','misread': 'misread/misread','misspell': 'misspelt/misspelt,misspelled/misspelled','mistake': 'mistook/mistaken','misunderstand': 'misunderstood/misunderstood','mow': 'mowed/mowed,mowed/mown',
'outspread': 'outspread/outspread','outshine': 'outshone/outshone','outgo': 'outwent/outgone','outride': 'outrode/outridden','outwear': 'outwore/outworn','outbid': 'outbid/outbid,outbid/outbidden','outdo': 'outdid/outdone',
'outgrow': 'outgrew/outgrown','outrun': 'outran/outrun','outsell': 'outsold/outsold','overspread': 'overspread/overspread','overset': 'overset/overset','overfeed': 'overfed/overfed',
'overleap': 'overleapt/overleapt,overleaped/overleaped','overbear': 'overbore/overborne','overgrow': 'overgrew/overgrown','overcast': 'overcast/overcast','overcome': 'overcame/overcome','overdo': 'overdid/overdone',
'overdraw': 'overdrew/overdrawn','overeat': 'overate/overeaten','overhang': 'overhung/overhung','overhear': 'overheard/overheard','overlay': 'overlaid/overlaid','overlie': 'overlay/overlain','overpay': 'overpaid/overpaid',
'override': 'overrode/overridden','overrun': 'overran/overrun','oversee': 'oversaw/overseen','oversell': 'oversold/oversold','overshoot': 'overshot/overshot','oversleep': 'overslept/overslept',
'befall': 'befell/befallen','begin': 'began/begun','behold': 'beheld/beheld','bend': 'bent/bent','bereave': 'bereaved/bereaved,bereft/bereft','beseech': 'beseeched/beseeched,besought/besought','bestride': 'bestrode/bestridden,bestrid/bestrid',
'beset': 'beset/beset','bespeak': 'bespoke/bespoke,bespoke/bespoken','bestrew': 'bestrewed/bestrewed,bestrewed/bestrewn,bestrewed/bestrown','betake': 'betook/betaken','bethink': 'bethought/bethought','bite': 'bit/bit,bit/bitten',
'blend': 'blent/blent,blended/blended','bless': 'blessed/blessed,blest/blest','blow (Br inf)': 'blew/blown,blew/blowed','bode': 'boded/boded','bide': 'bided/bided,bode/bided',
'break': 'broke/broken','brestfeed': 'breastfed/breastfed','breed': 'bred/bred','bring': 'brought/brought','browbeat': 'browbeat/browbeat','build': 'built/built',
'burn': 'burnt/burnt,burned/burned','burst': 'burst/burst','bust': 'bust/bust,busted/busted','buy': 'bought/bought','can': 'could/could','cast': 'cast/cast',
'catch': 'caught/caught','chide':'chided/chided,chid/chid,chid/chidden','choose': 'chose/chosen','cleave': 'cleft/cleft,cleaved/cleaved,clove/cloven','climb': 'climbed/climbed','cling': 'clung/clung',
'come': 'came/come','cost (normal,assign a price': 'cost/cost,costed/costed','creep (normal,creep sb out)': 'crept/crept,creeped/creeped','cut': 'cut/cut','dive': 'dived/dived,dove/dived','do': 'did/done','draw': 'drew/drawn', 'dream': 'dreamed/dreamed,dreamt/dreamt',
'drink': 'drank/drunk','drive': 'drove/driven','dwell': 'dwelt/dwelt,dwelled/dwelled'
}

def windowe():
    window = tk.Tk()
    window.geometry('910x400')
    window.title('Test')
    window.columnconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], minsize=150)
    window.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], minsize=150)
    x = random.choice(list(dict.keys()))
    y = dict[x]

    a = random.choice(list(dict.keys()))
    b = dict[a]

    c = random.choice(list(dict.keys()))
    d = dict[c]

    e = random.choice(list(dict.keys()))
    f = dict[e]

    g = random.choice(list(dict.keys()))
    h = dict[g]

    i = random.choice(list(dict.keys()))
    j = dict[i]

    k = random.choice(list(dict.keys()))
    l = dict[k]

    m = random.choice(list(dict.keys()))
    n = dict[m]

    o = random.choice(list(dict.keys()))
    p = dict[o]

    r = random.choice(list(dict.keys()))
    z = dict[r]

    t = random.choice(list(dict.keys()))
    u = dict[t]
    def sprawdzanie():
        if y == entry.get():
            sprawdzone["text"] = 'Good answer'
            odpowiedz["text"] = 'Bravo!'
            odpowiedz["fg"] = 'purple'
        else:
            sprawdzone["text"] = 'Bad answer'
            odpowiedz["text"] = y
    def sprawdzanie1():
        if b == entry1.get():
            sprawdzone1["text"] = 'Good answer'
            odpowiedz1["text"] = 'Bravo!'
            odpowiedz1["fg"] = 'purple'
        else:
            sprawdzone1["text"] = 'Bad answer'
            odpowiedz1["text"] = b
    def sprawdzanie2():
        if d == entry2.get():
            sprawdzone2["text"] = 'Good answer'
            odpowiedz2["text"] = 'Bravo!'
            odpowiedz2["fg"] = 'purple'
        else:
            sprawdzone2["text"] = 'Bad answer'
            odpowiedz2["text"] = d
    def sprawdzanie3():
        if f == entry3.get():
            sprawdzone3["text"] = 'Good answer'
            odpowiedz3["text"] = 'Bravo!'
            odpowiedz3["fg"] = 'purple'
        else:
            sprawdzone3["text"] = 'Bad answer'
            odpowiedz3["text"] = f
    def sprawdzanie4():
        if h == entry4.get():
            sprawdzone4["text"] = 'Good answer'
            odpowiedz4["text"] = 'Bravo!'
            odpowiedz4["fg"] = 'purple'
        else:
            sprawdzone4["text"] = 'Bad answer'
            odpowiedz4["text"] = h
    def sprawdzanie5():
        if j == entry5.get():
            sprawdzone5["text"] = 'Good answer'
            odpowiedz5["text"] = 'Bravo!'
            odpowiedz5["fg"] = 'purple'
        else:
            sprawdzone5["text"] = 'Bad answer'
            odpowiedz5["text"] = j
    def sprawdzanie6():
        if l == entry6.get():
            sprawdzone6["text"] = 'Good answer'
            odpowiedz6["text"] = 'Bravo!'
            odpowiedz6["fg"] = 'purple'
        else:
            sprawdzone6["text"] = 'Bad answer'
            odpowiedz6["text"] = l
    def sprawdzanie7():
        if n == entry7.get():
            sprawdzone7["text"] = 'Good answer'
            odpowiedz7["text"] = 'Bravo!'
            odpowiedz7["fg"] = 'purple'
        else:
            sprawdzone7["text"] = 'Bad answer'
            odpowiedz7["text"] = n
    def sprawdzanie8():
        if p == entry8.get():
            sprawdzone8["text"] = 'Good answer'
            odpowiedz8["text"] = 'Bravo!'
            odpowiedz8["fg"] = 'purple'
        else:
            sprawdzone8["text"] = 'Bad answer'
            odpowiedz8["text"] = p
    def sprawdzanie9():
        if z == entry9.get():
            sprawdzone9["text"] = 'Good answer'
            odpowiedz9["text"] = 'Bravo!'
            odpowiedz9["fg"] = 'purple'
        else:
            sprawdzone9["text"] = 'Bad answer'
            odpowiedz9["text"] = z
    def sprawdzanie10():
        if u == entry10.get():
            sprawdzone10["text"] = 'Good answer'
            odpowiedz10["text"] = 'Bravo!'
            odpowiedz10["fg"] = 'purple'
        else:
            sprawdzone10["text"] = 'Bad answer'
            odpowiedz10["text"] = u
    def exite():
        window.destroy()
    def again():
        window.destroy()
        windowe()
    frame = tk.Frame(
        master=window,
        relief=tk.SUNKEN,
        borderwidth=5
    )
    frame.pack()
    label = tk.Label(
        master=frame,
        text=x,
        width=35
    )

    label.grid(
        row=0,
        column=0,
        sticky='w'
    )

    entry = tk.Entry(
        master=frame,
        width=40,

    )
    entry.grid(
        row=0,
        column=1,
        sticky='w'
    )
    button = tk.Button(
        master=frame,
        text='Check',
        command=sprawdzanie
    )
    button.grid(
        row=0,
        column=2,
        sticky='w'
    )
    sprawdzone = tk.Label(
        master=frame,
        text='Not checked'
    )
    sprawdzone.grid(
        row=0,
        column=3,
        sticky='w'
    )
    odpowiedz = tk.Label(
        master=frame,
        text='Answer',
        width=35

    )
    odpowiedz.grid(
        row=0,
        column=4,
        sticky='w'
    )
    label1 = tk.Label(
        master=frame,
        text=a,
        width=35
    )

    label1.grid(
        row=1,
        column=0,
        sticky='w'
    )

    entry1 = tk.Entry(
        master=frame,
        width=40,

    )
    entry1.grid(
        row=1,
        column=1,
        sticky='w'
    )
    button1 = tk.Button(
        master=frame,
        text='Check',
        command=sprawdzanie1
    )
    button1.grid(
        row=1,
        column=2,
        sticky='w'
    )
    sprawdzone1 = tk.Label(
        master=frame,
        text='Not checked'
    )
    sprawdzone1.grid(
        row=1,
        column=3,
        sticky='w'
    )
    odpowiedz1 = tk.Label(
        master=frame,
        text='Answer',
        width=35

    )
    odpowiedz1.grid(
        row=1,
        column=4,
        sticky='w'
    )
    label2 = tk.Label(
        master=frame,
        text=c,
        width=35
    )

    label2.grid(
        row=2,
        column=0,
        sticky='w'
    )

    entry2 = tk.Entry(
        master=frame,
        width=40,

    )
    entry2.grid(
        row=2,
        column=1,
        sticky='w'
    )
    button2 = tk.Button(
        master=frame,
        text='Check',
        command=sprawdzanie2
    )
    button2.grid(
        row=2,
        column=2,
        sticky='w'
    )
    sprawdzone2 = tk.Label(
        master=frame,
        text='Not checked'
    )
    sprawdzone2.grid(
        row=2,
        column=3,
        sticky='w'
    )
    odpowiedz2 = tk.Label(
        master=frame,
        text='Answer',
        width=35
    )
    odpowiedz2.grid(
        row=2,
        column=4,
        sticky='w'
    )
    label3 = tk.Label(
        master=frame,
        text=e,
        width=35
    )

    label3.grid(
        row=3,
        column=0,
        sticky='w'
    )

    entry3 = tk.Entry(
        master=frame,
        width=40,

    )
    entry3.grid(
        row=3,
        column=1,
        sticky='w'
    )
    button3 = tk.Button(
        master=frame,
        text='Check',
        command=sprawdzanie3
    )
    button3.grid(
        row=3,
        column=2,
        sticky='w'
    )
    sprawdzone3 = tk.Label(
        master=frame,
        text='Not checked'
    )
    sprawdzone3.grid(
        row=3,
        column=3,
        sticky='w'
    )
    odpowiedz3 = tk.Label(
        master=frame,
        text='Answer',
        width=35
    )
    odpowiedz3.grid(
        row=3,
        column=4,
        sticky='w'
    )
    label4 = tk.Label(
        master=frame,
        text=g,
        width=35
    )

    label4.grid(
        row=4,
        column=0,
        sticky='w'
    )

    entry4 = tk.Entry(
        master=frame,
        width=40,

    )
    entry4.grid(
        row=4,
        column=1,
        sticky='w'
    )
    button4 = tk.Button(
        master=frame,
        text='Check',
        command=sprawdzanie4
    )
    button4.grid(
        row=4,
        column=2,
        sticky='w'
    )
    sprawdzone4 = tk.Label(
        master=frame,
        text='Not checked'
    )
    sprawdzone4.grid(
        row=4,
        column=3,
        sticky='w'
    )
    odpowiedz4 = tk.Label(
        master=frame,
        text='Answer',
        width=35
    )
    odpowiedz4.grid(
        row=4,
        column=4,
        sticky='w'
    )
    label5 = tk.Label(
        master=frame,
        text=i,
        width=35
    )

    label5.grid(
        row=5,
        column=0,
        sticky='w'
    )

    entry5 = tk.Entry(
        master=frame,
        width=40,

    )
    entry5.grid(
        row=5,
        column=1,
        sticky='w'
    )
    button5 = tk.Button(
        master=frame,
        text='Check',
        command=sprawdzanie5
    )
    button5.grid(
        row=5,
        column=2,
        sticky='w'
    )
    sprawdzone5 = tk.Label(
        master=frame,
        text='Not checked'
    )
    sprawdzone5.grid(
        row=5,
        column=3,
        sticky='w'
    )
    odpowiedz5 = tk.Label(
        master=frame,
        text='Answer',
        width=35
    )
    odpowiedz5.grid(
        row=5,
        column=4,
        sticky='w'
    )
    label6 = tk.Label(
        master=frame,
        text=k,
        width=35
    )

    label6.grid(
        row=6,
        column=0,
        sticky='w'
    )

    entry6 = tk.Entry(
        master=frame,
        width=40,

    )
    entry6.grid(
        row=6,
        column=1,
        sticky='w'
    )
    button6 = tk.Button(
        master=frame,
        text='Check',
        command=sprawdzanie6
    )
    button6.grid(
        row=6,
        column=2,
        sticky='w'
    )
    sprawdzone6 = tk.Label(
        master=frame,
        text='Not checked'
    )
    sprawdzone6.grid(
        row=6,
        column=3,
        sticky='w'
    )
    odpowiedz6 = tk.Label(
        master=frame,
        text='Answer',
        width=35
    )
    odpowiedz6.grid(
        row=6,
        column=4,
        sticky='w'
    )
    label7 = tk.Label(
        master=frame,
        text=m,
        width=35
    )

    label7.grid(
        row=7,
        column=0,
        sticky='w'
    )

    entry7 = tk.Entry(
        master=frame,
        width=40,

    )
    entry7.grid(
        row=7,
        column=1,
        sticky='w'
    )
    button7 = tk.Button(
        master=frame,
        text='Check',
        command=sprawdzanie7
    )
    button7.grid(
        row=7,
        column=2,
        sticky='w'
    )
    sprawdzone7 = tk.Label(
        master=frame,
        text='Not checked'
    )
    sprawdzone7.grid(
        row=7,
        column=3,
        sticky='w'
    )
    odpowiedz7 = tk.Label(
        master=frame,
        text='Answer',
        width=35
    )
    odpowiedz7.grid(
        row=7,
        column=4,
        sticky='w'
    )
    label8 = tk.Label(
        master=frame,
        text=o,
        width=35
    )

    label8.grid(
        row=8,
        column=0,
        sticky='w'
    )

    entry8 = tk.Entry(
        master=frame,
        width=40,

    )
    entry8.grid(
        row=8,
        column=1,
        sticky='w'
    )
    button8 = tk.Button(
        master=frame,
        text='Check',
        command=sprawdzanie8
    )
    button8.grid(
        row=8,
        column=2,
        sticky='w'
    )
    sprawdzone8 = tk.Label(
        master=frame,
        text='Not checked'
    )
    sprawdzone8.grid(
        row=8,
        column=3,
        sticky='w'
    )
    odpowiedz8 = tk.Label(
        master=frame,
        text='Answer',
        width=35
    )
    odpowiedz8.grid(
        row=8,
        column=4,
        sticky='w'
    )
    label9 = tk.Label(
        master=frame,
        text=r,
        width=35
    )

    label9.grid(
        row=9,
        column=0,
        sticky='w'
    )

    entry9 = tk.Entry(
        master=frame,
        width=40,

    )
    entry9.grid(
        row=9,
        column=1,
        sticky='w'
    )
    button9 = tk.Button(
        master=frame,
        text='Check',
        command=sprawdzanie9
    )
    button9.grid(
        row=9,
        column=2,
        sticky='w'
    )
    sprawdzone9 = tk.Label(
        master=frame,
        text='Not checked'
    )
    sprawdzone9.grid(
        row=9,
        column=3,
        sticky='w'
    )
    odpowiedz9 = tk.Label(
        master=frame,
        text='Answer',
        width=35
    )
    odpowiedz9.grid(
        row=9,
        column=4,
        sticky='w'
    )
    label10 = tk.Label(
        master=frame,
        text=t,
        width=35
    )

    label10.grid(
        row=10,
        column=0,
        sticky='w'
    )

    entry10 = tk.Entry(
        master=frame,
        width=40,

    )
    entry10.grid(
        row=10,
        column=1,
        sticky='w'
    )
    button10 = tk.Button(
        master=frame,
        text='Check',
        command=sprawdzanie10
    )
    button10.grid(
        row=10,
        column=2,
        sticky='w'
    )
    sprawdzone10 = tk.Label(
        master=frame,
        text='Not checked'
    )
    sprawdzone10.grid(
        row=10,
        column=3,
        sticky='w'
    )
    odpowiedz10 = tk.Label(
        master=frame,
        text='Answer',
        width=35
    )
    odpowiedz10.grid(
        row=10,
        column=4,
        sticky='w'
    )
    exit = tk.Button(
        master= frame,
        width= 10,
        text= 'Exit',
        command= exite
    )
    exit.grid(
        row= 11,
        column= 4,
        sticky= 'w'
    )
    again = tk.Button(
        master= frame,
        width= 10,
        text= 'Open Again',
        command= again
    )
    again.grid(
        row= 11,
        column= 3,
        sticky= 'w'
    )
    window.mainloop()


windowe()