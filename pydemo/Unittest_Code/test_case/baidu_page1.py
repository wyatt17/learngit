from poium import Page, Element

# 继承poium的Page类
class BaiduPage1(Page):
    
    search_input = Element(id_ = "kw")
    search_button = Element(id_ = "su")