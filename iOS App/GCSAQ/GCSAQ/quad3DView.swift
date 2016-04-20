//
//  quad3DView.swift
//  
//
//  Created by Shyam Ravikumar on 18/04/16.
//
//
import UIKit
import CoreMotion
import SceneKit
import GLKit
import Foundation

class quad3DView : SCNView {
	var ship = SCNNode()
	let updateInterval = 0.3
	
	override init(frame : CGRect){
		
		super.init(frame: frame)
		let scene = SCNScene(named: "art.scnassets/ship.dae")!
		
		// create and add a camera to the scene
		let cameraNode = SCNNode()
		cameraNode.camera = SCNCamera()
		scene.rootNode.addChildNode(cameraNode)
		// place the camera
		cameraNode.position = SCNVector3(x: 0, y: 3, z: 14)
		
		// create and add a light to the scene
		let lightNode = SCNNode()
		lightNode.light = SCNLight()
		lightNode.light!.type = SCNLightTypeOmni
		lightNode.position = SCNVector3(x: 0, y: 10, z: 10)
		scene.rootNode.addChildNode(lightNode)
		
		// create and add an ambient light to the scene
		let ambientLightNode = SCNNode()
		ambientLightNode.light = SCNLight()
		ambientLightNode.light!.type = SCNLightTypeAmbient
		ambientLightNode.light!.color = UIColor.darkGrayColor()
		scene.rootNode.addChildNode(ambientLightNode)
		
		// retrieve the ship node
		ship = scene.rootNode.childNodeWithName("ship", recursively: true)!
		// set the scene to the view
		self.scene = scene
		// allows the user to manipulate the camera
		self.allowsCameraControl = false
		
		// show statistics such as fps and timing information
		self.showsStatistics = true
		// configure the view
		self.backgroundColor = UIColor.whiteColor()
		
		ship.runAction(
			SCNAction.rotateToX(
				0,
				y: degToRad(180),
				z: 0,
				duration: 0.1))
		
		
		
	}
	func degToRad(angle : CGFloat) -> CGFloat{
		return CGFloat(GLKMathDegreesToRadians(Float(angle)))
	}
	func radToDeg(rad : Double) -> CGFloat{
		return CGFloat(GLKMathRadiansToDegrees(Float(rad)))
	}
	func rotate(yaw:CGFloat, pitch:CGFloat, roll:CGFloat){
		
		self.ship.runAction(
			SCNAction.rotateToX(
				degToRad(pitch),
				y : degToRad( 180 - yaw),
				z: degToRad(-roll),
				duration: self.updateInterval
			))
	}

	
	required init?(coder aDecoder: NSCoder) {
		super.init(coder: aDecoder)
	}
	
}
