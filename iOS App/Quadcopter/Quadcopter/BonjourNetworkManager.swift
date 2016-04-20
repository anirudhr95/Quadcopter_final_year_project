//
//  SharedBrowser.swift
//  SharingBrowser
//
//  Created by Peter Wood on 20.08.14.
//
//

import Foundation
import MultipeerConnectivity

class BonjourNetworkManager : NSNetServiceBrowser{
	private let BonjourServiceType = "_http._tcp."
	private let BonjourServiceDomain = "dont-have-a-server-socool"
	private let ServiceBrowser:NSNetServiceBrowser
	private let myPeerId = MCPeerID(displayName: UIDevice.currentDevice().name)
	override init(){
		self.ServiceBrowser = NSNetServiceBrowser()
		super.init()
		self.ServiceBrowser.delegate = self
		
	}
	
}
extension BonjourNetworkManager : NSNetServiceBrowserDelegate {
	
	func netServiceBrowser(browser: NSNetServiceBrowser, didNotSearch errorDict: [String : NSNumber]) {
		NSLog("%@", "COULD NOT SEARCH : \(errorDict)")
	}
	func netServiceBrowser(browser: NSNetServiceBrowser, didFindService service: NSNetService, moreComing: Bool) {
		NSLog("%@", "Found Name:\(service.hostName); IP:\(service.addresses); Port:\(service.port)")
		
	}
	func netServiceBrowser(browser: NSNetServiceBrowser, didRemoveService service: NSNetService, moreComing: Bool) {
		NSLog("%@", "Removed Service Name:\(service.hostName); IP:\(service.addresses); Port:\(service.port) ")
	}
	func netServiceBrowser(browser: NSNetServiceBrowser, didFindDomain domainString: String, moreComing: Bool) {
		NSLog("%@", "Found domain \(domainString);MoreComing : \(moreComing)")
	}
}