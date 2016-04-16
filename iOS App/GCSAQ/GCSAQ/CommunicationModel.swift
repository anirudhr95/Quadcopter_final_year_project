//
//  CommunicationModel.swift
//  GCSAQ
//
//  Created by Shyam Ravikumar on 11/04/16.
//  Copyright © 2016 Shyam Ravikumar. All rights reserved.
//

import Foundation
import SocketIOClientSwift
//IOSMESSAGE_TAKEOFF = 'TAKEOFF'
//IOSMESSAGE_LAND = 'LAND'
//IOSMESSAGE_SETSPEED = 'SET_SPEED'
//IOSMESSAGE_HOVER = 'MODE_HOVER'
//IOSMESSAGE_HOLDALTITUDE = 'MODE_ALTITUDE_HOLD'
//IOSMESSAGE_SETYPR = 'SET_YPR'
//IOSMESSAGE_ERROR = "ERROR"
//IOSMESSAGE_FLIGHTMODE = "MODE_FLIGHT"

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
class Communicator {
	let socketio:SocketIOClient
	let path: String = "/test/"
	let event = Events()
	let commands = Commands()
	
	
	init(url : NSURL){
		socketio = SocketIOClient(socketURL: url, options: [SocketIOClientOption.Log(true),SocketIOClientOption.Path(path)])
		
		self.socketHandlers()
		socketio.connect()
		
		 
		
	}
	func socketHandlers(){
		socketio.on("connect"){
			[weak self] data,ack in
			print("Connected")
		}
		socketio.on("disconnect"){
			[weak self] data,ack in
			print("Disconnected")
		}
		socketio.on(self.event.message){
			[weak self] data,ack in
			print("Connected")
		}
		socketio.on(self.event.ready){
			[weak self] data,ack in
			print("QUADCOPTER READY FOR TAKEOFF")
		}
		socketio.onAny{
			print("GOT EVENT \($0.event) with data \($0.items)")
		}
	}
	func sendMsgTakeoff(){
		socketio.emit(self.event.command, self.commands.takeoff)
	}
	func sendMsgLand(){
		socketio.emit(self.event.command, self.commands.takeoff)
	}
	func sendMsgSetYPR(Yaw:Double, Pitch:Double, Roll:Double) {
		socketio.emit(self.event.command, String(self.commands.setYPR, Yaw,Pitch,Roll))
	}
	func sendMsgSetSpeed(Speed:Int){
		socketio.emit(self.event.command, String(self.commands.setSpeed,Speed))
	}
	func sendMsgHoldAltitude( Enable:Bool){
		if(Enable){
			socketio.emit(self.event.command, String(self.commands.holdAltitude,1))
		}
		else{
			socketio.emit(self.event.command, String(self.commands.holdAltitude,0))
		}
	}
	func sendMsgModeHover() {
		socketio.emit(self.event.command, self.commands.hover)
	}
	func sendMsgModeFlight(){
		socketio.emit(self.event.command, self.commands.flightMode)
	}
	func sendMsgError(ErrorMessage : String){
		socketio.emit(self.event.command, String(self.commands.error,ErrorMessage))
	}
	
}