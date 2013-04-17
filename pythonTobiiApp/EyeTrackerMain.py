#!/usr/bin/env python
import tobii.sdk.browsing
from tobii.sdk.eyetracker import Eyetracker
from tobii.sdk.mainloop import MainloopThread
import gobject
import gobject
import gtk
from CallibrationUI import CallibrationUI
from CalibrationResultPlotter import CalibrationResultPlotter
from GazeTracker import GazeTracker
from GazeTracker_MeanSquaredError import GazeTracker_MeanSquaredError

glib_idle_add = gobject.idle_add
glib_timeout_add = gobject.timeout_add


class EyeTrackerMain:
    def __init__(self):
        tobii.sdk.init()
        self.eyetracker_info = None
        self.eyetracker = None
        self.connected_to_eyetracker = False
        self.callibration_completed = False
        print "In init method"
        tobii.sdk.init()      
        self.mainloop_thread = tobii.sdk.mainloop.MainloopThread()
        self.browser = tobii.sdk.browsing.EyetrackerBrowser(self.mainloop_thread, lambda evt, name, info: glib_idle_add(self.on_eyetracker_browser_event, evt, name, info))
        self.calib_result_plotter = CalibrationResultPlotter(self.eyetracker)
        self.gaze_tracker = GazeTracker_MeanSquaredError(self.eyetracker)
        self.setup_ui()
        
    def on_eyetracker_browser_event(self, event_type, event_name, eyetracker_info):
        print "In eye tracker browser event"
        if((event_type==tobii.sdk.browsing.EyetrackerBrowser.FOUND) or (event_type==tobii.sdk.browsing.EyetrackerBrowser.UPDATED)):
            self.eyetracker_info = eyetracker_info
            if ~self.connected_to_eyetracker:
                Eyetracker.create_async(self.mainloop_thread, self.eyetracker_info, lambda error, eyetracker: glib_idle_add(self.on_eyetracker_created, error, eyetracker, eyetracker_info))
                
    def on_eyetracker_created(self, error, eyetracker, eyetracker_info):
        if error:
            print "Error connecting to the tracker", self.eyetracker_info,":",error
        self.eyetracker = eyetracker
        self.connected_to_eyetracker = True
        print "connected successfully to the eyetracker"
        #print self.eyetracker
        #self.calibration_completed(True, "  ")

    def setup_ui(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.connect("delete_event", gtk.main_quit)
        self.window.set_size_request(400,200)
        self.window.set_position(gtk.WIN_POS_CENTER)
        self.window.set_border_width(10)
        self.callib_button = gtk.Button('Run Calibration')
        self.start_test_button = gtk.Button('Start Test')

        self.callib_button.connect("clicked", self.run_callib_button_pressed, None)
        self.start_test_button.connect("clicked", self.run_test_button_pressed, None)

        self.table = gtk.Table(1,2,True)
        self.table.attach(self.start_test_button, 0,1,0,1)
        self.table.attach(self.callib_button, 1,2,0,1)
        self.vbox = gtk.VBox(False, 2)
        self.vbox.pack_end(self.table, True, True, 0)
        self.window.add(self.vbox)
        self.window.show_all()

    def run_callib_button_pressed(self, widget, data=None):
        # Start the calibration procedure
        if self.eyetracker is not None:
            self.a = CallibrationUI(self.eyetracker)
            self.a.run_callibration(lambda calib_success_status, message: glib_idle_add(self.calibration_completed, calib_success_status, message))

    def calibration_completed(self, calib_success_status, message):
        print "Calibration procedure has ended with status: ", calib_success_status, "because of : ", message
        self.calib_result_plotter.set_eyetracker(self.eyetracker)
        self.calib_result_plotter.plot_calibration_result()
        self.callibration_completed = True

    def run_test_button_pressed(self, widget, data=None):
        if(self.eyetracker is not None) and (self.callibration_completed != False):
            #self.gaze_tracker.set_eyetracker(self.eyetracker)
            #self.gaze_tracker.begin_tracking()
            self.gaze_tracker.set_eyetracker(self.eyetracker)
            self.gaze_tracker.begin_tracking(lambda mse_stats: glib_idle_add(self.gaze_tracking_mean_square_error, mse_stats))
        else:
            print 'Woops! Try again when youve gone through callibration!'

    def gaze_tracking_mean_square_error(self, mse_stats):
        print "Collected mean squared error stats: "
        print "Cumulative MSE: ",mse_stats['Cumulative MSE'],"Averaged MSE: ",mse_stats['Averaged MSE'], ", MSE % Screen Width: ", mse_stats['mse_percent_of_width'],  ", MSE % Screen Height: ", mse_stats['mse_percent_of_height'], \
        ", Screen Width: ", mse_stats['screen_width'], ", Screen Height: ", mse_stats['screen_height']

    def delete_event(self, widget, event, data=None):
        gtk.main_quit()
        return False

    def main(self):
        gtk.gdk.threads_init()
        gtk.main()
        self.mainloop_thread.stop()

if __name__ == '__main__':
    a = EyeTrackerMain()
    a.main()