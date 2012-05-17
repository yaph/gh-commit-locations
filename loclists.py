def check_unresolved(locstr):
    pass

fix_unresolved = {
    frozenset(['Paris']): 'France',
    frozenset(['London', 'England', 'Scotland', 'London, England', 'Cambridge', 'Manchester', 'Oxford', 'Bristol', 'Brighton', 'Oxfordshire, England', 'United Kingdon']): 'United Kingdom',
    frozenset(['New York', 'Nyc', 'Boston', 'California', 'Utah', 'Texas', 'Silicon Valley', 'New York, New York', 'Ohio', 'Indiana', 'Michigan', 'Massachusetts', 'Portland', 'Austin, Texas', 'Sf', 'Florida', 'Columbus, Ohio', 'Minnesota', 'Arizona', 'Kansas City', 'Cleveland, Ohio', 'Washington, D.C', 'Southern California', 'North Carolina', 'South Carolina', 'Wisconsin', 'Gainesville, Florida', 'Pennsylvania', 'Boston, Massachusetts', 'Northern California', 'Austin', 'Maryland', 'New England', 'Washington', 'Connecticut', 'Iowa', 'Kansas', 'Santa Barbara', 'Nebraska', 'Oklahoma', 'Hawaii', 'Washington D.C', 'Vermont', 'Maine', 'Cleveland', 'Sacramento', 'Madison, Wisconsin', 'Rochester, New York']), 'United States',
    frozenset(['Moscow', 'Kyiv', 'Russian Federation', 'Kazan', 'Moscow, Russian Federation']): 'Russia',
    frozenset(['Sydney', 'Melbourne', 'Melbourne, Victoria']): 'Australia',
    frozenset(['Amsterdam']): 'Netherlands',
    frozenset(['Montreal', 'Vancouver, Bc', 'Vancouver', 'Montreal, Qc', 'Victoria, Bc', 'Ottawa, On', 'Waterloo, On', 'MontréAl', 'Ottawa', 'Vancouver Bc', 'QuéBec', 'Quebec']): 'Canada',
    frozenset(['Madrid', 'Barcelona', 'Madrid (Spain)', 'Barcelona (Spain)', 'Sevilla']): 'Spain',
    frozenset(['Korea']): 'South Korea',
    frozenset(['Istanbul']): 'Turkey',
    frozenset(['Munich', 'Cologne', 'DüSseldorf', 'MüNchen']): 'Germany',
    frozenset(['Vienna']): 'Austria',
    frozenset(['Brasil', 'SãO Paulo', 'SãO Paulo, Brasil', 'SãO Paulo - Brasil', 'Sao Paulo', 'SãO Paulo - Sp', 'SãO Paulo / Brasil', 'SãO Paulo, Sp']): 'Brazil',
    frozenset(['Dublin']): 'Ireland',
    frozenset(['Hyderabad', 'Kharagpur']): 'India',
    frozenset(['Zurich', 'ZüRich']): 'Swizerland',
    frozenset(['MéXico']): 'Mexico',
    frozenset(['Yokohama', 'Osaka']): 'Japan',
    frozenset(['GöTeborg', 'LinköPing', 'Gothenburg']): 'Sweden',
    frozenset(['KrakóW', 'WrocłAw', 'Cracow']): 'Poland',
    frozenset(['Rome', 'Milano']): 'Italy',
    frozenset(["Xi'An"]): 'China',
    frozenset(['Viet Nam']): 'Vietnam'
}

#Rotterdam	9
#Tehran	9
#Chiba	9
#Kanagawa	9
#Birmingham	9
#Tennessee	9
#Turin	9
#The Internet	9
#Sapporo	9
#SãO Paulo, Sp, Brasil	9
#İStanbul	8
#Bengaluru	8
#Bloomington, Indiana	8
#Montreal, Quebec	8
#Alabama	8
#Athens	8
#Zaragoza	8
#Wales	8
#Halifax, Ns	8
#Perth	8
#Lansing, Michigan	8
#Nagoya	8
#Kharkov	8
#Santa Cruz	8
#Kent, Ohio	8
#Russian Federation, Moscow	8
#Paris (France)	8
#Coventry	8
#NüRnberg	8
#Patagonya	8
#Stanford	8
#KöLn	8
#MüNster	8
#Kerala	8
#Buffalo	8
#Catalonia	8
#Campinas	8
#Manchester, England	8
#Wellington	8
#Chicagoland	8
#Victoria	8
#Ha Noi	7
#Bavaria	7
#Antwerp	7
#Cape May Court House	7
#Colima, MéXico	7
#Missouri	7
#Italia	7
#Europe->Poland->Gorzow	7
#Cambridge, England	7
#Granada	7
#Barcelona, Catalunya	7
#Ahmedabad	7
#Lima, Perú	7
#Aberdeen, Scotland	7
#Quebec City	7
#MontréAl, QuéBec	7
#Kent	7
#Aix En Provence	7
#Varanasi	7
#Valencia	7
#New Hampshire	7

#Kolkata	7
#Arkansas	7
#Moon	7
#London | KrakóW	7
#Illinois	7
#Orange County, California	7
#Ekaterinburg	7
#Kentucky	7
#Redmond	7
#Boulder	7
#Vancouver, British Columbia	7
#The Internets	7
#MéXico City	7
#Oxford, England	7
#Localhost	7
#Philly	7
#Deutschland	6
#Suwon	6
#TüBingen	6
#Birmingham, England	6
#Upstate New York	6
#World Wide Web	6
#Warszawa	6
#Shanghai.China	6
#Newcastle Upon Tyne	6
#Reading, England	6
#FlorianóPolis	6
#Hangzhou.China	6
#Madrid, EspañA	6
#Eldridge, Alabama	6
#Bogota	6
#The Cloud	6
#Lima - Perú	6
#Flanders, Eu	6
#Russian	6
#Reading	6
#☠☠☠ Nyc ☠☠☠	6
#Odessa	6
#Lille	6
#Sao Paulo, Brasil	6
#KøBenhavn	6
#Socal	6
#Washington State	6
#Hackity-Hack	6
#Colima	6
#Bristol, England	6
#Bruxelles	6
#Bucuresti	6
#York	6
#Rj	6
#Vancouver, B.C	6
#Santa Barbara, California	6
#Moskow	6
#Canary Islands	6
#The New York Metropolitan Area	6
#Stony Brook, New York	6
#Home	5
#Manipal	5
#Irvine	5
#U.K	5
#Aarhus	5
#Santo Domingo	5
#GdańSk	5
#Nizhny Novgorod	5
#Nomadic	5
#Lisboa	5
#Santiago	5
#Heidelberg	5
#Shang Hai	5
#Hz	5
#Madison	5
#Shenzhen.China	5
#Broughty Ferry, Scotland	5
#Uiuc	5
#Ha Noi, Viet Nam	5
#Hamilton, On	5
#Turkiye	5
#Dundee	5
#Louisiana	5
#Eskisehir	5
#Earth, Solar System	5
#Hradec KráLové	5
#广州	5
#/Dev/Null	5
#Seville	5
#Hollywood	5
#Galactic Sector Zz9 Plural Z Alpha	5
#Portsmouth	5
#Snowdonia, North Wales	5
#Tyumen	5
#Ciracas	5
#Bluffton, Ohio	5
#Swansea	5
#West Coast	5
#Over There	5
#Ghent	5
#Alaska	5
#Louisville, Kentucky	5
#萧山	5
#Someplace Near You	5
#Campinas, Brasil	5
#Irvine, California	5
#Latvija, RīGa	5
#Banglore	5
#Ulyanovsk	5
#Earth:Usa:Florida:Tampa:33624	5
#Norwich	5
#Milky Way	5
#Fukuoka	5
#South Florida	5
#Portland, Maine	5
#Western Hemisphere	5
#Rhode Island	5
#MöNchengladbach	5
#Grimes, Iowa	5
#Usofa	5
#CóRdoba	5
#America	5
#A CoruñA	5
#Scl	5
#Wilmington, North Carolina	5
#Charleston, South Carolina	5
#Yokohma	5
#Lincoln	5
#Lima	5
#Pluto	5
#Hanoi	5
#Silicon Valley, California	5
#--> (X) <--	5
#Belmont, Calfornia	5
#MéXico Df	5
#MontréAl, Qc	5
#Playa Del Rey, California	5
#Moskau	5
#Москва	5
#Iit Kharagpur	5
#Fremont, California	5
#Mtl	4
#Cherkassy	4
#Liverpool	4
#D.C	4
#Bei Jing	4
#Austin/Boulder	4
#97203	4
#大连	4
#Meridian, Idaho	4
#Sao Paulo / Brasil	4
#Desconocida	4
#U.S	4
#L3	4
#Saint Petersburg, Florida	4
#MáLaga	4
#The Yay	4
#LidköPing	4
#BrasíLia	4
#Burbank, California	4
#-	4
#Chiavenna, Lombardia, Italia	4
#Waterloo / On	4
#Granada (Spain)	4
#Evry	4
#Http://Git.Io/Djb	4
#SãO Paulo - Sp, Brasil	4
#Odessa, Ukrain	4
#Praha	4
#Traverse City, Michigan	4
#Peking	4
#Vilafranca Del PenedèS. Barcelona	4
#Ah.... Who Knows	4
#GöTtingen	4
#Platteville, Wisconsin	4
#Fennectar, Fennectus State, Planet Cyrusian	4
#Middle Earth	4
#Syracuse	4
#Columbia, Missouri	4
#ŁóDź	4
#North America	4
#Remote Developer	4
#Poznan	4
#Chicagoland+Wi	4
#Brest	4
#Kapolei, Hawaii	4
#New York/Connecticut	4
#Santa Clara, California	4
#台灣(Taiwan)	4
#MáLaga (Spain)	4
#Chisinau	4
#Pacific Northwest	4
#Kansas City, Missouri	4
#Ft. Lauderdale, Florida	4
#ChambéRy	4
#Perm	4
#Saint-Petersburg, Russian Federation	4
#JoãO Pessoa	4
#Sevilla, EspañA	4
#Hellsinki / Funland	4
#Campinas, Sp	4
#31.593469,120.772855	4
#Midwest	4
#Gansu	4
#Tver	4
#Greater Boston Area	4
#Newcastle	4
#Barcelona, Catalonia	4
#Murcia	4
#Great Britain	4
#Cyberspace	4
#Downriver, Michigan	4
#Aix-En-Provence	4
#Sophia Antipolis	4
#Plymouth	4
#中国	4
#Ranchi	4
#Greater Boston	4
#JyväSkylä	4
#Shizuoka	4
#LièGe	4
#Columbus	4
#JoãO Pessoa, ParaíBa	4
#フランス	4
#Wien	4
#Ucla	4
#Mainly Europe	4
#Blagoveschensk, Amur Region, Russian Federation	4
#Somerset / London	4
#Guadalajara, Jalisco, MéXico	4
#LüBeck	4
#Erewhon	4
#Muc	4
#Leidschendam	4
#Karkala	4
#34 S, 138 E	4
#Victoria Bc	4
#74	4
#Llanfrothen, North Wales	4
#Atx	4
#Icbm: 38° 35' 27'' N, 89° 59' 38'' W	4
#Squamish, Bc	4
#Bundeshauptstadt	4
#Sacramento, California	4
#Iasi	4
#Dunedin	4
#ViệT Nam	4
#Unfashionable End, Western Spiral Arm, Milky Way	4
#$Home	4
#SàI GòN	4
#Envigado! :)	4
#Florence	4
#Burlington, Vermont	4
#International	4
#Brxx0043	4
#Swizerland	4
#Http://Gitorious.Org/Tlevine/	4
#Vinnitsa	4
#Halifax	4
#Ekb	4
#Gangsta'S Paradise	4
#Gandhinagar	4
#North Wales	4
#Brighton, England	4
#Florianopolis, Brasil	4
#Oxfordshire	4
#Remote	4
#家	4
#Sdut	4
#Sevastopol	4
#Moscow, New-Peredelkino	4
#Ahoka@Rizon	4
#Guadalajara, Jalisco	4
#The North East	4
#Various	4
#Mid-Earth	4
#Krakow	4
#Santa Clara	4
#Portland, Ore	4
#Valencia (Spain)	4
#I Came. I Saw. I Refactored	4
#İStanbul, TüRkiye	4
#Lviv	4
#Ukrain	4
#Lsju	4
#Colombo	4
#Sf Baby!	4
#Orange County	4
#Xidian	4
#Durham	4
#Jacksonville, Florida	4
#Den Haag (Nl)	4
#Cardrona	4
#Hang Zhou	4
#*	4
#Dnepropetrovsk	4
#The Hague	4
#Donostia	4
#Somewhere Between Here And There	3
#ÅRhus	3
#On The Run	3
#Troon, Scotland	3
#Zh	3
#Here, Now	3
#Heidelberg, Baden-WüRtemburg, Deutschland	3
#Vilafranca Del PenedèS, Catalunya	3
#Stl	3
#Murray, Utah	3
#Rottedam	3
#Sai Gon	3
#192.168.1.1	3
#Japanese	3
#Trinidad & Tobago	3
#06103	3
#Zhodino	3
#OrléAns	3
#Inland Norcal	3
#Fresno, California	3
#East Coast	3
#Wainiha, Hawaii	3
#SuwałKi	3
#Narnia	3
#SãO Paulo / Sp	3
#Slovenija	3
#Trinidad	3
#Pasadena, California	3
#Chelsea, Michigan	3
#/Home/Emineker	3
#Stony Brook	3
#Beijingchina	3
#Nova Scotia	3
#XàTiva	3
#Kasaragod	3
#MüNster, Deustchland	3
#Pek	3
#Whitby, On	3
#Tunbridge Wells	3
#SãO Paulo/Sp	3
#Kingston, New York	3
#Rj, Brasil	3
#Troy, New York	3
#Schweiz	3
#Left-Handed Coordinate	3
#Right Here	3
#Parma	3
#45.391921,-122.567767	3
#Dfw, Texas	3
#Fresno	3
#Plain Dealing, Louisiana	3
#GoiâNia - Go	3
#Beyond Your Wildest Dreams	3
#Colbert Nation	3
#Colima, Colima (MéXico)	3
#Moscow, Rissia	3
#London | Reading	3
#BeléM/Pa (Brasil)	3
#Essen	3
#Odessa, Ukrane	3
#Waterloo On	3
#Firenze	3
#Interwebs	3
#Interwebz	3
#Beijng	3
#Reykjavik	3
#Czech	3
#Londinium	3
#Korat	3
#Waterloo, Ont	3
#London, U.K	3
#Hanoi, Viet Nam	3
#Sevilla-Madrid	3
#Kerala.India	3
#Polska	3
#~	3
#Hà NộI, ViệT Nam	3
#Laaaaandon	3
#5Th Floor	3
#LeganéS	3
#The Interwebs	3
#GoiâNia, GoiáS, Brasil	3
#London, On	3
#Ufsc	3
#Trento	3
#GijóN	3
#風見学園	3
#94123	3
#Xi'An, Shaanxi	3
#Mississippi	3
#70115	3
#Norwich, England	3
#NiteróI/Rj	3
#Arlington, Texas	3
#South Dakota	3
#Uc Santa Barbara	3
#Ucsc	3
#Spain!	3
#L.A	3
#Saint Louis Missouri	3
#Phl	3
#Emerald Hills, California	3
#Teh Intertubes!!!1!	3
#ベルリン	3
#ZüRich / Melbourne	3
#Montabaur	3
#Sonoma County, California	3
#Nomad	3
#Meyrargues	3
#Campinas - Sp	3
#Homalg Project	3
#Минск	3
#Venice	3
#Saxony_Germany	3
#Bcn	3
#Anywhere	3
#Bronx, New York	3
#MéXico, D.F	3
#Jackson, Mississippi	3
#Milano, Italia	3
#Irc.Datnode.Net	3
#Luxemburg	3
#EspañA	3
#Valladolid	3
#Pakkret, Nonthaburi	3
#Paudex	3
#PréVost	3
#Brasil, BrasíLia	3
#Korolev, Moscow, Russian Federation	3
#Lancaster	3
#/Home/Askn	3
#Lax	3
#Perú	3
#Dollar, Clackmannanshire	3
#Toledo, Ohio	3
#200 Varick Street	3
#East Village, New York	3
#World Citizen	3
#Macau	3
#Oceanside, California	3
#BrasíLia, Df, Brasil	3
#Avesnes Sur Helpe	3
#Canton	3
#Санкт-Петербург, Россия	3
#South Wales	3
#BahíA Blanca	3
#BesançOn	3
#Россия	3
#RzeszóW/KrakóW	3
#GoiâNia, Brasil	3
#Oisy Le Verger	3
#GoiâNia	3
#Victoria B.C	3
#SaarbrüCken	3
#'Merica	3
#Moor Row, Cumbria	3
#Worcestershire, England	3
#Eastern Seaboard	3
#The Czech Republic	3
#Campinas, SãO Paulo, Brasil	3
#Gensokyo	3
#The Pleiades	3
#Skagit County	3
#Bhubaneswar	3
#Atl	3
#Kyiv, Ukrane	3
#Fayetteville, Arkansas	3
#Minnesotta	3
#Ja	3
#Sbo / Campinas - Sp/Brasil	3
#/Home	3
#SüDwestdeutschland	3
#RéUnion	3
#福建厦门	3
#/Dev/Random	3
#Guadalajara, MéXico	3
#Asuncion	3
#The Unknown	3
#Los Angeles Area	3
#Kobe	3
#SãO Paulo - Sp - Brasil	3
#MéXico, MéRida	3
#10009	3
#Garia, West Bengal, Kolkata	3
#Mdle Hell	3
#The Mountains	3
#Western Massachusetts	3
#浙江，杭州	3
#RomâNia	3
#48° 46′ 42.96″ N, 2° 17′ 26.16″ E	3
#Espirito Santo, Brasil	3
#Manhattan, New York	3
#Greater New York City Area	3
#Wasatch Front, Utah	3
#Arkhangelsk	3
#Bedroom	3
#Andreazevedo	3
#Salto	3
#Hampshire	3
#Manhattan	3
#Dolores Park	3
#Grand Rapids Michigan	3
#Rochester N.Y	3
#Cloud	3
#Oaxaca, MéXico	3
#60601	3
#Rychnov Nad Kneznou / Praha	3
#Rendsburg@Germany	3
#Europe, Earth, The Universe	3
#Almere	3
#Sussex, England	3
#Mozzanella	3
#West London	3
#Winchester	3
#Oceanside	3
#London/Reading	3
#Brasilia	3
#Null	3
#Le Bourget Du Lac	3
#Pnw	3
#22302	3
#Ryazan	3
#Neuchatel	3
#Potrero, Sf	3
#Boston Massachusetts	3
#Wakayama Pref	3
#Albany, New York	3
#Tamara (Ferrara), Italia	3
#Barcelona, EspañA	3
#Paris (Fr)	3
#Lawrence, Kansas	3
#Auburn, Alabama	3
#Sydney, Nsw	3
#Wellington New Zealand	3
#Beijing.China	3
#Bonnie Scotland	3
#Uddel	3
#Alresford	3
#Suzhou Jiangsu	3
#Iss, Leo	3
#Ann Arbor And Austin	3
#Rochester	3
#Singularity	3
#Ely(Cambridge), London & Trains Between Them	3
#WüRzburg	3
#Alnilam	3
#Lille (France)	3
#Saint Petersburg, Russian Federation	3
#Spaceship Earth	3
#Yaroslavl	3
#Richmond, Bc	3
#Likely Indoors	3
#ValparaíSo, SãO Paulo, Brasil	3
#Россия, Москва	3
#Ft. Worth, Texas	3
#Http://Labs.Scaltinof.Net/Supabakka	3
#N43, W86	3
#Underground	3
#CầN Thơ	3
#Zz9 Plural Z Alpha	3
#Lexington, Kentucky	3
#Guadalajara	3
#Xda-Developers	3
#World Wide	3
#Ciudad JuáRez, MéXico	3
#City 17	2
#Jo'Burg	2
#Nizhny Novgorod, Russian Federation	2
#Http://Www.Gravatar.Com/Avatar/Ac315Cd6B30Acecfe321184D5De7650A?S=80	2
#Colima,Colima	2
#Europe/Paris	2
#Way Up North, Scotland	2
#Gz	2
#Hamilton	2
#Fotaleza	2
#Georgetown, Texas	2
#Ciudad Juarez	2
#Brussel	2
#Wonderland	2
#StäFa	2
#Bj.China	2
#Dfw	2
#Chicoutimi, QuéBec	2
#中国深圳	2
#North East, England	2
#Traveling	2
#Neither Here Not There	2
#Finalnd	2
#Http://Twimpact.Com/	2
#福井	2
#Alsace	2
#Earth, Sol, Western Spiral Arm, Milky Way, Omniverse	2
#27614	2
#Secret Volcano Lair	2
#Perth, Scotland	2
#Rajshahi	2
#Kotamobagu	2
#Nagpur	2
#Anglesey, North Wales	2
#South-Africa	2
#Eastern U.S.A	2
#Where You Live	2
#Kanazawa, Ishikawa	2
#Durgapur	2
#Stary Oskol	2
#Canterlot	2
#Kreuzberg	2
#Black Books	2
#SãO José Dos Campos, SãO Paulo, Brasil	2
#West Michigan	2
#Frankfurt	2
#Saint Nazaire	2
#Valles Marineris, Mars	2
#The Great White North	2
#Bhimavaram	2
#Scotts Valley, California	2
#Clayton, On	2
#Stavropol	2
#Bruges	2
#Сибирь, Кузбасс	2
#Anyang	2
#TubarãO/Sc, Brasil	2
#Cern	2
#Fontana, California	2
#Canton, Ohio	2
#Wroclaw	2
#Ja_Jp	2
#Llanarmon Dyffryn Ceiriog	2
#York, England	2
#Tel-Aviv	2
#$Texas	2
#OrduñA, Bizkaia	2
#Lockport, New York	2
#Gambier, Ohio	2
#Rio Piedras	2
#Joao Pessoa, Pb - Brasil	2
#Whatloo	2
#中国山东省青岛市	2
#Sector 8, Reality Sigma, Cow	2
##Jbpm On Irc.Codehaus.Org	2
#Saginaw, Michigan	2
#Columbus Ohio	2
#Rit	2
#Rio	2
#Northern England	2
#Oporto	2
#Dover, Ohio	2
#合肥,安徽	2
#TrêS Rios - Rj	2
#Moscow, Idaho	2
#44Th District, California	2
#Bronx	2
#South Carolina, U.S.A	2
#Earth, Sol	2
#Ldn	2
#Somewhere Random On Planet Earth	2
#Aberdeen	2
#Takoyaki	2
#Where Pigs Fly	2
#California, U.S	2
#Las Angeles, California	2
#Симферополь	2
#Worcester	2
#Buffalo, New York	2
#Northeast Ohio	2
#/Dev/Console	2
#Dniepropetrovsk	2
#Scenic Hinxton	2
#Wiltshire, England	2
#РФ, г. Екатеринбург	2
#Tiohtiake	2
#Root	2
#Sachsen	2
#Clifton, South Carolina	2
#BeléM	2
#The Universe	2
#Connecticut/New York - Rit	2
#Piera	2
#ItäMerenkatu 13	2
#Moraine, Ohio	2
#Cluj Napoca	2
#Uestc	2
#Wollishofen, ZüRich	2
#Floduh	2
#Palmas, Tocantins, Brasil	2
#Sea / Sfo / Nyc / Bos	2
#/Home/Wintervenom	2
#Http://Toolchain.Eu	2
#Corea	2
#RibeirãO Preto - Sp	2
#United States (Est)	2
#Sydney, Aus	2
#Chengdu.Sichuan.China	2
#Nyc/Sf	2
#Trichy	2
#Usc	2
#中国辽宁沈阳	2
#Saint-Petes	2
#Korean	2
#S. Florida	2
#Burlington Vermont	2
#Nagano	2
#Mitchellville, Iowa	2
#Fukushima Koriyama	2
#Kansas! City!	2
#RondôNia - Brasil	2
#Bahia Blanca	2
#Ugvydggsief1C3Ryywxpyq==	2
#Woclaw	2
#Yorkshire, England	2
#中国西安	2
#Pilani	2
#Berne	2
#Devon/Bournemouth (Home/Uni)	2
#Boulogne	2
#Coffee Bean & Tea Leaf	2
#Newcastle-Upon-Tyne, England	2
#North East England	2
#Idf	2
#DąBrowa GóRnicza, Polska	2
#Moscow, Rf	2
#Location Independent	2
#Softslayer	2
#Oxford - St.Petersburg	2
#Halifax, Nova Scotia	2
#SãO Paulo - Sp / Brasil	2
#Gotham	2
#Reggio Emilia	2
#首都相模大野	2
#Spb.Ru	2
#Leningrad	2
#Malaga	2
#бобруйск	2
#Hell On Earth	2
#Mission District	2
#Sydney,Nsw	2
#Northwest	2
#Montgomery, Texas	2
#Lazistan	2
#Syracuse, New York	2
#Sjamgjao	2
#Diss, Norfolk	2
#Http://Github.Com/Wewetom/Jsutil	2
#Mensk	2
#Breizh	2
#Undisclosed	2
#Ivry Sur Seine (France)	2
#Earht Planet	2
#Kingwood	2
#Www.Fraudpointer.Com	2
#Rupnagar	2
#Www.Emlprime.Com	2
#Lexexa, Kansas	2
#Beijing&Chengdu	2
#CuliacáN, Sinaloa, MéXico	2
#Manhattan, Kansas	2
#'The' Earth	2
#Mit	2
#Loltah	2
#Sfo	2
#Kagurazaka	2
#Yay Area	2
#Sausalito	2
#Vienna, Aut	2
#Dublin ⇄ London	2
#SãO Paulo-Sp (Brasil)	2
#中国，杭州	2
#Ururu	2
#Peterborough	2
#Upton	2
#Haboobland	2
#Aichi	2
#94110	2
#Planet Pumpkin	2
#Klagenfurt	2
#Alfaro City	2
#Wellington; New Zealand	2
#Utc+2/Utc+1 (Berlin Timezone)	2
#Colima, Col	2
#NøRrebrogade 34-36, ÅRhus	2
#İStanbul/KadıKöY	2
#Iitm	2
#That Place Between Dreaming And Awake	2
#Colima, Colima	2
#Pego (P.P.C.C)	2
#IruñEa Nafarroa	2
#Danmark	2
#Celestial Empire	2
#Ville D'Emery	2
#Aubergenville	2
#Heavenly Dynasty（和谐的天朝）	2
#Oaxaca	2
#Montreal Qc	2
#Miyagi	2
#Brasilia - Df, Brasil	2
#中国南昌	2
#Alexandria, Alabama	2
#Timisoara	2
#Bruxelles (Belgium) And Lille (France)	2
#Rpi	2
#Sart Lez Spa	2
#Saigon	2
#London England	2
#Trivandrum, Kerala	2
#Hinxton, Cambridge	2
#Idaho	2
#Windermere, Florida	2
#/Pub	2
#207	2
#Somewhere Else	2
#Didu	2
#New New York	2
#Rueti Zh	2
#92129 Macs Ln	2
#Stratford-Upon-Avon	2
#Boston, Mass	2
#Bluelovers	2
#A Few Places	2
#Nova Kahovka	2
#Brownsville, Texas	2
#天津市南开区华苑产业园区	2
#Kosice	2
#MéRida,YucatáN,MéXico	2
#Paia, Hawaii	2
#Berkshire, England	2
#Montreal (Canada)	2
#Villeneuve D'Ascq	2
#Akihabara	2
#Deajeon	2
#Victoria, B.C	2
#BanˈDuŋ ˌɪNdoʊˈNiːZiə	2
#Krk	2
#Brasov	2
#Russian, Ryazan	2
#Ottawa On	2
#1720	2
#Tejas	2
#Peachtree Corners	2
#PéRuwelz (Belgium)	2
#Kharkov (Ukraine)	2
#Sverige	2
#Soerabaja, East Java	2
#Sp - Brasil	2
#Beijinchaina	2
#Iamfredng@Gmail.Com	2
#Http://Cyberbusking.Net/	2
#Paris (Gmt +1)	2
#Lostwithiel	2
#British Columbia	2
#SãO Paulo/Sp Brasil	2
#Northwest Ohio	2
#Nullptr	2
#Groenlo	2
#Екатеринбург	2
#Nor Cal	2
#Wild Wild Web	2
#Block Island	2
#Nit Kozhikode, Kerala	2
#İZmir	2
#Here :D	2
#Unlv	2
#Trivandrum	2
#Munich (Germany)	2
#Hackney, London	2
#Peterborough, England	2
#Долгопрудный	2
#Казань	2
#CáDiz(Spain)	2
#Midland, Texas	2
#Biggest Little City	2
#New York City!	2
#Maryland'S Eastern Shore	2
#On A Boat	2
#Rus, Spb	2
#Jorvas	2
#FüRth	2
#Campinas -Sp	2
#Manningtree, England	2
#Jp.Kanawaga.Zama	2
#Yokohama City	2
#Bolzano, SüDtirol	2
#FlekkerøY	2
#ElbląG	2
#Typically The Office	2
#Cascadia	2
#嘉義	2
#New York, New York, New York	2
#@Denmark	2
#Space	2
#@Edebill	2
#A CoruñA (Spain)	2
#江苏苏州	2
#Auvergne	2
#Topanga, California	2
#South Weber, Utah	2
#Vienna - Aut	2
#--	2
#Ifoc	2
#Uae	2
#JoãO Pessoa - Pb	2
#千葉県千葉市(Chiba, Japan)	2
#Schwyz	2
#Europe.Ukraine.Sumy	2
#Cracov	2
#Somewhere Dark And Creepy	2
#Maine/D.C	2
#Lancashire, England	2
#On The Intraweb	2
#Very Small Small Town	2
#Kazakstan, Karaganda	2
#Belgique	2
#Changes A Lot	2
#TüRkiye,İStanbul	2
#Langhorne, Pennsylvania	2
#+-20Km LitoměřIce@Czechrepublic.Europe	2
#Triniad And Tobago	2
#Greater New York City Area (Fairfield County, Ct)	2
#The Intergalactic Interwebs	2
#Twitter.Com/Leemallabone	2
#The Nether	2
#HyèRes Les Palmiers	2
#İStanbul / TüRkiye	2
#SãO Carlos	2
#Pune(India)	2
#The Big Blue Ocean (Us Navy On Deployment)	2
#MéRida	2
#Kanpur	2
#AlmeríA (Spain)	2
#秦皇岛	2
#Ain Taya	2
#Louisianna	2
#Cheonan, Korea	2
#Bowling Green, Ohio	2
#OsnabrüCk	2
#Bangor, Maine	2
#Oaklandia	2
#Birmingham, Alabama	2
#Starvropol', Russian Federation	2
#16802	2
#Italia, Milano	2
#Irc://Irc.Datnode.Net:6667/#Hacking	2
#Kingston Rhode Island	2
#SãO Carlos/Sp	2
#Cambridge (Uk)	2
#Norfolk, England	2
#Western Pennsylvania	2
#LåNgshyttan	2
#10010	2
#Lancashire	2
#MéXico D.F	2
#Cluj	2
#32.251225,-111.017906	2
#The Netherlands, Near Amsterdam	2
#Le Kremlin-BicêTre	2
#Sthlm	2
#Sydneylondon	2
#"China Wuan"	2
#Bedum	2
#Gothenburg(Sweden)	2
#On The Interwebz	2
#Yoyogi	2
#Ussel	2
#Kakinada	2
#Apeiron	2
#在地球上	2
#WrocłAw (Poland)	2
#Batam	2
#Aurora, Illinois	2
#Shoreditch, London	2
#Kennington, London	2
#21042	2
#Laurel, Maryland	2
#MéXico, Df	2
#Vitebsk	2
#NorrköPing	2
#Pici	2
#Jazzgumpy	2
#Www	2
#Http://Www.Kylemulka.Com	2
#Lasalle, Quebec	2
#Banagalore	2
#Dundee, Scotland	2
#Itlay	2
#Hokkaido	2
#Acapulco Guerrero	2
#Neo-Sitama	2
#Teh Interwebs	2
#Newyork	2
#Itay	2
#U.S.A	2
#Bielsko-BiałA	2
#Http://Maps.Google.Co.Jp/Maps?F=Q&Source=S_Q&Hl=Ja&Geocode=&Q=%E8%88%B9%E6%A9%8B%E5%B8%82%E5%B1%B1%E6%89%8B1-1-3&Sll=35.681382,139.766084&Sspn=0.013752,0.021865&Brcurrent=3,0X601880F51Ff19F8B:0X8Fcd67F74Df26297,0,0X6018808A850A7131:0X19938147D2910912&Ie=U	2
#中国天津	2
#Durham, North Carolina	2
#Izmir	2
#Pepperland	2
#Blowmage	2
#Utc -0500	2
#Bolzano	2
#Tc_Hydro	2
#Alexandria	2
#Santa Barbara, Ca/ Southlake, Texas	2
#South England	2
#中国-浙江-衢州	2
#Jhb (Za)	2
#Prag	2
#Http://Webchat.Freenode.Net/?Channels=#Unhosted	2
#Norcal	2
#Medellin	2
#Mpls	2
#Oviedo	2
#CompièGne	2
#100' Above Ground Floating On A Balloon	2
#Nikolaev	2
#Kent, England	2
#Cebu	2
#Россия, Казань	2
#Planet Earth, Mostly	2
#Lincolnshire, England	2
#BucureșTi, RomâNia	2
#St.Petesburg	2
#Osaka,Kobe	2
#Sulthan Bathery	2
#Pacific Palisades	2
#/Bin	2
#Bonsall, Derbyshire	2
#Mass, U.S	2
#@Non_117	2
#Parts Unknown	2
#Conifer	2
#Derby	2
#Western Europe	2
#Libertatia	2
#Philly Burbs	2
#Tunisie	2
#Uzb	2
#California (Us) / Sydney (Au)	2
#Cmpt 470	2
#Granada - Madrid	2
#Hinxton	2
#Vilafranca Del PenedèS	2
#19.341435, -99.165237	2
#Nanking	2
#Burgum	2
#Минеральные Воды	2
#MüNster, Deutschland	2
#Chesterfield	2
#Santa ÚRsula	2
#上海,中国	2
#Kratumban, Samutsakorn	2
#Wtf Prc	2
#中国福建福州	2
#Souther California	2
#Moscow.Russia	2
#SãO Paulo/Brasil	2
#Amsterdam(Nl)/Auxerre(Fr)	2
#Shuswap, Bc	2
#Chinese	2
#SãO Carlos - SãO Paulo - Brasil	2
#PetróPolis, Rj	2
#Http://Www.Youtube.Com/Watch?V=Gawixbt599E	2
#SãO Paulo/Sp - Brasil	2
#MáLaga, EspañA	2
#Soho, London	2
#Galway	2
#Suburbia	2
#The Island	2
#Snoqualmie Washington	2
#Punjab (India)	2
#Nevada	2
#The Semantic Web	2
#Niteroi - Rj	2
#Nwa	2
#Yayyyy	2
#57° 42' 49 N, 11° 59' 53	2
#55409	2
#Big O	2
#14, James Robertson Street, Surulere, Lagos	2
#Gothenburg(Swedgen)	2
#Brooklyn!	2
#Hongkong	2
#Earth-616	2
#Swedish Igloo	2
#Warwick	2
#Oau, Ile Ife	2
#Whu	2
#Boston, Massachusetts, U.S	2
#/Dev/Hell	2
#Украина, Запорожье	2
#Lima :)	2
#Kongens Lyngby	2
#Southeastern Washington State	2
#Franklin, Wisconsin	2
#Winchester, Hampshire	2
#Fuzhou.China	2
#/Users/Rzm102	2
#Tasmania	2
#Hell	2
#Beijing，China	2
#Uhh, I'M Here, I Think	2
#Jamespic.Info	2
#Ku	2
#Montreal,Qc	2
#11231	2
#Santo Andre - Sp - Brasil	2
#Right Here!	2
#Sysu	2
#Prueba	2
#Vernon, Bc	2
#Salamanca, Madrid, Seville (Spain)	2
#Suzhou	2
#Dell Inc	2
#Hamburg(Germany)	2
#415, 516	2
#Osaka && Munich	2
#Reggio Emilia,Italia	2
#Alwernia	2
#CúCuta	2
#Vellerat	2
#Chn	2
#Oviedo/GijóN	2
#Monterrey.Mx	2
#Kumamoto	2
#Goettingen	2
#Centerville, Utah	2
#Linden	2
#Cologne (Ger)	2
#Middle Tennessee	2
#Beaujolais (France)	2
#Liverpool, England	2
#The D	2
#KrakóW / Jaworznia	2
#S	2
#Northeastern United States	2
#Livermore, California	2
#BrasíLia/Df, Brasil	2
#Hi.Baidu.Com/Quqiufeng	2
#Washington-Lee High School	2
#Victoria, British Columbia	2
#Villefranche-Sur-SaôNe	2
#North Dakota	2
#Moose Creek, On	2
#Xi'An,Shaanxi,P.R.C	2
#Isny	2
#BrasíLia, Brasil	2
#Brasil, SãO Paulo - Sp	2
#SãO José Dos Campos/Sp - Brasil	2
#Brasil, Rj	2
#東京都杉並区	2
#Sant Cugat Del VallèS (Barcelona)	2
#Campo Grade - Ms, Brasil	2
#Dit Kevin St, Dublin	2
#Oosterwolde	2
#Xalapa, Veracruz	2
#Qro	2
#Vancouver / Nyc	2
#Rueil Malmaison	2
#Yorkshire	2
#Slovak Republic	2
#Pernambuco, Brasil	2
#China.Beijing	2
#中国青岛(China )	2
#London (Uk)	2
#Montreal, Qc, Can	2
#Patra	2
#Brasil/GoiáS/GoiâNia	2
#Building 47	2
#London. Close Enough	2
#Donostia - Gasteiz	2
#Silicon Slopes	2
#Gainesville	2
#Rajkot	2
#Lansing Michigan	2
#Saltaire, West Yorkshire	2
#Tenerife	2
#Newfoundland	2
#Zanè	2
#Ptz	2
#Cornell	2
#पुणे, महाराष्ट्र, भारत	2
#Coventry, England	2
#Manhattan Kansas	2
#Who Knows Where	2
#SträNgnäS	2
#Odd Pod, Troon, Scotland	2
#Thrissur	2
#West Sussex	2
#American Midwest	2
#Nizhnyi Novgorod	2
#St.Petersburg	2
#Brunswick, Maine	2
#Taoyuan	2
#Chambery	2
#@Ryan_Kirkman On Twitter	2
#Greater New York Area	1
#Http://Codingcafe.Jp/	1
#Kazahstan	1
#Aichi, Jpan	1
#Yurrup	1
#Roudnice Nad Labem	1
#Plymouth, England	1
#Россия, Московская область, Долгопрудный	1
#Cartago	1
#Washington, England	1
#Las Colinas, Texas	1
#Hier	1
#Hinterlands	1
#Ural	1
#Vancouver, Washington	1
#Uzhgorod	1
#Nyc, Sf	1
#BeléM Pará	1
#Guaruja	1
#Plainview, Texas	1
#Idolgo.Com	1
#Jerez	1
#Clayton, Melbourne	1
#Barcelona, Europe	1
#Floating About The Globe	1
#Ballina	1
#Neotropic	1
#NiteróI, Rj	1
#Stanford, California	1
#North Sydney	1
#Duesseldorf	1
#Twin Cities, Minn	1
#Love Field	1
#Sebastopol	1
#Санкт-Петербург	1
#SkoczóW	1
#Co.Uk	1
#Allen, Texas	1
#West Coast, The States	1
#Gunma	1
#Guerrero, MéXico	1
#Http://Subimage.Com	1
#Grande Pointe, Mb	1
#SãO FéLix, Bahia, Brasil	1
#Burbank	1
#Bp-Czech	1
#Verges, Catalonia	1
#Blagoveshchensk	1
#Trabuco Canyon	1
#@Malsup On Twitter	1
#Austin/Vienna	1
#Ffm	1
#Internettsburg	1
#MichoacáN, MéXico	1
#/Var/Www	1
#Earth, Sol System	1
#Padua (It)	1
#武汉	1
#Santo Domingo, Dr	1
#Campinas - Sp, Brasil	1
#SãO José Dos Campos, Sp - Brasil	1
#Var Location = { Country: 'Germany', City: 'SaarbrüCken' };	1
#Mount Dora, Florida	1
#Neverland	1
#UberlâNdia - Minas Gerais, Brasil	1
#Cambridge, Mass	1
#Astoria, New York	1
#Sao Paulo Brasil	1
#Global - (Currently Japan)	1
#Birmingham Alabama	1
#Djursholm	1
#KöLn-HüRth	1
#Mydlovary	1
#Greater Minneapolis-St. Paul Area	1
#济南	1
#Standing Behind You, Stalking	1
#/Dev/Null;	1
#SãO GonçAlo / Rj	1
#Dehradun	1
#Niteroi, Rj	1
#Caltech	1
#Zhejiang Province	1
#Locating	1
#Chernivtsy.Ukraine	1
#Seggauberg (At)	1
#Madrid (Spain) And London(Uk)	1
#Minnepolis Minnesota	1
#Zz9: Plural Zα	1
#World2.0	1
#Montverde, Florida	1
#Perú - Lima	1
#The Hague (Netherlands)	1
#BrasíLia-Df-Brasil	1
#昆明	1
#Fringecity	1
#Silicon Valey	1
#Http://Www.Funtoo.Org	1
#UberlâNdia	1
#珠海	1
#23509	1
#Xintend	1
#Matlock, Derbyshire	1
#Http://Sysphonic.Com/	1
#Reken	1
#Vienna (Austria)	1
#Uchicago	1
#Aus Moskau	1
#Hangzhou，Zhejiang，China	1
#Schoonhoven	1
#Tahiti, French Polynedia	1
#Http://Www.Sophists.Com	1
#˚∆˚	1
#Catskills	1
#Saint Paul Minnesota	1
#Weiqing Building 709, Thu	1
#Somewhere Far Beyond	1
#Niagara Falls, New York	1
#WrocłAw, Polska	1
#Frankfurt / Main	1
#Dark Alley	1
#Right Behind You!!!	1
#Portland, Dorset, England	1
#Milky Way, Universe, Expanding Mass	1
#EspíRito Santo - Brasil	1
#12 Hours From Anywhere	1
#Http://Www.Gravatar.Com/Avatar/3905D18F425Fddc2873Fdc818827B7B5?S=80	1
#Southern Illinois	1
#Nyc / Ber	1
#Ruhrgebiet	1
#Corydon Indiana	1
#Sao Paulo - Brasil	1
#06106	1
#02138	1
#19382	1
#Linares	1
#Glendale, Arizona	1
#Aarhus (Denmark)	1
#Northamptonshire	1
#Republica 701	1
#The Matrix	1
#GöRlitz (Germany)	1
#Luxmebourg	1
#Sei Pana, Batam	1
#Schwanau	1
#Lutsk	1
#Haleiwa, Hawaii	1
#Right Near The Submodule	1
#埼玉県	1
#| Rm -Rf /* |	1
#Utc+1	1
#Big D	1
#Emeryville	1
#Germany#Frankfurt	1
#Cpan, Rop	1
#SéOul	1
#Clemson, South Carolina	1
#Cracow (Poland)	1
#JoãO Pessoa, Brasil	1
#Mogi Das Cruzes, Sp	1
#Hamburgo	1
#Hammah	1
#Yamaguchi	1
#Uk_Uk, Lviv	1
#Gmt+2	1
#Https://Gitorious.Org/~Elf-Pavlik	1
#Emeryville, California	1
#Waterford	1
#Milano (Italy)	1
#MaríLia/Sp - Brasil	1
#Manipal/Bokaro	1
#Oronogo, Missouri	1
#Republica Dominicana	1
#Enfield, Ns	1
#Me13 7Be	1
#Iron Mountain, Michigan	1
#Www.Bulk-Inc.Com	1
#ReykjavíK	1
#Colima, Mex	1
#ChişInăU	1
#Manhattan , New York	1
#Campinas, Sp - Brasil	1
#Charleston	1
#Zp.Ua	1
#Catalunya	1
#CóRdoba/Veracruz - MéXico	1
#Japon	1
#Http://Ewakened.Com	1
#On The Planet	1
#Transnistria	1
#Freenode	1
#SãO José Dos Campos, Brasil	1
#<Radar Offline>	1
#Boulogne Billancourt	1
#Devon	1
#Arrakis	1
#The Wild, Wild West	1
#Qz	1
#2次元	1
#Rus	1
#Sun/Sol	1
#Long Island, New York	1
#It'S Complicated	1
#Rome (It)	1
#Fedora	1
#Santa Rosa California	1
#Cristais Paulista, Sp, Brasil	1
#Rva + Nyc	1
#Harwell, Oxford	1
#中华人民共和国福建省厦门市	1
#BeléM - Pará	1
#Darlinghurst	1
#A Desert Island	1
#Valladolid ó Madrid	1
#Http://Bambae.Com	1
#Fasdf	1
#法国，Tours	1
#Lietuva	1
#23603	1
#Bolzano-Bozen (Italy)	1
#Brasilia - Brasil	1
#Dumbo	1
#/Home/Foozzi	1
#Problemania.Org	1
#GoiâNia GoiáS Brasil	1
#黑龙江省哈尔滨市南岗区西大直街92号哈尔滨工业大学一校区A02公寓6047寝室	1
#Huntsville Alabama	1
#Cancun, Qroo	1
#Ladkrabang	1
#Томия, Япония	1
#KnuróW	1
#Great Russell Street	1
#四机房	1
#Genoa (Italy)	1
#Arces	1
#Improving Izariam	1
#Terrier	1
#Hongkou	1
#North West England	1
#Brasil, Sp, SãO Paulo, Centro	1
#Johnson City Tennessee	1
#Tty0	1
#Segovia	1
#The Localhost	1
#Linares (JaéN)	1
#Russian Federation, Moscow Region	1
#Miensk-Litowski, KryŭJa	1
#Vidin;Bulgaria	1
#1 Raffles Institution Lane	1
#BrasíLia - Df - Brasil	1
#Moscow, Korolev	1
#PéCs	1
#90805	1
#Ub,Mgl	1
#Granada Hills, California	1
#The North	1
#N.Novgorog	1
#Seilles	1
#10.331681,123.907886	1
#Kennebunk, Maine	1
#Cenote	1
#Avranches	1
#Targu Mures, Romainia	1
#Utd	1
#Kyiv, Ukarine	1
#Elgin	1
#JoãO Pessoa / Pb / Brasil	1
#Perm'	1
#IlhéUs - Bahia	1
#河南，中国	1
#Murcia (Spain)	1
#中国黑龙江大庆	1
#Chitrakoot	1
#Madison Wisconsin Babay	1
#Leon, Gto	1
#Sydney, New South Wales	1
#Troy, Newyork	1
#中国 杭州	1
#Liphook	1
#Cloverdale, B.C	1
#Missal	1
#Glorious Nippon	1
#Fairfield County	1
#Alexanderie, ÉGypte	1
#Dublin 8	1
#Renteria	1
#Long Island New York	1
#Southwest Missouri	1
#Lomagna	1
#Sp/Brasil	1
#Vienna/Europe	1
#Colchester, Vermont	1
#Dogpatch	1
#Euskadi	1
#Teh Internetz	1
#Oxford Mississippi	1
#Teh Internets	1
#Wakefield, West Yorkshire	1
#SãO José Dos Campos, Sp	1
#Mozhajsk	1
#ViñA Del Mar	1
#Here, Ithink	1
#Linodia	1
#Russian Federation, Kirov	1
#Vodafone, Internet	1
#Украина, г. Винница	1
#България, Свищов	1
#19.334873, -99.064627	1
#Amsterdam / Global	1
#BalneáRio Camboriú	1
#Goiania	1
#Curitba/Pr - Brasil	1
#Iowa, U.S.A	1
#D	1
#Orhem	1
#Sz.China	1
#Florida Center For Library Automation]	1
#/C/Emu/Trinitycore/	1
#Bloomington Indiana	1
#Des Moines, Iowa	1
#Cleveland Ohio	1
#-_-	1
#Malnova, Latgola	1
#Http://Calendaraboutnothing.Com/~Ahamid	1
#West Philly	1
#JoãO Pessoa, Pb - Brasil	1
#Nehterlands	1
#Shenzheng	1
#地獄	1
#Crimea(Ukraine)	1
#SãO José Dos Campos/Sp	1
#Nippon	1
#Trivandrum Kerala	1
#Little Brington, England	1
#Salamanca & Madrid	1
#Anime And Mango	1
#Pratteln, Schweiz	1
#Hh	1
#Hkd	1
#LéVis	1
#Funky Town	1
#Janelia Farm Research Campus	1
##Eggsml	1
#Shibuya,Toshima	1
#Moscu, Rusia	1
#Florianopolis	1
#Mataro, Barcelona	1
#RüSselsheim	1
#上海市浦东新区居里路222号	1
#England (Uk)	1
#I'M Around	1
#MontréAl QuéBec	1
#Cucuta	1
#36, Rue Scheffer - 75116 Paris	1
#Zaragoza (Spain)	1
#CréPy-En-Valois	1
#Seattle<->Boston	1
#Belleville	1
#Thrissur, Kerala	1
#Moscow\	1
#Kaslo, Bc	1
#Hcm	1
#Ntnu	1
#Calfornia	1
#Eivissa	1
#OsóRio	1
#Lincoln, Nebraska	1
#El CeñIdor, MúGica, MichoacáN, MéXico	1
#Near Munich (Germany)	1
#Russian,Rh,Sayanogrosk	1
#Http://Www.Iwr.Uni-Heidelberg.De/	1
#London Town	1
#Williams Lake, Bc	1
#Lexington, Massachusetts	1
#Cgn	1
#Благовещенск	1
#Worldwide Baby!	1
#Di Dalam Hati Wanita	1
#Xi'An, Shanxi	1
#Greater Chicagoland-Nw Indiana	1
#Windows	1
#Kowale	1
#Venezia	1
#Lonodn	1
#London - Uik	1
#Vzla	1
#Mazangé	1
#Trinidad And Tobago	1
#Athens, Ohio	1
#Madeira	1
#East & West	1
#Bigbuzzylocation	1
#Transcontinental	1
#北京海淀	1
#Ondres	1
#Chang Sha	1
#94610	1
#Lenzburg	1
#Hajom, Mark, Sverige	1
#Hangchow	1
#ÚStí Nad Orlicí Megapolis	1
#Пятигорск	1
#BeléM - Pará - Brasil	1
#Perros Guirec	1
#Internetz	1
#GrudziąDz	1
#Camaragibe	1
#Transylvania	1
#Magrathea	1
#Effretikon	1
#Opus	1
#GeorgsmarienhüTte	1
#Cluj Napoca, RomâNia	1
#Chiapas	1
#All Over The Place (London, Nz)	1
#Iwate	1
#Hcmc	1
#Luoyang	1
#Mrthe.Name	1
#Southwest	1
#Chicagoland Area	1
#UviéU (Asturies)	1
#Lake Tahoe	1
#England, Kent	1
#Sfca	1
#Deepest, Darkest Wiltshire	1
#Chain,Bei Jing	1
#Nigeira	1
#BesançOn / Aix-En-Provence	1
#日本	1
#Hanoi/Saint-Petersbourg/Moscow	1
#Russian Federation/Moscow	1
#Ciudad Obregon Sonora , MéXico	1
#天津市河东区	1
#Taegu, Southkorea	1
#Rome, V. S.M. Della Battaglia	1
#Outer Space	1
#TrollhäTtan	1
#Jkl/Fin	1
#Hampshire, England	1
#SãO Leopoldo	1
#Old Street, London	1
#Campinas - SãO Paulo - Brasil	1
#Lago Di Garda	1
#Davidson, North Carolina	1
#Queretaro	1
#@Home	1
#Gdansk	1
#Mallorca (Spain)	1
#Nuzild	1
#Montermorelos	1
#河南焦作	1
#Neumarkt	1
#Near Cleveland Ohio	1
#Campinas, SãO Paulo - Brasil	1
#Abq	1
#Azeroth	1
#Korea, South	1
#Ussr	1
#North Texas	1
#Germay	1
#Level 3	1
#Россия, г.Рубцовск	1
#Czestochowa	1
#Estudiante	1
#CesáRio Lange/Itapetininga - Sp	1
#Shiga	1
#@Sfrdmn	1
#Mission, Texas	1
#Unnc	1
#Venera Planet	1
#Tampon	1
#North-West England	1
#Sask, Can	1
#Milky Way Galaxy	1
#Bra[Sz]Il	1
#Korea (Republic Of)	1
#Shandong	1
#Highland, Maryland	1
#LièGe, Belgique	1
#Pgh	1
#Lagos	1
#Right Where You Are Sitting Now	1
#Altach, ÖSterreich	1
#Barnet	1
#Rf	1
#Cayenne (French Guiana)	1
#Cambridge, U.K	1
#Wybcz	1
#Forest Row, England	1
#Livry Gargan	1
#LabèGe	1
#P.S.D.R.E.R.F	1
#Uta (Ca)	1
#94117	1
#Help! Polar Bears Are Attacking Me!	1
#中国广州	1
#Nagoya Univ	1
#Nipppon	1
#Goiania, GoiáS, Brasil	1
#Saint-Petersburg, Russian Fed	1
#Lima,Perú	1
#Tufts	1
#Pasadena	1
#VsetíN	1
#Arlington, Massachusetts	1
#Zanjan	1
#Somewhere Out There	1
#Srinagar, Kashmir	1
#Eire	1
#Nw Arkansas	1
#Trujillo, Perú	1
#Dracena, SãO Paulo, Brasil	1
#West-Brabant	1
#Sk.Ca	1
#Bewdley, Worcestershire	1
#Inotherworld	1
#Oakville, On	1
#Earth?	1
#Far Far Away Land	1
#95348	1
#浙江宁波	1
#Earth!	1
#Sampa	1
#Docoka	1
#Munich, Bavaria	1
#Campinas/Sp - Brasil	1
#Chandler'S Ford	1
#Apt	1
#Tirol	1
#Wuhan.China	1
#Kashipur	1
#Cancun, MéXico	1
#Baiona (Spain)	1
#Eastern Washington	1
#Galicia	1
#Germany; 2.Osgrid - Volksland	1
#Madrid/Oviedo	1
#Essen/Ruhr	1
#Third Planet From The Sun	1
#中国>北京	1
#Definitely!	1
#Consulting	1
#Jogjakarta	1
#Toyko	1
#Bmnville	1
#Dans Le 45	1
#Seville (Spain)	1
#Guwahati	1
#Location	1
#London, Enland	1
#Appsterdam	1
#@Philingrey	1
#Jamaca	1
#Jutphaas	1
#Mobo	1
#Sfbay Area	1
#Df	1
#JaéN	1
#Phx	1
#So.Cal	1
#Southwest Washington	1
#Vorarlberg	1
#Angus65	1
#Athens, Hellas	1
#Somewhere Over The Rainbow	1
#Southern Africa	1
#District 3, Hcmc	1
#Hong Kong And Vancouver	1
#Saint Mandé	1
#Chennai.India	1
#CompièGne (France)	1
#En Fuga	1
#Czecho	1
#横浜市, 日本	1
#Germantown	1
#Charleville-Mezieres	1
#Ucl London	1
#Web	1
#Northeast	1
#KöLn (Germany)	1
#33A Cuu Long, F.2, Tan Binh, Tp.Hcm	1
#Markt Berolzheim	1
#Earth, Spiral Arm, Milky Way	1
#Test	1
#Miensk-Litowski, BiełAruthenia	1
#SęPóLno KrajeńSkie	1
#Bahia	1
#Greater Nyc	1
#Nyc - Amsterdam	1
#MaranhãO, Brasil	1
#Mhm	1
#Czech Rep	1
#Украина, Винница; Ukraine, Vinnitsya	1
#Knivsta	1
#Montreal, QuéBec	1
#Dortmund(Germany)	1
#Laaaarndon	1
#Russland	1
#The Planet	1
#Goring-On-Thames	1
#Columbus,Ohio	1
#+52° 21' 16.01", +4° 57' 20.67"	1
#FlorianóPolis - Brasil	1
#Troy, Michigan	1
#Великий Новгород	1
#LöHne	1
#Plymouth (Uk)	1
#/Root/	1
#@Squarism	1
#Saint Germain-En-Laye	1
#Ldn — Nyc	1
#AlmeríA	1
#127.0.0.1:8888	1
#GijóN, Asturias (Spain)	1
#Bilbo/Bizkaia	1
#Demark	1
#Tecumseh, Michigan	1
#Twisted Disneyland	1
#BrasíLia -Df	1
#Western Siberia	1
#Hambizzle	1
#Riverside	1
#Université Laval	1
#Redmond, Washington	1
#Kent State University, Ohio	1
#Sardinia	1
#4546176880394011	1
#TimișOara	1
#Bue	1
#Bedford, New Hampshire	1
#Ghaziabad	1
#Iraquis	1
#Earth (Mostly)	1
#Mckinney, Texas	1
#Park City	1
#Undecided	1
#Gloucseter	1
#Kanhangad	1
#CafelâNdia-Sp	1
#Sevilla (Spain)	1
#Marilia/Sp - Brasil	1
#Katwijk Zh	1
#Nyc And Albany	1
#H.K.China	1
#Some Where, I Think	1
#Maarn	1
#BrasíLia - Df, Brasil	1
#Earth::Unitedkingdom::London::Bermondseystreet::Thestage	1
#Moscow (Russia)	1
#BrasíLia - Brasil	1
#Df, Brasil	1
#Glenavy	1
#Lucerne	1
#North Wilkesboro	1
#Normandie	1
#Los Angeles & Portland	1
#China.Shanghai	1
#Nasa Goddard	1
#Amherst, Massachusetts	1
#Pondicherry	1
#Dumfries	1
#Outah Space	1
#World Wide Wiretap	1
#Somewhere Beyond The Sea	1
#Columbia Missouri	1
#BorläNge	1
#Hong Kong S.A.R	1
#Geek Between The Keyboard And The Chair	1
#Guidlford	1
#Long Beach	1
#Palm Beach, Florida	1
#Yorkshire (England)	1
#Net	1
#JöNköPing	1
#Bellevue, Washington	1
#Brentwood	1
#Virgo Supercluster, Milky Way Galaxy, Sol System, Earth	1
#90292	1
#Osca, Pyrenees	1
#Cape Breton, Ns	1
#Йошкар-Ола	1
#Rmit Uni	1
#Tacos'R'Us	1
#Bolsward	1
#Daiict,Gandhinagar	1
#KöThen (Anhalt)	1
#Oxford, Yo	1
#Vernouillet	1
#MedellíN	1
#Rua Timbira, 2145 Teresina/Piauí	1
#70123	1
#Www.Tellago.Com	1
#Vitoria (Alava, Spain)	1
#Ohio Among Other Places	1
#Earth, Solar System, Milky Way Galaxy, Universe	1
#BéZiers	1
#China.Zhuhai	1
#SantaréM	1
#Solar System	1
#Greater Dfw	1
#94720	1
#Bla	1
#Lith	1
#Auvelais	1
#Cyberjaya	1
#ValparaíSo	1
#On A Minecraft Server, Somewhere	1
#10001	1
#Украина	1
#Derbyshire	1
#Slc, Utah	1
#Santa Cruz, California	1
#Россия, Санкт-Петербург	1
#Nyc / Ucsc / Polar	1
#92883	1
#Black Forest (Germany)	1
#Yeah Right	1
#Suwon, Korea	1
#Nyc / Paris	1
#Devon, England	1
#London & Kent	1
#Yew Nork	1
#Bnagalore	1
#Arkania	1
#Mead, Washington	1
#CrançOt (France)	1
#Los Angeles And Sydney	1
#Kharkov, Urkaine	1
#Maui Hawaii	1
#Right Behind You!	1
#Wenen, Oostenrijk	1
#Massonnens, Suisse	1
#Boston Area	1
#PenedèS - Catalunya	1
#Monroe, Louisiana	1
#Lyngby	1
#La?	1
#Idaho National Laboratory Project Office	1
#Castlemaine, Australila	1
#Wow Freakz	1
#Www.Matsinopoulos.Gr	1
#GoiâNia, GoiáS	1
#Nowhere Important	1
#NüRtingen	1
#	1
#Westchester	1
#Sendenhorst	1
#GoiâNia-Go / Brasil	1
#Epicmorgia	1
#Sandisfield, Massachusetts	1
#CóRdoba - EspañA	1
#Struck Oil	1
#Pitesti	1
#Shambala	1
#Behind You	1
#Vinaros, EspañA	1
#Debatable	1
#94109 (San Francisco)	1
#Ringerike	1
#Cascavel	1
#Gxnn	1
#Easy	1
#Isla	1
#The Haque	1
#Chong Qing	1
#Beaches, North Carolina	1
#Padua	1
#MéXico D,F	1
#Roncade	1
#Classified	1
#Somewhere On The West Coast	1
#AlmeríA, EspañA	1
#Occupied Palestinian Territory	1
#Northampton	1
##Dtla	1
#Langley, Bc	1
#Kirov	1
#0X000000	1
#ÖSterreich	1
#SlavičíN	1
#Iit Punjab	1
#Richmond	1
#Aus	1
#Bedfordshire	1
#Ciechanki	1
#しんじく	1
#Santiago / Rep. Dominicana	1
#Moon Base Alpha	1
#Epfl	1
#B-Town	1
#22602	1
#Thessaloniki (Greece)	1
#Washington (State)	1
#Location 0	1
#Greater Philly Area	1
#Mdn	1
#Osaka-Shi Osaka-Pref	1
#Irc.Freenode.Net #Python Veloutin	1
#Cape Town South Africa	1
#OśWięCim	1
#ViêT Nam	1
#Burlington, Mass	1
#Съемная норка кролика	1
#Ivano-Frankivsk (Ukraine)	1
#Hà NộI - ViệT Nam	1
#Hertfordshire, England	1
#Cambridge, Massachusetts	1
#Denbigh, North Wales	1
#Huntsville	1
#東京都世田谷区用賀	1
#Visakapatnam	1
#Dublin, Irealnd	1
#845	1
#Bengaluru/Marudhur	1
#Inner Space	1
#Centallo	1
#Stack	1
#Www.Gzur.Org	1
#Hanover	1
#Turin, Italiy	1
#Center Valley	1
#Urumqi	1
#Akb	1
#Left Bank, London	1
#Austin, Planet Claire	1
#Tarnowskie GóRy	1
#Mcveytown	1
#Leicestershire, England	1
#Christchurch New Zealand	1
#BréBeuf, Qc	1
#495	1
#Cal Poly Slo	1
#Uiwang, Korea	1
#Mid-Atlantic	1
#Zurich, Swtizerland	1
#Europe/Czech Rep	1
#SãO Paulo Brasil	1
#Europe/Moscow	1
#Delluf	1
#台灣（Taiwan）	1
#Kharagpur, West Bengal	1
#Leghorn	1
#Sockerbruket 33, 414 51, GÖTeborg	1
#Cis, Eecs, Peking Univ	1
#Makati	1
#Trissur	1
#Brasil - Sp	1
#East Midlands	1
#Mallorca, EspañA	1
#Andheri	1
#Irc.Perl.Org	1
#Kazaǹ	1
#Some Random Top Secret Base	1
#Jhb	1
#SãO Carlos, Sp - Brasil	1
#Orel, Rf	1
#Http://Twitter.Com/Hiboma	1
#Planet Mars, Cydonia	1
#Набережные Челны	1
#Wired	1
#BrasíLia, Df - Brasil	1
#Naters	1
#Ukraina	1
#United Stated	1
#Www.Accesshome.Com.Au	1
#Camerino	1
#Gelderland	1
#Lalaland	1
#@Fredrocious	1
#Wellington, N.Z	1
#Rover	1
#TüRkiye	1
#/Home/Dilibau/	1
#East Bay, California	1
#Upstate New Yawk	1
#Czechrepublic/Orlová-Lutyně	1
#Algerie	1
#ŁAziska GóRne	1
#Bazil	1
#Salamanca	1
#Гомель, Беларусь	1
#東京都渋谷区神宮前1-1-1	1
#SãO Carlos, Sp	1
#Dehiwala	1
#Slo	1
#東京都	1
#Petsamo, Lapland	1
#Babia	1
#Ksa	1
#Ny.Us	1
#N 52.507377 E 13.460589	1
#Sw Michigan	1
#Gandhinagar, Gujarat	1
#VaražDin	1
#Behind The Phosphor	1
#Http://Gravatar.Com/Hyardimci	1
#Scotland, U.K	1
#Cze	1
#Default City	1
#ČEské BuděJovice	1
#Kettering, Ohio	1
#Somerset	1
#Paris 6	1
#Long Beach, California	1
#94041	1
#Higashi-Nihonbashi	1
#Bopohe}|{	1
#North East England (Uk)	1
#Phillynyc	1
#Chendu	1
#Doap.Com	1
#IlhéUs/Bahia/Brasil	1
#Parkstein	1
#Hà NộI	1
#N.L.L.V	1
#北京，中国	1
#Zhuhai.Guangdong.China	1
#Poble Nou, Barcelona	1
#沖縄県名護市	1
#Gandhinagar/Ahmedabad	1
#Whistler, Bc	1
#Kochi, Kerala	1
#Hessle, England	1
#Bengalooru	1
#(Shell)	1
#Macae-Rj, Brasil	1
#Intertubes	1
#Cluj - Napoca	1
#Cet	1
#Http://Gravatar.Com/Saki007Ster	1
#Here And There	1
#United States (Florida)	1
#Bardowick	1
#French	1
#Kozloduy	1
#Helm'S Deep	1
#Danville Indiana	1
#Ratnagiri	1
#+09:00	1
#Http://Www.Gravatar.Com/Avatar/4F74Dd674Dbe18096Fec081Baab1A404.Png	1
#Sandy, Utah	1
#Behind Your Firewall	1
#Underhat	1
#A Five Line Poem	1
#Campinas Sp	1
#Somewhere Over The Slaughterhouse	1
#Stafford, England	1
#K55Ca-Uet	1
#Sillycone Valley	1
#Windsor	1
#Denver!	1
#Казахстан	1
#Rochester, N.Y	1
#太倉，蘇州	1
#Http://Www.Knowledgetree.Com	1
#SãO José Dos Campos-Sp	1
#BistrițA, RomâNia	1
#11201	1
#Florida, U.S	1
#경남 창원시 마산회원구	1
#Tokyo.Jp	1
#Boardtown 32, Bitstreet 8	1
#Ludhiana	1
#The Netherlanths	1
#Paris, Fra	1
#Moscow, Wastelands	1
#Ilheus	1
#Somewhere Cloudy	1
#Zulte	1
#Altanta	1
#Beauharnois, Qc	1
#The Earth	1
#Tarashcha	1
#Southern Ohio	1
#Ponyland	1
#Eivissa, EspañA	1
#CóRdoba, EspañA	1
#Melborune, Florida	1
#Http://G.Co/Maps/Jqvg5	1
#Palmira	1
#Santa Brigida	1
#Goodland Kansas	1
#Campinas/Sp	1
#Yes	1
#Russian Federation, Spb	1
#NeumüNster, Deutschland	1
#Bs.As	1
#The United States	1
#Cape Town. South Africa	1
#Phillipines	1
#Serbien	1
#Nyu	1
#Wirral, England	1
#Waterford/Dublin	1
#Otaniemi	1
#Online	1
#California Foothills	1
#Singaproe	1
#Halifax, Nova Scotia (Canada)	1
#Queensland	1
#Teldrassil	1
#Hobart, Indiana	1
#/Home/Necronet	1
#Vancouver Washington	1
#Whistler	1
#Salisbury, Great Britain	1
#L'Viv	1
#Iphone.Git	1
#HảI PhòNg, Hồ Chí Minh	1
#(37.768372, -122.449139)	1
#Cambrdige	1
#Shropshire, England	1
#Moscow Idaho	1
#衡阳	1
#Newcastle Upon Tyne, England	1
#Middle England	1
#SãO Carlos - Sp	1
#Melbourne (Au)	1
##Occupyatlanta	1
#Sant Cugat Del ValléS	1
#St.Petersburg Florida	1
#GoiâNia - GoiáS - Brasil	1
#Can Tho, Viet Nam	1
#Cipherspace	1
#Glendale	1
#Bitbucket	1
#Western Michigan	1
#75000	1
#Western New York State	1
#Uxbridge	1
#Mattgoldman	1
#Eastern United States	1
#ÍSland	1
#Massachusetts/New York/California	1
#KöLn, Deutschland	1
#成都	1
#Frozen Reindeer Country	1
#Mvdc	1
#İZmir, TüRkiye	1
#The Hidden Fortress	1
#SãO Paulo, Sp - Brasil	1
#Herson	1
#Marquillies (France)	1
#Lafayette, Indiana	1
#Hertfordshire	1
#Malibu, California	1
#浙江省杭州市文二路391号	1
#Somewhere, Over The Rainbow	1
#Hauj Khas	1
#Aib	1
#Http://Www.The-Tech-Tutorial.Com/?P=1868	1
#Http://Blakemizerany.Com	1
#Tj.Cn	1
#Dominican Rapublic	1
#Comodo	1
#GijóN/Madrid	1
#With The Finger On The Keyboard... ;)	1
#Java	1
#Mikew	1
#Vancouver, British-Columbia	1
#Worcestershire	1
#Durham, England	1
#Santa Rosa, California	1
#Belle Vernon, Pennsylvania	1
#Vagabonding	1
#Praha, ČEská Republika	1
#SúRia, Barcelona	1
#Россия, Москва, Ногинск	1
#Osaka.Japan	1
#Lietuva (Lithuania, Gmt+2)	1
#Grosse Pointe, Michigan	1
#Around Michigan	1
#Sfo / Sjc	1
#Xjf	1
#UberlâNdia Brasil	1
#Sankt-Peterburg	1
#11215	1
#Kyiev	1
#Brasilia, Df	1
#中国浙江杭州	1
#SãO José	1
#Bunnik	1
#CancúN, MéXico	1
#Durandalingrad	1
#Melverley, Shropshire	1
#Oahu	1
#Lower Haight	1
#Melitopol	1
#Msp	1
#1Eb4 6803 B229 Ef40 87E2 E7Dc 0Ac8 9A32 4C9F Beca	1
#Planet Earth, With Firmly Both Feet	1
#Zju	1
#Cylon Occupied Caprica	1
#Phila	1
#Creating Your Github Account	1
#Traveling Salesman	1
#Solaro	1
#If City	1
#Enfield, London	1
#Amoy.China	1
#Variable	1
#Http://Www.Twitter.Com/Abionic	1
#Kocaeli, Turkiye	1
#London, Shoreditch	1
#Halifax Ns	1
#Virtually Everywhere (Tm)	1
#Scott Afb	1
#Lower Mainland, British Columbia	1
#94131	1
#Catamarca	1
#Davidwright@Gmail.Com	1
#Africa	1
#Stornoway	1
#Always Moving	1
#Http://Gravatar.Com/Tryambakeg	1
#Blackstone, Qld	1
#Ici	1
#Europe (Currently Wroclaw, Poland)	1
#ČEská Republika, Praha	1
#Patras	1
#Cny	1
#G-Rap	1
#BèGles	1
#MüNchen, Deutschland	1
#Muree	1
#Madonna, Maryland	1
#Far Planet	1
#Somewhere Around The World	1
#Veliko Tarnovo	1
#Seffner, Florida	1
#Tucuman	1
#Salem, Virg., Uasr	1
#North Idaho	1
#Http://Www.Gravatar.Com/Avatar/14Cdd9Dd97899E09D30Ee7B012A73117.Png	1
#HäRnöSand	1
#Ac	1
#Bruxelles - Belgique	1
#Shen Zhen,Guang Dong	1
#Ap	1
#Http://Memespace.Net	1
#Onion Land	1
#41015	1
#En_Us	1
#West Yorkshire	1
#Skype: Fljot_	1
#Git Oovyaonge@Oovyaonge.Cafe24App.Com:Oovyaonge_Oovyaonge	1
#Los Angles, California	1
#Noe	1
#Morroco	1
#Vimim	1
#Kuantan.Pahang	1
#Kochi	1
#Boston/San Diego	1
#Украина, Донецк	1
#Liestal, Schweiz	1
#Dundalk	1
#Bangor, Wales	1
#Osaka@Japan	1
#Waseco Building	1
#Irc.Freenode.Net (At5L)	1
#Krakow/Kyiv	1
#Lower Florida Keys	1
#Http://Gravatar.Com/Bhoriem	1
#New Buffalo, Michigan	1
#深圳	1
#The Multiverse	1
#Panopticon	1
#Rhone-Alpes	1
#UberlâNdia, Minas Gerais, Brasil	1
#ZáHony	1
#Osaka-City	1
#Los Angeles City, California	1
#Anus	1
#Sector Zz9 Plural Z Alpha	1
#Cordoba	1
#The Netherlands, Europe	1
#Cancun	1
#Schauernheimerstr. 8, D-67125 Dannstadt-Schauernheim	1
#Ailleurs	1
#Grid	1
#Nieuwdorp	1
#Warszawa, Polska	1
#Traveling The World	1
#Jehay	1
#Kalymnos	1
#Pushkino, Moscow Province	1
#Niteroi - Rj - Brasil	1
#广东 深圳	1
#Nimes	1
#Middlebury	1
#Les Ulis (91)	1
#Miyazaki	1
#ThüRingen, Deutschland	1
#Auvergne / Herault (France)	1
#Yangon	1
#Rnd	1
#Savar, Dhaka-1342	1
#Oak Ridge, Tenn	1
#Gasteiz, Basque Country	1
#Томск, Россия	1
#Http://Git.Io/Duzy	1
#Chicoutimi, Qc	1
#Trentino	1
#РФ	1
#Bellarine Peninsula	1
#сеть)	1
#Argyll, Scotland	1
#Flanders	1
#Ustc	1
#Palamos	1
#Lost Between Bits	1
#София, България	1
#Allegheny College	1
#Asia.Harbin	1
#Kyev	1
#Russian/Tyumen	1
#Boston/New England	1
#Amherst, Nova Scotia	1
#Campina	1
#Silicon Valley / Hawaii	1
#Polska KrakóW	1
#Blighty	1
#Frankfurt, Gemany	1
#Tamworth, Staffordshire	1
#D.F. MéXico	1
#Roaming	1
#Middle River Maryland	1
#IaşI, RomâNia	1
#Mry	1
#中国湖北武汉	1
#Paris / Sf	1
#Phily	1
#Argetnina	1
#Http://Funnymonkey.Com	1
#Vitoria-Gasteiz	1
#Kalix	1
#/Users/Fabi	1
#Rua Turi 184	1
#Alger	1
#Cymru (South Wales) Uk, Tywi Valley	1
#Long Island	1
#Xi`An	1
#Milton, On	1
#Lidzbark WarmińSki / GdańSk	1
#Pamplona/IruñA	1
#Hainau (Germany)	1
#Jinju	1
#Herzliya	1
#四川.绵阳	1
#Staten Island, New York	1
#MaríLia - Sp - Brasil	1
#横浜	1
#Mallorca	1
#Luik	1
#Glyfada	1
#YucatáN	1
#Mukachevo	1
#Brignoud	1
#The Nederlands	1
#Nederlands	1
#China.Qd	1
#Greater Washington	1
#Skyrim	1
#Ederbringhausen	1
#08691	1
#Da Nang, Viet Nam	1
#Spencer, New York	1
#Prg	1
#Prc	1
#Http://Www.Gravatar.Com/Avatar/C603592A890Df32023Ed4E7D9Cfcdbe2?S=80	1
#South Pole	1
#Puebla, Puebla	1
#Venice Beach	1
#WłAdysłAwowo	1
#GenèVe	1
#Sol 3	1
#Swansea, Wales	1
#Kiev.Ua	1
#Nurnberg	1
#China.Gz	1
#日本国 広島県広島市	1
#Sussex	1
#Москва, Русь (Moscow, Russia)	1
#Uruapan MichoacáN MéXico	1
#Medellin(Colombia)	1
#A Happy Place	1
#Joao Pessoa - Pb	1
#The Rose City	1
#Existing Between Keyboard And Chair	1
#Caloocan City	1
#GöRlitz	1
#Software Engineer	1
#Ukreine	1
#Http://Goo.Gl/Maps/4Qgc	1
#Gotland	1
#Dnepr	1
#Hopefully Somewhere Warm And Sunny	1
#Los PaíSes Bajos	1
#Colima,Col,MéXico	1
#Shang	1
#日の本	1
#Everywhere But Nowhere	1
#Oahu, Hawaii	1
#One The Move	1
#Phase Space	1
#Kc	1
#Jonestown	1
#Campinas / Sp	1
#Hyper Island	1
#Space The Final Frontier	1
#Russian, Moscow	1
#Hacking From The Moon	1
#Jocala.Com	1
#Zeeland, Michigan	1
#Loon Lake, Washington	1
#Engineer	1
#Sapporo, Hokkaido	1
#Bruz	1
#Tenerife (Spain)	1
#Da.R-W.In	1
#Jacksonville Florida	1
#Xanth	1
#Lindon, Utah	1
#BruyèRes-Le-ChâTel (91)	1
#Lietuva (Lithuania)	1
#Rensselaer Polytechnic Institute	1
#Elgin, Scotland	1
#Colima,Col	1
#Campinas / Mogi Das Cruzes - Sp	1
#The Grid	1
#Decatur	1
#Siberia	1
#Tianjin.China	1
#Limanowa/KrakóW	1
#Makeevka	1
#Vtech	1
#Birmingham,Alabama	1
#Far East	1
#Galicia, EspañA	1
#山楂树树枝	1
#Skehanagh Park, Watergrasshill	1
#Poa	1
#Kensington, Maryland	1
#Aizu	1
#Webernets	1
#Eliot, Maine	1
#Eets	1
#EllingsøY, ÅLesund	1
#Nomadic (Currently Ogden, Ut)	1
#A CoruñA, Galicia, EspañA	1
#中山大学	1
#Karlruhe	1
#Brittany	1
#Sonoma	1
#Украина, Житомир	1
#Homel	1
#Santiago Compostela	1
#Layer 13	1
#North California	1
#Http://Clarkparsia.Com	1
#Mar Del Plata	1
#Brussel, België	1
#Maginus	1
#Royal Leamingtin Spa	1
#Http://X-Coder.Mobi	1
#Colima, Col. MéXico	1
#Http://Heliosinteractive.Com/	1
#Pku:China	1
#Sab.Com	1
#Aberdeen Scotland	1
#Vironezh	1
#Cozumel, MéXico	1
#Kathmandy	1
#РФ, Владимир	1
#Thessaloniki	1
#Winchester, England	1
#Forlimpopoli	1
#Hồ Chí Minh City	1
#Airdrie, Scotland	1
#Arbucies	1
#Wilrijk	1
#Qualicum Beach, Bc	1
#Sergiev Posad, Moscow Region	1
#Nagoya,Aichi / Mt関連の物など色々作っています。	1
#Sao Paulo Sp	1
#Salisbury, Maryland	1
#Hel	1
#PaulíNia, SãO Paulo	1
#Hampshire, United Kingdon	1
#Paris/London	1
#Gex	1
#Graz.At	1
#Northern Nevada	1
#Self Confidence Comes From Being Sure That Your Predictions Are Accurate	1
#Lanzarote, Canary Islands	1
#Dimap	1
#Planet An-Z 52245	1
#Avon	1
#Massassachusetts	1
#Iit Kanpur	1
#Holland!	1
#Burwood East	1
#New York / Silicon Valley	1
#SãO Mateus - Espirito Santo	1
#Merry Ol' England	1
#Mines	1
#ÚStí Nad Labem	1
#Chania Crete	1
#Ha Noi - Viet Nam	1
#中国浙江省杭州市	1
#Moscow/Spb	1
#AlcorcóN, Madrid	1
#Schipluiden	1
#Hyogo.Japan	1
#Near Madison, Wisconsin	1
#Asturias	1
#Zuerich	1
#Nuermberg	1
#North Liberty, Iowa	1
#Moray	1
#The Netherlands, Amsterdam	1
#Port Coquitlam, Bc	1
#KrakóW, Polska	1
#Shaanxi Xi'An	1
#French Riviera	1
#Bloomington	1
#Nevada, U.S.A	1
#Rossendale, Lancashire	1
#Bellevue	1
#Bc	1
#London And Faversham, Kent	1
#PlanèTe Terre, Voie LactéE	1
#Wales, Britain	1
#ChorzóW	1
#Dorset	1
#Frankfurt/Hanau	1
#Deklein	1
#Березники	1
#Bellatrix	1
#Кривой Рог	1
#WüRselen	1
#Oreana Idaho	1
#Compiegne (France)	1
#Россия, Екатеринбург	1
#Far, Far Away!	1
#Rva	1
#Www.Daum.Net	1
#Czech Rebublic	1
#Dungeons	1
#Bretagne	1
#Http://Thomasflemming.No/	1
#Brasil, Natal-Rn	1
#Vancouver, Canda	1
#河南	1
#Melbourne, Florida	1
#Teton Valley, Idaho	1
#2:450	1
#Valladolid (Spain)	1
#Northern, Kentucky	1
#VendéE (France)	1
#BrasíLia, Df	1
#Lancaster, England	1
#Wittenberg, Wisconsin	1
#Marieville, Qc	1
#Berchem	1
#MüNchen/Munich/Mnichov/Мюнхен	1
#Maui	1
#Samstagern	1
#The Desert	1
#Ростов-на-Дону	1
#Rio Das Ostras	1
#North Yorkshire, England	1
#Romney Marsh, Kent	1
#Cambridge Massachusetts	1
#Custom Real Estate Websites	1
#Stavropol, Russian Federation	1
#Santa Clara Del Mar	1
#Down Under	1
#MontéLimar	1
#Les Bois (Switzerland)	1
#Россия, Оренбург	1
#Ottawa/Montreal	1
#Berkel	1
#Suomi (Finland)	1
#Nazi Moonbase (On The Moon)	1
#Huntsville, Alabama	1
#Hyrule	1
#Калуга	1
#Ilfracombe, Devon	1
#Stari Zednik	1
#The_Darkside	1
#Puerto Real (CáDiz)	1
#London, Se22	1
#Wordwide	1
#Sassenheim	1
#Berkshire	1
#Sf, California	1
#Bosnia & Herzegovina	1
#Missouri, U.S.A	1
#Sallisaw, Oklahoma	1
#Харьков	1
#Geneve	1
#Illnoise	1
#27318, Hoya	1
#Mikocheni	1
#Amsterdamn	1
#Universe	1
#Sutz	1
#Kiyv	1
#Milwaukee.Com	1
#Santa Rosalia	1
#Mount Vernon, New York	1
