pip3 install scrapy  
pip3 install beautifulsoup4  
scrapy genspider yeyinfu "bilibili.com"
scrapy scraw yeyinfu  
python3 countJ4.py  

bs抓到的script内容，这里面的东西都可以用re筛出来
```
<script>window.__INITIAL_STATE__={"aid":78560319,"bvid":"BV1vJ411v7ev","p":"","videoData":{"bvid":"BV1vJ411v7ev","aid":78560319,"videos":12,"tid":171,"tname":"电子竞技","copyright":1,"pic":"http:\u002F\u002Fi1.hdslb.com\u002Fbfs\u002Farchive\u002Fee441418d23df987d484006bef35e883eddb2d03.jpg","title":"【叶音符直播】皇子蜘蛛螳螂男枪 奥拉夫梦魇龙龟龙女 12.07 周六","pubdate":1575812771,"ctime":1575812771,"desc":"叶音符直播 douyu.com\u002F12313\n主玩打野，每晚18点到24点","state":0,"attribute":16512,"duration":20131,"rights":{"bp":0,"elec":0,"download":1,"movie":0,"pay":0,"hd5":0,"no_reprint":1,"autoplay":1,"ugc_pay":0,"is_cooperation":0,"ugc_pay_preview":0,"no_background":0},"owner":{"mid":9954236,"name":"叶音符工作室","face":"http:\u002F\u002Fi2.hdslb.com\u002Fbfs\u002Fface\u002F8c813220291e0303c71c5dda3c664eb4435eaeba.jpg"},"stat":{"aid":78560319,"view":"--","danmaku":"--","reply":38,"favorite":"--","coin":"--","share":"--","now_rank":0,"his_rank":0,"like":"--","dislike":0,"evaluation":"","viewseo":13142},"dynamic":"#LOL##英雄联盟##叶音符#","cid":134407712,"dimension":{"width":2560,"height":1440,"rotate":0},"no_cache":false,"pages":[{"cid":134407712,"page":1,"from":"vupload","part":"1皇子vs凯隐20-8","duration":2066,"vid":"","weblink":"","dimension":{"width":2560,"height":1440,"rotate":0}},{"cid":134409533,"page":2,"from":"vupload","part":"2龙女vs龙龟15-2","duration":2011,"vid":"","weblink":"","dimension":{"width":2560,"height":1440,"rotate":0}},{"cid":134410807,"page":3,"from":"vupload","part":"3龙龟vs瞎子13-2","duration":2273,"vid":"","weblink":"","dimension":{"width":2560,"height":1440,"rotate":0}},{"cid":134412288,"page":4,"from":"vupload","part":"4梦魇vs瞎子8-0","duration":1090,"vid":"","weblink":"","dimension":{"width":1920,"height":1080,"rotate":0}},{"cid":134412615,"page":5,"from":"vupload","part":"5螳螂vs人马4-4","duration":1475,"vid":"","weblink":"","dimension":{"width":1920,"height":1080,"rotate":0}},{"cid":134413220,"page":6,"from":"vupload","part":"6皇子vs蜘蛛29-4","duration":1850,"vid":"","weblink":"","dimension":{"width":1920,"height":1080,"rotate":0}},{"cid":134413678,"page":7,"from":"vupload","part":"7奥拉夫vs男枪17-3","duration":1970,"vid":"","weblink":"","dimension":{"width":1920,"height":1080,"rotate":0}},{"cid":134414494,"page":8,"from":"vupload","part":"8男枪vs瞎子14-4","duration":1605,"vid":"","weblink":"","dimension":{"width":1920,"height":1080,"rotate":0}},{"cid":134415221,"page":9,"from":"vupload","part":"9皇子vs酒桶20-1","duration":1541,"vid":"","weblink":"","dimension":{"width":1920,"height":1080,"rotate":0}},{"cid":134415718,"page":10,"from":"vupload","part":"10螳螂vs瞎子31-1","duration":1484,"vid":"","weblink":"","dimension":{"width":1920,"height":1080,"rotate":0}},{"cid":134416133,"page":11,"from":"vupload","part":"11蜘蛛vs瞎子18-2","duration":1481,"vid":"","weblink":"","dimension":{"width":1920,"height":1080,"rotate":0}},{"cid":134416522,"page":12,"from":"vupload","part":"12皇子vs螳螂5-2","duration":1285,"vid":"","weblink":"","dimension":{"width":1920,"height":1080,"rotate":0}}],"subtitle":{"allow_submit":false,"list":[]},"embedPlayer":"EmbedPlayer(\"player\", \"\u002F\u002Fs1.hdslb.com\u002Fbfs\u002Fstatic\u002Fplayer\u002Fmain\u002Fflash\u002Fplay.swf\", \"cid=134407712&aid=78560319&attribute=16512&bvid=BV1vJ411v7ev&show_bv=1\")"},"upData":{"mid":"9954236","name":"叶音符工作室","approve":false,"sex":"保密","rank":"10000","face":"http:\u002F\u002Fi2.hdslb.com\u002Fbfs\u002Fface\u002F8c813220291e0303c71c5dda3c664eb4435eaeba.jpg","DisplayRank":"0","regtime":0,"spacesta":0,"birthday":"","place":"","description":"","article":0,"attentions":[],"fans":79486,"friend":91,"attention":91,"sign":"斗鱼房间号12313，主玩打野，每晚18点到24点，微博：lol叶音符","level_info":{"current_level":6,"current_min":0,"current_exp":0,"next_exp":0},"pendant":{"pid":0,"name":"","image":"","expire":0},"nameplate":{"nid":8,"name":"知名偶像","image":"http:\u002F\u002Fi1.hdslb.com\u002Fbfs\u002Fface\u002F27a952195555e64508310e366b3e38bd4cd143fc.png","image_small":"http:\u002F\u002Fi0.hdslb.com\u002Fbfs\u002Fface\u002F0497be49e08357bf05bca56e33a0637a273a7610.png","level":"稀有勋章","condition":"所有自制视频总播放数\u003E=100万"},"Official":{"role":0,"title":"","desc":"","type":-1},"official_verify":{"type":-1,"desc":""},"vip":{"vipType":2,"dueRemark":"","accessStatus":0,"vipStatus":1,"vipStatusWarn":"","theme_type":0},"archiveCount":890},"staffData":[],"tags":[{"tag_id":62526,"tag_name":"电子竞技","cover":"http:\u002F\u002Fi0.hdslb.com\u002Fbfs\u002Farchive\u002Fa2a72561d08920a244b789b76ebf09c40028e661.jpg","head_cover":"http:\u002F\u002Fi0.hdslb.com\u002Fbfs\u002Farchive\u002F6b9942efbef31dd77ed49c492af34a32950efbcf.png","content":"电子竞技（Electronic Sports）就是电子游戏比赛达到“竞技”层面的体育项目。","short_content":"","type":3,"state":0,"ctime":1436866637,"count":{"view":0,"use":2539811,"atten":107337},"is_atten":0,"likes":0,"hates":0,"attribute":0,"liked":0,"hated":0,"showDetail":false,"showReport":false,"timeOut":null},{"tag_id":9222,"tag_name":"英雄联盟","cover":"http:\u002F\u002Fi0.hdslb.com\u002Fbfs\u002Farchive\u002F75b405de75271b729b0fb18f552b6b76c7b7725b.jpg","head_cover":"http:\u002F\u002Fi0.hdslb.com\u002Fbfs\u002Farchive\u002Fe57a622f470c03db553091fdb4fb8f2e850ec30a.jpg","content":"《英雄联盟》是由美国Riot Games开发的3D大型竞技场战网游戏，让玩家感受全新的英雄对战。","short_content":"英雄，志逐传奇！","type":3,"state":0,"ctime":1436866637,"count":{"view":0,"use":1396189,"atten":1235942},"is_atten":0,"likes":0,"hates":0,"attribute":0,"liked":0,"hated":0,"showDetail":false,"showReport":false,"timeOut":null},{"tag_id":3093,"tag_name":"LOL","cover":"","head_cover":"","content":"","short_content":"","type":3,"state":0,"ctime":1436866637,"count":{"view":0,"use":812310,"atten":49729},"is_atten":0,"likes":0,"hates":0,"attribute":0,"liked":0,"hated":0,"showDetail":false,"showReport":false,"timeOut":null},{"tag_id":3221,"tag_name":"娱乐","cover":"","head_cover":"","content":"","short_content":"","type":3,"state":0,"ctime":1436866637,"count":{"view":0,"use":2552298,"atten":119216},"is_atten":0,"likes":0,"hates":0,"attribute":0,"liked":0,"hated":0,"showDetail":false,"showReport":false,"timeOut":null},{"tag_id":66406,"tag_name":"精彩集锦","cover":"","head_cover":"","content":"","short_content":"","type":3,"state":0,"ctime":1436866637,"count":{"view":0,"use":497101,"atten":62984},"is_atten":0,"likes":0,"hates":0,"attribute":0,"liked":0,"hated":0,"showDetail":false,"showReport":false,"timeOut":null},{"tag_id":108165,"tag_name":"打野","cover":"","head_cover":"","content":"","short_content":"","type":0,"state":0,"ctime":1436866637,"count":{"view":0,"use":37398,"atten":297},"is_atten":0,"likes":0,"hates":0,"attribute":0,"liked":0,"hated":0,"showDetail":false,"showReport":false,"timeOut":null},{"tag_id":455863,"tag_name":"斗鱼","cover":"","head_cover":"","content":"","short_content":"","type":0,"state":0,"ctime":1436866637,"count":{"view":0,"use":83463,"atten":944},"is_atten":0,"likes":0,"hates":0,"attribute":0,"liked":0,"hated":0,"showDetail":false,"showReport":false,"timeOut":null},{"tag_id":44567,"tag_name":"叶师傅","cover":"","head_cover":"","content":"","short_content":"","type":0,"state":0,"ctime":1436866637,"count":{"view":0,"use":853,"atten":40},"is_atten":0,"likes":0,"hates":0,"attribute":0,"liked":0,"hated":0,"showDetail":false,"showReport":false,"timeOut":null},{"tag_id":1393843,"tag_name":"叶音符","cover":"","head_cover":"","content":"","short_content":"","type":0,"state":0,"ctime":1444714695,"count":{"view":0,"use":1707,"atten":79},"is_atten":0,"likes":0,"hates":0,"attribute":0,"liked":0,"hated":0,"showDetail":false,"showReport":false,"timeOut":null},{"tag_id":2475790,"tag_name":"国服第一皇子","cover":"","head_cover":"","content":"","short_content":"","type":0,"state":0,"ctime":1470639318,"count":{"view":0,"use":461,"atten":2},"is_atten":0,"likes":0,"hates":0,"attribute":0,"liked":0,"hated":0,"showDetail":false,"showReport":false,"timeOut":null}],"comment":{"count":38,"list":["主播是叫叶灿么","我是第一个投币的[doge]","录男别更新这么快，mm怕"]},"related":[{"aid":56661074,"cid":98989257,"bvid":"BV1Hx411o7bH","duration":437,"pic":"http:\u002F\u002Fi2.hdslb.com\u002Fbfs\u002Farchive\u002F156bce805ce9e173561446cd8768ade505d911b5.jpg","title":"「叶音符」23杀千伤泰坦！真就一键秒人这么方便？","owner":{"name":"音符木木","mid":431443083},"stat":{"danmaku":180,"view":51580}},{"aid":40606981,"cid":71316283,"bvid":"BV1zt411W7Dq","duration":23413,"pic":"http:\u002F\u002Fi0.hdslb.com\u002Fbfs\u002Farchive\u002Fc90fec55420e7494e3b05a6e642ba7e1629ed1b5.png","title":"【叶音符】残血反身杀三个，阿木木是你能追的？ 01.12周六","owner":{"name":"叶音符工作室","mid":9954236},"stat":{"danmaku":179,"view":14411}},{"aid":73376312,"cid":125518928,"bvid":"BV1YE41117Yi","duration":665,"pic":"http:\u002F\u002Fi0.hdslb.com\u002Fbfs\u002Farchive\u002Fe685a4604fe19a347de92a61b2e03726ee47554f.jpg","title":"叶音符：说出来你可能不信，这英雄刷野比木木蜘蛛还快，伤害不是一个量级","owner":{"name":"叶音符工作室","mid":9954236},"stat":{"danmaku":186,"view":53969}},{"aid":91249299,"cid":155747330,"bvid":"BV1Y7411M7km","duration":22395,"pic":"http:\u002F\u002Fi2.hdslb.com\u002Fbfs\u002Farchive\u002F48818b31d9ed3bdbfade74a4e9384a71ac36ecd6.jpg","title":"【叶音符直播】岩雀人马蜘蛛皇子 艾克螳螂龙女奥拉夫 02.23周日","owner":{"name":"叶音符工作室","mid":9954236},"stat":{"danmaku":234,"view":13866}},{"aid":62863035,"cid":109207743,"bvid":"BV1Nt411K7uw","duration":549,"pic":"http:\u002F\u002Fi1.hdslb.com\u002Fbfs\u002Farchive\u002F471457a94aa1cfb12bf725a35c9325dcfe8b6552.jpg","title":"叶音符：这把打完分手吧？搞不懂你们这些七夕顶着情侣id双排的人，给你们安排安排","owner":{"name":"叶音符工作室","mid":9954236},"stat":{"danmaku":213,"view":31343}},{"aid":76545863,"cid":130934409,"bvid":"BV1vJ41127mS","duration":746,"pic":"http:\u002F\u002Fi0.hdslb.com\u002Fbfs\u002Farchive\u002F69c8d6ebc18f360aa5357383411f94b879bec61c.jpg","title":"叶音符：螳螂孤立无援Q不加伤害？你这个问题就像在跟一个厨子说扬州炒饭不加米饭一样","owner":{"name":"叶音符工作室","mid":9954236},"stat":{"danmaku":203,"view":27480}},{"aid":60785249,"cid":105783794,"bvid":"BV1dt411j7fM","duration":615,"pic":"http:\u002F\u002Fi0.hdslb.com\u002Fbfs\u002Farchive\u002Ff45edbd50cc3540b260be67358e12fe7844ef3fa.jpg","title":"叶音符：20秒一个R，一个R瞬间融化AD，这个英雄发育起来简直无解","owner":{"name":"叶音符工作室","mid":9954236},"stat":{"danmaku":239,"view":32041}},{"aid":56984040,"cid":99581787,"bvid":"BV1nx411d7ga","duration":492,"pic":"http:\u002F\u002Fi2.hdslb.com\u002Fbfs\u002Farchive\u002Fe025ff9dc8ff8f0bf272b1ee62bec4df13381e96.jpg","title":"「叶音符」23杀食肉阿木木！高伤捆绑一Q一个准！","owner":{"name":"音符木木","mid":431443083},"stat":{"danmaku":54,"view":9241}},{"aid":88579547,"cid":151311009,"bvid":"BV1D7411V7M9","duration":28301,"pic":"http:\u002F\u002Fi2.hdslb.com\u002Fbfs\u002Farchive\u002F48818b31d9ed3bdbfade74a4e9384a71ac36ecd6.jpg","title":"【叶音符直播】皇子专场+酒桶龙女木木奥拉夫 02.12周三","owner":{"name":"叶音符工作室","mid":9954236},"stat":{"danmaku":334,"view":13460}},{"aid":80778099,"cid":138250760,"bvid":"BV1YJ411Y7Hd","duration":418,"pic":"http:\u002F\u002Fi2.hdslb.com\u002Fbfs\u002Farchive\u002F76a8971d9c8ce213e89c604db7841e706dbf46bf.jpg","title":"叶音符：你们放心，目前还没有加强ad的任何消息放出，除了ad都有加强^^","owner":{"name":"叶音符工作室","mid":9954236},"stat":{"danmaku":118,"view":58392}},{"aid":80164355,"cid":137181104,"bvid":"BV1kJ41147hM","duration":18573,"pic":"http:\u002F\u002Fi1.hdslb.com\u002Fbfs\u002Farchive\u002Fee441418d23df987d484006bef35e883eddb2d03.jpg","title":"【叶音符直播】龙女奥拉夫男枪皇子 末日蒙多螳螂 12.21 周六","owner":{"name":"叶音符工作室","mid":9954236},"stat":{"danmaku":216,"view":14947}},{"aid":93517741,"cid":159660245,"bvid":"BV1rE41147Tj","duration":24202,"pic":"http:\u002F\u002Fi1.hdslb.com\u002Fbfs\u002Farchive\u002F3813423273164375aa7405d9ca01f362d63d9b1f.jpg","title":"【叶音符直播】人马老鼠皇子男枪 龙女酒桶螳螂 03.03周二","owner":{"name":"叶音符工作室","mid":9954236},"stat":{"danmaku":341,"view":16594}},{"aid":80024074,"cid":136952703,"bvid":"BV1FJ41147se","duration":13492,"pic":"http:\u002F\u002Fi1.hdslb.com\u002Fbfs\u002Farchive\u002Fee441418d23df987d484006bef35e883eddb2d03.jpg","title":"【叶音符直播】皇子螳螂男枪 蔚龙女酒桶 12.20 周五","owner":{"name":"叶音符工作室","mid":9954236},"stat":{"danmaku":208,"view":12439}},{"aid":77015301,"cid":131728718,"bvid":"BV1YJ411R74w","duration":892,"pic":"http:\u002F\u002Fi1.hdslb.com\u002Fbfs\u002Farchive\u002F18a8c244869c4140500e0f162229fcd69dc75b91.jpg","title":"叶音符：二拖三，五杀四杀拿不停，32杀螳螂带领全队绝境翻盘，服！","owner":{"name":"叶音符工作室","mid":9954236},"stat":{"danmaku":255,"view":29235}},{"aid":63609742,"cid":110451172,"bvid":"BV1N4411D7Yx","duration":530,"pic":"http:\u002F\u002Fi1.hdslb.com\u002Fbfs\u002Farchive\u002Fe05a2c3daa9a6a49339330e45acb26ea89439008.jpg","title":"叶音符：20分钟775的射程你们见过没？这英雄顺风随便一打五","owner":{"name":"叶音符工作室","mid":9954236},"stat":{"danmaku":145,"view":40733}},{"aid":57855941,"cid":100971962,"bvid":"BV174411A7zK","duration":543,"pic":"http:\u002F\u002Fi2.hdslb.com\u002Fbfs\u002Farchive\u002Fae3d75ee64d5a26ef249265a7a890866b78294ec.png","title":"神超AP龙女把对面和队友都看呆了 诺手：鬼一样  什么鬼伤害?","owner":{"name":"积极向上的十二","mid":361840091},"stat":{"danmaku":528,"view":214990}},{"aid":94792906,"cid":161814400,"bvid":"BV1cE411u75f","duration":17992,"pic":"http:\u002F\u002Fi1.hdslb.com\u002Fbfs\u002Farchive\u002F3813423273164375aa7405d9ca01f362d63d9b1f.jpg","title":"【叶音符直播】中单卡萨丁 艾克狗熊龙女盖伦奥拉夫 皇子酒桶蜘蛛螳螂男枪 03.08周日","owner":{"name":"叶音符工作室","mid":9954236},"stat":{"danmaku":266,"view":17503}},{"aid":84196244,"cid":144012287,"bvid":"BV1p7411v7x2","duration":21664,"pic":"http:\u002F\u002Fi1.hdslb.com\u002Fbfs\u002Farchive\u002F0eb7be31312aaccdbb5cb8610f587ded120fb17f.jpg","title":"【叶音符直播】腕豪皇子酒桶老鼠 龙女螳螂男枪 01.19周日","owner":{"name":"叶音符工作室","mid":9954236},"stat":{"danmaku":379,"view":20422}},{"aid":51491879,"cid":90126689,"bvid":"BV1H4411i7Hm","duration":640,"pic":"http:\u002F\u002Fi2.hdslb.com\u002Fbfs\u002Farchive\u002F0eb86946536ff8dbc125b166d8163f7c95f9e80a.jpg","title":"最新版本野区刷野路线教学，永远比对面快一步，看到就是赚到","owner":{"name":"叶音符工作室","mid":9954236},"stat":{"danmaku":543,"view":120238}},{"aid":89785527,"cid":153343536,"bvid":"BV1H741177AE","duration":26209,"pic":"http:\u002F\u002Fi2.hdslb.com\u002Fbfs\u002Farchive\u002F48818b31d9ed3bdbfade74a4e9384a71ac36ecd6.jpg","title":"【叶音符直播】艾克皇子龙女梦魇凯隐 酒桶木木蜘蛛螳螂+挖石油 02.17周一","owner":{"name":"叶音符工作室","mid":9954236},"stat":{"danmaku":255,"view":14529}},{"aid":80926642,"cid":138509432,"bvid":"BV1MJ411e7Me","duration":18663,"pic":"http:\u002F\u002Fi1.hdslb.com\u002Fbfs\u002Farchive\u002Fee441418d23df987d484006bef35e883eddb2d03.jpg","title":"【叶音符直播】中单拉克丝卡萨丁龙女皇子老鼠 螳螂奥拉夫狮子狗男枪 12.27周五","owner":{"name":"叶音符工作室","mid":9954236},"stat":{"danmaku":235,"view":14318}},{"aid":78513808,"cid":134337932,"bvid":"BV1HJ411v79L","duration":394,"pic":"http:\u002F\u002Fi1.hdslb.com\u002Fbfs\u002Farchive\u002F4bbdbd402c6199d02eb433e31d9ba0c34b1cf48c.jpg","title":"【黑店百地】男枪上单打的过谁？都是你爸爸!","owner":{"name":"黑店百地的小本本_","mid":59903834},"stat":{"danmaku":245,"view":154645}},{"aid":92460050,"cid":157866573,"bvid":"BV1LE411H72J","duration":21334,"pic":"http:\u002F\u002Fi1.hdslb.com\u002Fbfs\u002Farchive\u002F3813423273164375aa7405d9ca01f362d63d9b1f.jpg","title":"【叶音符直播】盖伦劫男刀男枪 皇子老鼠螳螂 02.28周五","owner":{"name":"叶音符工作室","mid":9954236},"stat":{"danmaku":430,"view":19502}},{"aid":87697913,"cid":149831445,"bvid":"BV1M7411b7BS","duration":283,"pic":"http:\u002F\u002Fi2.hdslb.com\u002Fbfs\u002Farchive\u002F9e8e14626e8d1f50fd93849eaca8f04f4eb234d8.png","title":"移速龙龟","owner":{"name":"移速猫猫","mid":276193816},"stat":{"danmaku":1250,"view":604790}},{"aid":77284131,"cid":132196375,"bvid":"BV1NJ41197fg","duration":985,"pic":"http:\u002F\u002Fi2.hdslb.com\u002Fbfs\u002Farchive\u002F11bc46d3154bb5894b1dc97c284910e3dced7f07.jpg","title":"超神解说：狂战士奥拉夫，秒叠10层征服者，S10最强打野","owner":{"name":"lol超神解说lol","mid":384631356},"stat":{"danmaku":207,"view":65180}},{"aid":78161263,"cid":133734590,"bvid":"BV15J411i7fC","duration":1188,"pic":"http:\u002F\u002Fi0.hdslb.com\u002Fbfs\u002Farchive\u002Fe41e12c0c6d1d75d9489f1a3420bc0c8074c3592.jpg","title":"「叶音符」极速风火轮，千甲铁王八！","owner":{"name":"音符木木","mid":431443083},"stat":{"danmaku":476,"view":20342}},{"aid":55226906,"cid":96567568,"bvid":"BV1M4411K7RL","duration":18291,"pic":"http:\u002F\u002Fi0.hdslb.com\u002Fbfs\u002Farchive\u002F421052fbd816d171e5e194c99bcf0905a9559abf.jpg","title":"【叶音符直播】狼人剑魔凯隐皇子 EZ木木酒桶 06.10 周一","owner":{"name":"叶音符工作室","mid":9954236},"stat":{"danmaku":251,"view":16089}},{"aid":78614242,"cid":134508328,"bvid":"BV1QJ411v78a","duration":549,"pic":"http:\u002F\u002Fi2.hdslb.com\u002Fbfs\u002Farchive\u002Fe2f934b84b277f035fce2009a7a1c58d67c8d239.jpg","title":"叶音符打野龙女写意收四杀，教对面皇子怎么打野","owner":{"name":"我寻思我也不胖啊","mid":162709001},"stat":{"danmaku":6,"view":1938}},{"aid":79904185,"cid":136750804,"bvid":"BV1wJ411b7CK","duration":19463,"pic":"http:\u002F\u002Fi1.hdslb.com\u002Fbfs\u002Farchive\u002Fee441418d23df987d484006bef35e883eddb2d03.jpg","title":"【叶音符直播】蜘蛛奥拉夫螳螂皇子 狮子狗龙女蒙多 12.19 周四","owner":{"name":"叶音符工作室","mid":9954236},"stat":{"danmaku":156,"view":13589}},{"aid":83329071,"cid":142546779,"bvid":"BV14J411H7Az","duration":17520,"pic":"http:\u002F\u002Fi1.hdslb.com\u002Fbfs\u002Farchive\u002F0eb7be31312aaccdbb5cb8610f587ded120fb17f.jpg","title":"【叶音符直播】皇子艾克男枪 酒桶螳螂龙女 1.13周一","owner":{"name":"叶音符工作室","mid":9954236},"stat":{"danmaku":177,"view":13255}},{"aid":77127643,"cid":131925475,"bvid":"BV1LJ411X78C","duration":592,"pic":"http:\u002F\u002Fi2.hdslb.com\u002Fbfs\u002Farchive\u002F2ede7e2dabea844c2caff383b88bc32fbe426e3c.jpg","title":"叶音符：油头叶灿，在线battle，700法强阿木木连续三回合击败刀妹，心态爆炸","owner":{"name":"叶音符工作室","mid":9954236},"stat":{"danmaku":167,"view":18781}},{"aid":94274197,"cid":160934911,"bvid":"BV16E411p72j","duration":25962,"pic":"http:\u002F\u002Fi1.hdslb.com\u002Fbfs\u002Farchive\u002F3813423273164375aa7405d9ca01f362d63d9b1f.jpg","title":"【叶音符直播】凯隐人马提莫盖伦老鼠 皇子男枪酒桶螳螂 03.06周五","owner":{"name":"叶音符工作室","mid":9954236},"stat":{"danmaku":246,"view":10502}},{"aid":77764170,"cid":133036174,"bvid":"BV1vJ411z7zV","duration":20437,"pic":"http:\u002F\u002Fi1.hdslb.com\u002Fbfs\u002Farchive\u002Fee441418d23df987d484006bef35e883eddb2d03.jpg","title":"【叶音符直播】皇子奥拉夫螳螂千珏 火男男枪蜘蛛酒桶龙女 12.1 周日","owner":{"name":"叶音符工作室","mid":9954236},"stat":{"danmaku":399,"view":20712}}],"isClient":false,"error":{},"player":"","playurl":{},"user":{},"cidMap":{},"insertScripts":["\u002F\u002Fs1.hdslb.com\u002Fbfs\u002Fstatic\u002Fjinkela\u002Fvideo\u002Fstardust-video.bbdf0c46e45670bd8288b7b3c84b076e6290abaf.js"],"BILI_CONFIG":{"show_bv":true}}
```
