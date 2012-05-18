# -*- coding: utf-8 -*-

def check_unresolved(locstr):
    for key in fix_unresolved:
        if locstr in key: return fix_unresolved[key]


def tests():
    assert(check_unresolved('nyc') == 'United States')
    assert(check_unresolved('perú') == 'Peru')
    print 'tests pass'


fix_unresolved = {
    frozenset(['nyc', 'silicon valley', 'sf', 'uiuc', 'new england', 'philly', 'ucla', 'west coast', 'potrero, sf', 'cape may court house', 'u.s.a.', 'rit', 'northwest', 'trabuco canyon', 'west philly', 'mit', 'unlv', 'chicagoland', 'sdut']): 'United States',
    frozenset(['montreal', 'montreal, qc', 'montréal, québec', 'québec', 'montréal', 'quebec', 'prévost', 'montréal, qc', 'tiohtiake', 'montreal, quebec']): 'Canada',
    frozenset(['england', 'scotland', 'oxfordshire', 'oxfordshire, england', 'u.k.', 'snowdonia, north wales', 'broughty ferry, scotland', 'cambrdige']): 'United Kingdom',
    frozenset(['munich', 'cologne', 'münchen', 'deutschland', 'düsseldorf', 'nürnberg', 'köln', 'göttingen', 'osnabrück', 'isny', 'duesseldorf', 'montabaur', 'münster']): 'Germany',
    frozenset(['são paulo, brasil', 'brasil', 'são paulo', 'são paulo - sp', 'sao paulo', 'são paulo - brasil', 'são paulo, sp, brasil', 'são paulo, sp', 'goiânia', 'joão pessoa', 'três rios - rj', 'florianópolis', 'santo andre - sp - brasil', 'são paulo - sp - brasil']): 'Brazil',
    frozenset(['russian federation', 'ekaterinburg', 'ulyanovsk', 'Москва', 'stary oskol', 'nizhny novgorod', 'moskow', 'ptz', 'russian']): 'Russia',
    frozenset(['chambéry', 'meyrargues', 'auvergne']): 'France',
    frozenset(['korea']): 'South Korea',
    frozenset(['istanbul', 'eskisehir', 'izmir']): 'Turkey',
    frozenset(['hyderabad', 'varanasi', 'bengaluru', 'ahmedabad', 'kerala', 'gandhinagar, gujarat']): 'India',
    frozenset(['zurich', 'zürich', 'neuchatel', 'lucerne', 'paudex', 'stäfa']): 'Swizerland',
    frozenset(['méxico', 'méxico city']): 'Mexico',
    frozenset(['sapporo', 'osaka', 'yokohama', 'japanese''kagurazaka', 'kanagawa', 'nagoya', 'chiba']): 'Japan',
    frozenset(['göteborg', 'linköping', 'gothenburg']): 'Sweden',
    frozenset(['europe->poland->gorzow', 'kraków', 'wrocław', 'cracow', 'warszawa', 'dąbrowa górnicza, polska']): 'Poland',
    frozenset(['bucuresti', 'bucurești, românia', 'iaşi, românia', 'cluj-napoca', 'iasi']): 'Romania',
    frozenset(['ghent', 'bruxelles', 'liège']): 'Belgium',
    frozenset(['ukreine', 'lviv', 'kyiv', 'kharkov', 'cherkassy']): 'Ukraine',
    frozenset(['patagonya']): 'Argentina',
    frozenset(['valparaíso']): 'Chile',
    frozenset(['gansu', "xi'an", 'beijng', 'hang zhou']): 'China',
    frozenset(['medellin', 'envigado! :)']): 'Colombia',
    frozenset(['czech rebublic']): 'Czech Republic',
    frozenset(['itämerenkatu 13']): 'Finland',
    frozenset(['soerabaja, east java']): 'Indonesia',
    frozenset(['milano', 'turin', 'mozzanella', 'italia']): 'Italy',
    frozenset(['almere', 'antwerp', 'flanders, eu', 'uddel']): 'Netherlands',
    frozenset(['perú']): 'Peru',
    frozenset(['phillipines']): 'Philippines',
    frozenset(['catalunya', 'canary islands', 'seville', 'santa Úrsula', 'piera']): 'Spain',
    frozenset(['taoyuan']): 'Taiwan',
    frozenset(['viet nam', 'hanoi', 'ha noi, viet nam', 'ha noi - viet nam', 'ha noi']): 'Vietnam',
    frozenset(['tehran']): 'Iran',
    frozenset(['joburg']): 'South Africa',
    frozenset(['luxemburg']): 'Luxembourg',

    frozenset([]): 'Australia',
    frozenset([]): 'Austria',
    frozenset([]): 'Ireland'
}

if __name__ == '__main__':

    tests()


#uruapan michoacán méxico	69
#blagoveschensk, amur region, russian federation	69
#unfashionable end, western spiral arm, milky way	69
#广东 深圳	69
#devon, england	69
#*	69
#tc_hydro	68
#on the intraweb.	68
#xda-developers	68
#Набережные Челны	67
#geneve	67
#københavn	67

#babia	66
#libertatia	66
#beijingchina	66
#/home/emineker	65
#bonnie scotland	65
#são paulo, brasil.	65
#brasilia	65
#Россия, Москва, Ногинск	65
#mdle hell	65
#gex	64
#bonsall, derbyshire	64

#hà nội, việt nam	63
#kolkata	63
#beyond your wildest dreams	62
#cmpt 470	62
#pacific northwest	62
#northern england	62
#60601	62
#stornoway	61

#hampshire, england	61
#cern	61




#samstagern	59

#burgum	59
#27318, hoya	59

#belém/pa (brasil)	59
#yokohma	58
#uzb	58
#united kingdon	58
#wien	58
#ciracas	58
#luik	58
#bolzano	58
#jogjakarta	57
#tübingen	57
#l3	57
#200 varick street	57
#中国上海	56
#06103	56
#n 52.507377 e 13.460589	56
#gijón	56
#matlock, derbyshire	55
#u.s.	55
#::1	55
#north east england	55
#interwebs	54
#cal poly slo	54
#the yay	54
#troon, scotland	54
#37°4252.24"n 89°1307.92"w 141m	53
#root	53
#online	53
#cardrona	53
#pluto	52
#aarhus	52
#muc	52
#north wales	52
#s	52
#pici	52
#ffm	52
#altach, Österreich	52
#aix en provence	51

#argetnina	51
#45.391921,-122.567767	50
#america	50
#stanford	50
#lietuva (lithuania, gmt+2)	50
#reykjavik	50
#neo-sitama	49
#espirito santo, brasil	49
#atl	49
#homalg project	49

#berkshire, england	49
#415, 516	49
#atx	48
#odd pod, troon, scotland.	48
#bahia blanca	48
#nurnberg	48
#belgique	48
#lisboa	48
#/home/askn	47
#merica	47
#浙江宁波	47
#lostwithiel	47
#32.251225,-111.017906	47
#nizhny novgorod, russian federation	47
#jorvas	46
#vilafranca del penedès, catalunya	46
#sfbay area	46
#gandhinagar	46
#nova scotia	46
#n/a	46
#中国浙江省杭州市	46
#praha	46
#a coruña	45
#córdoba	45
#nova	45
#tver	45
#swizerland	45
#hacking from the moon	45
#the nederlands	45
#aix-en-provence	45
#uc santa barbara	45
#tejas	44
#niterói/rj	44
#latvija, rīga	44
#méxico, d.f.	44
#渋谷	44
#rupnagar	44
#chn	44
#upstate new yawk	44
#manipal	43
#whistler, bc	43
#russian, ryazan	43
#block island	43
#karkala	43
#tunbridge wells	43
#上海市浦东新区居里路222号	42
#krakow	42
#風見学園	42
#leningrad	42
#74	42
#hradec králové	42
#frankfurt, gemany	42
#lith.	42
#saarbrücken	41
#strängnäs	41
#köln, deutschland	41
#são carlos/sp	41
#idf	41
#slavičín	41
#hampshire	41
#newfoundland	40
#nomadic	40
#são paulo / brasil	40
#brasil/goiás/goiânia	40
#suwon	39
#the mountains	39
#perm	39
#cần thơ	39
#czecho	39
#south wales	39
#fukuoka	39
#over there	39
#rychnov nad kneznou / praha	39
#var location = { country: germany, city: saarbrücken };	38
#.	38
#ryazan	38
#sea / sfo / nyc / bos	38
#jocala.com	38
#port coquitlam, bc	38
#deajeon	38
#Россия, Московская область, Долгопрудный	37
#saigon	37
#wales	37
#urumqi	37
#méxico df	37
#lancashire	37
#eivissa, españa	37
#são paulo - sp, brasil	37
#fennectar, fennectus state, planet cyrusian	37
#méxico d.f.	37
#españa	37
#hà nội - việt nam	37
#Казань	36
#arkania	36
#Сибирь, Кузбасс	36
#hell on earth	36
#浙江省杭州市文二路391号	36
#fotaleza	36
#-	35
#/home/necronet	35
#leon, gto	35
#kobe	35
#barnet	35
#tyumen	35
#galactic sector zz9 plural z alpha	34
#north america	34
#@philingrey	34
#catalonia	34
#elbląg	34
#málaga	34
#belém pará	34
#quebec city	34
#oświęcim	34
#武汉	33
#jyväskylä	33
#stony brook	33
#oaxaca, méxico	33
#záhony	33
#l.a.	33
#málaga, españa	33
#waseco building	33
#(37.768372, -122.449139)	33
#pacific palisades	33
#55409	33
#sun/sol	33
#poznan	33
#shang hai	32
#joão pessoa, paraíba	32
#brasília, brasil	32
#hellsinki / funland	32
#cascadia	32
#gdansk	32
#gdańsk	32
#alresford	32
#dollar, clackmannanshire	32
#the d	32
#Харьков	32
#scenic hinxton	31
#rendsburg@germany	31
#timisoara	31
#kyiv, ukrane	31
#behind you	31
#idolgo.com	31
#gotland	31
#the cloud	31
#wow freakz	31
#wonderland	31
#bronx	31
#vernouillet	31
#space	31
#˚∆˚	30
#cornell	30
#cheonan, korea	30
#chania crete	30
#effretikon	30
#bavaria	30
#llanfrothen, north wales	30
#oisy le verger	30
#woclaw	30
#windows	30
#bundeshauptstadt	30
#vorarlberg	30
#bogota	30
#durandalingrad	30
#mass, u.s.	29
#românia	29
#prg	29
#right behind you!!!	29
#brasília	29
#internets	29
#united stated	29
#milky way	29
#kocaeli, turkiye	29
#galway	29
#american midwest	29
#shizuoka	29
#hanoi, viet nam	29
#peking	29
#ciudad obregon sonora , méxico	29
#livry gargan	29
#brasília, df, brasil	29
#south england	29
#frankfurt	29
#suburbia	28
#llanarmon dyffryn ceiriog	28
#milky way galaxy	28
#sfca	28
#here, now	28
#nit kozhikode, kerala	28
#janelia farm research campus	28
#softslayer	28
#thrissur	28
#hz	28
#中山大学	28
#usofa	28
#bahía blanca	28
#joão pessoa - pb	28
#jamaca	27
#montermorelos	27
#le bourget du lac	27
#irc.datnode.net	27
#brasil, brasília	27
#whatloo	27
#the pleiades	27
#location independent	27
#nagpur	27
#ederbringhausen	27
#kotamobagu	27
#hyrule	27
#valles marineris, mars	27
#iit kanpur	27
#vironezh	27
#singularity	26
#/home	26
#sausalito	26
#right behind you!	26
#turkiye	26
#yayyyy	26
#campina grande-pb	26
#gandhinagar/ahmedabad	26
#solaro	26
#schweiz	26
#nanking	26
#münchen, deutschland	26
#22302	26
#earth, solar system	26
#phx	26
#Österreich	26
#bhubaneswar	25
#/home/wintervenom	25
#shambala	25
#epfl	25
#location 0	25
#italia, milano	25
#việt nam	25
#70115	25
#engineer	25
#banglore	25
#são carlos, sp	25
#on a boat	25
#balneário camboriú	25
#north east, england	25
#kaslo, bc	25
#97203	24
#the rose city	24
#tampon	24
#България, Свищов	24
#medellín	24
#help! polar bears are attacking me!	24
#down under	24
#slovenija	24
#yorkshire	24
#noe	24
#långshyttan	24
#glyfada	24
#moskau	24
#bcn	24
#中国-浙江-衢州	24
#goiânia - go	24
#brasília/df, brasil	24
#cologne (ger)	24
#görlitz	24
#sussex, england	24
#west yorkshire	24
#florianopolis, brasil	23
#curitba/pr - brasil	23
#mtl	23
#sf baby!	23
#réunion	23
#Санкт-Петербург, Россия	23
#lidköping	23
#ukrain	23
#秦皇岛	23
#campo grade - ms, brasil	23
#narnia	23
#south pole	23
#marylands eastern shore	23
#kumamoto	23
#Минеральные Воды	23
#phl	23
#donostia	23
#hertfordshire	22
#sao paulo, brasil	22
#right behind you.	22
#rensselaer polytechnic institute	22
#gmt+2	22
#ufsc	22
#sp - brasil	22
#萧山	22
#são josé dos campos, são paulo, brasil	22
#goiania, goiás, brasil	22
#great britain	22
#remote developer	22
#cis, eecs, peking univ.	21
#floduh	21
#ilhéus/bahia/brasil	21
#los angeles area	21
#rmit uni	21
#da nang, viet nam	21
#vellerat	21
#aubergenville	21
#brasil, rj	21
#sevastopol	21
#dans le 45	21
#roaming	21
#herzliya	21
#100 above ground floating on a balloon	21
#frozen reindeer country	21
#melverley, shropshire	21
#irc://irc.datnode.net:6667/#hacking	21
#alnilam	21
#inland norcal	21
#the hague	21
#wollishofen, zürich	21
#zurich, swtizerland	21
#eastern seaboard	21
#hangzhou，zhejiang，china	21
#los países bajos	21
#definitely!	21
#galicia, españa	21
#münster, deutschland	20
#interwebz	20
#cesário lange/itapetininga - sp	20
#57° 42 49 n, 11° 59 53	20
#bunnik	20
#zhodino	20
#nullptr	20
#who knows where	20
#takoyaki	20
#blowmage	20
#ku	20
#arkhangelsk	20
#sthlm	20
#compiègne	20
#web	20
#chisinau	20
#bengalooru	20
#südwestdeutschland	19
#münster, deustchland	19
#rio piedras	19
#são carlos	19
#way up north, scotland	19
#cny	19
#schwyz	19
#very small small town	19
#leidschendam	19
#phillynyc	19
#qro	19
#goiânia, brasil	19
#likely indoors.	19
#Łaziska górne	19
#montreal,qc	19
#10010	19
#pek	19
#colbert nation	19
#nippon	19
#北京，中国	19
#yokohama city	19
#a few places.	19
#space the final frontier.	19
#ranchi	18
#reken	18
#firenze	18
#blighty	18
#河南，中国	18
#le kremlin-bicêtre	18
#everywhere but nowhere.	18
#@malsup on twitter	18
#日本	18
#中国南昌	18
#brasil, são paulo - sp	18
#mönchengladbach	18
#wroclaw	18
#isla	18
#pécs	18
#xian,shaanxi,p.r.c	18
#none	18
#socal	18
#ussel	18
#sophia antipolis	18
#浙江，杭州	18
#/dev/hell	18
#bedum	18
#rus, spb	18
#louisianna	18
#lasalle, quebec	18
#teldrassil	18
#default city	18
#dnepropetrovsk	18
#freenode	18
#united states (est)	18
#home	18
#würzburg	17
#east coast	17
#somewhere around the world	17
#alwernia	17
#Ústí nad orlicí megapolis	17
#hcm	17
#worcestershire, england	17
#williams lake, bc	17
#pakkret, nonthaburi	17
#prag	17
#xàtiva	17
#level 3	17
#sao paulo sp	17
#earth, spiral arm, milky way	17
#middle earth	17
#rio	17
#kosice	17
#custom real estate websites	17
#manningtree, england	17
#moon base alpha	17
#none.	17
#nehterlands	17
#nowhere.	17
#loltah	17
#lsju	17
#with the finger on the keyboard... ;)	16
#peachtree corners	16
#warszawa, polska	16
#krakow/kyiv	16
#bei jing	16
#cúcuta	16
#Украина, г. Винница	16
#nasa goddard	16
#kharkov, urkaine	16
#oaklandia	16
#cordoba	16
#mallorca, españa	16
#shuswap, bc	16
#gloucseter	16
#cloverdale, b.c.	16
#upton	16
#Долгопрудный	16
#nagano	16
#western hemisphere	16
#chicoutimi, qc	16
#milano, italia	16
#newyork	16
#silicon slopes	16
#sachsen	16
#在地球上.	16
#são mateus - espirito santo	16
#the desert	16
#petsamo, lapland	15
#siberia	15
#the czech republic	15
#londinium	15
#oaxaca	15
#bluelovers	15
#rueti zh	15
#bellatrix.	15
#wakayama pref.	15
#donostia - gasteiz	15
#trivandrum kerala	15
#rajkot	15
#nederlands	15
#kansas! city!	15
#ladkrabang	15
#maarn	15
#orléans	15
#world wide wiretap	15
#(shell)	15
#russian federation, spb	15
#@squarism	15
#norrköping	15
#rajshahi	15
#sonoma	15
#anime and mango	15
#on the interwebz	15
#euskadi	15
#Россия, Москва	15
#roudnice nad labem	15
#goiânia, goiás, brasil	15
#nwa	14
#el ceñidor, múgica, michoacán, méxico.	14
#slovak republic	14
#teh internets	14
#earht planet	14
#bistrița, românia	14
#czech	14
#polska	14
#stavropol	14
#sassenheim	14
#chicagoland+wi	14
#hongkou	14
#中国>北京	14
#são paulo / sp	14
#helms deep	14
#joao pessoa, pb - brasil	14
#sai gon	14
#davidwright@gmail.com	14
#hà nội	14
#dfw	14
#cluj - napoca	14
#d.c.	14
#ringerike	14
#asuncion	14
#bruges	14
#black books	14
#rzeszów/kraków	14
#a town near you	14
#avesnes sur helpe	13
#guwahati	13
#aus	13
#bellarine peninsula	13
##dtla	13
#derbyshire	13
#puebla, puebla	13
#☠☠☠ nyc ☠☠☠	13
#dell inc.	13
#lost between bits	13
#skype: fljot_	13
#campina	13
#otaniemi	13
#lidzbark warmiński / gdańsk	13
#self confidence comes from being sure that your predictions are accurate	13
#köthen (anhalt)	13
#Россия	13
#横浜市, 日本	13
#i came. i saw. i refactored.	13
#frankfurt (oder)	13
#hokkaido	13
#太倉，蘇州	13
#borlänge	13
#arbucies	13
#nizhnyi novgorod	13
#löhne	13
#$home	13
#eastern u.s.a.	13
#vitebsk	13
#fürth	13
#michoacán, méxico	13
#hier	13
#hyères les palmiers	13
#breizh	12
#mpls	12
#黑龙江省哈尔滨市南岗区西大直街92号哈尔滨工业大学一校区a02公寓6047寝室	12
#oahu	12
#23603	12
#são paulo-sp (brasil)	12
#transnistria	12
#europe, earth, the universe	12
#hcmc	12
#boulogne	12
#tubarão/sc, brasil	12
#devon	12
#Россия, г.Рубцовск	12
#right here	12
#lincolnshire, england	12
#intertubes	12
#somewhere between here and there	12
#worldwide baby!	12
#toxicity	12
#lviv	12
#nor cal	12
#knivsta	12
#kanpur	12
#devon/bournemouth (home/uni)	12
#kozloduy	12
#xintend	12
#santo andré - sp	12
#batam	12
#minnesotta	12
#ja_jp	12
#méxico, df	12
#rhone-alpes	12
#Калуга	12
#chain,bei jing	11
#n.novgorog	11
#brasília - df - brasil	11
#uae	11
#四机房	11
#東京都杉並区	11
#triniad and tobago	11
#orel, rf	11
#georgsmarienhütte	11
#someplace near you.	11
#world citizen	11
#a five line poem.	11
#tasmania	11
#cenote	11
#skagit county	11
#xi`an	11
#toyko	11
#trivandrum	11
#tenerife	11
#kreuzberg	11
#31.593469,120.772855	11
#worcestershire	11
#royal leamingtin spa	11
#chicoutimi, québec	11
#secret volcano lair.	11
#brittany	11
#somewhere else.	11
#midwest	11
#中国 杭州	11
#pego (p.p.c.c)	11
#reggio emilia	11
#bielsko-biała	11
#kowale	11
#on the run	11
#cyberjaya	11
#saint nazaire	11
#hải phòng, hồ chí minh	11
#oosterwolde	11
#são leopoldo	11
#danmark	11
#left-handed coordinate	11
#scott afb	11
#andreazevedo	11
#19.334873, -99.064627	11
#são paulo/brasil	11
#desconocida	11
#montreal qc	11
#lenzburg	11
#saint germain-en-laye	10
#coffee bean & tea leaf	10
#planet java	10
#合肥,安徽	10
#würselen	10
#akihabara	10
#sector zz9 plural z alpha	10
#kongens lyngby	10
#nagoya univ.	10
#undisclosed	10
#kraków / jaworznia	10
#herson	10
#the north east	10
#vinnitsa	10
#liège, belgique	10
#yeah right	10
#saint-petes	10
#fringecity	10
#沖縄県名護市	10
#saltaire, west yorkshire	10
#cracov	10
#Казахстан	10
#osório	10
#jazzgumpy	10
#ondres	10
#kochi, kerala	10
#haboobland	10
#belém - pará	10
#big o	10
#são paulo/sp - brasil	10
#traveling	10
#cloud	10
#köln-hürth	10
#lübeck	10
#trissur	10
#on a minecraft server, somewhere.	10
#ilfracombe, devon.	10
#whu	10
#where pigs fly	10
#neither here not there	10
#mydlovary	10
#hinxton	10
#garia, west bengal, kolkata	10
#villeneuve dascq	9
#yaroslavl	9
#ntnu	9
#flekkerøy	9
#sao paulo / brasil	9
#japon	9
#бобруйск	9
#polska kraków	9
#planet mars, cydonia	9
#prc	9
#moor row, cumbria	9
#joão pessoa, pb - brasil	9
#sulthan bathery	9
#always moving	9
#bolzano, südtirol	9
#some where, i think.	9
##occupyatlanta	9
#são paulo - sp / brasil	9
#@denmark	9
#zju	9
#third planet from the sun	9
#tarashcha	9
#berkel	9
#cebu	9
#mvdc	9
#shibuya,toshima	9
#caloocan city	9
#成都	9
#brasília - df, brasil	9
#ilheus	9
#centallo	9
#kasaragod	9
#mérida	9
#hongkong	9
#sài gòn	9
#chandlers ford	9
#qualicum beach, bc	9
#sei pana, batam	9
#nuermberg	9
#sutz	9
#पुणे, महाराष्ट्र, भारत	9
#brasil.	9
#hajom, mark, sverige	9
#uhh, im here, i think.	9
#uberlândia brasil	8
#petrópolis, rj	8
#lax	8
#xidian	8
#long island	8
#earth, solar system, milky way galaxy, universe	8
#the north	8
#right near the submodule	8
#thüringen, deutschland	8
#squamish, bc	8
#РФ, г. Екатеринбург	8
#valparaíso, são paulo, brasil	8
#brooklyn!	8
#sfo	8
#bp-czech	8
#alsace	8
#sendenhorst	8
#@tc	8
#niteroi, rj	8
#北京海淀	8
#southwest	8
#ekb	8
#beijing，china	8
#heavenly dynasty（和谐的天朝）	8
#sjamgjao	8
#são paulo - sp, brasil.	8
#ville demery	8
#mry	8
#banagalore	8
#whitby, on	8
#Минск	8
#brasília -df	8
#western europe	8
#santarém	8
#ain taya	8
#poa	8
#scl	8
#sverige	8
#itay	8
#joão pessoa, brasil	8
#lazistan	8
#suwałki	8
#outer space	8
#thrissur, kerala	8
#oporto	8
#the universe	8
#/bin	8
#Ростов-на-Дону	8
#banˈduŋ ˌɪndoʊˈniːziə	8
#terrier	8
#korean	8
#bedroom	8
#besançon	8
#sysu	8
#Украина, Житомир	8
#kazakstan, karaganda	8
#wiltshire, england	8
#canterlot	8
#varaždin	8
#cluj napoca	8
#far planet	8
#floating about the globe...	8
#acapulco guerrero	8
#cristais paulista, sp, brasil	8
#the interwebs	8
#that place between dreaming and awake	8
#melitopol	7
#eire	7
#大连	7
#mattgoldman	7
#jonestown	7
#g-rap	7
#.......................	7
#brasilia - df, brasil	7
#中华人民共和国福建省厦门市	7
#df	7
#日本国 広島県広島市	7
#onion land	7
#lake tahoe	7
#nova kahovka	7
#中国西安	7
#Благовещенск	7
#typically the office.	7
#planète terre, voie lactée	7
#knurów	7
#saint mandé	7
#wild wild web	7
#27614	7
#montréal québec	7
#iit punjab	7
#cancún, méxico	7
#almería, españa	7
#rottedam	7
#chendu	7
#alfaro city	7
#osaka && munich	7
#嘉義	7
#cluj-napoca, cluj, românia	7
#puerto real (cádiz)	7
#"china wuan"	7
#Гомель, Беларусь	7
#nowhere important	7
#ciudad juárez, méxico	7
#itlay	7
#山楂树树枝	7
#kingwood	7
#marilia/sp - brasil	7
#git oovyaonge@oovyaonge.cafe24app.com:oovyaonge_oovyaonge	7
#docoka	7
#sępólno krajeńskie	7
#bc	7
#bazil	7
#utd	7
#big d	7
#the matrix	7
#moscu, rusia	7
#ural	7
#renteria	7
#somewhere random on planet earth	7
#santa clara del mar	7
#/var/www	7
#beijing&chengdu	7
#standing behind you, stalking...	7
#Березники	7
#debatable	7
#krk	7
#dnepr	7
#bue	7
#nyc / ucsc / polar	6
#philly burbs	6
#xian, shaanxi	6
#cze	6
#福井	6
#patra	6
#ulan-ude	6
#nuzild	6
#16802	6
#córdoba - españa	6
#ludhiana	6
#中国山东省青岛市	6
#munich, bavaria	6
#asturias	6
#great russell street	6
#deepest, darkest wiltshire	6
#cpan, rop	6
#maranhão, brasil	6
#some random top secret base	6
#sussex	6
#ussr	6
#earth, sol, western spiral arm, milky way, omniverse	6
#chiavenna, lombardia, italia	6
#brasília, df	6
#the intergalactic interwebs	6
#Пятигорск	6
#fasdf	6
#unnc	6
#yoyogi	6
#french	6
#フランス	6
#brussel, belgië	6
#goiânia, goiás	6
#pnw	6
#zhejiang province	6
#finalnd	6
#paulínia, são paulo	6
#ベルリン	6
#ururu	6
#zuerich	6
#nikolaev	6
#kakinada	6
#middlebury	6
#the earth	6
#bopohe}|{	6
#Съемная норка кролика	6
#padua	6
#ugvydggsief1c3ryywxpyq==	6
#xian, shanxi	6
#visakapatnam	6
#lyngby	6
#são paulo/sp	6
#yurrup	6
#21042	6
#starvropol, russian federation	6
#stack	6
#sampa	6
#brasil, sp, são paulo, centro	6
#bruz	6
#seattle<->boston	6
#someplace near you	6
#kazahstan	6
#skehanagh park, watergrasshill	6
#the earth	6
#planet pumpkin	6
#iraquis	6
#a city within a state	6
#rpi	6
#appsterdam	6
#homel	6
#méxico, mérida	6
#spain!	6
#córdoba, españa	6
#montreal, qc, can	6
#shenzheng	6
#mukachevo	6
#kraków, polska	5
#charleville-mezieres	5
#中国，杭州	5
#lomagna	5
#ratnagiri	5
#chişinău	5
#webernets	5
#southern africa	5
#uestc	5
#ghaziabad	5
#makati	5
#deklein	5
#arces	5
#kyiev	5
#russland	5
#bolsward	5
#niteroi - rj - brasil	5
#brasov	5
#lancashire, england	5
#consulting	5
#can tho, viet nam	5
#aichi, jpan	5
#problemania.org	5
#hong kong s.a.r.	5
#bhimavaram	5
#germany; 2.osgrid - volksland	5
#brasilia, df	5
#trollhättan	5
#didu	5
#miyazaki	5
#zanè	5
#gothenburg(swedgen)	5
#207	5
#apeiron	5
#bewdley, worcestershire	5
#hambizzle	5
#its complicated	5
#celestial empire	5
#greater nyc	5
#92129 macs ln.	5
#/users/rzm102	5
#lietuva	5
#chinese	5
#levallois-perret	5
#north yorkshire, england	5
#solar system	5
#ciechanki	5
#mérida,yucatán,méxico	5
#cape breton, ns	5
#earth, sol	5
#here :d	5
#anglesey, north wales	5
#belém	5
#aichi	5
#almería	5
#stl	5
#inner space	5
#struck oil	5
#cylon occupied caprica	5
#yorkshire, england	5
#ldn	5
#Россия, Казань	5
#mar del plata	5
#amsterdamn	5
#lonodn	5
#belém - pará - brasil	5
#nieuwdorp	5
#Симферополь	5
#wellington; new zealand	5
#world2.0	5
#klagenfurt	5
#hessle, england	5
#dehradun	5
#www.gzur.org	5
#中国辽宁沈阳	5
#various	5
#santa brigida	5
#europe/czech rep.	5
#maui	5
#jinju	5
#Украина, Запорожье	5
#silicon valey	4
#iitm	4
#kyiv, ukarine	4
#chiapas	4
#earth-616	4
#where you live	4
#grande pointe, mb	4
#hyper island	4
#rf	4
#www.emlprime.com	4
#iruñea nafarroa	4
#ballina	4
#neumarkt	4
#existing between keyboard and chair	4
#sector 8, reality sigma, cow	4
#ifoc	4
#slo	4
#@non_117	4
#venera planet	4
#rua timbira, 2145 teresina/piauí	4
#河南	4
#ribeirão preto - sp	4
#santa rosalia	4
#variable	4
#df, brasil	4
#eivissa	4
#bardowick	4
#laaaaandon	4
#cluj	4
#gunma	4
#brussel	4
#denbigh, north wales	4
#neumünster, deutschland	4
#dniepropetrovsk	4
#bla	4
#anus	4
#n.l.l.v	4
#leganés	4
#underhat	4
#panopticon	4
#天津市南开区华苑产业园区	4
#the nether	4
#bilbo/bizkaia	4
#montreal, québec	4
#district 3, hcmc	4
#west sussex	4
#oau, ile ife.	4
#wired	4
#angus65	4
#Украина	4
#gz	4
#abq	4
#hell	4
#wilrijk	4
#osaka,kobe	4
#séoul	4
#verges, catalonia	4
#Санкт-Петербург	4
#mhm.	4
#sp/brasil	4
#Екатеринбург	4
#lévis	4
#taegu, southkorea.	4
#uxbridge	4
#sol 3	4
#crépy-en-valois	4
#illnoise	4
#orduña, bizkaia	4
#ciudad juarez	4
#magrathea	4
#penedès - catalunya	4
#41015	4
#zz9: plural zα	4
#sant cugat del vallés	4
#深圳	4
#somewhere on the west coast	4
#ukraina	4
#usc	4
#РФ	4
#hertfordshire, england	4
#twitter.com/leemallabone	4
#横浜	4
#são carlos, sp - brasil	4
#saxony_germany	4
#11231	4
#+53.3 -001.5	4
#the semantic web	4
#/home/foozzi	4
#morroco	4
#goiânia - goiás - brasil	4
#schoonhoven	4
#miyagi	4
#building 47	4
#vilafranca del penedès	3
#tty0	3
#são gonçalo / rj	3
#di dalam hati wanita	3
#groenlo	3
#www.fraudpointer.com	3
#la?	3
#中国广州	3
#rondônia - brasil	3
#mcveytown	3
#en fuga	3
#osca, pyrenees	3
#33a cuu long, f.2, tan binh, tp.hcm	3
#leghorn	3
#埼玉県	3
#@edebill	3
#České budějovice	3
#sydneylondon	3
#上海,中国	3
#galicia	3
#campo grande - ms, brasil	3
#mobo	3
#dungeons.	3
#srinagar, kashmir	3
#12 hours from anywhere	3
#aus moskau	3
#shen zhen,guang dong	3
#madeira	3
#utc -0500	3
#rüsselsheim	3
#osaka@japan	3
#10.331681,123.907886	3
#gasteiz, basque country	3
#www.bulk-inc.com	3
#culiacán, sinaloa, méxico	3
#internettsburg	3
#Česká republika, praha	3
#www	3
#nipppon	3
#djursholm	3
#reykjavík	3
#b-town	3
#parts unknown	3
#the grid	3
#palamos	3
#northeastern united states	3
#alger	3
#wybcz	3
#neverland	3
#hamburgo	3
#pernambuco, brasil	3
#korat	3
#yoshkar-ola	3
#parkstein	3
#durgapur	3
#patras	3
#prueba	3
#somewhere beyond the sea	3
#software engineer	3
#west-brabant	3
#internetz	3
#mallorca	3
#rj, brasil	3
#tirol	3
#90805	3
#kratumban, samutsakorn	3
#the netherlanths	3
#massonnens, suisse	3
#08691	3
#schwanau	3
#serbien	3
#altanta	3
#rva	3
#ap	3
#$texas	3
#ustc	3
#corea	3
#	3
#scotland, u.k	3
#earth (mostly)	3
#sfo / sjc	3
#dorset	3
#goettingen	3
#north-west england	3
#trichy	3
#niteroi - rj	3
#world wide	3
#são josé dos campos, sp - brasil	3
#yangon	3
#underground	3
#limanowa/kraków	3
#brasilia - brasil	3
#viêt nam	3
#władysławowo	3
#são paulo brasil	3
#algerie	3
#greater dfw	3
#en_us	3
#衡阳	3
#queretaro	3
#brasil - sp	3
#virtual space	3
#11215	3
#mrthe.name	3
#são josé dos campos/sp - brasil	3
#vimim	3
#love field	3
#hkd	3
#camaragibe	3
#anywhere	3
#kyev	3
#四川.绵阳	3
#fukushima koriyama	3
#markt berolzheim	3
#joao pessoa - pb	3
#moose creek, on	3
#enfield, ns	3
#0x000000	3
#日の本	3
#the netherlands, europe	3
#chitrakoot	3
#vzla	3
#90028	3
#yamaguchi	3
#РФ, Владимир	3
#tunisie	3
#north west england	3
#wirral, england	3
#tucuman	3
#malaga	3
#if city	3
#eastern united states	3
#são félix, bahia, brasil	3
#one the move	3
#the_darkside	3
#mines	3
#béziers	3
#wales, britain	3
#northamptonshire	3
#神奈川県藤沢市	3
#beijinchaina	3
#reggio emilia,italia	3
#Россия, Оренбург	3
#shang	3
#frankfurt/hanau	3
#Ústí nad labem	2
#pilani	2
#shiga	2
#concórdia - santa catarina	2
#akb	2
#dehiwala	2
#dimap	2
#济南	2
#middle england	2
#kashipur	2
#fedora	2
#jhb	2
#zulte	2
#yew nork	2
#creating your github account...	2
#córdoba/veracruz - méxico	2
#schipluiden	2
#irc.freenode.net #python veloutin	2
#behind your firewall	2
#06106	2
#19382	2
#mdn	2
#maginus	2
#montélimar	2
#bruyères-le-châtel (91)	2
#forest row, england	2
#dumfries	2
#vitoria-gasteiz	2
#czechrepublic/orlová-lutyně	2
#east & west	2
#amherst, nova scotia	2
#Томия, Япония	2
#brasília-df-brasil	2
#rossendale, lancashire	2
#lalaland	2
#normandie	2
#/c/emu/trinitycore/	2
#teh internetz	2
#schauernheimerstr. 8, d-67125 dannstadt-schauernheim	2
#suwon, korea	2
#中国黑龙江大庆	2
#targu mures, romainia	2
#chicagoland area	2
#makeevka	2
#地獄	2
#uzhgorod	2
#vinaros, españa	2
#beauharnois, qc	2
#russian,rh,sayanogrosk	2
#são carlos - são paulo - brasil	2
#guidlford	2
#delluf	2
#sao paulo - brasil	2
#94610	2
#首都相模大野	2
#east midlands	2
#cgn	2
#são josé dos campos/sp	2
#here.	2
#中国福建福州	2
#nyu	2
#layer 13	2
#yucatán	2
#sab.com	2
#94117	2
#cluj napoca, românia	2
#the great white north	2
#são josé	2
#stari zednik	2
#flanders	2
#dracena, são paulo, brasil	2
#hinxton - united kingdom	2
#somewhere, over the rainbow	2
#avranches	2
#ponyland	2
#planet earth...	2
#gotham	2
#berne	2
#trivandrum, kerala	2
#bra[sz]il	2
#sapporo, hokkaido	2
#vsetín	2
#city 17	2
#macae-rj, brasil	2
#22602	2
#hammah	2
#lower haight	2
#são josé dos campos, sp	2
#uiwang, korea	2
#cancun, qroo.	2
#czestochowa	2
#guaruja	2
#holland!	2
#liphook	2
#the united states	2
#845	2
#mensk	2
#4546176880394011	2
#hel	2
#czech rep.	2
#caltech	2
#nyc/sf	2
#cancun, méxico.	2
#glorious nippon	2
#undecided	2
#méxico d,f.	2
#goring-on-thames	2
#far, far away!	2
#africa	2
#skoczów	2
#blackstone, qld	2
#iamfredng@gmail.com	2
#chong qing	2
#praha, Česká republika	2
#são paulo, sp - brasil	2
#cozumel, méxico	2
#tahiti, french polynedia	2
#são paulo/sp brasil	2
#sockerbruket 33, 414 51, gÖteborg	2
#traveling salesman	2
#phily	2
#kc	2
#19.341435, -99.165237	2
#glenavy	2
#www.tellago.com	2
#/users/fabi	2
#11201	2
#chambery	2
#niterói, rj	2
#french riviera	2
#mikew	2
#cape town - south africa	2
#10001	2
#trentino	2
#vodafone, internet	2
#tufts	2
#location	2
#nyc / ber	2
#stavropol, russian federation	2
#camerino	2
#75000	2
#berchem	2
#rus	2
#shandong	2
#forlimpopoli	2
#berkshire	2
#kiyv	2
#milky way, universe, expanding mass	2
#ruhrgebiet	2
#vidin;bulgaria	2
#laaaarndon	2
#shaanxi xian	2
#София, България	2
#Украина, Донецк	2
#grid	2
#rva + nyc	2
#villefranche-sur-saône	2
#02138	2
#cape town south africa	2
#hồ chí minh city	2
#neotropic	2
#improving izariam	2
#法国，tours	2
#中国湖北武汉	2
#sardinia	2
#the island	2
#massassachusetts	2
#guerrero, méxico	2
#norcal	2
#eu.	2
#cymru (south wales) uk, tywi valley	2
#sask, can.	2
#hangchow	2
#pgh	2
#the haque	2
#hopefully somewhere warm and sunny	2
#earth planet	2
#48.723197,12.768805	2
#western siberia	2
#bedfordshire	2
#florianópolis - brasil	2
#malnova, latgola	2
#uviéu (asturies)	2
#earth, sol system	2
#osaka-city	2
#p.s.d.r.e.r.f.	2
#planet earth, with firmly both feet	2
#somewhere cloudy	2
#espírito santo - brasil	2
#pondicherry	2
#türkiye	2
#sart lez spa	2
#bigbuzzylocation	2
#vagabonding	2
#wordwide	1
#denver!	1
#hauj khas	1
#jkl/fin	1
#mozhajsk	1
#net	1
#florianopolis	1
#härnösand	1
#geek between the keyboard and the chair.	1
#the ham	1
#russian/tyumen	1
#珠海	1
#bretagne	1
#dumbo	1
#@fredrocious	1
#Великий Новгород	1
#demark	1
#opus	1
#burwood east	1
#lanzarote, canary islands	1
#classified	1
#genève	1
#alexanderie, Égypte	1
#92883	1
#the multiverse ...	1
#tacosrus	1
#gxnn	1
#chorzów	1
#linodia	1
#jehay	1
#mikocheni	1
#twisted disneyland	1
#perros guirec	1
#apt	1
#jerez	1
#uk_uk, lviv	1
#northeast	1
#brasília, df - brasil	1
#the planet	1
#traveling the world.	1
#greater philly area	1
#xanth	1
#pitesti	1
#behind the phosphor	1
#dark alley	1
#katwijk zh	1
#kazaǹ	1
#easy	1
#ilhéus - bahia	1
#everywhere yet nowhere	1
#/root/	1
#veliko tarnovo	1
#miensk-litowski, biełaruthenia	1
#the localhost	1
#xjf	1
#karlruhe	1
#https://gitorious.org/~elf-pavlik	1
#a happy place	1
#here and there.	1
#-_-	1
#occupied palestinian territory	1
#lutsk	1
#west coast, the states	1
#calfornia	1
#Ísland	1
#brasília - brasil	1
#naters	1
#+52° 21 16.01", +4° 57 20.67"	1
#495	1
#little brington, england	1
#mid-atlantic	1
#münchen/munich/mnichov/Мюнхен	1
#test	1
#90292	1
#brignoud	1
#bitbucket	1
#a desert island	1
#www.daum.net	1
#bahia	1
#transcontinental	1
#germay	1
#nazi moonbase (on the moon)	1
#msp	1
#somewhere out there	1
#Томск, Россия	1
#/dev/null;	1
#中国浙江杭州	1
#goiânia goiás brasil	1
#labège	1
#epicmorgia	1
#ub,mgl	1
#@sfrdmn	1
#republica dominicana	1
#orhem	1
#uberlândia	1
#phase space	1
#qz	1
#sankt-peterburg	1
#23509	1
#cancun	1
#95348	1
#iwate	1
#nürtingen	1
#sebastopol	1
#earth?	1
#earth!	1
#perm	1
#bnagalore	1
#im around.	1
#the universe.	1
#天津市河东区	1
#goiania	1
#boardtown 32, bitstreet 8	1
#1 raffles institution lane	1
#center valley	1
#moscow\	1
#127.0.0.1:8888	1
#singaproe	1
#locating...	1
#allegheny college	1
#marília/sp - brasil	1
#nagoya,aichi / mt関連の物など色々作っています。	1
#somewhere over the rainbow.	1
#the internet.	1
#sao paulo brasil	1
#tarnowskie góry	1
#rover	1
#ici	1
#boulogne billancourt	1
#argyll, scotland	1
#uchicago	1
#94131	1
#miensk-litowski, kryŭja	1
#Йошкар-Ола	1
#venezia	1
#@home	1
#94720	1
#kalix	1
#cafelândia-sp	1
#muree	1
#viña del mar	1
#ldn — nyc	1
#osaka-shi osaka-pref	1
#darlinghurst	1
#inotherworld	1
#jaén	1
#しんじく	1
#grudziądz	1
#joão pessoa / pb / brasil	1
#aizu	1
#far far away land	1
#catskills	1
#東京都世田谷区用賀	1
#경남 창원시 마산회원구	1
#eets	1
#mazangé	1
#bruxelles - belgique	1
#wenen, oostenrijk	1
#cipherspace	1
#cape town. south africa	1
#estudiante	1
#seilles	1
#korea, south	1
#twin cities, minn.	1
#nigeira	1
#台灣（taiwan）	1
#chang sha	1
#virgo supercluster, milky way galaxy, sol system, earth	1
#rua turi 184	1
#santo andré - sp - brasil	1
#pratteln, schweiz	1
#東京都渋谷区神宮前1-1-1	1
#zanjan	1
#besançon / aix-en-provence	1
#phila	1
#são josé dos campos, brasil	1
#andheri	1
#cucuta	1
#/home/dilibau/	1
#nimes	1
#auvelais	1
#Россия, Санкт-Петербург	1
#сеть)	1
#+09:00	1
#turin, italiy	1
#kanhangad	1
#moray	1
#70123	1
#roncade	1
#montes claros - brasil	1
#marília - sp - brasil	1
#java	1
#higashi-nihonbashi	1
#north wilkesboro	1
#catamarca	1
#marieville, qc	1
#bosnia & herzegovina	1
#lago di garda	1
#kochi	1
#Россия, Екатеринбург	1
#são carlos - sp	1
#shropshire, england	1
#sillycone valley	1
#d	1
#timișoara	1
#rio das ostras	1
#utc+1	1
#jutphaas	1
#the wild, wild west	1
#ailleurs	1
#here, ithink	1
#yorkshire (england)	1
#weiqing building 709, thu	1
#a coruña, galicia, españa	1
#東京都	1
#kathmandy	1
#private	1
#doap.com	1
#kalymnos	1
#goiânia-go / brasil	1
#mogi das cruzes, sp	1
#dominican rapublic	1
#outah space	1
#frankfurt / main	1
#comodo	1
#liestal, schweiz	1
#<radar offline>	1
#manipal/bokaro	1
#castlemaine, australila	1
#missal	1
#thessaloniki	1
#park city	1
#skyrim	1
#11230	1
#azeroth	1
#merry ol england	1
#brébeuf, qc	1
#ksa	1
#leicestershire, england	1
#far east	1
#daiict,gandhinagar	1
#bègles	1
#94041	1
#on the planet	1
#queensland	1
#hinterlands	1
#Украина, Винница; ukraine, vinnitsya	1
#ac	1
#transylvania	1
#bengaluru/marudhur	1
#nyc, sf	1
#vtech	1
#bmnville	1
#Кривой Рог	1
#2次元	1
#emeryville	1
#2:450	1
#universe	1
#whistler	1
#hampshire, united kingdon	1
#the hidden fortress	1
#luxmebourg	1
#d.f. méxico	1
#wrocław, polska	1
#jönköping	1
#dogpatch	1
#gelderland	1
#funky town	1
#republica 701	1
