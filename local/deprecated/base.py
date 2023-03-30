import os  # Operating System
import requests  # Handle API requests
import json  # Read JSON data
import pprint  # Prints the json in a more friendly fashion

usernames = ["griffpatch","Will_Wam","ScratchCat*","griffpatch_tutor","sharkyshar","ceebee*","WazzoTV","atomicmagicnumber","TimMcCool","theChAOTiC","Hobson-TV","Scratchteam*","-BoyMcBoy-","Dhilly","Berricake","DerpAnimation","FunnyAnimatorJimTV","huntedskelly","ipzy","kevin_eleven_1234","CrystalKeeper7","TheInternetIsCoool","Sterlon","-NerdAnimator-","potatobear616","moss-shadow","Coltroc","Bubbles_Official","Rosyda","PotatoAnimator","yunnie2005","Zinnea*","StratfordJames","4CHR","7Sofa","FUZZIE-WEASEL","cwkteacher","warfame","-Cinematic-","MJM3","FUNUT","9rainbowtails","scratchU8","World_Languages","PaddlerGames","TNTsquirrel","ToadfanSchool","-cafecat-","JWhandle","GoldenEagleStudios","chipm0nk","KIKOKO_","ChewingFruitGum","Brad-Games","OmbraTheFurry2","awesomeal82","RokCoder","-TheGreenNinja-","-Rocket-","nednilclan","Astro947","lisabc","Silvershimmer43","nekopyon","MistCat","xamuil2","pandakun","The_Updator","bear123bear456","CapitanFluffy","speakvisually","TurboKitten","Castle_Hippopotamus","Wildflight","Meekaryo","TrentonTNT","-PhantomAnimations-","ivypool2","WO997","Paddle2See*","Silverpelt_","-SkyStar-","alphabetica","lightblue012","s00384206","cartoonnetwork","scmb1","Realises","RacingAce","astro-tears","Za-Chary","DarkLava","gobo","ScratchDesignStudio","Pearlescence","Canarysong","AnimationsScratch","PetalsSilversteam","-AmberKitti-","Raysworkshop","BurntPotatoArts","Lionclaws","_MistyLight_","QuaXX","ArcanisHD","whylikejustwhy","LeiIani","BIazeheart","-butterwaffle-","coder_d6","AquaLeafStudios","CattyCodes","14049","Dinoboi_Animations","madrid2030","FaceOs","RedCuzImAwesome","Jeila","colinmacc","Capt_Boanerges","x__0","amylaser","Eloctrasyd","KillerByte","CS_Iewis","Artinqq","SCRACO65","legobuzz12","Warriorcats4life9","GameGirlX","Rae-TV","ThePancakeMan","ilhp10","Moonpaw12345","rainbowleenie","D_i_a_v_l_o","SquigglyTuff","Derble","RememberNovember","zevo","holybird3","you","PrimordialChaos","-EmberAnimations-","BenjaminWins11","GarboMuffin","ScratchStang","sekkai","Artisticat","nini2009ph","SkittlesTheBunny","Greninja714","creeperkizi","ExperienceSea","Bubble-Frog","amee-","PEER_Foundation","1dat_doodles","geijutsu","Shadow_Kid21","kirah201","diggerboy12","Will_Test","MathMathMath","PeteyTheParrot","CoverMusic","cutupuss","SullyBully","tomokid","Pickle-Productions","-FunnyToons-","Bradk2005","-Xaf-","jacko1234567","PurpleBand-aids","radscience","PullJosh","norumaku","ShiftClickLearn","sab_pg","Pikoki--","AnaniAnime","zvardin","CatFan12","bubble103","MIMOKYOTO","-mintea-","CJKB","codeplus-1","SharkyPup","rosebreezee","-RobloxAnimations","The-Nick-of-Time","FireMayro","MaciTheGamerYT","kewl999","--Explosion--","TheEpicCake","OreoPopPupper","Goldy675","Twin138956Scratch","code_iot","LiFaytheGoblin","mres","BirdNani","Yllie","DEFAULTDANCEONEM","s-a-l-t-i","PennyQuest","NHK_for_School","Baqel","huntedskelly_Test","awesomebricks1","Finlay_Cool","nyanco-guy","MagicaJaphet","mekkuo","Mallonations","countinqsheep","MegaComedyCentral","logic_lab","foxfood","Splow","Coolbe22","aesthetes","kirbyzaz","BobbyF","Carbogast","Matthew_K1","epninja","Pikurin","h0rnet15","MirrorsAreLiars","cheddargirl*","cactivi","meurpTV","-SuperFunnyAnimator-","JamesOuO","natalie*","Dedsher","lIIIIl","ChelseaPup","LawsOfScienceChanger","amazingQ","eggnormous","UltraCoolGames","kaleido-ghost","hern1","-WallyAnimations-","-clovershine-","bluestem","Birdah","alexandretherrien","MajesticPie","GoldAnimations","vollrineVPS1","icmy123","-Silverpaw-","DuckGoose9254","luviinqq","JS_Coder","TeacupTrinkets","monkey9927","cupcakenoah","hgwrs16","max_and_zeke234","Echostrike","dreamyrxse","Titanium01","kodlarize","TheGamingArcher","Jumper-","Paralyzed_Potato","awesome-llama","MasterAndras","MoreBetter","mariocrafter","duck--","--Waterfall--","RoastedSquirrel64","unknownscratcher1234","-magpie-","pastryy","HenryWolfe","Scratcher_No-1","Pahunkat","averagelife","TNTend","CoachOC","kuri-pa-2","Nightstarwarriorcat","ggenije","Yumii-Frost","Glitch-Tech","-TIC-","wxtermelxn","PetalCrest","Chewzers","Loud_Shorts","HItTheReplayButton","venomous-squirrel","Paperclips","JC_ProGold","Ask_LightningStar","_Kodland_","Tigrrish","kodekursosloskolen","Unrealisation","AwezomeXD","praplane","cs2889410","andresmh","mini-macaron","Blossom_Crowfeather","me","CSFirst","Starredsky","ocearuii","isomorphism_","PlZZAZZ","Lightnin","GLECK","TurkScratcher125","NyantyuGO","Aqua-Kitty","mrcreeper34","Spidertest","AgentQuirt","maDU59_","kaaakeee","23ScratchMan","p-aesthetics","SpriteMaster","teeeeeeen","The_Guy_","NinjiKai","CoLLoRBLiND","Game-Cloud","DINOMAHTER","cherrei","suitcasedog","loganvcairns","Noentiendo2005","King_Spacebar","cinnabungirl13","Benelem12","-CodingAnimations-","-Rex-","bookdog17","pixelpichux3","Brightpawquest","Fidessa-Chan","NickyNouse","Hanzhe","applepiesleth","52Blue","thoyal","tikilla3","xVanyx","PrimeGuy_1001","-still-dreaming-","fluffkeys","TheGreenFlash","MartinBraendli","-Vanilly-","-Ninja-Animations-","mallo222","ElectromanRocks718","cxerryblossom","-GlitterSquad-","LukeManiaStudios","Scratch-Minion","Pichi-","-TotallyEpic-","04tmoody","vantqe","UXRCF","Judpomme","maplepancakes","firepaw_rusty","MrA-","Haudio","DragonOfPyrrhia","-HappyPotato-","-RISEN-","kuma_monn","Mangi_lx","DadOfMrLog","zigzaq","MooDingo","jonzo","Rebeat","Tralaxy","VinCrafts","-TheDoctor-","IcoQuest","Doctor_What_","-SAUS-","RomaniM","squig3","Yourflez","LunaShadow","HopesNDreams","papipupepappa","-PandasQueen-","Painted-Pupper","qucchia","coyotears","Shadowblaze-the-WC","Lucasliu9595","Coocalici","Wavecolor","PastelFlower","GonSanVi","-BreadMan-","LinkScratchStar","kotsu-_","PinksMonkey","yosiotouzyou2","ComplicatedCodes","FoIlow-For-FolIow","Giolaboman","TheGamingKitten","dark_72","cookie947","thisandagain","violet_raven","PlsGiveMeT0es","Burning_sky","twonerds","FontGod","TheTrueColeye","alps88","Poteto143","stariiko","Painted_Serenity","-SapphireDemon-","t9decode","-applepie-","l3oom","IguanaLover","12345kkkkk","TikiIIaReis","ricarose","WazzoTEST","atomic-osushi","chikenzi","gamepg","Cool_NickXD","RainbowWaffle","MusicManJoe","Gleamur","MaxyBrian","yukamenseki","Pikakit","isIand","-Finicky-","deeki","Splo","Cuhkaerion","DANISON","ScaIes","Elephant71","kaerusennin","xFlameFuryx","Coco_Berri","skyset","Ashwel","Ixliora","kitkatkittycat","LifeExplained","Fazah_Champ","beet-eggs","Tanqerine","mawz","kriblo","Walle10-0","pvzlover11","Choco-Doggo","ShowPasswrd","WhatNotToDo","CodeKirby","gdpr0000001","hoppingicon","Ryham301","honey-lavender_","kittengalaxy","mikeono102","Supercube_123","123768631","EllaPHNT","mr_snowbuddy","CygonTheDragonCoder","Purplekitten22","ProbabIy_Not","Natures_love","everyone","TheLogFather","Psiborg","akua11v","ManxNinjaPig","purplebeanie","Chamomiile-","NilsTheBest","kode-x","THE_MOST","PutneyCat","dn_scrtch","dawn0877a","firstject","The-Green-Dragon","PuppysILove1200","-ShatteredSilence-","-iinkwiinqs-","key01134","GailAnimates","Thepugmen","0429aaa","-Moontale-","Kloudheart","otter_puggy","wolfychan10","Cherizy","-squichaii-","oriquack","StollerTech","roselush-","PandaTimmyMrT","chooper100","otterstar","anime-tions","Zebracheetah","AwesomeGamesTV","alilpotato101","FollowCherryBlossom","2v6","hanngousuihann","Ninjimaro902","glados10","poliakoff","Crystal-25","crazyweasle123","Shwip","SharkysharTest","yotacopaco","rainbowenderz","BluePlanet1","bidulule","thesuperguidegames","Relatable-","rainbow_waves","HehtorOCH","Pika-Girl03","KichiChan","dreamiistars","JTHEJET","Awesomemandudegames","1000652","PhatDudeProductions","250119code2","harukimann","cs511598","MapleSkyTiger","sceptile100","Hambegar","dezland","haunted_enderman","_HollyFrost_","CodeZillaKids","lZXTVhCSVlr","cranegame","Evelynn-","naokimann","-ABIC-","SharkyMAPs","Silver-skies","Romanchik_","artisticdragonpaw","CinnamonNugget","Doodlebug450","meron0gou","pocopocojohn","papers-","LearningResources","nonkakk","pixieblossom","-LilWolfy-","yourfriendoqueen","MoonFuryBeatz","Foxy_umbreon","OHAMedia","ericr*","--poison-pen--","-Add-Some-Color-","Minecraft_123459","CrazyNimbus","Blizzy2","scarpaw13","-RedWolf","puppypaws","ratchiId","CgBB","abee","crastalhorse22","Cloud-Multiplayer","-Boont-","BoltBait","-_-_-Becca_Arts-_-_-","-Achelxis-","millyComedian4567","BIG-red-BUTTON","coralsong","bodi3","gurikkus","MrRaisin","CardboardGuy236","raion112","lunna-blu23","RoboDog31","zayzaril","alba-magica","BisketDog","Dress-up_games","Etalion","shadowspear1","08jackt","objectionz","marshmellothelegend","-Auron-","swifty2","TemWatchEgg","Laladragon","--owo--","lucap1877","kekelolo","daisykitty","FlowerCat4444","PS58","achavez77","T2V","okae","Chociily","TansGames","Kittydog098","Raininqq","AiyanMind","-risu","Pixar2000","noodlebot743","itzs_me","remixsuper","Shattered_Diamond","CMlukian","--Accension--","PQS2017","AlSweigart","-Nightfire-","flamingenius","Catosaurus","NikkeiBP","rayyaka","smash-20","O2009H","CodeSpeakLabs","287228","AUMSUMTHEGREATHULK","-Orbitron-","griffinboy","TheInternetIsCoool_2","portishead7","Jikyi","nabaiko","Darcythecat","-UnderTale-","DorkwingDuck","gumboygames","Sugaryxsweet--","hiohbye","CosmicKiwi","PerryTheChiweenie","Nutupita","GD_player__","dcsm","ApplePiie","GlitchedWolf","charli987","Frostpuff","new_houjon","cs50","ScribbleAnimator","Apfellord","cinnqwon","fib1123meow","JackPigPro","pococikapusta","FreezeNova","TheSoftCake","PokemonDude21","takasyu","iPhone_ATT_TWC115","Time_Tripper","piano_miles","Geotale","Canthiar","weegaweek","Kouzone"]
follows = ["424056","92980","81893","81613","59037","58449","58280","49834","43959","40109","39915","39840","36476","35767","35530","34746","34308","32933","31794","30880","30767","28840","28565","27815","27008","26672","26307","26194","26063","25479","23644","21938","21522","21426","21294","21111","20556","19824","19087","19007","18763","18725","18657","18492","18215","18141","17967","17938","17882","17291","17071","16646","16601","16487","16213","15848","15835","15735","15414","15343","15262","15094","15077","14457","14189","14185","13913","13824","13395","13377","13340","12948","12796","12776","12469","12416","12226","12183","12020","11889","11852","11747","11647","11600","11410","11378","11356","11259","11111","11044","11019","10989","10962","10944","10907","10900","10892","10710","10697","10695","10641","10589","10497","10476","10431","10394","10215","10212","9886","9874","9847","9752","9633","9519","9374","9330","9329","9321","9257","9235","9233","9219","9201","9187","9113","9081","9057","9023","8956","8910","8890","8862","8861","8851","8807","8790","8696","8644","8638","8610","8411","8382","8311","8308","8287","8284","8270","8258","8217","8183","8172","8069","8053","7980","7926","7890","7780","7768","7750","7728","7710","7700","7689","7660","7654","7643","7606","7588","7585","7522","7508","7501","7489","7477","7447","7443","7357","7286","7270","7252","7250","7247","7235","7221","7096","7084","7027","6995","6982","6974","6954","6954","6950","6941","6930","6917","6904","6841","6818","6793","6747","6707","6694","6687","6619","6580","6566","6559","6546","6542","6520","6510","6498","6484","6422","6406","6398","6370","6366","6349","6340","6338","6337","6335","6321","6319","6289","6254","6239","6219","6209","6203","6191","6124","6122","6114","6108","6085","6078","6071","6045","6024","6024","6020","5975","5973","5955","5894","5855","5853","5843","5836","5831","5818","5818","5794","5743","5729","5715","5705","5703","5692","5685","5682","5679","5671","5669","5654","5599","5591","5587","5582","5575","5571","5569","5559","5547","5546","5537","5476","5462","5453","5449","5446","5446","5445","5442","5441","5426","5426","5408","5407","5405","5398","5395","5350","5345","5314","5307","5299","5295","5287","5279","5276","5273","5264","5255","5221","5206","5196","5187","5185","5182","5177","5165","5154","5136","5127","5104","5102","5092","5040","5036","5028","5018","4995","4946","4944","4942","4941","4937","4934","4933","4928","4926","4924","4914","4903","4896","4885","4879","4871","4870","4868","4857","4846","4838","4835","4829","4828","4828","4822","4817","4817","4794","4792","4788","4786","4776","4749","4748","4735","4727","4722","4716","4707","4683","4670","4659","4658","4655","4647","4642","4640","4637","4635","4633","4630","4616","4609","4607","4604","4594","4591","4588","4587","4584","4581","4580","4570","4559","4552","4549","4544","4541","4536","4531","4531","4524","4517","4513","4506","4495","4495","4489","4489","4488","4487","4483","4476","4462","4461","4455","4452","4426","4398","4391","4376","4360","4358","4357","4334","4325","4323","4321","4318","4315","4313","4312","4304","4296","4293","4286","4284","4284","4279","4272","4270","4266","4263","4245","4205","4196","4193","4193","4188","4184","4176","4131","4127","4118","4115","4102","4100","4090","4088","4082","4077","4077","4073","4060","4058","4056","4055","4049","4049","4044","4042","4040","4039","4035","4034","4033","4033","4033","4024","4023","4010","4002","4001","3998","3997","3996","3994","3993","3990","3988","3987","3980","3978","3977","3977","3967","3965","3953","3938","3935","3916","3904","3897","3896","3889","3886","3885","3882","3875","3868","3868","3855","3849","3828","3821","3812","3811","3805","3802","3800","3798","3791","3787","3787","3787","3781","3777","3776","3763","3760","3743","3742","3736","3734","3731","3730","3720","3717","3715","3710","3710","3709","3704","3692","3691","3687","3685","3680","3676","3671","3669","3664","3663","3661","3647","3645","3644","3644","3635","3635","3634","3633","3633","3630","3626","3622","3620","3618","3615","3615","3615","3607","3594","3589","3587","3579","3573","3570","3565","3559","3556","3539","3538","3538","3531","3526","3524","3523","3520","3509","3509","3501","3500","3500","3497","3490","3480","3464","3459","3457","3456","3455","3452","3444","3440","3437","3437","3430","3430","3428","3423","3422","3421","3420","3418","3411","3411","3410","3401","3391","3390","3383","3381","3374","3372","3371","3368","3355","3354","3353","3353","3352","3352","3349","3348","3347","3344","3341","3339","3338","3338","3338","3334","3329","3319","3318","3316","3312","3308","3301","3297","3293","3291","3290","3290","3289","3283","3282","3280","3279","3269","3268","3260","3258","3257","3257","3256","3256","3255","3252","3252","3250","3240","3230","3228","3227","3226","3226","3225","3225","3224","3223","3221","3221","3217","3213","3212","3208","3207","3199","3196","3191","3189","3186","3183","3182","3180","3171","3168","3161","3158","3158","3154","1466","1104","974","795","500","155"]

print("Starting")


def printl(label, data):
    print("\n"+label+":")
    print(data)


def jdump(obj):
    # Create a formatted string of the Python JSON object
    return json.dumps(obj, sort_keys=True, indent=4)


def jget(url, log):
    try:
        response = requests.get(url)
    except:
        print("Failed GET request.")
        quit()
    else:
        sc = response.status_code
        if log:
            print(f"Status: {str(sc)}")
        if sc == 200:
            if log:
                print("Result returned successfully.")
            return json.loads(jdump(response.json()))
        elif log:
            if sc == 301:
                print("The server is redirecting you to a different endpoint.")
            elif sc == 400:
                print("The server thinks you made a bad request. Incorrect credentials.")
            elif sc == 401:
                print("The server thinks you’re not authenticated.")
            elif sc == 403:
                print(
                    "The resource you’re trying to access is forbidden. You do not have the right permissions.")
            elif sc == 404:
                print("The resource you tried to access wasn’t found on the server.")
            elif sc == 503:
                print("The server is not ready to handle the request.")
            else:
                print("Unknown error type.")
            quit()


# featured = jget("https://api.scratch.mit.edu/proxy/featured", True)  # Featured
# explore = jget("https://api.scratch.mit.edu/explore/projects?q=games&mode=trending&language=en", True) #Trending explore

# print(response.json())
# print(jdump(response.json()))

header = "User,,,,Average Project Statistics,,,,,,,\nUsername,Followers,Country,Join Date,Views,Loves,Favorites,Remixes,Public,Published,Visible,Commentable\n"
data = header  # format ex: "piano_miles,1000,United States,2018-08-24,1000,200,100,50,1,1,1,1\n"

# https://api.scratch.mit.edu/users/mres/messages/count
# https://api.scratch.mit.edu/users/mres/projects

for K in range(len(follows)):
    print(f"{str(int(1000 * K / len(follows)) / 10)}%")
    username = usernames[K]

    valid = (
        jget(
            f"https://api.scratch.mit.edu/accounts/checkusername/{username}",
            False,
        )["msg"]
        == "username exists"
    )

    if valid:
        user = jget(f"https://api.scratch.mit.edu/users/{username}", False)
        country = user["profile"]["country"]
        joinDate = user["history"]["joined"].split("T")[0]

        sample = jget(f"https://api.scratch.mit.edu/users/{username}/projects", False)

        loves = 0
        favorites = 0
        remixes = 0
        public = 0
        published = 0
        visible = 0
        commentable = 0
        count = 0

        views = 0
        for i in range(len(sample)):
            project = sample[i]

            #title = project["title"]
            #projectID = project["id"]
            views += project["stats"]["views"]
            loves += project["stats"]["loves"]
            favorites += project["stats"]["favorites"]
            remixes += project["stats"]["remixes"]
            #parent = project["remix"]["parent"]
            #root = project["remix"]["root"]
            public += 1 if project["public"] else 0
            published += 1 if project["is_published"] else 0
            visible += 1 if project["visibility"] == "visible" else 0
            #creationDate = project["history"]["created"]
            commentable += 1 if project["comments_allowed"] else 0

            # throw out data not accessable to the public
            if project["public"] and project["is_published"] and project["visibility"] == "visible":
                count += 1

        if count > 0:
            views = str(views/count)
            loves = str(loves/count)
            favorites = str(favorites/count)
            remixes = str(remixes/count)
            public = str(public/count)
            published = str(published/count)
            visible = str(visible/count)
            commentable = str(commentable/count)

            data += (
                f"{username},{follows[K].strip()},{country},{joinDate},{views},{loves},{favorites},{remixes},{public},{published},{visible},{commentable}"
                + "\n"
            )
            # print(data)
            # print(remixes)
            # print(commentable)
            # print(visible)

print("Data collected\nWriting file")
with open("dataset.csv", "w") as f:
    f.write(data)
print("Complete")

        # print(jdump(pass_times))
