#Boa:Frame:Frame1

import wx, os, sys, threading;


class MainFrame(wx.Frame):
    
    #/sys/devices/platform/hdaps/position
    
    vertical_pacing = 32
    
    second_collumn_x = 260;
    second_collumn_width = 40;
    
    thrid_collumn_x = 350;
    thrid_collumn_width = 400;
    
    
    def _init_coll_notebook1_Pages(self, parent):
        # generated method, don't edit

        parent.AddPage(imageId=-1, page=self.panel1, select=True,
              text=u'Battery')
        parent.AddPage(imageId=-1, page=self.panel2, select=False,
              text=u'HDD Active Protection System')

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, name='', parent=prnt,
              pos=wx.Point(609, 299), size=wx.Size(800, 450),
              style=wx.DEFAULT_FRAME_STYLE,
              title=u'ThinkPad battery and HDD APS utility')
        self.SetClientSize(wx.Size(800, 450))
        self.SetMaxSize(wx.Size(800, 450))
        self.SetMinSize(wx.Size(800, 450))
        
        #http://www.iconfinder.com/icondetails/9203/48/battery_discharging_full_icon
        icon1 = wx.Icon('icon.png', wx.BITMAP_TYPE_PNG)
        self.SetIcon(icon1)

        self.notebook1 = wx.Notebook(name='notebook1',
              parent=self, pos=wx.Point(20, 40), size=wx.Size(760, 342), style=0)

        self.panel1 = wx.Panel(name='panel1',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(796, 338),
              style=wx.TAB_TRAVERSAL)

        self.panel2 = wx.Panel(name='panel2',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(796, 338),
              style=wx.TAB_TRAVERSAL)




        self.close_button = wx.Button(label=u'Close',
              name='close', parent=self, pos=wx.Point(695, 400),
              size=wx.Size(85, 28), style=0)
        self.close_button.Bind(wx.EVT_BUTTON, self.on_close)
        self.close_button.SetToolTipString("Close the application")
        
        self.save_button = wx.Button(label=u'Save',
              name='save', parent=self, pos=wx.Point(600, 400),
              size=wx.Size(85, 28), style=0)
        self.save_button.Bind(wx.EVT_BUTTON, self.on_save)
        self.save_button.SetToolTipString("Apply modified settings")
        self.save_button.Disable()





        y = self.vertical_pacing;

        self.start_charge_thresh_text = wx.StaticText(
              label=u'Battery start charge threshold', name='start_charge_thresh',
              parent=self.panel1, pos=wx.Point(24, y), size=wx.Size(200, 16),
              style=0)
        self.start_charge_thresh_text.SetToolTipString("Percentage at which charging starts")
        
        self.start_charge_thresh_text_val = wx.StaticText(
              label=u'0%', name='start_charge_thresh',
              parent=self.panel1, pos=wx.Point(self.second_collumn_x, y), size=wx.Size(self.second_collumn_width, 16),
              style=0)
        
        y += self.vertical_pacing;

        self.stop_charge_thresh_text = wx.StaticText(
              label=u'Battery stop charge threshold', name='stop_charge_thresh_test',
              parent=self.panel1, pos=wx.Point(24, y), size=wx.Size(200, 16),
              style=0)
        self.stop_charge_thresh_text.SetToolTipString("Percentage at which charging stops")
        
        self.stop_charge_thresh_test_val = wx.StaticText(
              label=u'0%', name='stop_charge_thresh_test',
              parent=self.panel1, pos=wx.Point(self.second_collumn_x, y), size=wx.Size(self.second_collumn_width, 16),
              style=0)

        y = self.vertical_pacing;




        self.start_charge_thresh_slider = wx.Slider(maxValue=100,
              minValue=0, name='slider1', parent=self.panel1, pos=wx.Point(self.thrid_collumn_x,
              y), size=wx.Size(self.thrid_collumn_width, 20), style=wx.SL_AUTOTICKS | wx.SL_LABELS, value=0)
        self.start_charge_thresh_slider.Bind(wx.EVT_SLIDER, self.update_values_as_they_change)
        self.start_charge_thresh_slider.SetToolTipString("Set the percentage at which charging will start. Decrementing this value can extend your batterie's live span")
        
        y += self.vertical_pacing;
        self.stop_charge_thresh_slider = wx.Slider(maxValue=100,
              minValue=0, name='slider2', parent=self.panel1, pos=wx.Point(self.thrid_collumn_x,
              y), size=wx.Size(self.thrid_collumn_width, 20), style=wx.SL_AUTOTICKS | wx.SL_LABELS, value=0)
        self.stop_charge_thresh_slider.Bind(wx.EVT_SLIDER, self.update_values_as_they_change)
        self.stop_charge_thresh_slider.SetToolTipString("Set the percentage at which charging will stop. Decrementing this value can extend your batterie's live span for lion and lipo batteries")


        y += self.vertical_pacing;
        self.batery_state_text = wx.StaticText(
              label=u'Battery state',
              parent=self.panel1, pos=wx.Point(24, y), size=wx.Size(200, 16),
              style=0)
        self.batery_state_text.SetToolTipString("Current state of the battery. Charging, idle, discharging...")
        self.batery_state_text_val = wx.StaticText(
              label=u'loading...',
              parent=self.panel1, pos=wx.Point(self.second_collumn_x, y), size=wx.Size(self.second_collumn_width, 16),
              style=0)
        
        
        y += self.vertical_pacing;
        self.batery_cycles_text = wx.StaticText(
              label=u'Battery cycles',
              parent=self.panel1, pos=wx.Point(24, y), size=wx.Size(200, 16),
              style=0)
        self.batery_cycles_text.SetToolTipString("Number of charging cycles of your battery")
        
        self.batery_cycles_val = wx.StaticText(
              label=u'loading...',
              parent=self.panel1, pos=wx.Point(self.second_collumn_x, y), size=wx.Size(self.second_collumn_width, 16),
              style=0)
        
        y += self.vertical_pacing;
        self.last_full_capacity_text = wx.StaticText(
              label=u'Last full capacity',
              parent=self.panel1, pos=wx.Point(24, y), size=wx.Size(200, 16),
              style=0)
        self.last_full_capacity_text.SetToolTipString("The last full battery capacity. Battery capacity decrements in time.")
        
        self.last_full_capacity_val = wx.StaticText(
              label=u'loading...',
              parent=self.panel1, pos=wx.Point(self.second_collumn_x, y), size=wx.Size(self.second_collumn_width, 16),
              style=0)
        
        y += self.vertical_pacing;
        self.design_capacity_text = wx.StaticText(
              label=u'Design capacity',
              parent=self.panel1, pos=wx.Point(24, y), size=wx.Size(200, 16),
              style=0)
        self.design_capacity_text.SetToolTipString("The initial capacity of your battery")
        self.design_capacity_val = wx.StaticText(
              label=u'loading...',
              parent=self.panel1, pos=wx.Point(self.second_collumn_x, y), size=wx.Size(self.second_collumn_width, 16),
              style=0)
        
        y += self.vertical_pacing;
        self.battery_health_text = wx.StaticText( 
              label=u'Battery health',
              parent=self.panel1, pos=wx.Point(24, y), size=wx.Size(200, 16),
              style=0)
        self.battery_health_text.SetToolTipString("Ratio between the last full capacity and designed capacity of the battery")
        
        self.battery_health_val = wx.StaticText(
              label=u'loading...',
              parent=self.panel1, pos=wx.Point(self.second_collumn_x, y), size=wx.Size(self.second_collumn_width, 16),
              style=0)
        
        y += self.vertical_pacing;
        self.batery_temperature_text = wx.StaticText(
              label=u'Battery temperature',
              parent=self.panel1, pos=wx.Point(24, y), size=wx.Size(200, 16),
              style=0)
        self.batery_temperature_text.SetToolTipString("Current temperature of the battery")
        
        self.batery_temperature_val = wx.StaticText(
              label=u'loading...',
              parent=self.panel1, pos=wx.Point(self.second_collumn_x, y), size=wx.Size(self.second_collumn_width, 16),
              style=0)
        
        
        #
        #
        #
        
        y = self.vertical_pacing;
        self.position_x_text = wx.StaticText(
              label=u'Position',
              parent=self.panel2, pos=wx.Point(24, y), size=wx.Size(200, 16),
              style=0)
        self.position_x_text.SetToolTipString("X and Y coordinates returned by position sensor")
        
        self.position_x_val = wx.StaticText(
              label=u'loading...',
              parent=self.panel2, pos=wx.Point(self.second_collumn_x, y), size=wx.Size(self.second_collumn_width, 16),
              style=0)
        
        y += self.vertical_pacing;
        self.hdaps_state_text = wx.StaticText(
              label=u'Shock detection',
              parent=self.panel2, pos=wx.Point(24, y), size=wx.Size(200, 16),
              style=0)
        self.hdaps_state_text.SetToolTipString("HDD protection state")
        
        self.hdaps_state_val = wx.StaticText(
              label=u'loading...',
              parent=self.panel2, pos=wx.Point(self.second_collumn_x, y), size=wx.Size(self.second_collumn_width, 16),
              style=0)
        
        
        
        if os.getuid():
            self.save_button.Disable()
            self.start_charge_thresh_slider.Disable()
            self.stop_charge_thresh_slider.Disable()
            self.warning_text = wx.StaticText(
              label=u'You need to be root to be able to save configuration.',
              parent=self, pos=wx.Point(360, 405), size=wx.Size(300, 16),
              style=0)
        

        self._init_coll_notebook1_Pages(self.notebook1)

    def __init__(self, parent):
        self._init_ctrls(parent)
        f=open('/sys/devices/platform/smapi/BAT0/start_charge_thresh','r')
        line=f.readline()
        f.close()
        self.start_charge_thresh_slider.SetValue(int(line))
        
        f=open('/sys/devices/platform/smapi/BAT0/stop_charge_thresh','r')
        line=f.readline()
        f.close()
        self.stop_charge_thresh_slider.SetValue(int(line))
        
        self.read_smapi_configuration();
        self.read_hdaps_configuration();

        self.update_values_as_they_change(None)
        
        self.timer = wx.Timer(self)
        self.timer.Start(100)
        self.Bind(wx.EVT_TIMER, self.on_timer, self.timer)
    
    def on_timer(self, event):
        self.read_smapi_configuration()
        self.read_hdaps_configuration()
    
    def read_hdaps_configuration(self):
        f=open('/sys/devices/platform/hdaps/position','r')
        line=f.readline()
        f.close()
        self.position_x_val.SetLabel(str(line).strip())
        
        f=open('/sys/block/sda/device/unload_heads','r')
        line=f.readline()
        f.close()
        if( int(str(line).strip()) != 0 ):
            self.hdaps_state_val.SetLabel('Shock detected')
        else:
            self.hdaps_state_val.SetLabel('No shock detected')
        
        
    def read_smapi_configuration(self):
        
        f=open('/sys/devices/platform/smapi/BAT0/state','r')
        line=f.readline()
        f.close()
        self.batery_state_text_val.SetLabel(str(line).strip())
        
        f=open('/sys/devices/platform/smapi/BAT0/cycle_count','r')
        line=f.readline()
        f.close()
        self.batery_cycles_val.SetLabel(str(line).strip())
        
        f=open('/sys/devices/platform/smapi/BAT0/design_capacity','r')
        line=f.readline()
        f.close()
        
        design_capacity = float(line);        
        self.design_capacity_val.SetLabel(str(line).strip()+" mA")
        
        f=open('/sys/devices/platform/smapi/BAT0/last_full_capacity','r')
        line=f.readline()
        f.close()
        
        last_full_capacity = float(line);
        self.last_full_capacity_val.SetLabel(str(line).strip()+" mA")
        
        self.battery_health_val.SetLabel(str(round(100*last_full_capacity/design_capacity, 2))+"%")
        
        
        f=open('/sys/devices/platform/smapi/BAT0/temperature','r')
        line=f.readline()
        f.close()
        self.batery_temperature_val.SetLabel(str(float(line)/1000).strip()+' '+unichr(176)+'C')
        
        
        
        

    def update_values_as_they_change(self, event):
        
        if os.getuid() == 0:
            self.save_button.Enable()
        
        self.start_charge_thresh_text_val.SetLabel(str(self.start_charge_thresh_slider.GetValue())+"%")
    
        # For security reasons
        if(self.start_charge_thresh_slider.GetValue() < 5):
            self.start_charge_thresh_slider.SetValue(5)
    
        # Stop charge threshold must be greater than start charge threshold!
        if(self.stop_charge_thresh_slider.GetValue() < self.start_charge_thresh_slider.GetValue()):
            self.stop_charge_thresh_slider.SetValue(self.start_charge_thresh_slider.GetValue())
    
        self.stop_charge_thresh_test_val.SetLabel(str(self.stop_charge_thresh_slider.GetValue())+"%")
       



    def on_close(self, event):
        self.Destroy()
        
    def on_save(self, event):
        self.save_button.Disable()
        cmd = "sudo echo "+str(int(self.start_charge_thresh_slider.GetValue()))+" > /sys/devices/platform/smapi/BAT0/start_charge_thresh; echo "+str(int(self.stop_charge_thresh_slider.GetValue()))+" > /sys/devices/platform/smapi/BAT0/stop_charge_thresh";
        os.popen4(cmd);
          

class ThinkUtilsApp(wx.App):
    def OnInit(self):
        self.main = MainFrame(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True
        

if( __name__ == '__main__' ):
        application = ThinkUtilsApp(0)
        application.MainLoop()
