#ifndef GAZEDATASUBSCRIBER_H
#define GAZEDATASUBSCRIBER_H
#pragma once

#include "tobii/sdk/cpp/tracking/eyetracker.hpp"
#include "tobii/sdk/cpp/tracking/gaze-data-item.hpp"
#include "tobii/sdk/cpp/mainloop.hpp"

using namespace tobii::sdk::cpp::tracking;

class GazeDataSubscriber
{
	//eyetracker::pointer eyetracker_object_ptr;
	tobii::sdk::cpp::mainloop _mainloop;
public:
	GazeDataSubscriber(const tobii::sdk::cpp::mainloop &mainloop, eyetracker::pointer ptr);
	~GazeDataSubscriber(void);
	void dummy_gazeDataRcvr(gaze_data_item::pointer ptr);
};
#endif
