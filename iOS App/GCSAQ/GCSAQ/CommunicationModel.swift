//
//  CommunicationModel.swift
//  GCSAQ
//
//  Created by Shyam Ravikumar on 11/04/16.
//  Copyright © 2016 Shyam Ravikumar. All rights reserved.
//

import Foundation
import SocketIOClientSwift
class Communicator {
	let socketio:SocketIOClient
	let path: String = "/test/"
	let event = Events()
	let commands = Commands()
	
	
	init(url : NSURL){
		socketio = SocketIOClient(socketURL: url, options: [SocketIOClientOption.Log(true),SocketIOClientOption.Path(path)])
		
		self.socketHandlers()
		socketio.connect()
		print("COMPLETE")
		 
		
	}
	func socketHandlers(){
		socketio.on("connect"){
			[weak self] data,ack in
			print("Connected")
			let notif = NSNotification(name: "connected", object: nil)
			NSNotificationCenter.defaultCenter().postNotification(notif)
			
		}
		socketio.on("disconnect"){
			[weak self] data,ack in
			print("Disconnected")
			let notif = NSNotification(name: "disconnected", object: nil)
			NSNotificationCenter.defaultCenter().postNotification(notif)
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