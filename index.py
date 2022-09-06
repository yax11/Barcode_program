
import wx
import os
import time

"""hi"""

class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(
            self,
            parent,
            wx.ID_ANY,
            title,
            size=(850,550),
            style=(wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN))

        self.font = wx.Font(14,  wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, faceName='Times New Roman')
        self.font2 = wx.Font(14,  wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, faceName='Times New Roman')

        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour('#45C7EF')

        self.control = wx.TextCtrl(self.panel, 1, style=(wx.TE_MULTILINE|wx.BORDER_SUNKEN | wx.TE_PROCESS_ENTER), size=(500, 400), pos=(-1, 35))
        self.control.SetFont(wx.Font(20,  wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_BOLD, faceName='Times New Roman'))
        self.control.Bind(wx.EVT_TEXT_ENTER, self.verify)
        self.control.SetBackgroundColour('#6ACDED')
        self.control.SetForegroundColour('#ffffff')

        self.Ofile = wx.Button(self.panel, -1, "Update DB", pos=(82, 1), size=(80, 30), style=wx.NO_BORDER)
        self.Ofile.SetBackgroundColour("#00ff00")
        self.Ofile.Bind(wx.EVT_BUTTON, self.updateDB)

        self.log = wx.Button(self.panel, -1, "View Log", pos=(164, 1), size=(80, 30), style=wx.NO_BORDER)
        self.log.SetBackgroundColour("#ffaa00")
        self.log.Bind(wx.EVT_BUTTON, self.openLog)

        self.clear = wx.Button(self.panel, -1, "Clear", pos=(1, 1), size=(80, 30), style=wx.NO_BORDER)
        self.clear.SetBackgroundColour("#DDDDDD")
        self.clear.Bind(wx.EVT_BUTTON, self.clearArea)

        self.ls = wx.StaticText(self.panel, pos=(510, 20), label="Last Scan : ")
        self.ls.SetFont(self.font2)
        self.ls.SetForegroundColour('white')

        self.lastscan = wx.StaticText(self.panel, pos=(550, 40))
        self.lastscan.SetForegroundColour('#00aa00')
        self.lastscan.SetFont(self.font)

        self.lvs = wx.StaticText(self.panel, pos=(510, 80), label="Last Valid Scan : ")
        self.lvs.SetFont(self.font2)
        self.lvs.SetForegroundColour('white')

        self.lastValidScan = wx.StaticText(self.panel, pos=(550, 100))
        self.lastValidScan.SetFont(self.font)
        self.lastValidScan.SetForegroundColour('white')

        self.fn = wx.StaticText(self.panel, pos=(510, 150), label="First Name : ")
        self.fn.SetFont(self.font2)
        self.fn.SetForegroundColour('white')

        self.firstN = wx.StaticText(self.panel, pos=(550, 170))
        self.firstN.SetForegroundColour('#ff0000')
        self.firstN.SetFont(self.font)

        self.ln = wx.StaticText(self.panel, pos=(510, 210), label="Last  Name : ")
        self.ln.SetFont(self.font2)
        self.ln.SetForegroundColour('white')

        self.lastN = wx.StaticText(self.panel, pos=(550, 230))
        self.lastN.SetForegroundColour('#ff0000')
        self.lastN.SetFont(self.font)

        state = wx.StaticText(self.panel, pos=(510, 270), label="State Name : ")
        state.SetFont(self.font2)
        state.SetForegroundColour('white')

        self.state = wx.StaticText(self.panel, pos=(550, 290))
        self.state.SetFont(self.font)
        self.state.SetForegroundColour("#ff0000")

        nation = wx.StaticText(self.panel, pos=(510, 330), label="Nationality : ")
        nation.SetFont(self.font2)
        nation.SetForegroundColour('white')

        self.nationality = wx.StaticText(self.panel, pos=(550, 350))
        self.nationality.SetFont(self.font)
        self.nationality.SetForegroundColour('#ff0000')

        self.sc = wx.StaticText(self.panel, pos=(510, 390), label="Scan Count : ")
        self.sc.SetFont(self.font2)
        self.sc.SetForegroundColour('white')

        self.scan_count = wx.StaticText(self.panel, pos=(550, 410))
        self.scan_count.SetFont(self.font)

        self.scanLog = wx.Button(self.panel, label=("View User Log"), size=(90,30), pos=(639, 390), style=wx.BORDER_SUNKEN)
        self.scanLog.SetBackgroundColour("#aaaaaa")
        self.scanLog.Bind(wx.EVT_BUTTON, self.userScanCount)

        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer.Add(self.panel, wx.ALL | wx.EXPAND)

        menuFile = wx.Menu()
        menuFile.Append(1, "&Select Database file")
        menuFile.AppendSeparator()
        menuFile.Append(2, "E&xit")

        helpmenu = wx.Menu()
        helpmenu.Append(3, '&About...')

        menuBar = wx.MenuBar()
        menuBar.Append(menuFile, "&File")
        menuBar.Append(helpmenu, '&HELP')

        self.Bind(wx.EVT_MENU, self.update_Database_file, id=1)
        self.Bind(wx.EVT_MENU, self.on_Exit, id=2)
        self.Bind(wx.EVT_MENU, self.on_About, id=3)

        self.SetMenuBar(menuBar)
        self.CreateStatusBar()
        self.SetStatusText("© MEBDOS TECHNOLOGY! 2018.")

        try:
            os.mkdir('DB')
        except FileExistsError:
            pass

        with open('DB\Database.csv','a'), open('DB\log.txt','a'), open('DB\db_file_location.txt', 'a'), open('DB\scan_log.csv', 'a') as f:
            pass

        self.Center()
        self.Show()

    def update_Database_file(self, evt):
        fd = wx.FileDialog(self,
                           message="SELECT DATABASE FILE",
                           defaultDir="",
                           defaultFile="",
                           wildcard="Text Files (*.txt)|*.txt| Comma Separated Values (*.csv)|*.csv",
                           style=wx.FD_DEFAULT_STYLE)
        fd.SetBackgroundColour("green")
        fd.ShowModal()

        try:
            print(fd.GetDirectory(),'\\',fd.GetFilename())
            with open(fd.GetDirectory() + '\\' + fd.GetFilename(), 'r') as x:
                with open('DB\db_file_location.txt', 'w') as dbfile:
                    dbfile.write(str(fd.GetDirectory() + '\\' + fd.GetFilename()))
                with open('DB\database.csv', 'w') as db:
                    db.write(x.read())
        except FileNotFoundError:
            pass

    def clearArea(self, evt):
        self.control.Clear()
        self.control.SetFocus()

    def updateDB(self, evt):
        with open('DB\db_file_location.txt', 'r') as db:
            try:
                with open(db.read(), 'r') as file:
                    open('DB\database.csv', 'w').write(file.read())
            except IOError:
                print("DATABASE NOT SET???")
            finally:
                self.control.SetFocus()

    def openLog(self,evt):
        notepad = wx.Dialog(self,-1, title="ALL LOG", pos=(self.GetPosition()[0], self.GetPosition()[1]), size=(350,500))
        n = wx.TextCtrl(notepad, -1, style=(wx.TE_MULTILINE | wx.TE_READONLY))
        n.SetValue('\n\n')
        self.log = open('DB\log.txt', 'r')
        v = self.log.read()
        n.SetValue(v)
        notepad.Center()
        notepad.Show()

    def userScanCount(self,evt):
        fr = wx.Dialog(self, -1, title="USER SCAN LOG", pos=(self.GetPosition()[0], self.GetPosition()[1]), size=(350,500))
        n = wx.TextCtrl(fr, -1, style=(wx.TE_MULTILINE | wx.NO_BORDER | wx.TE_READONLY))
        v = ''
        with open("DB\log.txt", 'r') as f:
            for i in f.readlines():
                if self.lastValidScan.GetLabel() in i:
                    v = v+str(i)

        n.SetValue(v)
        fr.Show()

    def getNumber(self, uid, first, last):
        f = open('DB\Database.csv', 'r')
        first = f.readlines()[int(first)]
        f.close()
        f = open('DB\Database.csv', 'r')
        last = f.readlines()[int(last)]
        f.close()
        self.lastValidScan.Label = str(uid)
        self.firstN.Label = first.split(',', first.count(','))[4].capitalize()
        self.lastN.Label = last.split(',', first.count(','))[5].capitalize()
        self.state.Label = last.split(',', first.count(','))[6].capitalize()
        self.nationality.Label = last.split(',', first.count(','))[7].capitalize()
        self.no_of_scan(uid)
        noOfScan = self.no_of_scan(uid)

        with open("DB\scan_log.csv", 'a') as f:
            f.write(uid+","+first.split(',', first.count(','))[4].capitalize()+','+first.split(',', first.count(','))[5].capitalize()+','+str(noOfScan)+'\n')
        #self.lastscan.Label = uid
        #self.lastValidScan.Label = first.split(',', first.count(','))[2].capitalize()

    def verify(self, evt):
        f = open('DB\Database.csv', 'r')
        v = self.control.GetValue()
        self.control.SetSelection(-1,-1) # Read from the beginning to the end of the line
        uid = str(self.control.GetStringSelection()).replace('\n', '')
        #print(uid)
        if len(uid)<1:
            return False
        
        self.lastscan.SetLabel(uid)
        self.control.Clear()
        n = -1

        while True:
            for i in f.readlines():
                n=n+1
                if uid in i:
                    #print("FOUND IN LINE : ", n)
                    f.close()
                    MainWindow.getNumber(self, uid, n, n)
                    MainWindow.writeScan(self, uid=uid)
                    break
                else:
                    f.close()
                    #print("NOT FOUND")
            break
        #f.close()

    def writeScan(self, uid,):
        with open('DB\log.txt', 'a') as f:
            f.write(str(uid)+' @ '+time.asctime()+'\n')

    def no_of_scan(self,user):
        n = 1
        with open("DB\log.txt", 'r') as f:
            for i in f.readlines():
                if user in i:
                    n = n+1
        self.scan_count.SetLabel(str(n))
        return n

    def on_Help(self, event):
        font = wx.Font(12, family=wx.FONTFAMILY_ROMAN, style=wx.FONTSTYLE_NORMAL, weight=wx.FONTWEIGHT_BOLD,
                       underline=False, faceName="Arial")
        abountWin = wx.Dialog(self.panel, -1, size=(400, 500))
        aTextLabel = """
                BARCODE SCANS MANAGEMENT OFFICE
                __Version__ 1.0.0 

                This program was developed by
                MEBDOS Technology.
                Release Date: 21ST December, 2018.

                >>>>>>>>>>>>>>>>>>>>
                """
        tx = wx.TextCtrl(abountWin, -1, value=aTextLabel, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.BORDER_NONE)
        tx.SetBackgroundColour("#45C7EF")
        tx.SetForegroundColour("#ffffff")
        tx.SetFont(font)
        abountWin.Show()

    def on_About(self, event):
        font = wx.Font(12, family=wx.FONTFAMILY_ROMAN, style=wx.FONTSTYLE_NORMAL, weight=wx.FONTWEIGHT_BOLD, underline=False, faceName="Arial")
        abountWin = wx.Dialog(self.panel, -1, size=(500, 500), pos=(self.GetPosition()), title="ABOUT!!!")
        aTextLabel = """
        BARCODE SCANS MANAGEMENT OFFICE (BSMO)
        __Version__ 1.0.0 

        This program was developed by MEBDOS Technology.
        Release Date: 21ST December, 2018.

        This software help Organizations manage user's access
        (to events) after (the user) has been isued a unique
        Barcode on-Success-registration for the event.
        

        Authors/Programmers:
        ___________
        Haruna Yakubu Gata
        yakubuharuna11@gmail.com
        +234-8143002447, +234-8188511786
        ___________
        Silas Simon
        silassimon1000@yahoo.com
        +234-8150791283, +234-7030219652
        ___________
        Barnabas Simon
        simonbarnabas049@gmail.com
        +234-8063087551, +234-9051639333


        Credits:
        ............................................
        David Allahyayi,
        Ano-Supermax Technology.

        .................................................................................
        """
        tx = wx.TextCtrl(abountWin, -1, value=aTextLabel, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.BORDER_NONE,
                         pos=(-1, 200))
        tx.SetBackgroundColour("#ffffff")
        tx.SetForegroundColour("#45C7EF")
        tx.SetFont(font)
        abountWin.Show()

    def on_Exit(self, event):
        self.Close()

    def onChar(self, event):
        key = event.GetKeyCode()
        try:
            character = chr(key)
            #print character
        except ValueError:
            character = ""  # arrow keys will throw this error
        acceptable_characters = "1234567890."

        if key in range(33,127) or key == 8:
            #print "KEY DOWN"
            event.Skip()
            return True
        else:
            return False

app = wx.App()
view = MainWindow(None, "BARCODE SCANS MANAGEMENT OFFICE")
app.MainLoop()

