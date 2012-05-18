# -*- coding: utf-8 -*-

def check_unresolved(locstr):
    for key in fix_unresolved:
        if locstr in key: return fix_unresolved[key]


def tests():
    assert(check_unresolved('nyc') == 'United States')
    assert(check_unresolved('perú') == 'Peru')
    assert(check_unresolved('###############') == None)
    print 'tests pass'


fix_unresolved = {
    frozenset(['nyc', 'silicon valley', 'sf', 'uiuc', 'new england', 'philly', 'ucla', 'west coast', 'potrero, sf', 'cape may court house', 'u.s.a.', 'rit', 'northwest', 'trabuco canyon', 'west philly', 'mit', 'unlv', 'chicagoland', 'sdut', 'ucsc', 'pdx', 'u s a']): 'United States',
    frozenset(['montreal', 'montreal, qc', 'montréal, québec', 'québec', 'montréal', 'quebec', 'prévost', 'montréal, qc', 'tiohtiake', 'montreal, quebec']): 'Canada',
    frozenset(['england', 'scotland', 'oxfordshire', 'oxfordshire, england', 'u.k.', 'snowdonia, north wales', 'broughty ferry, scotland', 'cambrdige', 'u k', 'devon, england', 'bonnie scotland', 'bonsall, derbyshire']): 'United Kingdom',
    frozenset(['munich', 'cologne', 'münchen', 'deutschland', 'düsseldorf', 'nürnberg', 'köln', 'göttingen', 'osnabrück', 'isny', 'duesseldorf', 'montabaur', 'münster']): 'Germany',
    frozenset(['são paulo, brasil', 'brasil', 'são paulo', 'são paulo - sp', 'sao paulo', 'são paulo - brasil', 'são paulo, sp, brasil', 'são paulo, sp', 'goiânia', 'joão pessoa', 'três rios - rj', 'florianópolis', 'santo andre - sp - brasil', 'são paulo - sp - brasil', 'são paulo sp', 'são paulo brasil', 'três rios rj', 'são paulo sp brasil', 'santo andre sp brasil', 'brasilia']): 'Brazil',
    frozenset(['russian federation', 'ekaterinburg', 'ulyanovsk', 'Москва', 'stary oskol', 'nizhny novgorod', 'moskow', 'ptz', 'russian', 'rnd', 'blagoveschensk, amur region, russian federation', 'Набережные Челны', 'Россия, Москва, Ногинск']): 'Russia',
    frozenset(['chambéry', 'meyrargues', 'auvergne', 'rueil malmaison', 'evry', 'aix en provence', 'gex']): 'France',
    frozenset(['korea']): 'South Korea',
    frozenset(['istanbul', 'eskisehir', 'izmir']): 'Turkey',
    frozenset(['hyderabad', 'varanasi', 'bengaluru', 'ahmedabad', 'kerala', 'gandhinagar, gujarat', 'kolkata']): 'India',
    frozenset(['zurich', 'zürich', 'neuchatel', 'lucerne', 'paudex', 'stäfa', 'geneve']): 'Switzerland',
    frozenset(['méxico', 'méxico city', 'uruapan michoacán méxico']): 'Mexico',
    frozenset(['sapporo', 'osaka', 'yokohama', 'japanese', 'kagurazaka', 'kanagawa', 'nagoya', 'chiba', 'ja', '東京', 'kagurazaka']): 'Japan',
    frozenset(['göteborg', 'linköping', 'gothenburg', 'swedish igloo']): 'Sweden',
    frozenset(['europe->poland->gorzow', 'kraków', 'wrocław', 'cracow', 'warszawa', 'dąbrowa górnicza, polska', 'europe >poland >gorzow']): 'Poland',
    frozenset(['bucuresti', 'bucurești, românia', 'iaşi, românia', 'cluj-napoca', 'iasi', 'cluj napoca']): 'Romania',
    frozenset(['ghent', 'bruxelles', 'liège']): 'Belgium',
    frozenset(['ukreine', 'lviv', 'kyiv', 'kharkov', 'cherkassy']): 'Ukraine',
    frozenset(['patagonya']): 'Argentina',
    frozenset(['valparaíso']): 'Chile',
    frozenset(['gansu', "xi'an", 'beijng', 'hang zhou', '杭州', '福建厦门', '上海', '江苏苏州', '中国天津', '北京', '广州', '中国', '河南焦作', '家', '杭州西湖区', '广东 深圳', '中国深圳', 'beijingchina', '昆明']): 'China',
    frozenset(['medellin', 'envigado! :']): 'Colombia',
    frozenset(['czech rebublic']): 'Czech Republic',
    frozenset(['itämerenkatu 13', 'itämerenkatu']): 'Finland',
    frozenset(['soerabaja, east java']): 'Indonesia',
    frozenset(['milano', 'turin', 'mozzanella', 'italia']): 'Italy',
    frozenset(['almere', 'antwerp', 'flanders, eu', 'uddel']): 'Netherlands',
    frozenset(['perú']): 'Peru',
    frozenset(['phillipines']): 'Philippines',
    frozenset(['catalunya', 'canary islands', 'seville', 'santa Úrsula', 'piera']): 'Spain',
    frozenset(['taoyuan']): 'Taiwan',
    frozenset(['viet nam', 'hanoi', 'ha noi, viet nam', 'ha noi - viet nam', 'ha noi', 'ha noi viet nam', 'hà nội, việt nam']): 'Vietnam',
    frozenset(['tehran']): 'Iran',
    frozenset(['joburg', "jo'burg"]): 'South Africa',
    frozenset(['luxemburg']): 'Luxembourg',
    frozenset(['københavn']): 'Denmark'

#    frozenset([]): 'Australia',
#    frozenset([]): 'Austria',
#    frozenset([]): 'Ireland',
}

if __name__ == '__main__':

    tests()

#, 'irc perl org'
#, 'beyond your wildest dreams'
#, 'pacific northwest'
#, 'northern england'
#, 'cmpt'
#, 'stornoway'
#, 'ahoka@rizon'
#, 'hampshire, england'
#, 'cern'
#, '?'
#, 'yay area'
#, 'the internets'
#, 'world wide web'
#, ', hoya'
#, 'samstagern'
#, 'belém/pa brasil'
#, 'burgum'
#, 'zz plural z alpha'
#, 'changes a lot'
#, 'yokohma'
#, 'uzb'
#, 'united kingdon'
#, 'wien'
#, 'ciracas'
#, 'luik'
#, 'bolzano'
#, 'jogjakarta'
#, 'l'
#, 'tübingen'
#, 'varick street'
#, '中国上海'
#, 'n e'
#, 'gijón'
#, 'matlock, derbyshire'
#, '::'
#, 'u s'
#, 'north east england'
#, 'interwebs'
#, 'cal poly slo'
#, 'the yay'
#, 'troon, scotland'
#, 'root'
#, '° ' "n ° ' "w m'
#, 'online'
#, 'cardrona'
#, 'pluto'
#, 'aarhus'
#, 'muc'
#, 'north wales'
#, 's'
#, 'pici'
#, 'ffm'
#, 'altach, Österreich'
#, 'f:\project\monitorproject'
#, 'argetnina'
#, 'lietuva lithuania, gmt+'
#, 'america'
#, 'stanford'
#, 'reykjavik'
#, 'espirito santo, brasil'
#, 'neo sitama'
#, 'atl'
#, 'homalg project'
#, '/dev/console'
#, 'berkshire, england'
#, 'odd pod, troon, scotland'
#, 'atx'
#, 'bahia blanca'
#, 'nurnberg'
#, 'belgique'
#, 'lisboa'
#, '/home/askn'
#, ''merica'
#, '浙江宁波'
#, 'lostwithiel'
#, 'nizhny novgorod, russian federation'
#, 'jorvas'
#, 'vilafranca del penedès, catalunya'
#, 'sfbay area'
#, 'gandhinagar'
#, 'nova scotia'
#, 'n/a'
#, '中国浙江省杭州市'
#, 'praha'
#, 'a coruña'
#, 'córdoba'
#, 'são paulo sp, brasil'
#, 'nova'
#, 'tver'
#, 'swizerland'
#, 'hacking from the moon'
#, 'the nederlands'
#, 'uc santa barbara'
#, 'tejas'
#, 'niterói/rj'
#, 'latvija, rīga'
#, '渋谷'
#, 'belém pará'
#, 'rupnagar'
#, 'chn'
#, 'méxico, d f'
#, 'upstate new yawk'
#, 'manipal'
#, 'whistler, bc'
#, 'russian, ryazan'
#, 'block island'
#, 'karkala'
#, 'tunbridge wells'
#, 'krakow'
#, '上海市浦东新区居里路 号'
#, '風見学園'
#, 'frankfurt, gemany'
#, 'lith'
#, 'leningrad'
#, 'hradec králové'
#, 'saarbrücken'
#, 'strängnäs'
#, 'köln, deutschland'
#, 'são carlos/sp'
#, 'idf'
#, 'slavičín'
#, 'hampshire'
#, 'newfoundland'
#, 'nomadic'
#, 'são paulo / brasil'
#, 'brasil/goiás/goiânia'
#, 'rychnov nad kneznou / praha'
#, 'suwon'
#, 'the mountains'
#, 'perm'
#, 'cần thơ'
#, 'czecho'
#, 'south wales'
#, 'fukuoka'
#, 'over there'
#, 'var location = { country: 'germany', city: 'saarbrücken' };'
#, 'ryazan'
#, 'sea / sfo / nyc / bos'
#, 'deajeon'
#, 'jocala com'
#, 'port coquitlam, bc'
#, 'Россия, Московская область, Долгопрудный'
#, 'fennectar, fennectus state, planet cyrusian'
#, 'saigon'
#, 'wales'
#, 'urumqi'
#, 'méxico df'
#, 'lancashire'
#, 'hà nội việt nam'
#, 'eivissa, españa'
#, 'españa'
#, 'méxico d f'
#, 'Сибирь, Кузбасс'
#, '浙江省杭州市文二路 号'
#, 'Казань'
#, 'arkania'
#, 'hell on earth'
#, 'fotaleza'
#, '/home/necronet'
#, 'leon, gto'
#, 'none'
#, 'kobe'
#, 'barnet'
#, 'tyumen'
#, 'north america'
#, '@philingrey'
#, 'catalonia'
#, 'elbląg'
#, 'málaga'
#, 'galactic sector zz plural z alpha'
#, 'quebec city'
#, 'oświęcim'
#, '武汉'
#, 'záhony'
#, 'stony brook'
#, 'oaxaca, méxico'
#, 'jyväskylä'
#, 'l a'
#, 'málaga, españa'
#, 'waseco building'
#, 'pacific palisades'
#, 'sun/sol'
#, 'poznan'
#, 'joão pessoa, paraíba'
#, 'brasília, brasil'
#, 'hellsinki / funland'
#, 'shang hai'
#, 'cascadia'
#, 'gdansk'
#, 'gdańsk'
#, 'alresford'
#, 'dollar, clackmannanshire'
#, 'the d'
#, 'Харьков'
#, 'scenic hinxton'
#, 'timisoara'
#, 'kyiv, ukrane'
#, 'rendsburg@germany'
#, 'gotland'
#, 'wow freakz'
#, 'idolgo com'
#, 'wonderland'
#, 'behind you'
#, 'the cloud'
#, 'bronx'
#, 'vernouillet'
#, 'space'
#, '˚∆˚'
#, 'cornell'
#, 'chania crete'
#, 'effretikon'
#, 'bavaria'
#, 'llanfrothen, north wales'
#, 'oisy le verger'
#, 'woclaw'
#, 'windows'
#, 'bundeshauptstadt'
#, 'vorarlberg'
#, 'bogota'
#, 'durandalingrad'
#, 'cheonan, korea'
#, 'mass, u s'
#, 'românia'
#, 'prg'
#, 'right behind you!!!'
#, 'brasília'
#, 'internets'
#, 'united stated'
#, 'milky way'
#, 'kocaeli, turkiye'
#, 'galway'
#, 'american midwest'
#, 'shizuoka'
#, 'hanoi, viet nam'
#, 'peking'
#, 'ciudad obregon sonora , méxico'
#, 'livry gargan'
#, 'brasília, df, brasil'
#, 'south england'
#, 'frankfurt'
#, 'suburbia'
#, 'sfca'
#, 'llanarmon dyffryn ceiriog'
#, 'milky way galaxy'
#, 'here, now'
#, 'nit kozhikode, kerala'
#, 'janelia farm research campus'
#, 'softslayer'
#, 'thrissur'
#, 'joão pessoa pb'
#, '中山大学'
#, 'usofa'
#, 'bahía blanca'
#, 'hz'
#, 'jamaca'
#, 'whatloo'
#, 'montermorelos'
#, 'le bourget du lac'
#, 'brasil, brasília'
#, 'iit kanpur'
#, 'the pleiades'
#, 'location independent'
#, 'nagpur'
#, 'ederbringhausen'
#, 'irc datnode net'
#, 'kotamobagu'
#, 'hyrule'
#, 'valles marineris, mars'
#, 'location'
#, 'vironezh'
#, 'singularity'
#, 'campina grande pb'
#, '/home'
#, 'sausalito'
#, 'right behind you!'
#, 'turkiye'
#, 'yayyyy'
#, 'gandhinagar/ahmedabad'
#, 'solaro'
#, 'schweiz'
#, 'nanking'
#, 'münchen, deutschland'
#, 'earth, solar system'
#, 'phx'
#, 'Österreich'
#, 'bhubaneswar'
#, '/home/wintervenom'
#, 'shambala'
#, 'epfl'
#, 'italia, milano'
#, 'việt nam'
#, 'engineer'
#, 'banglore'
#, 'são carlos, sp'
#, 'on a boat'
#, 'balneário camboriú'
#, 'north east, england'
#, 'kaslo, bc'
#, 'the rose city'
#, 'goiânia go'
#, 'tampon'
#, 'България, Свищов'
#, 'medellín'
#, 'help! polar bears are attacking me!'
#, 'down under'
#, 'slovenija'
#, 'yorkshire'
#, 'noe'
#, 'långshyttan'
#, '中国 浙江 衢州'
#, 'glyfada'
#, 'cologne ger'
#, 'moskau'
#, 'bcn'
#, 'brasília/df, brasil'
#, 'görlitz'
#, 'sussex, england'
#, 'west yorkshire'
#, 'florianopolis, brasil'
#, 'mtl'
#, 'sf baby!'
#, 'réunion'
#, 'Санкт Петербург, Россия'
#, 'lidköping'
#, 'ukrain'
#, '秦皇岛'
#, 'maryland's eastern shore'
#, 'curitba/pr brasil'
#, 'kumamoto'
#, 'Минеральные Воды'
#, 'campo grade ms, brasil'
#, 'narnia'
#, 'phl'
#, 'south pole'
#, 'donostia'
#, 'gmt+'
#, 'hertfordshire'
#, 'sp brasil'
#, 'sao paulo, brasil'
#, 'rensselaer polytechnic institute'
#, 'ufsc'
#, '萧山'
#, 'são josé dos campos, são paulo, brasil'
#, 'goiania, goiás, brasil'
#, 'great britain'
#, 'remote developer'
#, 'los angeles area'
#, 'zurich, swtizerland'
#, 'ilhéus/bahia/brasil'
#, 'rmit uni'
#, 'da nang, viet nam'
#, 'vellerat'
#, 'brasil, rj'
#, 'aubergenville'
#, 'sevastopol'
#, 'roaming'
#, 'herzliya'
#, 'frozen reindeer country'
#, 'melverley, shropshire'
#, 'alnilam'
#, 'inland norcal'
#, 'the hague'
#, 'wollishofen, zürich'
#, 'dans le'
#, 'eastern seaboard'
#, 'cis, eecs, peking univ'
#, 'hangzhou，zhejiang，china'
#, 'floduh'
#, 'los países bajos'
#, '' above ground floating on a balloon'
#, 'definitely!'
#, 'galicia, españa'
#, 'irc://irc datnode net: /#hacking'
#, 'münster, deutschland'
#, 'interwebz'
#, 'bunnik'
#, 'zhodino'
#, 'nullptr'
#, '° ' n, ° ''
#, 'who knows where'
#, 'takoyaki'
#, 'blowmage'
#, 'ku'
#, 'arkhangelsk'
#, 'sthlm'
#, 'bengalooru'
#, 'cesário lange/itapetininga sp'
#, 'compiègne'
#, 'web'
#, 'chisinau'
#, 'südwestdeutschland'
#, 'münster, deustchland'
#, 'rio piedras'
#, 'são carlos'
#, 'way up north, scotland'
#, 'cny'
#, 'schwyz'
#, 'likely indoors'
#, 'very small small town'
#, 'leidschendam'
#, 'phillynyc'
#, 'qro'
#, 'goiânia, brasil'
#, 'Łaziska górne'
#, 'montreal,qc'
#, 'space the final frontier'
#, 'pek'
#, 'colbert nation'
#, 'nippon'
#, '北京，中国'
#, 'a few places'
#, 'yokohama city'
#, 'ranchi'
#, 'sophia antipolis'
#, 'reken'
#, 'firenze'
#, 'blighty'
#, '河南，中国'
#, '@malsup on twitter'
#, 'united states est'
#, '日本'
#, '中国南昌'
#, 'mönchengladbach'
#, 'wroclaw'
#, 'isla'
#, 'pécs'
#, 'le kremlin bicêtre'
#, 'socal'
#, 'everywhere but nowhere'
#, 'ussel'
#, '浙江，杭州'
#, '/dev/hell'
#, 'bedum'
#, 'brasil, são paulo sp'
#, 'rus, spb'
#, 'louisianna'
#, 'lasalle, quebec'
#, 'teldrassil'
#, 'default city'
#, 'dnepropetrovsk'
#, 'xi'an,shaanxi,p r c'
#, 'freenode'
#, 'home'
#, 'würzburg'
#, 'east coast'
#, 'somewhere around the world'
#, 'alwernia'
#, 'level'
#, 'Ústí nad orlicí megapolis'
#, 'hcm'
#, 'worcestershire, england'
#, 'williams lake, bc'
#, 'pakkret, nonthaburi'
#, 'prag'
#, 'xàtiva'
#, 'sao paulo sp'
#, 'custom real estate websites'
#, 'earth, spiral arm, milky way'
#, 'middle earth'
#, 'rio'
#, 'kosice'
#, 'manningtree, england'
#, 'moon base alpha'
#, 'someplace near you'
#, 'nehterlands'
#, 'loltah'
#, 'lsju'
#, 'cloverdale, b c'
#, 'with the finger on the keyboard ;'
#, 'peachtree corners'
#, 'warszawa, polska'
#, 'krakow/kyiv'
#, 'bei jing'
#, 'cúcuta'
#, 'nasa goddard'
#, 'kharkov, urkaine'
#, 'oaklandia'
#, 'são mateus espirito santo'
#, 'cordoba'
#, 'mallorca, españa'
#, 'shuswap, bc'
#, 'upton'
#, 'Долгопрудный'
#, 'gloucseter'
#, 'nagano'
#, 'western hemisphere'
#, 'Украина, г Винница'
#, '在地球上'
#, 'chicoutimi, qc'
#, 'milano, italia'
#, 'newyork'
#, 'silicon slopes'
#, 'sachsen'
#, 'the desert'
#, 'petsamo, lapland'
#, 'siberia'
#, 'shell'
#, 'the czech republic'
#, 'londinium'
#, 'oaxaca'
#, 'bluelovers'
#, 'rueti zh'
#, 'bellatrix'
#, 'donostia gasteiz'
#, 'trivandrum kerala'
#, 'rajkot'
#, 'nederlands'
#, 'kansas! city!'
#, 'ladkrabang'
#, 'maarn'
#, 'orléans'
#, 'world wide wiretap'
#, '@squarism'
#, 'norrköping'
#, 'rajshahi'
#, 'sonoma'
#, 'russian federation, spb'
#, 'anime and mango'
#, 'wakayama pref'
#, 'on the interwebz'
#, 'euskadi'
#, 'Россия, Москва'
#, 'roudnice nad labem'
#, 'goiânia, goiás, brasil'
#, 'nwa'
#, 'joao pessoa, pb brasil'
#, 'slovak republic'
#, 'teh internets'
#, 'earht planet'
#, 'bistrița, românia'
#, 'czech'
#, 'd c'
#, 'stavropol'
#, 'sassenheim'
#, 'chicagoland+wi'
#, 'hongkou'
#, '中国>北京'
#, 'polska'
#, 'são paulo / sp'
#, 'helm's deep'
#, 'sai gon'
#, 'hà nội'
#, 'davidwright@gmail com'
#, 'dfw'
#, 'ringerike'
#, 'asuncion'
#, 'el ceñidor, múgica, michoacán, méxico'
#, 'bruges'
#, 'black books'
#, 'rzeszów/kraków'
#, 'a town near you'
#, 'avesnes sur helpe'
#, 'guwahati'
#, 'aus'
#, 'bellarine peninsula'
#, '#dtla'
#, 'derbyshire'
#, 'puebla, puebla'
#, '☠☠☠ nyc ☠☠☠'
#, 'lost between bits'
#, 'Россия'
#, 'dell inc'
#, 'skype: fljot_'
#, 'campina'
#, 'otaniemi'
#, 'lidzbark warmiński / gdańsk'
#, 'self confidence comes from being sure that your predictions are accurate'
#, '横浜市, 日本'
#, 'frankfurt oder'
#, 'hokkaido'
#, '太倉，蘇州'
#, 'fürth'
#, 'borlänge'
#, 'arbucies'
#, 'nizhnyi novgorod'
#, 'löhne'
#, '$home'
#, 'i came i saw i refactored'
#, 'vitebsk'
#, 'köthen anhalt'
#, 'michoacán, méxico'
#, 'eastern u s a'
#, 'hier'
#, 'brasília df brasil'
#, 'hyères les palmiers'
#, 'Россия, г Рубцовск'
#, 'breizh'
#, 'transnistria'
#, 'europe, earth, the universe'
#, 'hcmc'
#, 'boulogne'
#, 'tubarão/sc, brasil'
#, 'devon'
#, 'right here'
#, 'lincolnshire, england'
#, 'intertubes'
#, 'somewhere between here and there'
#, 'devon/bournemouth home/uni'
#, 'oahu'
#, '黑龙江省哈尔滨市南岗区西大直街 号哈尔滨工业大学一校区a 公寓 寝室'
#, 'santo andré sp'
#, 'worldwide baby!'
#, 'toxicity'
#, 'l'viv'
#, 'nor cal'
#, 'knivsta'
#, 'kanpur'
#, 'são paulo/sp brasil'
#, 'kozloduy'
#, 'xintend'
#, 'mpls'
#, 'batam'
#, 'rhone alpes'
#, 'minnesotta'
#, 'ja_jp'
#, 'méxico, df'
#, 'Калуга'
#, 'chain,bei jing'
#, 'uae'
#, 'left handed coordinate'
#, 'n novgorog'
#, '四机房'
#, '東京都杉並区'
#, 'triniad and tobago'
#, 'orel, rf'
#, 'georgsmarienhütte'
#, 'world citizen'
#, 'tasmania'
#, 'cenote'
#, 'skagit county'
#, 'xi`an'
#, 'toyko'
#, 'trivandrum'
#, 'bielsko biała'
#, 'tenerife'
#, 'kreuzberg'
#, 'pego p p c c'
#, 'worcestershire'
#, 'royal leamingtin spa'
#, 'chicoutimi, québec'
#, 'brittany'
#, 'midwest'
#, '中国 杭州'
#, 'reggio emilia'
#, 'somewhere else'
#, 'kowale'
#, 'on the run'
#, 'cyberjaya'
#, 'saint nazaire'
#, 'hải phòng, hồ chí minh'
#, 'oosterwolde'
#, 'são leopoldo'
#, 'danmark'
#, 'scott afb'
#, 'andreazevedo'
#, 'são paulo/brasil'
#, 'secret volcano lair'
#, 'a five line poem'
#, 'desconocida'
#, 'montreal qc'
#, 'lenzburg'
#, 'coffee bean & tea leaf'
#, 'planet java'
#, 'ilfracombe, devon'
#, 'nagoya univ'
#, '合肥,安徽'
#, 'saint germain en laye'
#, 'whu'
#, 'würselen'
#, 'undisclosed'
#, 'kraków / jaworznia'
#, 'herson'
#, 'the north east'
#, 'vinnitsa'
#, 'liège, belgique'
#, 'yeah right'
#, 'saint petes'
#, 'fringecity'
#, 'akihabara'
#, 'köln hürth'
#, '沖縄県名護市'
#, 'saltaire, west yorkshire'
#, 'cracov'
#, 'Казахстан'
#, 'osório'
#, 'jazzgumpy'
#, 'ondres'
#, 'kochi, kerala'
#, 'haboobland'
#, 'big o'
#, 'traveling'
#, 'cloud'
#, 'lübeck'
#, 'trissur'
#, 'kongens lyngby'
#, 'where pigs fly'
#, 'neither here not there'
#, 'mydlovary'
#, 'sector zz plural z alpha'
#, 'on a minecraft server, somewhere'
#, 'hinxton'
#, 'garia, west bengal, kolkata'
#, 'villeneuve d'ascq'
#, 'yaroslavl'
#, 'ntnu'
#, 'flekkerøy'
#, 'sao paulo / brasil'
#, 'japon'
#, 'são paulo sp / brasil'
#, 'бобруйск'
#, 'polska kraków'
#, 'planet mars, cydonia'
#, 'prc'
#, 'moor row, cumbria'
#, 'sulthan bathery'
#, 'always moving'
#, 'bolzano, südtirol'
#, '#occupyatlanta'
#, 'brasília df, brasil'
#, '@denmark'
#, 'zju'
#, 'joão pessoa, pb brasil'
#, 'tarashcha'
#, 'berkel'
#, 'cebu'
#, 'mvdc'
#, 'shibuya,toshima'
#, 'caloocan city'
#, '成都'
#, 'some where, i think'
#, 'the universe'
#, 'ilheus'
#, 'centallo'
#, 'kasaragod'
#, 'mérida'
#, 'hongkong'
#, 'sài gòn'
#, 'uhh, i'm here, i think'
#, 'chandler's ford'
#, 'qualicum beach, bc'
#, 'sei pana, batam'
#, 'nuermberg'
#, 'third planet from the sun'
#, 'sutz'
#, 'पुणे, महाराष्ट्र, भारत'
#, 'hajom, mark, sverige'
#, 'uberlândia brasil'
#, 'petrópolis, rj'
#, 'lax'
#, 'xidian'
#, 'long island'
#, 'earth, solar system, milky way galaxy, universe'
#, 'the north'
#, 'right near the submodule'
#, 'thüringen, deutschland'
#, 'squamish, bc'
#, 'valparaíso, são paulo, brasil'
#, 'brooklyn!'
#, 'alsace'
#, 'sendenhorst'
#, '@tc'
#, 'niteroi, rj'
#, '北京海淀'
#, 'southwest'
#, 'ekb'
#, 'beijing，china'
#, 'heavenly dynasty（和谐的天朝）'
#, 'sjamgjao'
#, 'ville d'emery'
#, 'besançon'
#, 'mry'
#, 'РФ, г Екатеринбург'
#, 'banagalore'
#, 'poa'
#, 'whitby, on'
#, 'Минск'
#, 'western europe'
#, 'santarém'
#, 'ain taya'
#, 'floating about the globe'
#, 'scl'
#, 'Ростов на Дону'
#, 'sverige'
#, 'itay'
#, 'joão pessoa, brasil'
#, 'lazistan'
#, 'suwałki'
#, 'outer space'
#, 'thrissur, kerala'
#, 'brasília df'
#, 'oporto'
#, '/bin'
#, 'banˈduŋ ˌɪndoʊˈniːziə'
#, 'terrier'
#, 'bp czech'
#, 'korean'
#, 'sfo'
#, 'bedroom'
#, 'sysu'
#, 'Украина, Житомир'
#, 'kazakstan, karaganda'
#, 'wiltshire, england'
#, 'canterlot'
#, 'varaždin'
#, 'far planet'
#, 'acapulco guerrero'
#, 'cristais paulista, sp, brasil'
#, 'the interwebs'
#, 'that place between dreaming and awake'
#, 'melitopol'
#, 'eire'
#, '大连'
#, 'mattgoldman'
#, 'jonestown'
#, 'marilia/sp brasil'
#, '中华人民共和国福建省厦门市'
#, 'df'
#, '日本国 広島県広島市'
#, 'standing behind you, stalking'
#, 'brasilia df, brasil'
#, 'puerto real cádiz'
#, 'onion land'
#, 'Благовещенск'
#, 'lake tahoe'
#, 'nova kahovka'
#, '中国西安'
#, 'typically the office'
#, 'planète terre, voie lactée'
#, 'knurów'
#, 'saint mandé'
#, 'wild wild web'
#, 'montréal québec'
#, 'iit punjab'
#, 'cancún, méxico'
#, 'almería, españa'
#, 'rottedam'
#, 'chendu'
#, 'alfaro city'
#, 'osaka && munich'
#, '嘉義'
#, 'g rap'
#, '"china wuan"'
#, 'Гомель, Беларусь'
#, 'nowhere important'
#, 'ciudad juárez, méxico'
#, 'itlay'
#, '山楂树树枝'
#, 'cluj napoca, cluj, românia'
#, 'kingwood'
#, 'docoka'
#, 'sępólno krajeńskie'
#, 'bc'
#, 'bazil'
#, 'utd'
#, 'big d'
#, 'the matrix'
#, 'moscu, rusia'
#, 'git oovyaonge@oovyaonge cafe app com:oovyaonge_oovyaonge'
#, 'ural'
#, 'renteria'
#, 'somewhere random on planet earth'
#, 'santa clara del mar'
#, '/var/www'
#, 'beijing&chengdu'
#, 'Березники'
#, 'debatable'
#, 'krk'
#, 'dnepr'
#, 'bue'
#, 'nyc / ucsc / polar'
#, 'philly burbs'
#, 'xi'an, shaanxi'
#, 'cze'
#, '福井'
#, 'patra'
#, 'nuzild'
#, 'ludhiana'
#, '中国山东省青岛市'
#, 'munich, bavaria'
#, 'asturias'
#, 'great russell street'
#, 'deepest, darkest wiltshire'
#, 'cpan, rop'
#, 'maranhão, brasil'
#, 'some random top secret base'
#, 'sussex'
#, 'ussr'
#, 'earth, sol, western spiral arm, milky way, omniverse'
#, 'chiavenna, lombardia, italia'
#, 'the intergalactic interwebs'
#, 'Пятигорск'
#, 'fasdf'
#, 'unnc'
#, 'lyngby'
#, 'yoyogi'
#, 'french'
#, 'フランス'
#, 'brussel, belgië'
#, 'seattle< >boston'
#, 'goiânia, goiás'
#, 'ulan ude'
#, 'pnw'
#, 'zhejiang province'
#, 'paulínia, são paulo'
#, 'ベルリン'
#, 'finalnd'
#, 'ururu'
#, 'zuerich'
#, 'rpi'
#, 'nikolaev'
#, 'kakinada'
#, 'middlebury'
#, 'ugvydggsief c ryywxpyq=='
#, 'bopohe}|{'
#, 'brasília, df'
#, 'Съемная норка кролика'
#, 'padua'
#, 'xi'an, shanxi'
#, 'visakapatnam'
#, 'são paulo/sp'
#, 'yurrup'
#, 'starvropol', russian federation'
#, 'stack'
#, 'sampa'
#, 'brasil, sp, são paulo, centro'
#, 'bruz'
#, 'kazahstan'
#, 'skehanagh park, watergrasshill'
#, 'córdoba españa'
#, ''the' earth'
#, 'planet pumpkin'
#, 'iraquis'
#, 'a city within a state'
#, 'north west england'
#, 'appsterdam'
#, 'homel'
#, 'méxico, mérida'
#, 'spain!'
#, 'córdoba, españa'
#, 'montreal, qc, can'
#, 'the earth'
#, 'shenzheng'
#, 'mukachevo'
#, 'miyazaki'
#, 'lomagna'
#, 'ratnagiri'
#, 'chişinău'
#, 'webernets'
#, 'southern africa'
#, 'uestc'
#, 'ghaziabad'
#, 'www gzur org'
#, 'makati'
#, 'belém pará brasil'
#, 'deklein'
#, 'hong kong s a r'
#, 'cylon occupied caprica'
#, 'arces'
#, 'kyiev'
#, 'russland'
#, 'bolsward'
#, 'brasov'
#, 'lancashire, england'
#, 'charleville mezieres'
#, 'consulting'
#, 'can tho, viet nam'
#, 'aichi, jpan'
#, 'bhimavaram'
#, 'goiânia goiás brasil'
#, 'brasilia, df'
#, 'trollhättan'
#, 'didu'
#, 'kraków, polska'
#, 'cape breton, ns'
#, 'zanè'
#, 'levallois perret'
#, 'apeiron'
#, 'bewdley, worcestershire'
#, 'it's complicated'
#, 'celestial empire'
#, 'greater nyc'
#, 'lietuva'
#, 'chinese'
#, 'europe/czech rep'
#, 'north yorkshire, england'
#, 'solar system'
#, 'ciechanki'
#, 'earth, sol'
#, 'hambizzle'
#, 'here :d'
#, 'anglesey, north wales'
#, 'mérida,yucatán,méxico'
#, 'belém'
#, 'aichi'
#, 'almería'
#, 'stl'
#, 'inner space'
#, 'struck oil'
#, 'niteroi rj brasil'
#, 'yorkshire, england'
#, 'ldn'
#, 'Россия, Казань'
#, 'cape town south africa'
#, 'mar del plata'
#, 'amsterdamn'
#, 'lonodn'
#, 'macs ln'
#, 'nieuwdorp'
#, 'Симферополь'
#, 'germany; osgrid volksland'
#, 'wellington; new zealand'
#, '中国，杭州'
#, 'klagenfurt'
#, 'hessle, england'
#, 'dehradun'
#, 'problemania org'
#, '中国辽宁沈阳'
#, 'various'
#, 'santa brigida'
#, 'maui'
#, 'jinju'
#, 'gothenburg swedgen'
#, '/users/rzm'
#, 'Украина, Запорожье'
#, 'silicon valey'
#, 'iitm'
#, 'kyiv, ukarine'
#, '+'
#, 'chiapas'
#, 'where you live'
#, 'grande pointe, mb'
#, 'hyper island'
#, 'rf'
#, 'ballina'
#, 'neumarkt'
#, 'existing between keyboard and chair'
#, 'ifoc'
#, 'slo'
#, 'district , hcmc'
#, 'venera planet'
#, 'eivissa'
#, '河南'
#, 'sol'
#, 'santa rosalia'
#, 'variable'
#, 'df, brasil'
#, 'bardowick'
#, 'rua timbira, teresina/piauí'
#, 'laaaaandon'
#, 'cluj'
#, 'gunma'
#, 'brussel'
#, 'denbigh, north wales'
#, 'neumünster, deutschland'
#, 'dniepropetrovsk'
#, 'bla'
#, 'anus'
#, 'leganés'
#, 'underhat'
#, 'panopticon'
#, 'oau, ile ife'
#, '天津市南开区华苑产业园区'
#, 'the nether'
#, 'bilbo/bizkaia'
#, 'montreal, québec'
#, 'west sussex'
#, 'wired'
#, 'Екатеринбург'
#, 'iruñea nafarroa'
#, 'Украина'
#, 'building'
#, 'gz'
#, 'penedès catalunya'
#, 'angus'
#, 'abq'
#, 'séoul'
#, 'hell'
#, 'wilrijk'
#, 'sector , reality sigma, cow'
#, 'osaka,kobe'
#, 'verges, catalonia'
#, 'sp/brasil'
#, 'lévis'
#, 'uxbridge'
#, '@non_'
#, 'illnoise'
#, 'orduña, bizkaia'
#, 'ciudad juarez'
#, 'magrathea'
#, 'sant cugat del vallés'
#, '深圳'
#, 'n l l v'
#, 'somewhere on the west coast'
#, 'ukraina'
#, 'usc'
#, 'РФ'
#, 'hertfordshire, england'
#, 'crépy en valois'
#, 'zz : plural zα'
#, 'www emlprime com'
#, 'saxony_germany'
#, 'são carlos, sp brasil'
#, 'taegu, southkorea'
#, 'twitter com/leemallabone'
#, 'Санкт Петербург'
#, 'ribeirão preto sp'
#, '横浜'
#, 'the semantic web'
#, '/home/foozzi'
#, 'morroco'
#, 'mhm'
#, 'schoonhoven'
#, 'miyagi'
#, 'vilafranca del penedès'
#, 'aus moskau'
#, 'niteroi rj'
#, 'di dalam hati wanita'
#, 'groenlo'
#, 'west brabant'
#, 'the grid'
#, 'palamos'
#, 'la?'
#, '中国广州'
#, 'osca, pyrenees'
#, 'mcveytown'
#, 'leghorn'
#, '埼玉県'
#, '@edebill'
#, 'České budějovice'
#, 'sydneylondon'
#, '上海,中国'
#, 'são gonçalo / rj'
#, 'galicia'
#, 'mobo'
#, 'b town'
#, 'srinagar, kashmir'
#, 'joao pessoa pb'
#, 'shen zhen,guang dong'
#, 'madeira'
#, 'rüsselsheim'
#, 'osaka@japan'
#, 'en fuga'
#, 'são josé dos campos, sp brasil'
#, 'culiacán, sinaloa, méxico'
#, 'internettsburg'
#, 'reggio emilia,italia'
#, 'www'
#, 'Česká republika, praha'
#, 'nipppon'
#, 'yangon'
#, 'parts unknown'
#, 'scotland, u k'
#, 'northeastern united states'
#, 'alger'
#, 'tty'
#, 'são josé dos campos/sp brasil'
#, 'dungeons'
#, 'wybcz'
#, 'neverland'
#, 'hamburgo'
#, 'pernambuco, brasil'
#, 'korat'
#, 'parkstein'
#, 'durgapur'
#, 'patras'
#, 'prueba'
#, 'somewhere beyond the sea'
#, 'software engineer'
#, 'sfo / sjc'
#, 'internetz'
#, 'mallorca'
#, 'rj, brasil'
#, 'sao paulo brasil'
#, 'tirol'
#, 'kratumban, samutsakorn'
#, 'the netherlanths'
#, 'massonnens, suisse'
#, 'www fraudpointer com'
#, 'schwanau'
#, 'serbien'
#, 'rva'
#, 'ap'
#, '$texas'
#, 'corea'
#, 'a cuu long, f , tan binh, tp hcm'
#, ''
#, 'goettingen'
#, 'brasil sp'
#, 'reykjavík'
#, '四川 绵阳'
#, 'trichy'
#, 'world wide'
#, 'mrthe name'
#, 'yoshkar ola'
#, 'dorset'
#, 'limanowa/kraków'
#, 'viêt nam'
#, 'djursholm'
#, 'władysławowo'
#, 'x'
#, 'gasteiz, basque country'
#, 'the netherlands, europe'
#, 'algerie'
#, 'greater dfw'
#, 'en_us'
#, '衡阳'
#, 'queretaro'
#, 'virtual space'
#, 'utc'
#, 'altanta'
#, 'ustc'
#, 'vimim'
#, 'love field'
#, 'www bulk inc com'
#, 'hkd'
#, 'campo grande ms, brasil'
#, 'camaragibe'
#, 'anywhere'
#, 'kyev'
#, 'rondônia brasil'
#, 'fukushima koriyama'
#, 'yamaguchi'
#, 'markt berolzheim'
#, 'moose creek, on'
#, 'enfield, ns'
#, '日の本'
#, 'brasilia brasil'
#, 'chitrakoot'
#, 'vzla'
#, 'РФ, Владимир'
#, 'tunisie'
#, 'earth mostly'
#, 'wirral, england'
#, 'underground'
#, 'tucuman'
#, 'malaga'
#, 'if city'
#, 'hours from anywhere'
#, 'eastern united states'
#, 'são félix, bahia, brasil'
#, 'one the move'
#, 'the_darkside'
#, 'mines'
#, 'béziers'
#, 'wales, britain'
#, 'northamptonshire'
#, '神奈川県藤沢市'
#, 'beijinchaina'
#, 'Россия, Оренбург'
#, 'shang'
#, 'frankfurt/hanau'
#, 'Ústí nad labem'
#, 'pilani'
#, 'são carlos são paulo brasil'
#, 'shiga'
#, 'schauernheimerstr , d dannstadt schauernheim'
#, 'milky way, universe, expanding mass'
#, 'akb'
#, 'dehiwala'
#, 'dimap'
#, '济南'
#, 'middle england'
#, 'sask, can'
#, 'kashipur'
#, 'jhb'
#, 'zulte'
#, 'yew nork'
#, 'schipluiden'
#, 'behind your firewall'
#, 'mdn'
#, 'cancun, méxico'
#, 'maginus'
#, 'montélimar'
#, 'forest row, england'
#, 'dumfries'
#, 'sockerbruket , , gÖteborg'
#, 'east & west'
#, 'amherst, nova scotia'
#, 'Томия, Япония'
#, 'lalaland'
#, 'normandie'
#, 'creating your github account'
#, 'hinxton united kingdom'
#, 'teh internetz'
#, 'suwon, korea'
#, '中国黑龙江大庆'
#, 'targu mures, romainia'
#, 'chicagoland area'
#, '/c/emu/trinitycore/'
#, 'makeevka'
#, '地獄'
#, 'uzhgorod'
#, 'vinaros, españa'
#, 'beauharnois, qc'
#, 'russian,rh,sayanogrosk'
#, 'guidlford'
#, 'delluf'
#, 'espírito santo brasil'
#, '首都相模大野'
#, 'east midlands'
#, 'cgn'
#, 'são josé dos campos/sp'
#, '中国福建福州'
#, 'nyu'
#, 'yucatán'
#, 'cluj napoca, românia'
#, 'the great white north'
#, 'são paulo, sp brasil'
#, 'são josé'
#, 'stari zednik'
#, 'flanders'
#, 'dracena, são paulo, brasil'
#, 'city'
#, 'córdoba/veracruz méxico'
#, 'somewhere, over the rainbow'
#, 'avranches'
#, 'ponyland'
#, 'gotham'
#, 'berne'
#, 'trivandrum, kerala'
#, 'iamfredng@gmail com'
#, 'bra[sz]il'
#, 'sart lez spa'
#, 'sapporo, hokkaido'
#, 'mensk'
#, 'hammah'
#, 'lower haight'
#, 'são josé dos campos, sp'
#, 'vsetín'
#, 'uiwang, korea'
#, 'nyc/sf'
#, 'guaruja'
#, 'holland!'
#, 'liphook'
#, 'the united states'
#, 'hel'
#, 'irc freenode net #python veloutin'
#, 'caltech'
#, 'bruyères le châtel'
#, 'phily'
#, 'concórdia santa catarina'
#, 'glorious nippon'
#, 'earth, sol system'
#, 'osaka city'
#, 'undecided'
#, 'far, far away!'
#, 'africa'
#, 'méxico d,f'
#, 'skoczów'
#, 'blackstone, qld'
#, 'chong qing'
#, 'praha, Česká republika'
#, 'cozumel, méxico'
#, 'p s d r e r f'
#, 'tahiti, french polynedia'
#, 'czechrepublic/orlová lutyně'
#, 'traveling salesman'
#, 'kc'
#, 'glenavy'
#, '/users/fabi'
#, 'chambery'
#, 'niterói, rj'
#, 'french riviera'
#, 'mikew'
#, 'fedora'
#, 'shaanxi xi'an'
#, 'vitoria gasteiz'
#, 'trentino'
#, 'vodafone, internet'
#, 'tufts'
#, 'nyc / ber'
#, 'stavropol, russian federation'
#, 'camerino'
#, 'macae rj, brasil'
#, 'berchem'
#, 'cymru south wales uk, tywi valley'
#, 'rus'
#, ':'
#, 'shandong'
#, 'forlimpopoli'
#, 'berkshire'
#, 'kiyv'
#, 'czestochowa'
#, 'ruhrgebiet'
#, 'vidin;bulgaria'
#, 'laaaarndon'
#, 'Украина, Донецк'
#, 'grid'
#, 'villefranche sur saône'
#, 'rva + nyc'
#, 'uviéu asturies'
#, 'hồ chí minh city'
#, 'neotropic'
#, 'София, България'
#, 'improving izariam'
#, '法国，tours'
#, '中国湖北武汉'
#, 'sardinia'
#, 'the island'
#, 'massassachusetts'
#, 'guerrero, méxico'
#, 'norcal'
#, 'florianópolis brasil'
#, 'hangchow'
#, 'sab com'
#, 'goring on thames'
#, 'pgh'
#, 'the haque'
#, 'hopefully somewhere warm and sunny'
#, 'rossendale, lancashire'
#, 'earth planet'
#, 'western siberia'
#, 'bedfordshire'
#, 'cancun, qroo'
#, 'www tellago com'
#, 'malnova, latgola'
#, 'layer'
#, 'planet earth, with firmly both feet'
#, 'somewhere cloudy'
#, 'pondicherry'
#, 'türkiye'
#, 'bigbuzzylocation'
#, 'vagabonding'
#, 'czech rep'
#, '+ ° ' ", + ° ' "'
#, 'castlemaine, australila'
#, 'wordwide'
#, 'mid atlantic'
#, 'denver!'
#, 'jkl/fin'
#, 'chorzów'
#, 'hauj khas'
#, 'mozhajsk'
#, 'net'
#, 'moray'
#, 'florianopolis'
#, 'härnösand'
#, '次元'
#, 'doap com'
#, 'russian/tyumen'
#, '珠海'
#, 'bretagne'
#, 'dumbo'
#, '@fredrocious'
#, 'Великий Новгород'
#, 'demark'
#, 'opus'
#, 'burwood east'
#, 'brasília brasil'
#, 'www daum net'
#, 'classified'
#, 'genève'
#, 'alexanderie, Égypte'
#, '+ :'
#, 'yorkshire england'
#, 'weiqing building , thu'
#, 'venezia'
#, 'tacos'r'us'
#, 'gxnn'
#, 'são josé dos campos, brasil'
#, 'linodia'
#, 'jehay'
#, 'mikocheni'
#, 'twisted disneyland'
#, 'perros guirec'
#, 'apt'
#, 'jerez'
#, 'ilhéus bahia'
#, 'uk_uk, lviv'
#, 'northeast'
#, 'the planet'
#, 'greater philly area'
#, 'xanth'
#, 'earth!'
#, 'Кривой Рог'
#, 'iwate'
#, 'behind the phosphor'
#, 'dark alley'
#, 'katwijk zh'
#, 'kazaǹ'
#, 'são carlos sp'
#, 'easy'
#, '/root/'
#, 'veliko tarnovo'
#, 'the localhost'
#, 'xjf'
#, 'karlruhe'
#, 'goiânia go / brasil'
#, 'a happy place'
#, 'sankt peterburg'
#, 'everywhere yet nowhere'
#, 'uberlândia'
#, 'occupied palestinian territory'
#, 'lutsk'
#, 'west coast, the states'
#, 'calfornia'
#, 'Ísland'
#, 'naters'
#, 'little brington, england'
#, 'münchen/munich/mnichov/Мюнхен'
#, 'the 'ham'
#, 'test'
#, 'brignoud'
#, 'bitbucket'
#, 'a desert island'
#, 'bruxelles belgique'
#, 'bahia'
#, 'transcontinental'
#, 'rua turi'
#, 'higashi nihonbashi'
#, 'd f méxico'
#, 'lago di garda'
#, '天津市河东区'
#, 'raffles institution lane'
#, 'msp'
#, 'somewhere out there'
#, 'Томск, Россия'
#, '/dev/null;'
#, 'epicmorgia'
#, 'ub,mgl'
#, '@sfrdmn'
#, 'orhem'
#, '東京都渋谷区神宮前'
#, 'qz'
#, 'cancun'
#, 'nürtingen'
#, 'sebastopol'
#, 'boardtown , bitstreet'
#, 'earth?'
#, 'perm''
#, 'bnagalore'
#, 'germay'
#, 'goiania'
#, 'center valley'
#, 'moscow\'
#, 'allegheny college'
#, 'singaproe'
#, 'nagoya,aichi / mt関連の物など色々作っています。'
#, 'tarnowskie góry'
#, 'rover'
#, 'ici'
#, 'boulogne billancourt'
#, 'argyll, scotland'
#, 'uchicago'
#, '@home'
#, '_'
#, 'kalix'
#, 'Россия, Санкт Петербург'
#, 'park city'
#, 'utc+'
#, 'muree'
#, 'viña del mar'
#, 'queensland'
#, 'ldn — nyc'
#, 'marília/sp brasil'
#, 'inotherworld'
#, 'darlinghurst'
#, 'traveling the world'
#, 'phase space'
#, 'jaén'
#, 'しんじく'
#, 'grudziądz'
#, 'joão pessoa / pb / brasil'
#, 'aizu'
#, 'far far away land'
#, 'nazi moonbase on the moon'
#, '東京都世田谷区用賀'
#, 'catskills'
#, '경남 창원시 마산회원구'
#, 'republica dominicana'
#, 'eets'
#, 'mazangé'
#, 'wenen, oostenrijk'
#, 'cipherspace'
#, 'estudiante'
#, 'seilles'
#, 'korea, south'
#, 'nigeira'
#, '台灣（taiwan）'
#, 'chang sha'
#, 'virgo supercluster, milky way galaxy, sol system, earth'
#, 'jönköping'
#, 'pratteln, schweiz'
#, 'lanzarote, canary islands'
#, 'zanjan'
#, 'phila'
#, 'miensk litowski, biełaruthenia'
#, 'andheri'
#, 'cucuta'
#, '/home/dilibau/'
#, 'auvelais'
#, 'locating'
#, 'turin, italiy'
#, 'kanhangad'
#, 'roncade'
#, 'santo andré sp brasil'
#, 'java'
#, 'north wilkesboro'
#, 'catamarca'
#, 'marieville, qc'
#, 'bosnia & herzegovina'
#, 'kochi'
#, 'republica'
#, 'shropshire, england'
#, 'sillycone valley'
#, 'd'
#, 'here and there'
#, 'marília sp brasil'
#, 'timișoara'
#, 'rio das ostras'
#, '中国浙江杭州'
#, 'montes claros brasil'
#, 'jutphaas'
#, 'the wild, wild west'
#, 'the multiverse'
#, 'ailleurs'
#, 'here, ithink'
#, 'geek between the keyboard and the chair'
#, 'osaka shi osaka pref'
#, 'a coruña, galicia, españa'
#, '東京都'
#, 'kathmandy'
#, 'Йошкар Ола'
#, 'private'
#, 'somewhere over the rainbow'
#, 'kalymnos'
#, 'mogi das cruzes, sp'
#, 'dominican rapublic'
#, 'twin cities, minn'
#, 'outah space'
#, 'frankfurt / main'
#, 'comodo'
#, '<radar offline>'
#, 'manipal/bokaro'
#, 'funky town'
#, 'nimes'
#, 'missal'
#, 'cafelândia sp'
#, 'thessaloniki'
#, 'labège'
#, 'skyrim'
#, 'pitesti'
#, 'azeroth'
#, 'сеть'
#, 'i'm around'
#, 'brasília, df brasil'
#, 'miensk litowski, kryŭja'
#, 'merry ol' england'
#, 'brébeuf, qc'
#, 'ksa'
#, 'besançon / aix en provence'
#, 'leicestershire, england'
#, 'far east'
#, 'daiict,gandhinagar'
#, 'bègles'
#, 'on the planet'
#, 'hinterlands'
#, 'Украина, Винница; ukraine, vinnitsya'
#, 'ac'
#, 'transylvania'
#, 'bengaluru/marudhur'
#, 'vtech'
#, 'nyc, sf'
#, 'liestal, schweiz'
#, 'bmnville'
#, 'Россия, Екатеринбург'
#, 'universe'
#, 'whistler'
#, 'hampshire, united kingdon'
#, 'the hidden fortress'
#, 'luxmebourg'
#, 'wrocław, polska'
#, 'dogpatch'
#, 'gelderland'
#, 'emeryville'
#, 'https://gitorious org/~elf pavlik'
