from flet import *
def main(page:Page):
    page.title ="Mano"
    page.window.width= 300
    page.window.height =600
    page.bgcolor = 'blue'
    page.window.top=30
    page.window.left=1200
    page.window.resizable=False
    page.horizontal_alignment ="center"
    page.vertical_alignment ="center"
    page.scroll='auto'
    #text######
    te1 =Text("My App Titou" ,size=25 ,color='white' ,weight=FontWeight.BOLD)
    #field#####
    fe2 =TextField(label='Gmail',color='white',icon=Icons.MAIL,height=40)
    fe3 =TextField(label='Password',icon=Icons.PASSWORD,password=True,can_reveal_password=True ,height=40)
    #Botton####
    Bu1 =TextButton(' Domond Password ? ' )
    Bu2 = ElevatedButton('Next',color='blue',bgcolor='white',width=280)
    Bu3 = ElevatedButton('Criet Accont',color='white',bgcolor='black' , icon="add",width=280)
    #image#####
    kio = Image(src=f"https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjhIAKzfBUzc2ZazuNw0VXXD-upD7kj97yaSEVF3tzwWtvuz6C125iBpLc-q3xMGibXl-cBTON6ozK11kVftiYhuznRMhylOaC_w6dNlCXxK-i5S3G-YhO9Ou7YiokXRZghhp3Cv9DC95RaYA4WBsgOsVoO2CePsW53EdCMCe_J1WXxQF2FNiOlvIIV/s492/designevo-logo-maker.webp",width=100,height=150,border_radius=border_radius.all(80))

    page.add(kio,te1,fe2,fe3, Bu1,Bu2,Bu3)
    page.update()
app(main) 
