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
	var ip : String?
	var port: Int = 5000
	let dictKeys = dictVals()
	override func viewDidLoad() {
		super.viewDidLoad()
		self.browser = BonjourBrowser(forType: BType, inDomain: BDomain, customDomains: nil, showDisclosureIndicators: false, showCancelButton: false)
		self.browser.delegate = self
		self.view.addSubview(self.browser.view)
		
	}
	func copyStringFromDict(dict:Dictionary<String,NSData>, which:String) ->String? {
		let data:NSData? = dict[which]
		if(data != nil){
			return String(data: data!, encoding: NSUTF8StringEncoding)
		}
		
		return nil
		
	}
	override func didReceiveMemoryWarning() {
		super.didReceiveMemoryWarning()
	}
	@objc func bonjourBrowser(browser: BonjourBrowser!, didSelectService service: NSNetService!) {
		print(service.TXTRecordData())
		let dict = NSNetService.dictionaryFromTXTRecordData(service.TXTRecordData()!)
		self.ip = self.copyStringFromDict(dict, which: self.dictKeys.ip)
		self.port = service.port
		print(dict)
		print(service.hostName)
		print(service.port)
		print( self.ip!)
		performSegueWithIdentifier("scnSegue", sender: self)
	}
	@objc func bonjourBrowser(browser: BonjourBrowser!, didResolveInstance service: NSNetService!) {
		let dict = NSNetService.dictionaryFromTXTRecordData(service.TXTRecordData()!)
		let host = service.hostName
		let port = service.port
		let ip = self.copyStringFromDict(dict, which: self.dictKeys.ip)
		print("RESOLVED HOSTNAME : %@\nIP : %@:%d",host,port,ip)
		
	}
	override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
		if(segue.identifier=="scnSegue"){
			let vc = segue.destinationViewController as! ViewController
			vc.ip = String(format: "%@:%d",self.ip!,self.port)
		}
	}
	
}