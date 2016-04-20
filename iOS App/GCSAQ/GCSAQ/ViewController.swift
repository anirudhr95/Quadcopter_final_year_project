//
//  ViewController.swift
//  GCSAQ
//
//  Created by Shyam Ravikumar on 11/04/16.
//  Copyright © 2016 Shyam Ravikumar. All rights reserved.
//

import UIKit
import SceneKit
import CoreMotion
class ViewController: UIViewController {
	
	@IBOutlet weak var speedLabel: UILabel!
	
	@IBOutlet weak var modelView: quad3DView!
	
	let maxAcceptableAngle:CGFloat = 30.0
	var ip:String?
	var socket:Communicator!
	var ypr = YPR()
	let manager:CMMotionManager = CMMotionManager()
	let updateInterval = 0.3
	let buttonnames = buttonNames()
	
	var motionRefreshTriggered:Bool = false
	
	override func viewDidLoad() {
		super.viewDidLoad()

//		FIX: Remove this after debug completed
		print("HELLO\(self.ip)")
		
//		TODO:Initialize modelView

		
		socket =  Communicator(url: NSURL(string: self.ip!)!)
		
//		Creates onconnect and ondisconnect obserbers
		NSNotificationCenter.defaultCenter().addObserver(self, selector: #selector(self.onConnected), name: "connected", object: nil)
		NSNotificationCenter.defaultCenter().addObserver(self, selector: #selector(self.onDisconnected), name: "disconnected", object: nil)
		
//		CMMOTION STUFF
		self.manager.deviceMotionUpdateInterval = self.updateInterval
//		self.manager.startDeviceMotionUpdatesToQueue(NSOperationQueue.mainQueue(), withHandler: self.motionHandle)
		
	}
	
	func motionHandle(data : CMDeviceMotion?, error: NSError?) -> Void {
		if (data  != nil) && (error != nil){
			
			
			
			self.ypr.Pitch = (90-radToDeg(-data!.attitude.roll))
			self.ypr.Yaw = radToDeg(-data!.attitude.yaw)
			self.ypr.Roll = radToDeg(data!.attitude.pitch)
			
			if self.motionRefreshTriggered{
				self.motionRefreshTriggered = false
				self.ypr.setOffset(self.ypr.Yaw, PitchOffset: self.ypr.Pitch, RollOffset: self.ypr.Roll)
				self.ypr.Pitch = self.ypr.Pitch
				self.ypr.Yaw = self.ypr.Yaw
				self.ypr.Roll = self.ypr.Roll
			}
			
			
			if self.isMotionChangeAcceptable() {
				self.socket.sendMsgSetYPR(Double(self.ypr.Yaw), Pitch: Double(self.ypr.Yaw), Roll: Double(self.ypr.Yaw))
				self.modelView.rotate(degToRad( 180 - self.ypr.Yaw), pitch: degToRad(self.ypr.Pitch), roll: degToRad(-self.ypr.Roll))
			}
			else{
//				TODO: HANDLE BAD ROTATION OF DEVICE
			}
		}
	}
	func isMotionChangeAcceptable() -> Bool{
		if((abs(self.ypr.Yaw) > self.maxAcceptableAngle) || (abs(self.ypr.Pitch) > self.maxAcceptableAngle) || (abs(self.ypr.Roll) > self.maxAcceptableAngle)){
			//threshold value crossed
			return false
		}
		return true
	}
	
//	MARK: Angle Conversion Helpers
	func degToRad(angle : CGFloat) -> CGFloat{
		return CGFloat(GLKMathDegreesToRadians(Float(angle)))
	}
	func radToDeg(rad : Double) -> CGFloat{
		return CGFloat(GLKMathRadiansToDegrees(Float(rad)))
	}

	func onConnected(){
//#	TODO: Allow motion updates by enabling flight mode button
		
		
	}
	func onDisconnected(){
//#	TODO: Bring back bonjour screen
		self.manager.stopDeviceMotionUpdates()
		self.modelView.rotate(0, pitch: 180, roll: 0)
		
	}
	override func didReceiveMemoryWarning() {
		super.didReceiveMemoryWarning()
		// Dispose of any resources that can be recreated.
	}
// MARK: BUTTON ACTIONS
	@IBAction func takeoffLandButton(sender: UIButton) {
		if(sender.titleLabel!.text == self.buttonnames.takeoff){
			self.socket.sendMsgTakeoff()
			sender.setTitle(self.buttonnames.land, forState: UIControlState.Normal)
			sender.setTitleColor(UIColor.redColor(), forState: UIControlState.Normal)
			
			
			
		}
		else{
			self.socket.sendMsgLand()
			sender.setTitle(self.buttonnames.takeoff, forState: UIControlState.Normal)
			
			
			
		}
	}
	@IBAction func holdAltitudeSwitchTriggered(sender: UISwitch) {
		self.socket.sendMsgHoldAltitude(sender.on)
	}
	@IBAction func speedValueChanged(sender: UISlider) {
		let val = Int(sender.value)
		speedLabel.text = "\(val)"
//		FIX: Using magic numbers here.. Pass motor speeds when establishing connection
		let actualSpeed = (val * Int(sender.maximumValue) / 100) + 1000
		self.socket.sendMsgSetSpeed(actualSpeed)
	}
	@IBAction func FlightModeTriggered(sender: UIButton) {
		self.socket.sendMsgModeFlight()
		self.motionRefreshTriggered = true
		self.manager.startDeviceMotionUpdatesToQueue(NSOperationQueue.mainQueue(), withHandler: self.motionHandle)
		
		
	}
	@IBAction func hoverModeTriggered(sender: UIButton) {
		self.socket.sendMsgModeHover()
		self.ypr.resetOffsets()
		self.manager.stopDeviceMotionUpdates()
	}
}



