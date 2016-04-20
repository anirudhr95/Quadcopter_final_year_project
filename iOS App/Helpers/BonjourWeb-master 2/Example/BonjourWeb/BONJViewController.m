//
//  BONJViewController.m
//  BonjourWeb
//
//  Created by Claus Weymann on 08/10/2015.
//  Copyright (c) 2015 Claus Weymann. All rights reserved.
//

#import "BONJViewController.h"

@interface BONJViewController ()
@property (nonatomic, retain) BonjourBrowser *browser;
@end

@implementation BONJViewController

- (void)viewDidLoad
{
    [super viewDidLoad];
	// Do any additional setup after loading the view, typically from a nib.
    // Create the Bonjour Browser for Web services
    BonjourBrowser *aBrowser = [[BonjourBrowser alloc] initForType:kWebServiceType
                                                          inDomain:kInitialDomain
                                                     customDomains:nil // we won't save any additional domains added by the user
                                          showDisclosureIndicators:NO
                                                  showCancelButton:NO];
    self.browser = aBrowser;
    
    
    self.browser.delegate = self;
    
    // We want to let the user know that the services list is dynamic and always updating, even when there are no
    // services currently found.
    self.browser.searchingForServicesString = NSLocalizedString(@"Searching for web services", @"Searching for web services string");
    
    // Add the controller's view as a subview of the window
    [self.view addSubview:[self.browser view]];
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

- (NSString *)copyStringFromTXTDict:(NSDictionary *)dict which:(NSString*)which {
    // Helper for getting information from the TXT data
    NSData* data = [dict objectForKey:which];
    NSString *resultString = nil;
    if (data) {
        resultString = [[NSString alloc] initWithData:data encoding:NSUTF8StringEncoding];
    }
    return resultString;
}

-(void)bonjourBrowser:(BonjourBrowser *)browser didSelectService:(NSNetService *)service
{
    if (service.TXTRecordData.length > 0) {
        NSLog(@"Record data: %@",[[NSString alloc] initWithData:service.TXTRecordData encoding:NSUTF8StringEncoding]);
    }
}

- (void) bonjourBrowser:(BonjourBrowser*)browser didResolveInstance:(NSNetService*)service {
    // Construct the URL including the port number
    // Also use the path, username and password fields that can be in the TXT record
    NSDictionary* dict = [NSNetService dictionaryFromTXTRecordData:[service TXTRecordData]];
    NSString *host = [service hostName];
    
    NSString* user = [self copyStringFromTXTDict:dict which:@"u"];
    NSString* pass = [self copyStringFromTXTDict:dict which:@"p"];
    
    NSString* portStr = @"";
    
    // Note that [NSNetService port:] returns an NSInteger in host byte order
    NSInteger port = [service port];
    if (port != 0 && port != 80)
        portStr = [[NSString alloc] initWithFormat:@":%ld",(long)port];
    
    NSString* path = [self copyStringFromTXTDict:dict which:@"path"];
    if (!path || [path length]==0) {
        path = @"/";
    } else if (![[path substringToIndex:1] isEqual:@"/"]) {
        NSString *tempPath = [[NSString alloc] initWithFormat:@"/%@",path];
        path = tempPath;
    }
    
    NSString* string = [[NSString alloc] initWithFormat:@"http://%@%@%@%@%@%@%@",
                        user?user:@"",
                        pass?@":":@"",
                        pass?pass:@"",
                        (user||pass)?@"@":@"",
                        host,
                        portStr,
                        path];

    NSURL *url = [[NSURL alloc] initWithString:string];
    [[UIApplication sharedApplication] openURL:url];
    
}
@end
