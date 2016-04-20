//
//  ViewController.swift
//  Quadcopter
//
//  Created by Shyam Ravikumar on 02/04/16.
//  Copyright © 2016 Shyam Ravikumar. All rights reserved.
//

import UIKit
import Starscream
import SVProgressHUD
class ViewController: UIViewController {
	var socketIO : SocketIOManager?
	private var IPAddress : NSURL = NSURL(string: "ws://192.168.0.108")!
	override func viewDidLoad() {
		super.viewDidLoad()
		socketIO = SocketIOManager(IP_Address: IPAddress)
		
		
		// Do any additional setup after loading the view, typically from a nib.
	}

	override func didReceiveMemoryWarning() {
		super.didReceiveMemoryWarning()
		// Dispose of any resources that can be recreated.
	}


}

