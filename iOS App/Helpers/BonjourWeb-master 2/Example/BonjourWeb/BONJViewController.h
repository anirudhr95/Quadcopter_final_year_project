//
//  BONJViewController.h
//  based on BonjourWeb from Apple
//
//  Created by Claus Weymann on 08/10/2015.
//  Copyright (c) 2015 Claus Weymann. All rights reserved.
//

@import UIKit;

#import "BonjourBrowser.h"

#define kWebServiceType @"_http._tcp"
#define kInitialDomain  @"local"

@interface BONJViewController : UIViewController<BonjourBrowserDelegate>

@end
