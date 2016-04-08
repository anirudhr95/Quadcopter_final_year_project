//
//  SocketIOClient.swift
//  Quadcopter
//
//  Created by Shyam Ravikumar on 07/04/16.
//  Copyright © 2016 Shyam Ravikumar. All rights reserved.
//

import Foundation
import SocketIOClientSwift

class SocketIOClient : SocketIOClient {
	private let socket:SocketIOClient
	private let IP : NSURL
	init(IPAddress : NSURL, options: Set<SocketIOClientOption> = [Path("/test/")]){
		self.IP = IPAddress
		self.socket = SocketIOClient(IPAddress: IP)
		
		
	}
	
	
}
