//
//  BonjourModel.swift
//  GCSAQ
//
//  Created by Shyam Ravikumar on 11/04/16.
//  Copyright © 2016 Shyam Ravikumar. All rights reserved.
//

import Foundation
import BonjourWeb

struct dictVals {
	let ip = "ip"
	
}

class Bonjour : UIViewController, BonjourBrowserDelegate {
	var browser : BonjourBrowser!
	let BType : String = "_http._tcp"
	let BDomain : String = "local"
	var ip : String = ""
	let dictKeys = dictVals()
	override func viewDidLoad() {
		super.viewDidLoad()
		self.browser = BonjourBrowser(forType: BType, inDomain: BDomain, customDomains: nil, showDisclosureIndicators: false, showCancelButton: false)
		self.browser.delegate = self
		self.view.addSubview(self.browser.view)
		
	}
	func copyStringFromDict(dict:Dictionary<String,NSData>, which:String) ->String {
		let data:NSData? = dict[which]
		if(data != nil){
			return String(data)
		}
		else{
			return ""
		}
	}
	override func didReceiveMemoryWarning() {
		super.didReceiveMemoryWarning()
	}
	@objc func bonjourBrowser(browser: BonjourBrowser!, didSelectService service: NSNetService!) {
		let dict = NSNetService.dictionaryFromTXTRecordData(service.TXTRecordData()!)
		self.ip = self.copyStringFromDict(dict, which: self.dictKeys.ip)
		print(service.TXTRecordData())
		print(dict)
		print(String(self.ip))
//		performSegueWithIdentifier("hello", sender: self)
	}
	@objc func bonjourBrowser(browser: BonjourBrowser!, didResolveInstance service: NSNetService!) {
		let dict = NSNetService.dictionaryFromTXTRecordData(service.TXTRecordData()!)
		let host = service.hostName
		let port = service.port
		let ip = self.copyStringFromDict(dict, which: self.dictKeys.ip)
		print("RESOLVED HOSTNAME : %@\nIP : %@:%d",host,port,ip)
		
		
	}
	
}