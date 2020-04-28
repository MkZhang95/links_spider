from links_spider.modules.mothering import mothering
from links_spider.modules.infowars import infowars
from links_spider.modules.naturalnews import naturalnews
from links_spider.modules.childrenshealthdefense import childrenshealthdefense
from links_spider.modules.activistpost import activistpost
from links_spider.modules.ahrp import ahrp
from links_spider.modules.newstarget import newstarget
from links_spider.modules.truthwiki import truthwiki
from links_spider.modules.vaxtruth import vaxtruth
from links_spider.modules.vactruth import vactruth
from links_spider.modules.vaccines_news import vaccines_news
from links_spider.modules.vaxxter import vaxxter
from links_spider.modules.ageofautism import ageofautism

parsable_domain_list = ['mothering.com','infowars.com','naturalnews.com', 'childrenshealthdefense.org','activistpost.com',
                        'ahrp.org', 'newstarget.com'
                        ,'truthwiki.org','vaxtruth.org','vactruth.com', 'vaccines.news','vaxxter.com','ageofautism.com']
moddules = [mothering, infowars, naturalnews, childrenshealthdefense, activistpost, ahrp, newstarget, truthwiki,vaxtruth,vactruth,
            vaccines_news,vaxxter,ageofautism]