//
//  ViewController.swift
//  browseBonjour
//
//  Created by Shyam Ravikumar on 11/04/16.
//  Copyright © 2016 Shyam Ravikumar. All rights reserved.
//

import UIKit

class ViewController: UIViewController, NSNetServiceBrowserDelegate {
	let BType = "_http._tcp"
	let BDomain = ""
	var NSB : NSNetServiceBrowser!
	var services = [NSNetService]()

	override func viewDidLoad() {
		super.viewDidLoad()
		// Do any additional setup after loading the view, typically from a nib.
		self.NSB = NSNetServiceBrowser()
		self.NSB.delegate = self
		self.NSB.searchForServicesOfType("_http._tcp", inDomain: "local.")
		
		
		
	}

	override func didReceiveMemoryWarning() {
		super.didReceiveMemoryWarning()
		// Dispose of any resources that can be recreated.
	}
	func netServiceDidResolveAddress(sender: NSNetService) {
		print(sender.hostName)
	}
	
	func netServiceBrowser(aNetServiceBrowser: NSNetServiceBrowser, didFindService aNetService: NSNetService, moreComing: Bool) {
		print("adding a service")
		self.services.append(aNetService)
		print(aNetService.hostName)
		print(aNetService)
		print(aNetService.domain)
		print(aNetService.TXTRecordData())
		print(aNetService.)
		print(aNetService.name)
		print(aNetService.addresses!.count)
		
		//		 for (NSData *address in [service addresses]) {
//		struct sockaddr_in *socketAddress = (struct sockaddr_in *) [address bytes];
//		NSLog(@Service name: %@ , ip: %s , port %i", [service name], inet_ntoa(socketAddress->sin_addr), [service port]);
//	}
		var ips: [String] = []
		for address in aNetService.addresses!
		{
			let ptr = UnsafePointer<sockaddr_in>(address.bytes)
			var addr = ptr.memory.sin_addr
			var buf = UnsafeMutablePointer<Int8>.alloc(Int(INET6_ADDRSTRLEN))
			var family = ptr.memory.sin_family
			var ipc = UnsafePointer<Int8>()
			if family == __uint8_t(AF_INET)
			{
				ipc = inet_ntop(Int32(family), &addr, buf, __uint32_t(INET6_ADDRSTRLEN))
			}
			else if family == __uint8_t(AF_INET6)
			{
				let ptr6 = UnsafePointer<sockaddr_in6>(address.bytes)
				var addr6 = ptr6.memory.sin6_addr
				family = ptr6.memory.sin6_family
				ipc = inet_ntop(Int32(family), &addr6, buf, __uint32_t(INET6_ADDRSTRLEN))
			}
			
			if let ip = String.fromCString(ipc)
			{
				ips.append(ip)
			}
		}
		for ip in ips{
			print(ip)
		}
		if !moreComing {
//			self.updateInterface()
		}
	}
	
	func netServiceBrowser(aNetServiceBrowser: NSNetServiceBrowser, didRemoveService aNetService: NSNetService, moreComing: Bool) {
		if let ix = self.services.indexOf(aNetService) {
			self.services.removeAtIndex(ix)
			print("removing a service")
			print(aNetService)
			if !moreComing {
//				self.updateInterface()
			}
		}
	}


}

