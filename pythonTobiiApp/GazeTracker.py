import gtk
import pygtk
import gobject
from tobii.sdk.eyetracker import Eyetracker
from math import pi


idle_add = gobject.idle_add

class GazeTracker:
    def __init__(self, eyetracker):
        self.eyetracker = eyetracker
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.darea = gtk.DrawingArea()
        self.window.add(self.darea)
        self.darea.connect("expose_event", self.expose_event)
        self.gaze_data_selective = None

    def set_eyetracker(self, eyetracker):
        self.eyetracker = eyetracker

    def begin_tracking(self):
        if self.eyetracker is not None:
            self.eyetracker.events.OnGazeDataReceived += self.gaze_data_rcvd
            self.eyetracker.StartTracking()
            self.window.maximize()
            self.window.show_all()
        else:
            print "eyetracker is None. Use set_eyetracker() to set a connected eyetracker"

    def gaze_data_rcvd(self, error, gaze_data):
        self.gaze_data_selective = {
            'left':{
                'validity': gaze_data.LeftValidity, 'gazePt2d':   gaze_data.LeftGazePoint2D
            },
            'right':{
                'validity': gaze_data.RightValidity, 'gazePt2d': gaze_data.RightGazePoint2D
            }
        }
        self.activate_paint()

    def activate_paint(self):
        self.alloc = self.darea.get_allocation() ## This invalidates the screen, causing the expose event to fire.
        rect = gtk.gdk.Rectangle ( self.alloc.x, self.alloc.y, self.alloc.width, self.alloc.height )
        self.darea.window.invalidate_rect ( rect, True )

    def expose_event(self, widget, event):
        self.cairo_context = widget.window.cairo_create()
        self.cairo_context.rectangle(event.area.x, event.area.y, event.area.width, event.area.height)
        self.cairo_context.clip()
        self.paint_gaze_data(self.cairo_context)

    def paint_gaze_data(self, cairo_context):
        if(self.gaze_data_selective is not None):
            # screen coords
            screen_coords = self.darea.get_allocation()
            radius = 20
            # lets display the gaze tracking results
            # According to the recommendation in the user manual, when validity is >2, throw it away
            if(self.gaze_data_selective['left']['validity']<2):
                left_x = screen_coords.width*self.gaze_data_selective['left']['gazePt2d'].x
                left_y = screen_coords.height*self.gaze_data_selective['left']['gazePt2d'].y
                cairo_context.arc(left_x, left_y, radius, 0, 2* pi)
                cairo_context.set_source_rgb(1,0,0)
                cairo_context.fill_preserve()
                cairo_context.set_source_rgb(0,0,1)
                cairo_context.stroke()

            if(self.gaze_data_selective['right']['validity']<2):
                right_x = screen_coords.width*self.gaze_data_selective['right']['gazePt2d'].x
                right_y = screen_coords.height*self.gaze_data_selective['right']['gazePt2d'].y
                cairo_context.arc(right_x, right_y, radius, 0, 2* pi)
                cairo_context.set_source_rgb(0,1,0)
                cairo_context.fill_preserve()
                cairo_context.set_source_rgb(0,0,1)
                cairo_context.stroke()

            cairo_context.move_to(screen_coords.width*0.1, screen_coords.height*0.1)
            cairo_context.line_to(screen_coords.width*0.9, screen_coords.height*0.1)
            cairo_context.set_source_rgb(1,0,0)
            cairo_context.stroke()

            cairo_context.move_to(screen_coords.width*0.1, screen_coords.height*0.5)
            cairo_context.line_to(screen_coords.width*0.9, screen_coords.height*0.5)
            cairo_context.set_source_rgb(1,0,0)
            cairo_context.stroke()

            cairo_context.move_to(screen_coords.width*0.1, screen_coords.height*0.9)
            cairo_context.line_to(screen_coords.width*0.9, screen_coords.height*0.9)
            cairo_context.set_source_rgb(1,0,0)
            cairo_context.stroke()

            cairo_context.move_to(screen_coords.width*0.1, screen_coords.height*0.1)
            cairo_context.line_to(screen_coords.width*0.1, screen_coords.height*0.9)
            cairo_context.set_source_rgb(1,0,0)
            cairo_context.stroke()

            cairo_context.move_to(screen_coords.width*0.5, screen_coords.height*0.1)
            cairo_context.line_to(screen_coords.width*0.5, screen_coords.height*0.9)
            cairo_context.set_source_rgb(1,0,0)
            cairo_context.stroke()

            cairo_context.move_to(screen_coords.width*0.9, screen_coords.height*0.1)
            cairo_context.line_to(screen_coords.width*0.9, screen_coords.height*0.9)
            cairo_context.set_source_rgb(1,0,0)
            cairo_context.stroke()