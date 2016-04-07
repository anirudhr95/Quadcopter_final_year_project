//
//  SocketIOManager.swift
//  Quadcopter
//
//  Created by Shyam Ravikumar on 07/04/16.
//  Copyright © 2016 Shyam Ravikumar. All rights reserved.
//

import Foundation
import Starscream
class SocketIOManager {
	private let IP:NSURL
	private let socket:WebSocket
	
	init(IP_Address : NSURL){
		self.IP = IP_Address
		
		self.socket = WebSocket(url: IP_Address)
		self.socket.delegate = self
		self.socket.connect()
		
	}
	func send(Msg : String){
		
		self.socket.writeString(Msg)
	}
	func send(data : NSData){
		self.socket.writeData(data)
	}
	func isConnected() -> Bool {
		return self.socket.isConnected
	}
}

extension SocketIOManager : WebSocketDelegate {
	func websocketDidConnect(socket: WebSocket) {
		print("Connected to SOCKETIO")
	}
	func websocketDidReceiveData(socket: WebSocket, data: NSData) {
		print("Data Received : \(data)")
	}
	func websocketDidDisconnect(socket: WebSocket, error: NSError?) {
		print("Disconnected from SOCKETIO")
		if let error = error{
			print("Error : \(error)")
		}
	}
	func websocketDidReceiveMessage(socket: WebSocket, text: String) {
		print("Received Message : \(text)")
	}
	
	
}