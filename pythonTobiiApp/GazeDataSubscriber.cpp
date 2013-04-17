#include "GazeDataSubscriber.h"


GazeDataSubscriber::GazeDataSubscriber(const tobii::sdk::cpp::mainloop &mainloop, eyetracker::pointer ptr):
	_mainloop(mainloop)//, eyetracker_object_ptr(ptr)
{
	std::cout<<"In gaze data subscriber constructor..."<<std::endl;
	//eyetracker_object_ptr = ptr;
	//ptr->start_tracking();
	//typedef boost::signals2::signal<void (gaze_data_item::pointer)> gaze_data_received_event;
	eyetracker::gaze_data_received_event sig;
	sig.connect(boost::bind(&GazeDataSubscriber::dummy_gazeDataRcvr, this, _1));
}


GazeDataSubscriber::~GazeDataSubscriber(void)
{
}

void GazeDataSubscriber::dummy_gazeDataRcvr(gaze_data_item::pointer ptr)
{
	std::cout<<"I just received a gaze data event"<<std::endl;
}