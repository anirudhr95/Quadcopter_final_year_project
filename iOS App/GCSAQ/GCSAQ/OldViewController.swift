////
////  ViewController.swift
////  Quadcopter
////
////  Created by Shyam Ravikumar on 4/11/15.
////  Copyright (c) 2015 Shyam Ravikumar. All rights reserved.
////
//
//import UIKit
//import CoreMotion
//import SceneKit
//import GLKit
//let laptop_ip:String = "172.20.10.3"
//var pMotionData:CGFloat = 0
//var yMotionData:CGFloat = 0
//var rMotionData:CGFloat = 0
//var opMotionData:CGFloat = 0
//var oyMotionData:CGFloat = 0
//var orMotionData:CGFloat = 0
//let maxAngle = 30.0
//let minChange:CGFloat = 5
//var connected : Bool = false
//var client:TCPClient = TCPClient(addr: laptop_ip, port:20000)
//var receivingMotionUpdates = false
//
//
//
//class OldViewController: UIViewController {
//	let updateInterval = 0.3
//	var ship = SCNNode()
//	
//	@IBAction func retryConnection(sender: UIButton) {
//		connectionStatus.text = "Connecting..."
//		
//		establishConnection(10)
//		if connected{
//			setConnected()
//			
//		}
//		//        else{
//		//            setFailed()
//		//        }
//	}
//	@IBOutlet weak var retryIfConnectionFailed: UIButton!
//	@IBOutlet weak var connectionStatus: UILabel!
//	@IBOutlet weak var modelView: SCNView!
//	@IBOutlet weak var speedThrottleDisplay: UILabel!
//	
//	
//	let manager:CMMotionManager = CMMotionManager()
//	
//	func setFailed(){
//		connectionStatus.text = "Failed"
//		connectionStatus.textColor = UIColor.redColor()
//		speedThrottleDisplay.hidden = true
//		
//		retryIfConnectionFailed.hidden = false
//		retryIfConnectionFailed.enabled = true
//		ship.runAction(
//			SCNAction.rotateToX(
//				0,
//				y: degToRad(180),
//				z: 0,
//				duration: 0.1))
//		if receivingMotionUpdates{
//			manager.stopDeviceMotionUpdates()
//		}
//		
//	}
//	func setConnected(){
//		connectionStatus.text="Connected"
//		connectionStatus.textColor=UIColor.greenColor()
//		retryIfConnectionFailed.hidden = true
//		retryIfConnectionFailed.enabled = false
//		speedThrottleDisplay.hidden = false
//		motionStuff()
//	}
//	@IBAction func speedThrottle(sender: UISlider) {
//		
//		speedThrottleDisplay.text = "\(Int(sender.value * 100)) %"
//		
//		
//	}
//	
//	
//	@IBAction func speedNetworking(sender: UISlider) {
//		let val = Int(sender.value * 100)
//		print(val)
//		if !sendThrottleData(val){
//			setFailed()
//		}
//	}
//	override func viewDidLoad() {
//		super.viewDidLoad()
//		
//		
//		
//		// create a new scene
//		let scene = SCNScene(named: "art.scnassets/ship.dae")!
//		
//		// create and add a camera to the scene
//		let cameraNode = SCNNode()
//		cameraNode.camera = SCNCamera()
//		scene.rootNode.addChildNode(cameraNode)
//		
//		// place the camera
//		cameraNode.position = SCNVector3(x: 0, y: 3, z: 14)
//		
//		// create and add a light to the scene
//		let lightNode = SCNNode()
//		lightNode.light = SCNLight()
//		lightNode.light!.type = SCNLightTypeOmni
//		lightNode.position = SCNVector3(x: 0, y: 10, z: 10)
//		scene.rootNode.addChildNode(lightNode)
//		
//		// create and add an ambient light to the scene
//		let ambientLightNode = SCNNode()
//		ambientLightNode.light = SCNLight()
//		ambientLightNode.light!.type = SCNLightTypeAmbient
//		ambientLightNode.light!.color = UIColor.darkGrayColor()
//		scene.rootNode.addChildNode(ambientLightNode)
//		
//		// retrieve the ship node
//		ship = scene.rootNode.childNodeWithName("ship", recursively: true)!
//		
//		let scnView = modelView
//		
//		// set the scene to the view
//		scnView.scene = scene
//		
//		// allows the user to manipulate the camera
//		scnView.allowsCameraControl = false
//		
//		// show statistics such as fps and timing information
//		scnView.showsStatistics = false
//		// configure the view
//		scnView.backgroundColor = UIColor.whiteColor()
//		
//		ship.runAction(
//			SCNAction.rotateToX(
//				0,
//				y: degToRad(180),
//				z: 0,
//				duration: 0.1))
//		establishConnection(2)
//		if connected{
//			setConnected()
//			
//		}
//		else{
//			setFailed()
//		}
//	}
//	
//	override func shouldAutorotate() -> Bool {
//		return false
//	}
//	
//	override func prefersStatusBarHidden() -> Bool {
//		return true
//	}
//	
//	override func supportedInterfaceOrientations() -> UIInterfaceOrientationMask {
//		if UIDevice.currentDevice().userInterfaceIdiom == .Phone {
//			return UIInterfaceOrientationMask.AllButUpsideDown
//		} else {
//			return UIInterfaceOrientationMask.All
//		}
//	}
//	
//	
//	
//	func motionHandle(data : CMDeviceMotion?, error: NSError?) -> Void {
//		if (data  != nil) && (error != nil){
//			
//			pitch = (90-radToDeg(-data!.attitude.roll))
//			yaw = radToDeg(-data!.attitude.yaw)
//			roll = radToDeg(data!.attitude.pitch)
//			
//			if isMovementChangeBigEnough() {
//				
//				opMotionData = pitch
//				oyMotionData = yaw
//				orMotionData = roll
//				if !sendMotionData(){
//					self.setFailed()
//				}
//				
//				
//			}
//			
//			//            println("Pitch : \(pitch)) Yaw: \(yaw) Roll: \(roll)")
//			
//			
//			
//			self.ship.runAction(
//				SCNAction.rotateToX(
//					degToRad(pitch),
//					y : degToRad( 180 - yaw),
//					z: degToRad(-roll),
//					duration: self.updateInterval
//				))
//			
//			
//		}
//		
//		
//		
//		
//	}
//	func motionStuff(){
//		
//		manager.deviceMotionUpdateInterval = updateInterval
//		receivingMotionUpdates = true
//		manager.startDeviceMotionUpdatesToQueue(NSOperationQueue.mainQueue(), withHandler: motionHandle)
//		
//	}
//	var pitch: CGFloat{
//		get{
//			return pMotionData
//		}
//		set{
//			pMotionData = newValue
//			
//		}
//	}
//	var yaw: CGFloat{
//		get{
//			return yMotionData
//		}
//		set{
//			yMotionData = newValue
//			
//		}
//	}
//	var roll: CGFloat{
//		get{
//			return rMotionData
//		}
//		set{
//			
//			rMotionData = newValue
//			
//		}
//		
//	}
//	func establishConnection(timeout : Int) {
//		
//		var (success,errmsg)=client.connect(timeout: timeout)
//		print("Connection result is \(success) error message : \(errmsg)")
//		if success{
//			//发送数据
//			var (success,errmsg)=client.send(str:"ping" )
//			if success{
//				//读取数据
//				let data=client.read(1024*10)
//				if let d=data{
//					if let str=String(bytes: d, encoding: NSUTF8StringEncoding){
//						print(str)
//						if str=="success" {
//							connected = true
//							return
//						}
//						
//					}
//				}
//			}else{
//				print(errmsg)
//				return
//				
//			}
//		}
//		else{
//			print(errmsg)
//			
//		}
//		
//	}
//	func isMovementChangeBigEnough() -> Bool {
//		if (abs(pitch) > (abs(opMotionData) + minChange) || abs(yaw) > (abs(oyMotionData) + minChange) || abs(roll) > (abs(orMotionData) + minChange)){
//			return true
//		}
//		else{
//			return false
//		}
//	}
//	func sendMotionData() -> Bool {
//		var (success,err) = client.send(str : "\(Int(pitch)),\(Int(yaw)),\(Int(roll))")
//		if !success{
//			print(err)
//			return false
//		}
//		return true
//	}
//	func sendThrottleData(speed : Int) -> Bool{
//		var (success,err) = client.send(str: "\(speed)")
//		if !success{
//			print(err)
//			return false
//		}
//		return true
//	}
//	func degToRad(angle : CGFloat) -> CGFloat{
//		return CGFloat(GLKMathDegreesToRadians(Float(angle)))
//	}
//	func radToDeg(rad : Double) -> CGFloat{
//		return CGFloat(GLKMathRadiansToDegrees(Float(rad)))
//	}
//}
//
