//
//  YPR.swift
//  GCSAQ
//
//  Created by Shyam Ravikumar on 18/04/16.
//  Copyright © 2016 Shyam Ravikumar. All rights reserved.
//

import Foundation
import GLKit
struct YPR {
	var Yaw:CGFloat = 0.0 {
		willSet(newVal){
			self._oldYaw = Yaw
		}
		didSet {
			Yaw -= self._YawOffset
		}
	}
	var Pitch:CGFloat = 0.0 {
		willSet(newVal){
			self._oldPitch = Pitch
		}
		didSet {
			Pitch -= self._PitchOffset
		}
	}
	var Roll:CGFloat = 0.0 {
		willSet(newVal){
			self._oldRoll = Roll
		}
		didSet {
			Roll -= self._RollOffset
		}
	}
	var _oldYaw:CGFloat = 0.0
	var _oldPitch:CGFloat = 0.0
	var _oldRoll:CGFloat = 0.0
	var _YawOffset:CGFloat = 0.0
	var _PitchOffset:CGFloat = 0.0
	var _RollOffset:CGFloat = 0.0
	
	mutating func setOffset(YawOffset:CGFloat, PitchOffset:CGFloat, RollOffset:CGFloat){
		self._YawOffset = YawOffset
		self._PitchOffset = PitchOffset
		self._RollOffset = RollOffset
	}
	mutating func resetOffsets(){
		self._YawOffset = 0.0
		self._PitchOffset = 0.0
		self._RollOffset = 0.0
	}
}