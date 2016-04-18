//
//  CommunicatorStructs.swift
//  GCSAQ
//
//  Created by Shyam Ravikumar on 18/04/16.
//  Copyright © 2016 Shyam Ravikumar. All rights reserved.
//

import Foundation
struct Commands {
	let takeoff = "TAKEOFF"
	let land = "LAND"
	let setSpeed = "SET_SPEED:%d"
	let hover = "MODE_HOVER"
	let holdAltitude = "MODE_ALTITUDE_HOLD:%d"
	let setYPR = "SET_YPR:%f%f%f"
	let flightMode = "MODE_FLIGHT"
	let error = "ERROR:%@"
}
struct Events {
	let command = "message"
	let message = "message"
	let ready = "ready"
}