from links_spider.modules.mothering import mothering
from links_spider.modules.infowars import infowars
from links_spider.modules.naturalnews import naturalnews
from links_spider.modules.childrenshealthdefense import childrenshealthdefense
from links_spider.modules.activistpost import activistpost
from links_spider.modules.ahrp import ahrp
from links_spider.modules.newstarget import newstarget

parsable_domain_list = ['mothering.com','infowars.com','naturalnews.com', 'childrenshealthdefense.org','activistpost.com', 'ahrp.org', 'newstarget.com']
moddules = [mothering, infowars, naturalnews, childrenshealthdefense, activistpost, ahrp, newstarget]