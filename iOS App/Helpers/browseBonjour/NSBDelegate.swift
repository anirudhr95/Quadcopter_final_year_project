//
//  NSBDelegate.swift
//  browseBonjour
//
//  Created by Shyam Ravikumar on 11/04/16.
//  Copyright © 2016 Shyam Ravikumar. All rights reserved.
//

import Foundation
class NSBDelegate: NSObject, NSNetServiceBrowserDelegate {
	func netServiceBrowser(netServiceBrowser: NSNetServiceBrowser,
	                       didFindDomain domainName: String,
	                                     moreComing moreDomainsComing: Bool) {
		print("netServiceDidFindDomain")
	}
	
	func netServiceBrowser(netServiceBrowser: NSNetServiceBrowser,
	                       didRemoveDomain domainName: String,
	                                       moreComing moreDomainsComing: Bool) {
		print("netServiceDidRemoveDomain")
	}
	
	func netServiceBrowser(netServiceBrowser: NSNetServiceBrowser,
	                       didFindService netService: NSNetService,
	                                      moreComing moreServicesComing: Bool) {
		print("netServiceDidFindService")
	}
	
	func netServiceBrowser(netServiceBrowser: NSNetServiceBrowser,
	                       didRemoveService netService: NSNetService,
	                                        moreComing moreServicesComing: Bool) {
		print("netServiceDidRemoveService")
	}
	
	func netServiceBrowserWillSearch(aNetServiceBrowser: NSNetServiceBrowser){
		print("netServiceBrowserWillSearch")
	}
	func netServiceBrowser(browser: NSNetServiceBrowser, didNotSearch errorDict: [String : NSNumber]) {
		print("NService Did not search '\(errorDict)'")
	}
	
	
	func netServiceBrowserDidStopSearch(netServiceBrowser: NSNetServiceBrowser) {
		print("netServiceDidStopSearch")
	}

}