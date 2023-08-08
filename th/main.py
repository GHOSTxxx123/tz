import time
from kivymd.toast import toast
import os
from kivy.utils import platform
from kivy.metrics import dp
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.config import ConfigParser as Conf_1
from configparser import ConfigParser as Conf_2
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.navigationdrawer import *
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.button import *
from kivymd.uix.textfield import *
from kivymd.uix.label import *
from kivymd.uix.filemanager import *
from kivymd.uix.card import *
from kivymd.uix.textfield import *
from kivymd.uix.relativelayout import *
from kivy.uix.image import *
from kivymd.uix.scrollview import *
from kivymd.uix.gridlayout import *
from kivymd.uix.selection import *
from kivymd.uix.swiper import *
from kivy.utils import get_color_from_hex
from kivy.uix.camera import Camera
from kivy.properties import StringProperty
from requests_toolbelt import MultipartEncoder
import requests



Window.size = (375, 812)

class Card_Birds_add_db(MDCard):
    text = StringProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.padding = 4
        self.size_hint = (None, None)
        self.size = ("200dp", "350dp")
        self.style = "elevated"
        self.line_color = (0.2, 0.2, 0.2, 0.8)
        self.md_bg_color = "#f6eeee"
        self.shadow_offset = (0, -1)

        self.box = MDRelativeLayout()

        self.image_birds = AsyncImage() 
        self.image_birds.source = "https://i.pinimg.com/originals/a7/c4/37/a7c4372192f763ed3245ceb52a8dea26.jpg"
        #"https://itsourcecode.com/wp-content/uploads/2021/02/Python-Books-for-Beginners-and-Advanced.png"
        #"https://i.pinimg.com/originals/a7/c4/37/a7c4372192f763ed3245ceb52a8dea26.jpg" 
        #'http://fotorelax.ru/wp-content/uploads/2017/03/Mesmerizing-nature-photography-by-Eric-Bunting-24.jpg'
        self.image_birds.size_hint = (1, None)
        self.image_birds.size = (1, 250)
        self.image_birds.pos_hint = {'top':1.07}
        self.image_birds.opacity = .4

        self.lbl_name = MDLabel()
        self.lbl_name.text = "Name birds"
        self.lbl_name.adaptive_size = True
        self.lbl_name.font_size = 35
        self.lbl_name.color = "grey"
        self.lbl_name.pos_hint = {'center_x':.5, 'center_y':.5}
        self.lbl_name.bold = True

        self.lbl_color_feather = MDLabel()
        self.lbl_color_feather.text = "Color feather"
        self.lbl_color_feather.adaptive_size = True
        self.lbl_color_feather.font_size = 25
        self.lbl_color_feather.color = 'grey'
        self.lbl_color_feather.pos_hint = {'center_x':.5, 'center_y':.3}
        self.lbl_color_feather.bold = True

        self.lbl_time = MDLabel()
        self.lbl_time.text = "time on public"
        self.lbl_time.adaptive_size = True
        self.lbl_time.color = 'grey'
        self.lbl_time.font_size = 16
        self.lbl_time.pos_hint = {'right':1}
        self.lbl_time.bold = True

        self.box.add_widget(self.image_birds)
        self.box.add_widget(self.lbl_time)
        self.box.add_widget(self.lbl_color_feather)
        self.box.add_widget(self.lbl_name)
        self.add_widget(self.box)

class BaseNavigationDrawerItem(MDNavigationDrawerItem):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.radius = 24
        self.text_color = "#4a4939"
        self.icon_color = "#4a4939"
        self.focus_color = "green"


class DrawerClickableItem(BaseNavigationDrawerItem):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ripple_color = "#c5bdd2"
        self.selected_color = "#0c6c4d"

class ContentNavigationDrawer(MDNavigationLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.toolbar = MDTopAppBar()
        #self.toolbar.elevation=4
        self.toolbar.size_hint = (.1, .1)
        self.toolbar.radius = (25, 25, 25, 25)
        self.toolbar.pos_hint={"top":.98, 'center_x':.08}
        self.toolbar.md_bg_color = "#bbbbf00"
        self.toolbar.shadow_color = '#ffffff'
        self.toolbar.specific_text_color="green"
        self.toolbar.left_action_items=[['menu', lambda x: self.nav_drawer_open()]]      

        self.navigdraw = MDNavigationDrawer()
        self.navigdraw.id="nav_drawer"
        self.navigdraw.radius=(0, 16, 16, 0)

        self.navig_menu = MDNavigationDrawerMenu()

        self.navig_draw_manu_header = MDNavigationDrawerHeader()
        self.navig_draw_manu_header.title="Птицы"
        self.navig_draw_manu_header.title_color="#4a4939"
        self.navig_draw_manu_header.spacing="4dp"
        self.navig_draw_manu_header.padding=("12dp", 0, 0, "12dp")

        self.line_header = MDNavigationDrawerDivider()

        self.service = MDNavigationDrawerLabel()
        self.service.text = 'Сервисы'

        self.service_0 = DrawerClickableItem()
        self.service_0.icon="card-bulleted"
        self.service_0.text_right_color="#4a4939"
        self.service_0.text="Список птиц"
        self.service_0.on_release = self.func_ser_0_news

        self.service_1 = DrawerClickableItem()
        self.service_1.icon="card-search"
        self.service_1.text_right_color="#4a4939"
        self.service_1.text="Карточка птицы"
        self.service_1.on_release = self.func_ser_1_lib

        self.service_2 = DrawerClickableItem()
        self.service_2.icon="card-plus"
        self.service_2.text_right_color="#4a4939"
        self.service_2.text="Создание новой птицы"
        self.service_2.on_release = self.func_ser_2_sto

        self.service_3 = DrawerClickableItem()
        self.service_3.icon="history"
        self.service_3.text_right_color="#4a4939"
        self.service_3.text="Птицы которых я видел"
        self.service_3.on_release = self.func_ser_3_pre


        self.navig_menu.add_widget(self.navig_draw_manu_header)
        self.navig_menu.add_widget(self.line_header)
        self.navig_menu.add_widget(self.service)
        self.navig_menu.add_widget(self.service_0)
        self.navig_menu.add_widget(self.service_1)
        self.navig_menu.add_widget(self.service_2)
        self.navig_menu.add_widget(self.service_3)


        self.navigdraw.add_widget(self.navig_menu)


        self.add_widget(self.toolbar)
        self.add_widget(self.navigdraw)

    def nav_drawer_open(self, *args):
        self.navigdraw.set_state("open")

    def func_ser_0_news(self):
        sm.sm.current = 'birds-list'

    def func_ser_1_lib(self):
        sm.sm.current = 'search-birds'

    def func_ser_2_sto(self):
        sm.sm.current = 'add-birds'

    def func_ser_3_pre(self):
        sm.sm.current = 'histori'


class Birds_list(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def on_enter(self, *args):
        
        self.box = MDFloatLayout()

        self.scroll = MDScrollView()
        self.scroll.do_scroll_x = False
        self.scroll.bar_color = '#008000'
        self.scroll.size_hint = (None, None)
        self.scroll.size = ("250dp", "740dp")
        self.scroll.pos_hint = {"center_y":.45, 'center_x':.56}

        self.card_layout = MDGridLayout()
        self.card_layout.cols = 1
        self.card_layout.col_force_default = False
        self.card_layout.adaptive_height = True
        self.card_layout.padding = 10 
        self.card_layout.spacing = 50
        self.card_layout.pos_hint = {"center_y":.5, 'center_x':.5}

        self.navbar = ContentNavigationDrawer()
        
        try:

            m = MultipartEncoder(fields={'token':'Я-Хочу-У-Вас-Работать'})
            r = requests.post('http://localhost:8000/Birds/Card/', data=m, headers={'Content-Type': m.content_type})

            for i in r.json():
        
                try:
                    self.card = Card_Birds_add_db()
                    self.card.pos_hint = {'center_y':.5, 'center_x':.5}

                    self.card.lbl_name.text = i['name']
                    self.card.lbl_color_feather.text = i['color_feather']
                    self.card.lbl_time.text = i['created_at']
                    self.card.image_birds.source = f"http://localhost:8000/uploads/cover/{i['cover']}"

                    self.card_layout.add_widget(self.card)
                except:
                    toast("Карты прицы не созданы", duration=1.5)
        except:
            toast("Подключение не установлено", duration=1.5)

        self.scroll.add_widget(self.card_layout)

        self.box.add_widget(self.scroll)
        self.box.add_widget(self.navbar)
        self.add_widget(self.box)

    def on_leave(self, *args):
        self.clear_widgets()

    def card_func(self):
        print(self.card.lbl_name.text)

class Search_birds(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def on_enter(self, *args):
        
        self.box = MDFloatLayout()

        self.scroll = MDScrollView()
        self.scroll.do_scroll_x = False
        self.scroll.size_hint = (None, None)
        self.scroll.size = ("250dp", "740dp")
        self.scroll.pos_hint = {"center_y":.4, 'center_x':.56}

        self.card_layout = MDGridLayout()
        self.card_layout.cols = 1
        self.card_layout.col_force_default = False
        #self.card_layout.size_hint = (None, None)
        #self.card_layout.size = ("250dp", "400dp")
        self.card_layout.adaptive_height = True
        self.card_layout.padding = 10 
        self.card_layout.spacing = 50
        self.card_layout.pos_hint = {"center_y":.5, 'center_x':.5}

        self.navbar = ContentNavigationDrawer()

        self.search = MDTextField()
        self.search.hint_text_color_focus = '#008000'
        self.search.hint_text = 'Поиск'
        self.search.color_mode = 'custom'
        self.search.line_color_focus = '#008000'
        self.search.radius = (25, 25, 25, 25)
        self.search.mode = "rectangle"
        self.search.font_size = 27
        self.search.size_hint = (.6, .085)
        self.search.pos_hint = {'right':.85, 'top':.98}
        
        try:

            m = MultipartEncoder(fields={'token':'Я-Хочу-У-Вас-Работать'})
            r = requests.post('http://localhost:8000/Birds/Card/', data=m, headers={'Content-Type': m.content_type})

            for i in r.json():
        
                try:
                    self.card = Card_Birds_add_db()
                    self.card.pos_hint = {'center_y':.5, 'center_x':.5} 

                    self.card.lbl_name.text = i['name']
                    self.card.lbl_color_feather.text = i['color_feather']
                    self.card.lbl_time.text = i['created_at']
                    self.card.image_birds.source = f"http://localhost:8000/uploads/cover/{i['cover']}"

                    self.card_layout.add_widget(self.card)
                except:
                    toast("Карты прицы не созданы", duration=1.5)
        except:
            toast("Подключение не установлено", duration=1.5)

        self.scroll.add_widget(self.card_layout)

        self.btn_search = MDIconButton()
        self.btn_search.icon = 'magnify'
        self.btn_search.pos_hint = {'right':1, 'top':.973}
        self.btn_search.on_release = self.func_search

        self.box.add_widget(self.scroll)
        self.box.add_widget(self.btn_search)
        self.box.add_widget(self.search)
        self.box.add_widget(self.navbar)
        self.add_widget(self.box)

    def on_leave(self, *args):
        self.clear_widgets()

    def func_search(self):

        self.card_layout.clear_widgets()

        try:

            m = MultipartEncoder(fields={'token':'Я-Хочу-У-Вас-Работать', 'name':f'{self.search.text}'})
            r = requests.post('http://localhost:8000/Birds/Search/', data=m, headers={'Content-Type': m.content_type})

            for i in r.json():
        
                try:
                    self.card = Card_Birds_add_db()
                    self.card.pos_hint = {'center_y':.5, 'center_x':.5} 

                    self.card.lbl_name.text = i['name']
                    self.card.lbl_color_feather.text = i['color_feather']
                    self.card.lbl_time.text = i['created_at']
                    self.card.image_birds.source = f"http://localhost:8000/uploads/cover/{i['cover']}"

                    self.card_layout.add_widget(self.card)

                    self.card_save_histori(i['id'])


                except:
                    toast("Карты прицы не созданы", duration=1.5)
        except:
            toast("Подключение не установлено", duration=1.5)
        
    def card_save_histori(self, id):
        #print(id)
        m_1 = MultipartEncoder(fields={'token':'Я-Хочу-У-Вас-Работать', 'birds_id':f'{id}'})
        r_1 = requests.post('http://localhost:8000/Histori/', data=m_1, headers={'Content-Type': m_1.content_type})


class Add_birds(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def on_enter(self, *args):
        
        self.name_bir = None

        self.color_fea = None

        self.box = MDFloatLayout()
        #self.box.orientation = "horizontal"

        self.navbar = ContentNavigationDrawer()

        self.name_screen = MDLabel()
        self.name_screen.text = 'Новая птица'
        self.name_screen.font_size = 55
        self.name_screen.pos_hint = {"center_x":.73, "center_y":.94}
        self.name_screen.opacity = .7

        self.name_birds = MDTextField()
        self.name_birds.size_hint_max_x = 300
        self.name_birds.hint_text = 'Название птицы'
        self.name_birds.font_size = 25
        self.name_birds.pos_hint = {'center_x':.5, 'center_y':.65}
        self.name_birds.mode = "fill"
        self.name_birds.line_color_focus = '#008000'
        self.name_birds.text_color_focus = '#008000'
        self.name_birds.hint_text_color_focus = '#008000'
        self.name_birds.opacity = .5

        self.color_feather = MDTextField()
        self.color_feather.size_hint_max_x = 300
        self.color_feather.hint_text = 'Цвет перьев'
        self.color_feather.font_size = 25
        self.color_feather.pos_hint = {'center_x':.5, 'center_y':.55}
        self.color_feather.mode = "fill"
        self.color_feather.line_color_focus = '#008000'
        self.color_feather.text_color_focus = '#008000'
        self.color_feather.hint_text_color_focus = '#008000'
        self.color_feather.opacity = .5

        self.btn_further = MDRaisedButton()
        self.btn_further.text = "Далее"
        self.btn_further.font_size = 25
        self.btn_further.pos_hint = {'center_x':.5, 'center_y':.45}
        self.btn_further.on_release = self.upload

        self.box.add_widget(self.name_screen)
        self.box.add_widget(self.name_birds)
        self.box.add_widget(self.color_feather)
        self.box.add_widget(self.btn_further)
        self.box.add_widget(self.navbar)
        self.add_widget(self.box)

    def on_leave(self, *args):
        self.clear_widgets()

    def upload(self):
        if self.name_birds.text == "" or self.color_feather.text == "" or (self.name_birds.text == "" and self.color_feather.text == "") :
            toast("Заполните форму", duration=1.5)
        else:
            config = Conf_2()

            config['DEFAULT'] = {
            'data_name':f'{self.name_birds.text}',
            'data_color':f'{self.color_feather.text}'
            }

            with open('main.ini', 'w') as f:
                config.write(f)
            #Upload_image(data_name=self.name_birds.text, data_color=self.color_feather.text)
            sm.sm.current = 'upload-image'

class Histori(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def on_enter(self, *args):
        
        self.box = MDFloatLayout()

        self.scroll = MDScrollView()
        self.scroll.do_scroll_x = False
        self.scroll.bar_color = '#008000'
        self.scroll.size_hint = (None, None)
        self.scroll.size = ("250dp", "740dp")
        self.scroll.pos_hint = {"center_y":.45, 'center_x':.56}

        self.card_layout = MDGridLayout()
        self.card_layout.cols = 1
        self.card_layout.col_force_default = False
        self.card_layout.adaptive_height = True
        self.card_layout.padding = 10 
        self.card_layout.spacing = 50
        self.card_layout.pos_hint = {"center_y":.5, 'center_x':.5}

        self.navbar = ContentNavigationDrawer()
        
        try:

            m = MultipartEncoder(fields={'token':'Я-Хочу-У-Вас-Работать'})
            r = requests.post('http://localhost:8000/Histori/Card/', data=m, headers={'Content-Type': m.content_type})

            for i in r.json():
        
                try:
                    m_1 = MultipartEncoder(fields={'token':'Я-Хочу-У-Вас-Работать', 'birds_id':f'{i["birds_id"]}'})
                    r_1 = requests.post('http://localhost:8000/Birds/Histori/', data=m_1, headers={'Content-Type': m_1.content_type})
                    for i in r_1.json():
                        self.card = Card_Birds_add_db()
                        self.card.pos_hint = {'center_y':.5, 'center_x':.5} 

                        self.card.lbl_name.text = i['name']
                        self.card.lbl_color_feather.text = i['color_feather']
                        self.card.lbl_time.text = i['created_at']
                        self.card.image_birds.source = f"http://localhost:8000/uploads/cover/{i['cover']}"

                        self.card_layout.add_widget(self.card)
                except:
                    toast("Карты прицы не созданы", duration=1.5)
        except:
            toast("Подключение не установлено", duration=1.5)


        self.scroll.add_widget(self.card_layout)

        self.box.add_widget(self.scroll)
        self.box.add_widget(self.navbar)
        self.add_widget(self.box)

    def on_leave(self, *args):
        self.clear_widgets()

class Upload_image(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)

        #self.data_name = data_name
        #self.data_color = data_color

    def on_enter(self, *args):


        self.box = MDFloatLayout()
        self.box.orientation = "horizontal"

        self.navbar = ContentNavigationDrawer()

        self.name_screen = MDLabel()
        self.name_screen.text = 'Сохранить фото'
        self.name_screen.font_size = 45
        self.name_screen.halign = "center"
        self.name_screen.pos_hint = {"center_x":.57, "center_y":.94}
        self.name_screen.opacity = .7

        self.btn_image_open = MDRaisedButton()
        self.btn_image_open.text = 'Фото из галереи'
        self.btn_image_open.font_size = 25
        self.btn_image_open.md_bg_color = '#008000'
        self.btn_image_open.pos_hint = {'center_x':.5, 'center_y':.6}
        self.btn_image_open.on_release = self.file_manager_open

        self.btn_camera_open = MDRaisedButton()
        self.btn_camera_open.text = 'Камера'
        self.btn_camera_open.font_size = 25
        self.btn_camera_open.md_bg_color = '#008000'
        self.btn_camera_open.pos_hint = {'center_x':.5, 'center_y':.5}
        self.btn_camera_open.on_release = self.func_camera

        self.btn_miss = MDRaisedButton()
        self.btn_miss.text = "Пропустить"
        self.btn_miss.font_size = 25
        self.btn_miss.pos_hint = {'center_x':.5, 'center_y':.4}
        self.btn_miss.on_release = self.func_miss 

        self.manager_open = False
        self.file_manager = MDFileManager(
            ext = [".png", '.jpeg'], exit_manager=self.exit_manager, select_path=self.select_path
        )

        self.box.add_widget(self.name_screen)
        self.box.add_widget(self.btn_miss)
        self.box.add_widget(self.btn_camera_open)
        self.box.add_widget(self.btn_image_open)
        self.box.add_widget(self.navbar)
        self.add_widget(self.box)

    #def on_leave(self, *args):
        #self.clear_widgets()

    def func_camera(self):
        sm.sm.current = 'camera'

    def func_miss(self):
        try:

            cfg = Conf_2()
            cfg.read('main.ini')
            data_name = cfg.get('DEFAULT', 'data_name')
            data_color = cfg.get('DEFAULT', 'data_color')

            m = MultipartEncoder(fields={'token':'Я-Хочу-У-Вас-Работать', 'is_image':'False', 'name':f'{data_name}', 'color_feather':f'{data_color}'})
            r = requests.post('http://localhost:8000/Birds/Save/', data=m, headers={'Content-Type': m.content_type})

            sm.sm.current = 'birds-list'
            toast("Данные сохранены", duration=1.5)

        except:
            toast("Подключение не установлено", duration=1.5)
            sm.sm.current = 'birds-list'

    def file_manager_open(self):
        PATH ="."
        if platform == "android":
            from android.permissions import request_permissions, Permission
            request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])
            app_folder = os.path.dirname(os.path.abspath(__file__))
            PATH = "/storage/emulated/0" #app_folder
        self.file_manager.show(os.path.expanduser("~"))  # output manager to the screen
        self.manager_open = True


    def select_path(self, path: str):
        
        self.exit_manager()

        try:

            cfg = Conf_2()
            cfg.read('main.ini')
            data_name = cfg.get('DEFAULT', 'data_name')
            data_color = cfg.get('DEFAULT', 'data_color')

            m = MultipartEncoder(fields={'token':'Я-Хочу-У-Вас-Работать', 'is_image':'True', 'name':f'{data_name}', 'color_feather':f'{data_color}','image': ('layer.jpg', open(f'{path}', 'rb'))})
            r = requests.post('http://localhost:8000/Birds/Save/', data=m, headers={'Content-Type': m.content_type})

            toast("Данные сохранены", duration=1.5)
            sm.sm.current = "birds-list"
        except:
            toast("Подключение не установлено", duration=1.5)
            sm.sm.current = "birds-list"

    def exit_manager(self, *args):
        
        self.manager_open = False
        self.file_manager.close()

    def events(self, instance, keyboard, keycode, text, modifiers):
        
        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True

class Camera_image_save(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def on_enter(self, *args):
        self.box = MDFloatLayout()

        try:
            self.camera = Camera()
            self.camera.index = 0
            self.camera.resolution = (375, 812)
            self.camera.play = True
        except:
            self.camera.play = False
            sm.sm.current = "birds-list"
            toast("Камера не определена")


        self.btn_save_image_camera = MDIconButton()
        self.btn_save_image_camera.icon = "camera"
        self.btn_save_image_camera.pos_hint = {'center_x':.5,'center_y':.1}
        self.btn_save_image_camera.on_release = self.func_camera

        self.box.add_widget(self.camera)
        self.box.add_widget(self.btn_save_image_camera)

        self.add_widget(self.box)

    def on_leave(self, *args):
        self.clear_widgets()

    def func_camera(self):
        timestr = time.strftime("%Y%m%d_%H%M%S")
        self.camera.export_to_png(f"IMG_{timestr}.png")
        self.name_image = f"IMG_{timestr}.png"
        self.camera.play = False

        try:

            cfg = Conf_2()
            cfg.read('main.ini')
            data_name = cfg.get('DEFAULT', 'data_name')
            data_color = cfg.get('DEFAULT', 'data_color')

            m = MultipartEncoder(fields={'token':'Я-Хочу-У-Вас-Работать', 'is_image':'True', 'name':f'{data_name}', 'color_feather':f'{data_color}','image': ('layer.jpg', open(f"IMG_{timestr}.png", 'rb'))})
            r = requests.post('http://localhost:8000/Birds/Save/', data=m, headers={'Content-Type': m.content_type})

            toast("Данные сохранены", duration=1.5)
            sm.sm.current = "birds-list"
        except:
            toast("Подключение не установлено", duration=1.5)
            sm.sm.current = "birds-list"

        #sm.sm.current = "birds-list"
        #toast("Данные сохранены", duration=1.5)


class Main(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.sm = MDScreenManager()
        self.sm.add_widget(Birds_list(name='birds-list'))
        self.sm.add_widget(Search_birds(name='search-birds'))
        self.sm.add_widget(Add_birds(name='add-birds'))
        self.sm.add_widget(Histori(name='histori'))
        self.sm.add_widget(Upload_image(name='upload-image'))
        self.sm.add_widget(Camera_image_save(name='camera'))

        self.config = Conf_1()

    def set_value_from_config(self):
        self.config.read(os.path.join(self.directory, '%(appname)s.ini'))

    def get_application_config(self):
        return super(Main, self).get_application_config(
            '{}/%(appname)s.ini'.format(self.directory))

    def build(self):
        return self.sm
    
    

sm = Main()
sm.run()